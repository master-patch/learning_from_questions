#ifndef __ZLIB__
#define __ZLIB__

#include <nlp_string.h>
#include <nlp_socket.h>
#include <zlib.h>
using namespace std;



// -----------------------------------------------------
class ZlibWrapper
{
	public:
		static bool Compress (const String& _rText,
							  Buffer* _pBuffer);
		static bool Uncompress (const Buffer& _rBuffer,
								int _iUncompressedLength,
								String* _pText);
};



#endif

