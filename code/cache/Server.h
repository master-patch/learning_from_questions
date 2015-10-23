#ifndef __CACHE_SERVER__
#define __CACHE_SERVER__

#include <nlp_socket.h>
#include "Cache.h"
#include "CacheInterface.h"
#include "EnvInterface.h"


class Server : public ClientSocket, public CompressedResponseCallback
{
	private:
		static Cache* 							sp_Cache;
		static EnvironmentConnectionManager*	sp_EnvConManager;
		static bool								b_ShowComms;
		static bool								b_ShowCommsVerbose;

		pthread_t								thr_Server;
		bool									b_ServerActive;

		CacheInterface							o_CacheInterface;
		ThreadedEnvironmentInterface*			p_EnvironmentInterface;

		Buffer									o_Data;

		String GetRequestId (void);
		void SendResponse (Buffer& _rResponse);
		void SendResponse (String& _rResponse);

	public:
		Server (void);
		~Server (void);

		static void Init (Cache* _pCache, 
						  EnvironmentConnectionManager* _pManager);
		static ClientSocket* CreateClient (void);
		static void* RunThread (void* _pArg);

		virtual void OnConnect (void);
		virtual void OnReceive (const void* _zData, long _lBytes);
		virtual void OnDisconnect (void);

		virtual String OnResponse (String& _rId, 
								   CompressedBuffer& _rResponse);
};


#endif
