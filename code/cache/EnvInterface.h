#ifndef __ENV_INTERFACE_
#define __ENV_INTERFACE_

#include <set>
#include <map>
#include <deque>
#include <nlp_string.h>
#include <nlp_socket.h>
#include <pthread.h>
#include "CacheInterface.h"


class CallbackInfo;
class Request;
class EnvironmentConnection;
class EnvironmentConnectionManager;
class ThreadedEnvironmentInterface;
typedef set <EnvironmentConnection*>
							EnvironmentConnection_set_t;
typedef set <ThreadedEnvironmentInterface*>
							ThreadedEnvironmentInterface_set_t;
typedef map <EnvironmentConnection*, ThreadedEnvironmentInterface*>	
							EnvironmentConnectionToThreadedEnvironmentInterface_map_t;
typedef map <String, int>	FFResponseCategoryToCount_map_t;

typedef deque <CallbackInfo>	CallbackInfo_dq_t;
typedef deque <Request*>		Request_dq_t;
typedef map <String, Request*>	MessageToRequest_map_t;



// -----------------------------------------------------
class CallbackInfo
{
	public:
		ResponseCallback*	p_Callback;
		String				s_CallbackId;

		CallbackInfo (ResponseCallback* _pCallback, String& _sCallbackId)
		{
			p_Callback = _pCallback;
			s_CallbackId = _sCallbackId;
		};
};


// -----------------------------------------------------
class Request
{
	public:
		String				s_Message;
		CallbackInfo_dq_t	dq_CallbackInfo;
	
		Request (String& _sMessage,
				 ResponseCallback* _pCallback, 
				 String& _sCallbackId)
		{
			s_Message = _sMessage;
			dq_CallbackInfo.push_back (CallbackInfo (_pCallback, _sCallbackId));
		};

		void AddCallback (ResponseCallback* _pCallback,
						  String& _sCallbackId)
		{
			dq_CallbackInfo.push_back (CallbackInfo (_pCallback, _sCallbackId));
		};

		/*
		Request operator= (const Request& _rRight)
		{
			s_Message = ((Request&)_rRight).s_Message;
			p_Callback = ((Request&)_rRight).p_Callback;
			s_CallbackId = ((Request&)_rRight).s_CallbackId;
			return *this;
		}
		*/
};



// -----------------------------------------------------
class EnvironmentConnection : public ClientSocket
{
	private:
		pthread_mutex_t					mtx_Shutdown;
		Buffer							o_Buffer;

	public:
		EnvironmentConnectionManager*	p_Manager;
		Request*						p_CurrentRequest;
		long							l_Usage;
		int								i_TimeoutSeconds;
		FFResponseCategoryToCount_map_t	map_ResponseCategoryToCount;

		EnvironmentConnection (void);
		~EnvironmentConnection (void);

		void ClearBuffer (void)
		{ o_Buffer.Clear (); };

		void  OnError (const char* _zError);
		virtual void OnConnect (void);
		virtual void OnDisconnect (void);
		virtual void OnReceive (const void* _zData, long _lBytes);
};




// -----------------------------------------------------
class EnvironmentConnectionManager
{
	friend class EnvironmentConnection;

	private:
		static EnvironmentConnectionManager*	p_Manager;
		pthread_t								thr_RequestQueue;
		pthread_mutex_t							mtx_Access;
		pthread_mutex_t							mtx_PendingRequests;
		MessageToRequest_map_t					map_PendingRequests;
		Request_dq_t							dq_PendingRequests;


	protected:
		EnvironmentConnection_set_t			set_AllConnections;
		EnvironmentConnection_set_t			set_FreeConnections;

		void CloseConnection (EnvironmentConnection* _pConnection);

	public:
		EnvironmentConnectionManager (void);
		~EnvironmentConnectionManager (void);

		static ClientSocket* CreateClient (void);

		void Init (void);
		void Shutdown (void);

		long GetRequestQueueLength (void);
		String GetRequestQueueInfo (void);
		String GetFFClientInfo (void);
		String GetFFClientInfoDetailed (void);
		String GetFFResponseStats (void);
		void ClearRequestQueue (void);
		void RequestClientReconnect (int _iMinutes);

		void QueueRequest (String& _rMessage,
						   ResponseCallback* _pCallback,
						   String& _sCallbackId);

		// EnvironmentConnection* GetConnection (ThreadedEnvironmentInterface* _pInterface);
		bool ProcessRequest (EnvironmentConnection* _pConnection,
							 Request* _pRequest);
		static void* RunThread (void* _pArg);
		void ReleaseConnection (EnvironmentConnection* _pConnection);
};


// -----------------------------------------------------
class ThreadedEnvironmentInterface : public EnvironmentInterface
{
	friend class EnvironmentConnectionManager;

	protected:
		EnvironmentConnectionManager*	p_Manager;

	public:
		static bool						b_ShowComms;
		static bool						b_ShowCommsVerbose;

		//										
		ThreadedEnvironmentInterface (EnvironmentConnectionManager* _pManager)
		{ p_Manager = _pManager; };

		//										
		~ThreadedEnvironmentInterface (void)
		{
			assert ((EnvironmentConnectionManager*) 0x1 != p_Manager);
			p_Manager = (EnvironmentConnectionManager*) 0x1;
		}

		//										
		virtual void Send (String& _rMessage,
						   ResponseCallback* _pCallback,
						   String& _rCallbackId)
		{
			p_Manager->QueueRequest (_rMessage, _pCallback, _rCallbackId);
		}
};




#endif
