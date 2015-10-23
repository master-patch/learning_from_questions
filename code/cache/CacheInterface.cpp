#include "CacheInterface.h"
#include <iostream>
#include <nlp_macros.h>
#include <nlp_config.h>
#include <nlp_filesystem.h>
#include <assert.h>
using namespace std;


bool CacheInterface::b_Verbose = false;
ResponseMarker_dq_t	CacheInterface::dq_ResponseMarkers;



//																
CacheInterface::CacheInterface (void)
{
	p_Cache = NULL;
	p_EnvironmentInterface = NULL;
	b_KnownWorldOnly = false;
}




//																
CacheInterface::~CacheInterface (void)
{
	ITERATE (ResponseMarker_dq_t, dq_ResponseMarkers, ite)
		delete *ite;
	dq_ResponseMarkers.clear ();
}




//																
void CacheInterface::InitGlobals (void)
{
	b_Verbose = (1 == (int)(config)"verbose");

	String_dq_t dqLines;
	File::ReadLines ((config)"ff_response_marker_file", dqLines);
	ITERATE (String_dq_t, dqLines, ite)
	{
		ResponseMarker* pMarker = new ResponseMarker;
		dq_ResponseMarkers.push_back (pMarker);

		ite->LowerCase ();
		String_dq_t dqValues;
		ite->Split (dqValues, '\x01');
		pMarker->b_CacheSafe = (1 == (int)dqValues [0]);
		pMarker->s_Category = dqValues [1];
		pMarker->s_Marker = dqValues [2];
	}

	cout << "Read " << dq_ResponseMarkers.size ()
		 << " ff response markers." << endl;
	// ITERATE (ResponseMarker_dq_t, dq_ResponseMarkers, ite)
	//	cout << "   [" << (*ite)->s_Marker << ']' << endl;
}


//																
void CacheInterface::Init (Cache* _pCache,
						   EnvironmentInterface* _pEnvInterface,
						   CompressedResponseCallback* _pServerCallback)
{
	p_Cache = _pCache;
	p_EnvironmentInterface = _pEnvInterface;
	p_ResponseCallbackToServer = _pServerCallback;
}


//																
unsigned int CacheInterface::AddDomain (String& _rDomain)
{
	return p_Cache->AddDomain (_rDomain);
}


//																
CacheResponse_e CacheInterface::Send (String& _rId, 
									  size_t _iDomainId,
									  CompressedBuffer& _rProblem,
									  int _iTimelimit,
									  CompressedBuffer** _ppResponse)
{
	CompressedBuffer* pCacheHit = p_Cache->Find (_iDomainId, _rProblem, _iTimelimit);
	if (NULL != pCacheHit)
	{
		*_ppResponse = pCacheHit;
		return cr_hit;
	}

	*_ppResponse = NULL;
	if (true == b_KnownWorldOnly)
		return cr_outside_known_world;


	hmp_IdToTask [_rId] = Task (_iDomainId, _rProblem, _iTimelimit);

	String sUncompressedProblem;
	if (false == _rProblem.Uncompress (&sUncompressedProblem))
	{
		cerr << "[ERROR] Failed to uncompress problem in CacheInterface::Send."
			 << endl;
	}

	String sRequest;
	sRequest << _iTimelimit << '\x01'
			 << p_Cache->GetDomain (_iDomainId) << '\x01'
			 << sUncompressedProblem << "\x01\x05";

	
	p_EnvironmentInterface->Send (sRequest, this, _rId);
	return cr_miss;
}


//																
String CacheInterface::OnResponse (String& _rId, String& _rResponse)
{
	_rResponse.Strip ();
	_rResponse.LowerCase ();

	// Make sure this is a response we want to cache ...
	ResponseMarker* pMarker = NULL;
	ITERATE (ResponseMarker_dq_t, dq_ResponseMarkers, ite)
	{
		if (true ==_rResponse.Has ((*ite)->s_Marker))
		{
			pMarker = *ite;
			break;
		}
	}
	
	// compress response...	
	CompressedBuffer bufCompressedSolution (_rResponse);
	
	// Send to client...	
	p_ResponseCallbackToServer->OnResponse (_rId, bufCompressedSolution);

	// Save to cache...		
	IdToTask_hmp_t::iterator	ite;
	ite = hmp_IdToTask.find (_rId);
	if (hmp_IdToTask.end () != ite)
	{
		Task& rTask = ite->second;

		if ((NULL != pMarker) && (true == pMarker->b_CacheSafe))
		{
			if ("" != _rResponse)
				p_Cache->Add (rTask.ui_Domain,
							  rTask.buf_CompressedProblem,
							  rTask.i_Timelimit,
							  bufCompressedSolution);
		}
		hmp_IdToTask.erase (ite);
	}


	String sCategory;
	if ("" == _rResponse)
		sCategory = "empty";
	else if (NULL == pMarker)
		sCategory = "unknown";
	else
		sCategory = pMarker->s_Category;
	return sCategory;
}







