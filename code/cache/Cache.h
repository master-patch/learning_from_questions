#ifndef __CACHE_LIB__
#define __CACHE_LIB__

#include <hash_map>
#include <iostream>
#include <nlp_string.h>
#include "CompressedBuffer.h"
using namespace std;


// typedef hash_map <unsigned long, String>	TaskToResponse_hmp_t;
typedef hash_map <String, CompressedBuffer>			TaskToResponse_hmp_t;
typedef hash_map <String, unsigned int>				DomainToId_hmp_t;
typedef hash_map <CompressedBuffer, unsigned int>	ProblemToId_hmp_t;
typedef hash_map <unsigned int, String>				IdToDomain_hmp_t;



// -----------------------------------------------------
class Cache
{
	protected:
		pthread_rwlock_t				rwl_CacheAccess;
		DomainToId_hmp_t				hmp_DomainToId;
		ProblemToId_hmp_t				hmp_ProblemToId;
		TaskToResponse_hmp_t			hmp_TaskToResponse;
		IdToDomain_hmp_t				hmp_IdToDomain;
		double							d_Hits;
		double							d_Total;
		bool							b_Modified;

		bool LoadThreadUnsafe (void);
		bool SaveThreadUnsafe (String& _rFileName);

	public:
		Cache (void);
		virtual ~Cache (void);

		void Clear (void);

		virtual bool Load (void);
		bool Save (void);
		bool Backup (void);

		void LockForReading (void)
			{ pthread_rwlock_rdlock (&rwl_CacheAccess); };
		void LockForWriting (void)
			{ pthread_rwlock_wrlock (&rwl_CacheAccess); };
		void Unlock (void)
			{ pthread_rwlock_unlock (&rwl_CacheAccess); };

		unsigned int AddDomain (String& _rDomain);
		String& GetDomain (unsigned int _uiDomain);

		void Add (unsigned int _uiDomain,
				  CompressedBuffer& _rProblem,
				  int _iTimelimit,
				  CompressedBuffer& _rResponse);

		CompressedBuffer* Find (unsigned int _uiDomain,
								const CompressedBuffer& _rProblem,
								int _iTimelimit);
};



#endif

