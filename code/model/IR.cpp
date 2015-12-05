#include "IR.h"
#include "CompressedBuffer.h"
#include <nlp_config.h>
#include <nlp_macros.h>
#include <nlp_filesystem.h>
#include <assert.h>

#define RECEIVE_BUFFER	2048

// Book-keeping
bool IR::b_Active = false;
IR* IR::p_IR = NULL;
										
IR::IR (void)
{
	// p_Callback = NULL;
	pthread_mutex_init (&mtx_QuestionList, NULL);
}
											
IR::~IR (void)
{
	Disconnect ();
	pthread_mutex_destroy (&mtx_QuestionList);
}

void IR::Disconnect (void)
{
	b_Active = false;
	sleep (1);
	Socket::Close ();
}

void IR::OnDisconnect (void)
{
	cout << "[EE] Socket connection to cache server lost, attempting to reconnect."
		 << endl;

	exit (1);
}

bool IR::Connect (void)
{
	String sServer = (config)"ir_host";
	String sPort = (config)"ir_service";

	SetStandalone (true);

	if (false == ClientSocket::ConnectBlocking (sServer, sPort))
	{
		cout << "   [EE] Failed to connect to IR server at "
			 << sServer << ':' << sPort << endl;
		return false;
	}

	b_Active = true;
	// pthread_create (&thr_SocketLoop, NULL, RunThread, this);
	// pthread_detach (thr_SocketLoop);

	return true;
}
										
bool IR::SendMessage (const String& _rMessage)
{
	// TODO: what is the +1 for?
	int iLength = _rMessage.length ();

	// TODO: make sure that instead of sending the length, we send EOM
	Buffer bufMsg;
	bufMsg.Append (&iLength, sizeof (int));
	bufMsg.Append ((const char*)_rMessage, _rMessage.length ());

	// assert (iLength == bufMsg.Length ());
	return ClientSocket::SendBlocking (bufMsg.GetData (), bufMsg.Length ());
}

bool IR::ReceiveMessage (const void* _zData, long _lBytes)
{
	return ClientSocket::ReceiveBlocking (_zData, _lBytes, 1000);
}

//			
bool IR::SendQuestion (String _sType, String& _sQuestion)
{
	// TODO: check if we really need to lock the thread
	// pthread_mutex_lock (&mtx_QuestionList);
	// pthread_mutex_unlock (&mtx_QuestionList);

	String question;
	question << _sType << " " << _sQuestion;
	if (false == SendMessage (question))
		return false;

	return true;
}
										
