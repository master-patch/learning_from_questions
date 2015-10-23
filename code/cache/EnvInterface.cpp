#include "EnvInterface.h"
#include <nlp_config.h>
#include <nlp_macros.h>
#include <nlp_time.h>
#include <assert.h>
#include <string.h>



bool	ThreadedEnvironmentInterface::b_ShowComms = false;
bool	ThreadedEnvironmentInterface::b_ShowCommsVerbose = false;
EnvironmentConnectionManager*	EnvironmentConnectionManager::p_Manager = NULL;



//														
EnvironmentConnection::EnvironmentConnection (void)
{
	p_Manager = NULL;
	l_Usage = 0;
	p_CurrentRequest = NULL;
	pthread_mutex_init (&mtx_Shutdown, NULL);
}


//														
EnvironmentConnection::~EnvironmentConnection (void)
{
	assert ((EnvironmentConnectionManager*)0x1 != p_Manager);
	p_Manager = (EnvironmentConnectionManager*)0x1;
	p_CurrentRequest = NULL;
	pthread_mutex_destroy (&mtx_Shutdown);
}


//														
void EnvironmentConnection::OnConnect (void)
{
	cout << "Connected to "
		 << GetServerId () << ':' << GetServiceId ()
		 << endl;

	pthread_mutex_lock (&p_Manager->mtx_Access);	// lock !

	p_Manager->set_AllConnections.insert (this);
	p_Manager->set_FreeConnections.insert (this);

	pthread_mutex_unlock (&p_Manager->mtx_Access);	// unlock !

}


//														
void EnvironmentConnection::OnDisconnect (void)
{
	// if the client was lost while processing	
	// a request, queue the request back in.	
	pthread_mutex_lock (&p_Manager->mtx_PendingRequests);	// lock 
	if (NULL != p_CurrentRequest)
	{
		assert (NULL != p_Manager);
		// But first check if that there isn't a	
		// race condition...						
		if (p_Manager->map_PendingRequests.find (p_CurrentRequest->s_Message)
				!= p_Manager->map_PendingRequests.end ())
			p_Manager->dq_PendingRequests.push_back (p_CurrentRequest);
	}
	pthread_mutex_unlock (&p_Manager->mtx_PendingRequests);	// unlock 
	

	// handle the connection loss...			
	String sError;
	sError << "Lost connection to "
		   << GetServerId () << ':' << GetServiceId ();
	OnError (sError);
}


//														
void EnvironmentConnection::OnReceive (const void* _zData, long _lBytes)
{
	o_Buffer.Append (_zData, _lBytes);

	if (true == o_Buffer.HasTerminator ('\x05'))
	{
		String sResponse = o_Buffer.PopFirstMessageAsString ('\x05');

		// remove this request from the queue...	
		pthread_mutex_lock (&p_Manager->mtx_PendingRequests);		// lock		
		p_Manager->map_PendingRequests.erase (p_CurrentRequest->s_Message);


		// send out the responses...				
		ITERATE (CallbackInfo_dq_t, p_CurrentRequest->dq_CallbackInfo, ite)
		{
			CallbackInfo& rCallback = *ite;
			String sCategory = rCallback.p_Callback->OnResponse (rCallback.s_CallbackId,
																 sResponse);

			// compute internal stats...				
			FFResponseCategoryToCount_map_t::iterator	ite;
			ite = map_ResponseCategoryToCount.find (sCategory);
			if (map_ResponseCategoryToCount.end () == ite)
				map_ResponseCategoryToCount.insert (make_pair (sCategory, 1));
			else
				++ ite->second;
		}


		// clean up...								
		delete p_CurrentRequest;
		p_CurrentRequest = NULL;
		p_Manager->ReleaseConnection (this);

		pthread_mutex_unlock (&p_Manager->mtx_PendingRequests);	// unlock	
	}
}


//														
void EnvironmentConnection::OnError (const char* _zError)
{
	// It is possible for both child sockets (agent & reset)
	// to simultaneously encounter errors and call this		
	// method.  In this case, we would have a race condition
	// since this method deletes the EnvironmentConnection	
	// object.												
	pthread_mutex_lock (&mtx_Shutdown);	// lock !

	// EnvironmentConnectionManager* pManager = p_Manager;
	if (NULL == p_Manager)
		return;

	p_Manager->CloseConnection (this);
	p_Manager = NULL;

	cerr << "[ERROR]  " << _zError << endl;

	Close ();

	// We need to unlock before calling CloseConnection		
	// below since that's going to delete this object...	
	pthread_mutex_unlock (&mtx_Shutdown);	// unlock !

	delete this;

	// The funcky code below is to avoid loop-back calls.	
	// This code checks if p_Manager is NULL on top to 		
	// OnError calls to a deleted EnvironmentConnection 	
	// object.  But we could get OnError calls as a result	
	// of processing triggered by the CloseConnection call.	
	// So we need to set p_Manager = NULL before that call.	
	// pManager->CloseConnection (this);
}







