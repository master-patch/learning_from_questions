#include "Server.h"
#include <assert.h>
#include <string.h>
#include <nlp_time.h>

Cache* 							Server::sp_Cache = NULL;
EnvironmentConnectionManager*	Server::sp_EnvConManager = NULL;
bool							Server::b_ShowComms = false;
bool							Server::b_ShowCommsVerbose = false;


//												
Server::Server (void)
{
	p_EnvironmentInterface = NULL;
	b_ServerActive = false;
}


Server::~Server (void)
{
	assert ((ThreadedEnvironmentInterface*)0x1 != p_EnvironmentInterface);
	if (NULL != p_EnvironmentInterface)
		delete p_EnvironmentInterface;
	p_EnvironmentInterface = (ThreadedEnvironmentInterface*)0x1;
}



//												
void Server::Init (Cache* _pCache, EnvironmentConnectionManager* _pManager)
{
	sp_Cache = _pCache;
	sp_EnvConManager = _pManager;
}



//												
ClientSocket* Server::CreateClient (void)
{
	// create server object ...				
	Server* pServer = new Server;
	pServer->SetStandalone (true);
	pServer->p_EnvironmentInterface = new ThreadedEnvironmentInterface (sp_EnvConManager);
	pServer->o_CacheInterface.Init (sp_Cache,
									pServer->p_EnvironmentInterface,
									pServer);
	pServer->b_ServerActive = true;

	// create thread for server object ...	
	pthread_create (&pServer->thr_Server, NULL, RunThread, pServer);
	pthread_detach (pServer->thr_Server);

	return pServer;
}



//												
void Server::OnConnect (void)
{
	cout << "[INFO]  Connected to [" << s_Server << ':' << s_Service << ']' << endl;
	SetNoDelay (true);
}



//												
void Server::OnDisconnect (void)
{
	cout << "[INFO]  Disconnected from [" << s_Server << ':' << s_Service << ']' << endl;
	b_ServerActive = false;
}


//												
String Server::GetRequestId (void)
{
	String sId;
	sId << s_Service << '|' << Time::CurrentTime ();
	return sId;
}


//												
void Server::SendResponse (Buffer& _rResponse)
{
	size_t iLength = _rResponse.Length () + sizeof (size_t);

	Buffer bufSend;
	bufSend.Append (&iLength, sizeof (size_t));
	bufSend.Append (_rResponse);

	SendNonBlocking (bufSend.GetData (), bufSend.Length ());
}


//												
void Server::SendResponse (String& _rResponse)
{
	size_t iLength = _rResponse.length () + 1 + sizeof (size_t);

	Buffer bufSend;
	bufSend.Append (&iLength, sizeof (size_t));
	bufSend.Append (":", 1);
	bufSend.Append ((const char*)_rResponse, _rResponse.length ());

	SendNonBlocking (bufSend.GetData (), bufSend.Length ());
}


