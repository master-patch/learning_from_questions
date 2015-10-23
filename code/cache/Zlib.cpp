#include "Zlib.h"



//																
bool ZlibWrapper::Compress (const String& _rState,
							Buffer* _pBuffer)
{
	int iLength = _rState.length () + 1;
	uLongf iCompressedLength = compressBound (iLength);
	char pCompressed [iCompressedLength];
	int iRet = compress2 ((Bytef*)pCompressed, 
						  &iCompressedLength, 
						  (const Bytef*)(const char*)_rState, 
						  iLength,
						  9);
	if (Z_OK != iRet)
	{
		if (Z_MEM_ERROR == iRet)
			cerr << "[ERROR] ZlibWrapper::Compress failed - not enough memory."
				 << endl;
		else if (Z_BUF_ERROR == iRet)
			cerr << "[ERROR] ZlibWrapper::Compress failed - output buffer too small."
				 << endl;
		else if (Z_STREAM_ERROR == iRet)
			cerr << "[ERROR] ZlibWrapper::Compress failed - level param invalid."
				 << endl;
		return false;
	}

	_pBuffer->SetData (pCompressed, iCompressedLength);
	return true;
}



//																
bool ZlibWrapper::Uncompress (const Buffer& _rBuffer,
							  int _iUncompressedLength,
							  String* _pText)
{
	char pUncompressed [_iUncompressedLength];
	uLongf iUncompressedLength = _iUncompressedLength;
	int iRet = uncompress ((Bytef*) pUncompressed, 
							&iUncompressedLength,
							(Bytef*) ((Buffer&)_rBuffer).GetData (),
							_rBuffer.Length ());
	if (Z_OK != iRet)
	{
		if (Z_MEM_ERROR == iRet)
			cerr << "[ERROR] ZlibWrapper::Uncompress failed - Not enough memory."
				 << endl;
		else if (Z_BUF_ERROR == iRet)
			cerr << "[ERROR] ZlibWrapper::Uncompress failed - Output buffer too small."
				 << endl;
		else if (Z_DATA_ERROR == iRet)
			cerr << "[ERROR] ZlibWrapper::Uncompress failed - Data corrupted or incomplete."
				 << endl;
		else
			cerr << "[ERROR] ZlibWrapper::Uncompress failed - Unknown error."
				 << endl;

		return false;
	}

	assert (iUncompressedLength == (uLongf)_iUncompressedLength);
	*_pText = pUncompressed;
	return true;
}