//														
EnvironmentConnectionManager::EnvironmentConnectionManager (void)
{
	pthread_mutex_init (&mtx_Access, NULL);
	pthread_mutex_init (&mtx_PendingRequests, NULL);
	p_Manager = this;
}




//														
EnvironmentConnectionManager::~EnvironmentConnectionManager (void)
{
	Shutdown ();
	pthread_mutex_destroy (&mtx_Access);
	pthread_mutex_destroy (&mtx_PendingRequests);
}


//														
ClientSocket* EnvironmentConnectionManager::CreateClient (void)
{
	EnvironmentConnection* pConnection = new EnvironmentConnection;
	pConnection->p_Manager = p_Manager;
	pConnection->i_TimeoutSeconds = (config)"client_request_timeout";

	return pConnection;
}


//														
void EnvironmentConnectionManager::CloseConnection (EnvironmentConnection* _pConnection)
{
	pthread_mutex_lock (&mtx_Access);	// lock !

	cerr << "[WARNING]  disconnecting on error from "
		 << _pConnection->GetServerId () << ':' 
		 << _pConnection->GetServiceId () << endl;

	// cleanup connection stores ...
	assert (set_AllConnections.end () != set_AllConnections.find (_pConnection));
	set_AllConnections.erase (_pConnection);
	set_FreeConnections.erase (_pConnection);

	// delete _pConnection;

	cout << "[INFO]  available worlds : " << set_AllConnections.size () << endl;

	pthread_mutex_unlock (&mtx_Access);	// unlock !
}


//														
void EnvironmentConnectionManager::Init (void)
{
	// assert (true == set_ActiveInterfaces.empty ());
	// assert (true == map_ConnectionToInterface.empty ());
	assert (true == set_FreeConnections.empty ());

	pthread_create (&thr_RequestQueue, NULL, RunThread, this);
	pthread_detach (thr_RequestQueue);
}


//														
void EnvironmentConnectionManager::Shutdown (void)
{
	pthread_mutex_lock (&mtx_Access);	// lock !

	// set_ActiveInterfaces.clear ();
	// map_ConnectionToInterface.clear ();

	ITERATE (EnvironmentConnection_set_t, set_AllConnections, ite)
	{
		EnvironmentConnection* pConnection = *ite;
		pConnection->SendBlocking ("\x02\x05", 2);
		pConnection->Close ();
		delete pConnection;
	}
	set_AllConnections.clear ();
	set_FreeConnections.clear ();


	pthread_mutex_unlock (&mtx_Access);	// unlock !
}


//														
void EnvironmentConnectionManager::QueueRequest (String& _rMessage,
												 ResponseCallback* _pCallback,
												 String& _sCallbackId)
{
	pthread_mutex_lock (&mtx_PendingRequests);		// lock		

	MessageToRequest_map_t::iterator	ite;
	ite = map_PendingRequests.find (_rMessage);
	if (map_PendingRequests.end () != ite)
	{
		// this is identical to a currently	
		// pending request, so just add the	
		// callback to the original request.
		Request* pRequest = ite->second;
		pRequest->AddCallback (_pCallback, _sCallbackId);
	}
	else
	{
		// this is a new request...			
		Request* pRequest = new Request (_rMessage,
										 _pCallback,
										 _sCallbackId);
		dq_PendingRequests.push_back (pRequest);
		map_PendingRequests.insert (make_pair (_rMessage, pRequest));
	}

	pthread_mutex_unlock (&mtx_PendingRequests);	// unlock	
}


//														
bool EnvironmentConnectionManager::ProcessRequest (EnvironmentConnection* _pConnection,
												   Request* _pRequest)
{
	_pConnection->ClearBuffer ();
	_pConnection->p_CurrentRequest = _pRequest;
	_pConnection->SendNonBlocking ((const char*)_pRequest->s_Message,
								   _pRequest->s_Message.length ());

	if (false == _pConnection->IsConnected ())
	{
		_pConnection->OnError ("Connection failed on send");
		_pConnection = NULL;

		// We return false here on error.  The manager	
		// will re-queue this request on another 		
		// connection later...							
		return false;
	}

	return true;
}


