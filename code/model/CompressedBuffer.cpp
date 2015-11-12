


#include "CompressedBuffer.h"
#include "Zlib.h"


//													
CompressedBuffer::CompressedBuffer (void)
	: Buffer ()
{
	i_UncompressedSize = 0;
}


//													
CompressedBuffer::CompressedBuffer (const CompressedBuffer& _rBuffer)
	: Buffer (_rBuffer)
{
	i_UncompressedSize = _rBuffer.i_UncompressedSize;
}


//													
CompressedBuffer::CompressedBuffer (const String& _rText)
{
	i_UncompressedSize = _rText.length () + 1;
	if (true == ZlibWrapper::Compress (_rText, this))
		return;

	cerr << "[ERROR] Error during compression of text (length "
		 << i_UncompressedSize
		 << ") in CompressedBuffer::CompressedBuffer ()"
		 << endl;
	i_UncompressedSize = 0;
}


//													
void CompressedBuffer::SetData (const void* _zData,
								size_t _lCompressedSize,
								size_t _lUncompressedSize)
{
	Buffer::SetData (_zData, _lCompressedSize);
	i_UncompressedSize = _lUncompressedSize;
}


//													
bool CompressedBuffer::Compress (const String& _rUncompressedText)
{
	i_UncompressedSize = _rUncompressedText.length () + 1;
	if (true == ZlibWrapper::Compress (_rUncompressedText, this))
		return true;

	cerr << "[ERROR] Error during compression of text (length "
		 << i_UncompressedSize
		 << ") in CompressedBuffer::CompressedBuffer ()"
		 << endl;
	i_UncompressedSize = 0;
	return false;
}


//													
bool CompressedBuffer::Uncompress (String* _pUncompressedText) const
{
	return ZlibWrapper::Uncompress (*this,
									i_UncompressedSize,
									_pUncompressedText);
}


