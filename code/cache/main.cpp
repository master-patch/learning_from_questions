#include <iostream>
#include <time.h>
#include <signal.h>
#include <nlp_string.h>
#include <nlp_socket.h>
#include <nlp_config.h>
#include "Server.h"
#include "EnvInterface.h"


EnvironmentConnectionManager o_Manager;


void OnSignal (int _iSignal)
{
	cout << "Stopping all clients and closing sockets on termination." << endl;
	o_Manager.Shutdown ();
	AllSockets::CloseAndDeleteAllSockets ();
	exit (0);
}


int main (int argc, const char* argv[])
{
	signal (SIGINT, OnSignal);
	signal (SIGPIPE, SIG_IGN);

	Config::SetCommandLine (argc, argv);

	// initialize cache ...	

	Cache oCache;
	oCache.Load ();
	cout << "   Will save cache every " << (config)"cache_save_period" << " minutes." << endl;

	CacheInterface::InitGlobals ();


	// initialize interface to environment ... 
	cout << "Initializing environment connection manager ..." << endl;
	o_Manager.Init ();


	// initialize server ... 
	cout << "Initializing server ..." << endl;
	Server::Init (&oCache, &o_Manager);


	// start learner server socket ... 
	String sLearnerService ((config)"learner_service_port");
	cout << "Starting learner service on [" << sLearnerService << "]." << endl;
	ServerSocket socLearnerServer;
	socLearnerServer.SetAllowAddressReuse (true);

	if (true == sLearnerService.IsDigit ())
		socLearnerServer.ListenNonBlocking (sLearnerService,
										(int)(config)"service_backlog",
										Server::CreateClient);
	else
		socLearnerServer.ListenUnixDomainNonBlocking (sLearnerService,
										(int)(config)"service_backlog",
										Server::CreateClient);


	// start client server socket ... 
	String sClientService ((config)"client_service_port");
	cout << "Starting client service on [" << sClientService << "]." << endl;
	ServerSocket socClientServer;
	socClientServer.SetAllowAddressReuse (true);

	if (true == sClientService.IsDigit ())
		socClientServer.ListenNonBlocking (sClientService,
										(int)(config)"service_backlog",
										EnvironmentConnectionManager::CreateClient);
	else
		socClientServer.ListenUnixDomainNonBlocking (sClientService,
										(int)(config)"service_backlog",
										EnvironmentConnectionManager::CreateClient);


	long lCacheSavePeriod = 60 * (long)(config)"cache_save_period";
	time_t tLastSave = time (NULL);

	while (true)
	{
		AllSockets::ProcessEvents (1000);

		if (lCacheSavePeriod <= (time (NULL) - tLastSave))
		{
			oCache.Save ();
			tLastSave = time (NULL);
		}
	}
}