//														
void* EnvironmentConnectionManager::RunThread (void* _pArg)
{
	EnvironmentConnectionManager* pManager = (EnvironmentConnectionManager*)_pArg;

	while (true)
	{
		usleep (10000);


		// get request if present ...					
		pthread_mutex_lock (&pManager->mtx_PendingRequests);		// lock 
		if (true == pManager->dq_PendingRequests.empty ())
		{
			pthread_mutex_unlock (&pManager->mtx_PendingRequests);	// unlock 
			continue;
		}


		// get connection if available ...				
		pthread_mutex_lock (&pManager->mtx_Access);					// lock 

		if (true == pManager->set_FreeConnections.empty ())
		{
			pthread_mutex_unlock (&pManager->mtx_PendingRequests);	// unlock 
			pthread_mutex_unlock (&pManager->mtx_Access);			// unlock 
			continue;
		}


		//												
		Request* pRequest = pManager->dq_PendingRequests.front ();
		pManager->dq_PendingRequests.pop_front ();
		pthread_mutex_unlock (&pManager->mtx_PendingRequests);		// unlock 


		// send request on connection ...				
		EnvironmentConnection_set_t::iterator	iteToUse;
		iteToUse = pManager->set_FreeConnections.begin ();
		EnvironmentConnection* pConnectionToUse = *iteToUse;

		pManager->set_FreeConnections.erase (iteToUse);
		// map_ConnectionToInterface.insert (make_pair (pConnectionToUse, _pInterface));
		// set_ActiveInterfaces.insert (_pInterface);

		pthread_mutex_unlock (&pManager->mtx_Access);				// unlock !


		// if we couldn't send the request, queue		
		// it back ...									
		if (false == pManager->ProcessRequest (pConnectionToUse, pRequest))
		{
			pthread_mutex_lock (&pManager->mtx_PendingRequests);	// lock 
			p_Manager->ReleaseConnection (pConnectionToUse);

			pManager->dq_PendingRequests.push_back (pRequest);
			pthread_mutex_unlock (&pManager->mtx_PendingRequests);	// unlock 
		}
	}
	return NULL;
}




//														
void EnvironmentConnectionManager::ReleaseConnection (EnvironmentConnection* _pConnection)
{
	pthread_mutex_lock (&mtx_Access);	// lock !

	_pConnection->p_CurrentRequest = NULL;
	
	assert (set_AllConnections.end () != set_AllConnections.find (_pConnection));
	assert (set_FreeConnections.end () == set_FreeConnections.find (_pConnection));
	set_FreeConnections.insert (_pConnection);

	pthread_mutex_unlock (&mtx_Access);	// unlock !
}


//														
long EnvironmentConnectionManager::GetRequestQueueLength (void)
{
	pthread_mutex_lock (&mtx_PendingRequests);	// lock 
	long iLength = dq_PendingRequests.size ();
	pthread_mutex_unlock (&mtx_PendingRequests);	// unlock 
	return iLength;
}

//														
String EnvironmentConnectionManager::GetRequestQueueInfo (void)
{
	String sResponse;
	pthread_mutex_lock (&mtx_PendingRequests);	// lock 
	sResponse << "   Current queue length : "
			  << (long) dq_PendingRequests.size ()
			  << '\n';
	pthread_mutex_unlock (&mtx_PendingRequests);	// unlock 
	return sResponse;
}


//														
String EnvironmentConnectionManager::GetFFClientInfo (void)
{
	String_set_t setServers;
	pthread_mutex_lock (&mtx_Access);	// lock !
	ITERATE (EnvironmentConnection_set_t, set_AllConnections, ite)
		setServers.insert ((*ite)->GetServerId ());
	pthread_mutex_unlock (&mtx_Access);	// unlock !

	String sResponse;
	sResponse << "   Available machines : " << (long) setServers.size ()
			  << "\n   Available clients : " << (long) set_AllConnections.size ()
			  << "\n   Free clients      : " << (long) set_FreeConnections.size ()
			  << '\n';

	return sResponse;
}


//														
typedef map <String, int>	ServerToCount_map_t;

