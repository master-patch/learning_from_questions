#include "nlp_socket.h"
#include <assert.h>


//																
Buffer::Buffer (void)
{
	z_Data = NULL;
	l_Bytes = 0;
}



//																
Buffer::Buffer (const char* _zData)
{
	l_Bytes = strlen (_zData);
	if (0 == l_Bytes)
	{
		z_Data = NULL;
		return;
	}
	z_Data = realloc (NULL, l_Bytes);
	memcpy (z_Data, _zData, l_Bytes);
}



//																
Buffer::Buffer (const void* _zData, unsigned long _lBytes)
{
	l_Bytes = _lBytes;
	if (0 == l_Bytes)
	{
		z_Data = NULL;
		return;
	}
	z_Data = realloc (NULL, l_Bytes);
	memcpy (z_Data, _zData, l_Bytes);
}



//																
Buffer::Buffer (const Buffer& _rBuffer)
{
	l_Bytes = _rBuffer.l_Bytes;
	if (0 == l_Bytes)
	{
		z_Data = NULL;
		return;
	}
	z_Data = realloc (NULL, l_Bytes);
	memcpy (z_Data, _rBuffer.z_Data, l_Bytes);
}



//																
Buffer::Buffer (const String& _rString)
{
	l_Bytes = _rString.length ();
	if (0 == l_Bytes)
	{
		z_Data = NULL;
		return;
	}
	z_Data = realloc (NULL, l_Bytes);
	memcpy (z_Data, _rString.c_str (), l_Bytes);
}



//																
Buffer::~Buffer (void)
{
	assert ((void*)0x1 != z_Data);
	if (NULL != z_Data)
		free (z_Data);
	z_Data = (void*)0x1;
	l_Bytes = 0;
}


//																
void Buffer::SetData (const void* _zData, unsigned long _lBytes)
{
	l_Bytes = _lBytes;
	if (0 == l_Bytes)
	{
		if (NULL != z_Data)
			free (z_Data);
		z_Data = NULL;
		return;
	}
	z_Data = realloc (z_Data, l_Bytes);
	memcpy (z_Data, _zData, l_Bytes);
}


//																
void Buffer::Append (const char* _zData)
{
	long lExtension = strlen (_zData);
	if (0 == lExtension)
		return;
	z_Data = realloc (z_Data, l_Bytes + lExtension);
	memcpy ((char*)z_Data + l_Bytes, _zData, lExtension);
	l_Bytes += lExtension;
}



//																
void Buffer::Append (const void* _zData, unsigned long _lExtension)
{
	if (0 == _lExtension)
		return;
	z_Data = realloc (z_Data, l_Bytes + _lExtension);
	memcpy ((char*)z_Data + l_Bytes, _zData, _lExtension);
	l_Bytes += _lExtension;
}


//																
void Buffer::DropFront (unsigned long _lDropBytes)
{
	if (_lDropBytes >= l_Bytes)
	{
		Clear ();
		return;
	}

	memmove (z_Data, (char*)z_Data + _lDropBytes, l_Bytes - _lDropBytes);
	z_Data = realloc (z_Data, l_Bytes - _lDropBytes);
	l_Bytes -= _lDropBytes;
}



//																
void Buffer::Clear (void)
{
	if (NULL != z_Data)
		free (z_Data);
	z_Data = NULL;
	l_Bytes = 0;
}


//																
bool Buffer::HasTerminator (char _cTerminator)
{
	if (NULL == z_Data)
		return false;
	assert (0 != l_Bytes);
	return (NULL != memchr (z_Data, _cTerminator, l_Bytes));
}


//																
Buffer Buffer::PopFirstMessageAsBuffer (char _cTerminator)
{
	Buffer oBuffer;
	if (NULL == z_Data)
		return oBuffer;

	void* pEndOfMessage = memchr (z_Data, _cTerminator, l_Bytes);
	if (NULL == pEndOfMessage)
		return oBuffer;

	size_t lMessageLength = ((char*)pEndOfMessage - (char*)z_Data) + 1;
	oBuffer.Append ((char*)z_Data, lMessageLength);
	DropFront (lMessageLength);

	return oBuffer;
}


//																
bool Buffer::ReadFromIndex (size_t _iIndex, void* _pAddress, size_t _iSize) const
{
	if (l_Bytes < _iIndex + _iSize)
		return false;
	void* pFrom = &((char*) z_Data) [_iIndex];
	memcpy (_pAddress, pFrom, _iSize);
	return true;
}


//																
Buffer Buffer::PopFirstMessageAsBuffer (size_t _iLength)
{
	Buffer oBuffer;
	if (NULL == z_Data)
		return oBuffer;
	if (l_Bytes < _iLength)
		return oBuffer;

	oBuffer.Append ((char*)z_Data, _iLength);
	DropFront (_iLength);

	return oBuffer;
}


//																
String Buffer::PopFirstMessageAsString (char _cTerminator)
{
	String sMessage;
	if (NULL == z_Data)
		return sMessage;

	void* pEndOfMessage = memchr (z_Data, _cTerminator, l_Bytes);
	if (NULL == pEndOfMessage)
		return sMessage;

	size_t lMessageLength = ((char*)pEndOfMessage - (char*)z_Data) + 1;
	sMessage.Set ((char*)z_Data, lMessageLength);
	DropFront (lMessageLength);

	return sMessage;
}


//																
Buffer::operator String (void) const
{
	if (NULL != memchr (z_Data, '\0', l_Bytes))
		cerr << "[WARNING]  Buffer being copied to String contains \\x0 character"
			 << endl;
	String sValue;
	sValue.assign ((const char*)z_Data, l_Bytes);
	assert (sValue.length () == l_Bytes);

	return sValue;
}


//																
bool Buffer::operator== (const Buffer& _rBuffer) const
{
	if (l_Bytes != _rBuffer.l_Bytes)
		return false;
	return (0 == memcmp (z_Data, _rBuffer.z_Data, l_Bytes));
}


//																
ostream& operator << (ostream& _rStream, const Buffer& _rBuffer)
{
	for (unsigned long i = 0; i < _rBuffer.l_Bytes; ++ i)
		_rStream << ((const char*)_rBuffer.z_Data) [i];
	return _rStream;
}


