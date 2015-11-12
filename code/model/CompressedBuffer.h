#ifndef __COMPRESSED_BUFFER__
#define __COMPRESSED_BUFFER__

#include <nlp_socket.h>


class CompressedBuffer : public Buffer
{
	private:
		size_t	i_UncompressedSize;

	public:	
		CompressedBuffer (void);
		CompressedBuffer (const CompressedBuffer& _rBuffer);
		CompressedBuffer (const String& _rText);

		void SetData (const void* _zData,
					  size_t _lCompressedSize,
					  size_t _lUncompressedSize);
		bool Compress (const String& _rUncompressedText);
		bool Uncompress (String* _pUncompressedText) const;

		size_t UncompressedSize (void) const
		{ return i_UncompressedSize; };
		size_t CompressedSize (void) const
		{ return Buffer::Length (); };

		bool operator== (const CompressedBuffer& _rBuffer) const
		{ return *((Buffer*)this) == (const Buffer&)_rBuffer; };
};


namespace __gnu_cxx
{
	template <>
	struct hash<CompressedBuffer>
	{
		size_t operator()(const CompressedBuffer& b) const
		{
			unsigned long __b = 0;
			for (unsigned long i = 0;i < b.Length (); ++i) {
				__b ^= (( __b << 5) + (__b >> 2) + (int) b[i]);
      }
			return size_t(__b);
		}
	};
}



#endif
