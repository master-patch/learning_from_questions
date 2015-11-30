#ifndef __IR_INTERFACE__
#define __IR_INTERFACE__

#include <nlp_string.h>
#include <nlp_string.h>
#include <nlp_socket.h>
#include <hash_map>
using namespace std;
												
class IRAnswer
{
	public:
		size_t				i_Id;
		String				s_Sentence;
		String				s_Features;

		IRAnswer (void)
		{
			i_Id = -1;
		};
};

	
class IRCallback
{
	public:
		virtual void OnIRAnswer (int _iIndex, IRAnswer& _rResponse) = 0;
};


//														
class IR : public ClientSocket
{
	private:
		static bool			b_Active;
		static IR*			p_IR;

		Buffer						o_Data;
		pthread_t					thr_SocketLoop;
		pthread_mutex_t				mtx_QuestionList;
		IRCallback*					p_Callback;

		bool SendMessage (const String& _rMessage);
		bool SendMessage (const Buffer& _rMessage);

	public:
		IR (void);
		~IR (void);

		bool Connect (void);
		void Disconnect (void);
		void SetCallback (IRCallback* _pCallback)
		{ p_Callback = _pCallback; };

		bool SendQuestion (String _sType,
							String& _sQuestion);
		void OnReceive (const void* _zData, long _lBytes);
		void OnDisconnect (void);
		void ClearConnection (void);
		static void* RunThread (void* _pArg);
};


#endif