//												
void Server::OnReceive (const void* _zData, long _lBytes)
{
	o_Data.Append (_zData, _lBytes);

	while (true)
	{
		size_t iMessageSize;
		if (false == o_Data.ReadFromIndex (0, &iMessageSize, sizeof (iMessageSize)))
			return;
		if (iMessageSize > o_Data.Length ())
			return;

		Buffer bufMessage = o_Data.PopFirstMessageAsBuffer (iMessageSize);
		// [size_t size][char message type][payload...]
		char cType = bufMessage [sizeof (size_t)];
		size_t iOffset = sizeof (size_t) + 1;

		// cout << "message extracted : " << iMessageSize << " " << cType << endl;
		if (':' == cType)
		{
			char* zMessage = (char*) bufMessage.GetData () + iOffset;
			String sMessage (zMessage);

			// cout << "   " << sMessage << endl;

			// manually triggered support features ...	
			if ("help" == sMessage)
			{
				String sResponse;
				sResponse << "Valid support requests:\n"
							 "  help\n"
							 "  save cache\n"
							 "  clear cache\n"
							 "  clear queue\n"
							 "  queue info\n"
							 "  ff client info\n"
							 "  ff client info detailed\n"
							 "  ff response stats\n"
							 "  request client reconnect\n";
				if (true == IsConnected ())
					SendBlocking ((const char*)sResponse, sResponse.length ());
			}

			//									
			else if ("save cache" == sMessage)
			{
				String sResponse;
				if (NULL == sp_Cache)
					sResponse = "[ERROR] Failed to save cache. Pointer to cache is NULL\n";
				else
				{
					sp_Cache->Save ();
					sResponse = "Cache saved.\n";
				}
				if (true == IsConnected ())
					SendBlocking ((const char*)sResponse, sResponse.length ());
			}

			//									
			else if ("clear cache" == sMessage)
			{
				String sResponse;
				if (NULL == sp_Cache)
					sResponse = "[ERROR] Failed to save cache. Pointer to cache is NULL\n";
				else
				{
					sp_Cache->Backup ();
					sp_Cache->Clear ();
					sResponse = "Cache cleared.\n";
				}
				if (true == IsConnected ())
					SendBlocking ((const char*)sResponse, sResponse.length ());
			}

			//									
			else if ("clear queue" == sMessage)
			{
				String sResponse;
				sResponse << "Queue cleared, "
						  << sp_EnvConManager->GetRequestQueueLength ()
						  << " requests dropped.\n";
				sp_EnvConManager->ClearRequestQueue ();

				if (true == IsConnected ())
					SendBlocking ((const char*)sResponse, sResponse.length ());
			}


			//									
			else if ("queue info" == sMessage)
			{
				String sResponse = sp_EnvConManager->GetRequestQueueInfo ();
				if (true == IsConnected ())
					SendBlocking ((const char*)sResponse, sResponse.length ());
			}


			//									
			else if ("ff client info" == sMessage)
			{
				String sResponse = sp_EnvConManager->GetFFClientInfo ();
				if (true == IsConnected ())
					SendBlocking ((const char*)sResponse, sResponse.length ());
			}


			//									
			else if ("ff client info detailed" == sMessage)
			{
				String sResponse = sp_EnvConManager->GetFFClientInfoDetailed ();
				if (true == IsConnected ())
					SendBlocking ((const char*)sResponse, sResponse.length ());
			}


			//									
			else if ("ff response stats" == sMessage)
			{
				String sResponse = sp_EnvConManager->GetFFResponseStats ();
				if (true == IsConnected ())
					SendBlocking ((const char*)sResponse, sResponse.length ());
			}


			else if ("[known world only]" == sMessage)
			{
				String sResponse ("Known-world-only mode active");
				if (true == IsConnected ())
					SendResponse (sResponse);
				cout << "[INFO]  Switching to known-world-only mode." << endl;
				o_CacheInterface.b_KnownWorldOnly = true;
			}
		}


		// domain def caching...					
		else if ('+' == cType)
		{
			char* zMessage = (char*) bufMessage.GetData () + iOffset;
			String sMessage (zMessage);

			// learner line format: :[domain]
			long lDomainId = o_CacheInterface.AddDomain (sMessage);
			// cout << "[INFO] Registered domain. Id : " << lDomainId << endl;

			size_t iLength = 2 * sizeof (size_t) + 1;
			Buffer bufResponse;
			bufResponse.Append (&iLength, sizeof (size_t));
			bufResponse.Append ("d", 1);
			bufResponse.Append (&lDomainId, sizeof (size_t));

			SendNonBlocking (bufResponse.GetData (), bufResponse.Length ());
		}

		// environment interaction ...				
		else if ('?' == cType)
		{
			// learner line format: ?[size_t id][size_t timeout][size_t domain][size_t compressed][size_t uncompressed][problem]

			/*
			for (int i = iOffset; i < iOffset + 50; ++ i)
			{
				if ((0 != i) && (0 == (i % 8)))
					printf (" ");
				unsigned char ch = (unsigned char)bufMessage [i];
				printf ("%02x", ch);
			}
			printf ("\n");
			*/

			size_t iRequestId;
			if (false == bufMessage.ReadFromIndex (iOffset, &iRequestId, sizeof (size_t)))
			{
				cerr << "[ERROR] Error reading task id from buffer." << endl;
				break;
			}
			iOffset += sizeof (size_t);

			size_t iTimeout;
			if (false == bufMessage.ReadFromIndex (iOffset, &iTimeout, sizeof (size_t)))
			{
				cerr << "[ERROR] Error reading task timeout from buffer." << endl;
				break;
			}
			iOffset += sizeof (size_t);

			size_t iDomainId;
			if (false == bufMessage.ReadFromIndex (iOffset, &iDomainId, sizeof (size_t)))
			{
				cerr << "[ERROR] Error reading task domain id from buffer." << endl;
				break;
			}
			iOffset += sizeof (size_t);

			size_t iCompressedProblemSize;
			if (false == bufMessage.ReadFromIndex (iOffset, &iCompressedProblemSize,
												   sizeof (size_t)))
			{
				cerr << "[ERROR] Error reading compressed problem size from buffer."
					 << endl;
				break;
			}
			iOffset += sizeof (size_t);

			size_t iUncompressedProblemSize;
			if (false == bufMessage.ReadFromIndex (iOffset, &iUncompressedProblemSize,
												   sizeof (size_t)))
			{
				cerr << "[ERROR] Error reading uncompressed problem size from buffer."
					 << endl;
				break;
			}
			iOffset += sizeof (size_t);

			/*
			cout << "[INFO] Plan request. "
				 << iRequestId << ' '
				 << iDomainId << ' '
				 << iTimeout << ' '
				 << iCompressedProblemSize << ' '
				 << iUncompressedProblemSize << endl;
			*/


			void* pCompressedProblem = (char*) bufMessage.GetData () + iOffset;
			CompressedBuffer bufCompressedProblem;
			bufCompressedProblem.SetData (pCompressedProblem,
										  iCompressedProblemSize,
										  iUncompressedProblemSize);

			// client line format: [timeout]\x01[domain]\x01[problem]\x01\x05
			String sId;
			sId << GetRequestId () << '\x01' << (long)iRequestId;

			CompressedBuffer* pbufFFResponse;
			CacheResponse_e eRet = o_CacheInterface.Send (sId,
															iDomainId,
															bufCompressedProblem,
															(int)iTimeout,
															&pbufFFResponse);

			Buffer bufResponse;
			if (cr_hit == eRet)
			{
				bufResponse.Append ("c", 1);
				bufResponse.Append (&iRequestId, sizeof (size_t));
				size_t iCompressedSize = pbufFFResponse->CompressedSize ();
				size_t iUncompressedSize = pbufFFResponse->UncompressedSize ();
				bufResponse.Append (&iCompressedSize, sizeof (size_t));
				bufResponse.Append (&iUncompressedSize, sizeof (size_t));
				bufResponse.Append (*pbufFFResponse);

				if (true == IsConnected ())
					SendResponse (bufResponse);
			}

			else if (cr_outside_known_world == eRet)
			{
				// cout << "[outside known world]" << endl;
				bufResponse.Append ("u", 1);
				bufResponse.Append (&iRequestId, sizeof (size_t));

				if (true == IsConnected ())
					SendResponse (bufResponse);
			}
		}

		
		// unknown request ...						
		else
		{
			cerr << "[WARNING] Unknown message type received '"
				 << cType << "'" << endl;
		}
	}
}


//												
String Server::OnResponse (String& _rId, 
						   CompressedBuffer& _rResponse)
{
	// cout << "[sending ff response to learner] " << _rId << endl;
	String_dq_t dqId;
	_rId.Split (dqId, '\x01');
	size_t iRequestId = (long) dqId [1];

	Buffer bufResponse;
	bufResponse.Append ("f", 1);
	bufResponse.Append (&iRequestId, sizeof (size_t));
	size_t iCompressedSize = _rResponse.CompressedSize ();
	size_t iUncompressedSize = _rResponse.UncompressedSize ();
	bufResponse.Append (&iCompressedSize, sizeof (size_t));
	bufResponse.Append (&iUncompressedSize, sizeof (size_t));
	bufResponse.Append (_rResponse);

	/*
	cout << "[INFO] FF response. "
		 << iRequestId << ' '
		 << iCompressedSize << ' '
		 << iUncompressedSize << ' '
		 << bufResponse.Length () << endl;
	*/

	SendResponse (bufResponse);

	return "";
}


//												
void* Server::RunThread (void* _pArg)
{
	Server* pServer = (Server*) _pArg;
	while (true == pServer->b_ServerActive)
	{
		pServer->ProcessEvents (1000);
	};
	return NULL;
}