String EnvironmentConnectionManager::GetFFClientInfoDetailed (void)
{
	String_set_t setServers;
	ServerToCount_map_t	mapServerToFFCount;
	pthread_mutex_lock (&mtx_Access);	// lock !
	ITERATE (EnvironmentConnection_set_t, set_AllConnections, ite)
	{
		const String& rServerName = (*ite)->GetServerId ();
		setServers.insert (rServerName);

		ServerToCount_map_t::iterator	iteCount;
		iteCount = mapServerToFFCount.find (rServerName);
		if (mapServerToFFCount.end () == iteCount)
			mapServerToFFCount [rServerName] = 1;
		else
			++ iteCount->second;
	}
	pthread_mutex_unlock (&mtx_Access);	// unlock !

	String sResponse;
	sResponse << "   Available machines : " << (long) setServers.size ()
			  << "\n   Available clients : " << (long) set_AllConnections.size ()
			  << "\n   Free clients      : " << (long) set_FreeConnections.size ()
			  << "\n---------------------------------------\n";
	ITERATE (ServerToCount_map_t, mapServerToFFCount, ite)
		sResponse << "   " << ite->second << "  \t" << ite->first << '\n';
	sResponse << "---------------------------------------\n\n";

	return sResponse;
}


//														
typedef map <String, FFResponseCategoryToCount_map_t>	ServerToCategory_map_t;

String EnvironmentConnectionManager::GetFFResponseStats (void)
{
	ServerToCategory_map_t	mapServerToCategory;
	FFResponseCategoryToCount_map_t	mapOverallCategoryStats;

	// compute response stats over all connections ...	
	pthread_mutex_lock (&mtx_Access);	// lock !
	ITERATE (EnvironmentConnection_set_t, set_AllConnections, iteConn)
	{
		EnvironmentConnection* pConnection = *iteConn;
		String sServerId = pConnection->GetServerId ();

		FFResponseCategoryToCount_map_t* pmapCategoryToCount;
		ServerToCategory_map_t::iterator	iteServer;
		iteServer = mapServerToCategory.find (sServerId);
		if (mapServerToCategory.end () == iteServer)
		{
			pair <ServerToCategory_map_t::iterator, bool> pairInsert;
			pairInsert = mapServerToCategory.insert (make_pair (sServerId, FFResponseCategoryToCount_map_t ()));
			pmapCategoryToCount = &pairInsert.first->second;
		}
		else
			pmapCategoryToCount = &iteServer->second;


		ITERATE (FFResponseCategoryToCount_map_t,
				 pConnection->map_ResponseCategoryToCount, ite)
		{
			FFResponseCategoryToCount_map_t::iterator	iteTotal;
			iteTotal = pmapCategoryToCount->find (ite->first);
			if (pmapCategoryToCount->end () == iteTotal)
				pmapCategoryToCount->insert (make_pair (ite->first, ite->second));
			else
				iteTotal->second += ite->second;

			FFResponseCategoryToCount_map_t::iterator	iteOverall;
			iteOverall = mapOverallCategoryStats.find (ite->first);
			if (mapOverallCategoryStats.end () == iteOverall)
				mapOverallCategoryStats.insert (make_pair (ite->first, ite->second));
			else
				iteOverall->second += ite->second;
		}
	}
	pthread_mutex_unlock (&mtx_Access);	// unlock !


	// compile message with computed stats ...			
	String sResponse;
	sResponse << "   ---------------------------------------\n"
			  << "   Overall response stats. \n"
			  << "   ---------------------------------------\n";
	ITERATE (FFResponseCategoryToCount_map_t, mapOverallCategoryStats, ite)
		sResponse << "      " << ite->second << "  \t" << ite->first << '\n';

	ITERATE (ServerToCategory_map_t, mapServerToCategory, iteServer)
	{
		sResponse << "   ---------------------------------------\n"
				  << "   " << iteServer->first << '\n'
				  << "   ---------------------------------------\n";
		ITERATE (FFResponseCategoryToCount_map_t, iteServer->second, ite)
			sResponse << "      " << ite->second << "  \t" << ite->first << '\n';
	}

	return sResponse;
}


//														
void EnvironmentConnectionManager::ClearRequestQueue (void)
{
	pthread_mutex_lock (&mtx_PendingRequests);	// lock 
	ITERATE (MessageToRequest_map_t, map_PendingRequests, ite)
		delete ite->second;
	map_PendingRequests.clear ();
	dq_PendingRequests.clear ();
	pthread_mutex_unlock (&mtx_PendingRequests);	// unlock 
}


//														
void EnvironmentConnectionManager::RequestClientReconnect (int _iMinutes)
{
}








