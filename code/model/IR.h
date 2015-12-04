#ifndef __IR_INTERFACE__
#define __IR_INTERFACE__

#include <nlp_string.h>
#include <nlp_string.h>
#include <nlp_socket.h>
#include <hash_map>
using namespace std;

//														
class IR : public ClientSocket
{
	private:
		static bool			b_Active;
		static IR*			p_IR;

		Buffer						o_Data;
		pthread_mutex_t				mtx_QuestionList;
		bool SendMessage (const String& _rMessage);

	public:
		IR (void);
		~IR (void);

		bool Connect (void);
		void Disconnect (void);

		bool SendQuestion (String _sType, String& _sQuestion);
		void OnDisconnect (void);
		bool ReceiveMessage (const void* _zData, long _lBytes);
};

#endif
