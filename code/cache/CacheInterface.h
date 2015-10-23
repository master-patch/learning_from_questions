#ifndef __CACHE__
#define __CACHE__

#include <hash_map>
#include <iostream>
#include <nlp_string.h>
#include <nlp_vector.h>
#include "Cache.h"
using namespace std;

class Task;
class ResponseCallback;
class ResponseMarker;
typedef hash_map <String, Task>		IdToTask_hmp_t;
typedef deque <ResponseMarker*>		ResponseMarker_dq_t;


// -----------------------------------------------------
class ResponseMarker
{
	public:
		String	s_Marker;
		String	s_Category;
		bool	b_CacheSafe;
};


// -----------------------------------------------------
class Task
{
	public:
		unsigned int		ui_Domain;
		CompressedBuffer	buf_CompressedProblem;
		int					i_Timelimit;

		Task (void) {};
		Task (unsigned int _uiDomain,
			  CompressedBuffer& _rProblem,
			  int _iTimelimit)
		{
			ui_Domain = _uiDomain;
			buf_CompressedProblem = _rProblem;
			i_Timelimit = _iTimelimit;
		};

		Task operator= (const Task& _rTask)
		{
			ui_Domain = ((Task&)_rTask).ui_Domain;
			buf_CompressedProblem = ((Task&)_rTask).buf_CompressedProblem;
			i_Timelimit = ((Task&)_rTask).i_Timelimit;
			return *this;
		}
};


// -----------------------------------------------------
class EnvironmentInterface
{
	public:
		virtual ~EnvironmentInterface (void) {};
		virtual void Send (String& _rMessage,
						   ResponseCallback* _pCallback,
						   String& _rCallbackId) = 0;
};

class ResponseCallback
{
	public:
		virtual String OnResponse (String& _rId, String& _rResponse) = 0;
};

class CompressedResponseCallback
{
	public:
		virtual String OnResponse (String& _rId, CompressedBuffer& _rResponse) = 0;
};


// -----------------------------------------------------
enum CacheResponse_e
{
	cr_hit,
	cr_miss,
	cr_outside_known_world,
};

// -----------------------------------------------------
class CacheInterface : public ResponseCallback
{
	private:
		static ResponseMarker_dq_t	dq_ResponseMarkers;

		Cache*						p_Cache;
		IdToTask_hmp_t				hmp_IdToTask;
		EnvironmentInterface*		p_EnvironmentInterface;
		CompressedResponseCallback*	p_ResponseCallbackToServer;

	public:
		static bool					b_Verbose;
		bool						b_KnownWorldOnly;


		CacheInterface (void);
		~CacheInterface (void);

		static void InitGlobals (void);

		void Init (Cache* _pCache,
				   EnvironmentInterface* _pEnvInterface,
				   CompressedResponseCallback* _pServerCallback);

		unsigned int AddDomain (String& _rDomain);
		CacheResponse_e Send (String& _rId,
							  size_t _iDomain,
							  CompressedBuffer& _rProblem,
							  int _iTimelimit,
							  CompressedBuffer** _ppResponse);

		virtual String OnResponse (String& _rId, String& _rResponse);
};



#endif

