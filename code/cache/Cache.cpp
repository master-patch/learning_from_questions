#include "Cache.h"
#include <nlp_macros.h>
#include <nlp_config.h>
#include <nlp_filesystem.h>
#include <nlp_time.h>
#include <assert.h>
using namespace std;



// ================================================================
Cache::Cache (void)
{
	pthread_rwlock_init (&rwl_CacheAccess, NULL);
	b_Modified = false;
	d_Hits = 0;
	d_Total = 0;
}


Cache::~Cache (void)
{
	Clear ();
	pthread_rwlock_destroy (&rwl_CacheAccess);
}


//																
void Cache::Clear (void)
{
	hmp_DomainToId.clear ();
	hmp_ProblemToId.clear ();
	hmp_TaskToResponse.clear ();
}


//																
CompressedBuffer* Cache::Find (unsigned int _uiDomain,
							   const CompressedBuffer& _rProblem,
							   int _iTimelimit)
{
	LockForReading ();
	++ d_Total;

	// get problem id...		
	ProblemToId_hmp_t::iterator	iteProblem;
	iteProblem = hmp_ProblemToId.find (_rProblem);
	if (hmp_ProblemToId.end () == iteProblem)
	{
		Unlock ();
		return NULL;
	}
	unsigned int uiProblemId = iteProblem->second;
	

	// get planner output...	
	String sTaskId;
	sTaskId << (long)_uiDomain << '\x01' << (long)uiProblemId << '\x01' << _iTimelimit;

	TaskToResponse_hmp_t::iterator	ite;
	ite = hmp_TaskToResponse.find (sTaskId);
	if (hmp_TaskToResponse.end () == ite)
	{
		Unlock ();
		return NULL;
	}

	++ d_Hits;
	Unlock ();
	return &ite->second;
}


//																
unsigned int Cache::AddDomain (String& _rDomain)
{
	LockForWriting ();

	// insert domain if necessary...	
	pair <DomainToId_hmp_t::iterator, bool> pairInsertD;
	pairInsertD = hmp_DomainToId.insert (make_pair (_rDomain, hmp_DomainToId.size ()));
	unsigned int uiDomainId = pairInsertD.first->second;

	hmp_IdToDomain [uiDomainId] = _rDomain;
	b_Modified |= pairInsertD.second;

	Unlock ();
	return uiDomainId;
}


//																
String& Cache::GetDomain (unsigned int _uiDomain)
{
	return hmp_IdToDomain [_uiDomain];
}


//																
void Cache::Add (unsigned int _uiDomain,
				 CompressedBuffer& _rProblem,
				 int _iTimelimit,
				 CompressedBuffer& _rResponse)
{
	LockForWriting ();

	// insert problem if necessary...	
	unsigned int uiProblemId;
	ProblemToId_hmp_t::iterator	ite;
	ite = hmp_ProblemToId.find (_rProblem);
	if (hmp_ProblemToId.end () == ite)
	{
		uiProblemId = hmp_ProblemToId.size ();
		hmp_ProblemToId.insert (make_pair (_rProblem, uiProblemId));
	}
	else
		uiProblemId = ite->second;


	// insert task if necessary...		
	String sTaskId;
	sTaskId << (long)_uiDomain << '\x01' << (long)uiProblemId << '\x01' << _iTimelimit;
	hmp_TaskToResponse.insert (make_pair (sTaskId, _rResponse));

	b_Modified = true;

	Unlock ();
}


//																
bool Cache::Load (void)
{
	LockForWriting ();

	bool bRet = LoadThreadUnsafe ();
	b_Modified = false;

	Unlock ();
	return bRet;
}


//																
bool Cache::Save (void)
{
	if (false == b_Modified)
		return true;

	String sTempPath = (config)"temp_cache_path";

	// remove old temporary files...			
	String_dq_t	dqOldFiles;
	if (true ==	Path::GetPathList (sTempPath, dqOldFiles))
	{
		if (false == dqOldFiles.empty ())
		{
			String_set_t setOldFiles;
			setOldFiles.insert (dqOldFiles.begin (), dqOldFiles.end ());

			dqOldFiles.clear ();
			ITERATE (String_set_t, setOldFiles, ite)
			{
				String sFileName (*ite);
				if (false == sFileName.Has ("/env.cache.tmp."))
					continue;
				dqOldFiles.push_back (*ite);
			}

			if (false == dqOldFiles.empty ())
				dqOldFiles.pop_back ();

			if (false == dqOldFiles.empty ())
			{
				ITERATE (String_dq_t, dqOldFiles, ite)
					Path::RemoveFile (*ite);

				cout << "Deleted " << dqOldFiles.size () 
					 << " old temporary files." << endl;
			}
		}
	}


	// lock cache & save to temporary file ...	
	LockForWriting ();
	cout << "Saving Cache; ("
		 << hmp_TaskToResponse.size () << ", "
		 << hmp_DomainToId.size () << ", "
		 << hmp_ProblemToId.size () << ") nodes @ "
		 << Time::sDateTime () << endl;
	cout << "Hit ratio : " << d_Hits / d_Total << endl;
	d_Hits = 0;
	d_Total = 0;

	String sTempCacheFileName;
	bool bRet = SaveThreadUnsafe (sTempCacheFileName);
	Unlock ();
	
	// SaveInternal returns false only if		
	// the cache is uninitialized, so there's	
	// nothing to save...						
	if (false == bRet)
		return true;
	
	// move temporary file to actual name...	
	String sCacheFileName = (config)"cache_file_name";
	if (true == Path::Exists (sCacheFileName))
	{
		if (false == Path::RemoveFile (sCacheFileName))
			return false;
	}
	if (false == Path::MoveFile (sTempCacheFileName, sCacheFileName))
		return false;

	b_Modified = false;
	return true;
}



//																
bool Cache::LoadThreadUnsafe (void)
{
	File file;
	if (false == Path::Exists ((config)"cache_file_name"))
	{
		cout << "Cache file does not exist, will be created anew." << endl;
		return true;
	}
	if (false == file.Open ((config)"cache_file_name"))
		return false;

	cout << "Loading cache..." << endl;

	char cSection = ' ';
	bool bHaveId = false;

	String sLine;
	String sId;
	String sText;
	while (true == file.ReadLine (sLine))
	{
		String sStrippedLine (sLine);
		sStrippedLine.Strip ();

		if ("[DOMAINS]" == sStrippedLine)
		{
			cSection = 'd';
			continue;
		}
		if ("[PROBLEMS]" == sStrippedLine)
		{
			cSection = 'r';
			continue;
		}
		if ("[PLANS]" == sStrippedLine)
		{
			cSection = 'p';
			continue;
		}

		if ("\x10" == sStrippedLine)
		{
			bHaveId = true;
			continue;
		}
		if ("\x11" == sStrippedLine)
		{
			sId.Strip ();
			sText.Strip ();

			if ('d' == cSection)
				hmp_DomainToId [sText] = (long) sId;
			else if ('r' == cSection)
				hmp_ProblemToId [sText] = (long) sId;
			else if ('p' == cSection)
				hmp_TaskToResponse [sId] = sText;
			else
			{
				cerr << "[ERROR] unknown section type [" 
					 << cSection << "] with id ["
					 << sId << "] and text ["
					 << sText << "]" << endl;
			}
			bHaveId = false;
			sId = "";
			sText = "";
			continue;
		}

		if (false == bHaveId)
			sId << sLine;
		else
			sText << sLine << '\n';
	}

	if (("" != sId) && ("" != sText))
	{
		sId.Strip ();
		sText.Strip ();

		if ('d' == cSection)
			hmp_DomainToId [sText] = (long) sId;
		else if ('r' == cSection)
			hmp_ProblemToId [sText] = (long) sId;
		else if ('p' == cSection)
			hmp_TaskToResponse [sId] = sText;
		else
		{
			cerr << "[ERROR] unknown section type [" 
				 << cSection << "] with id ["
				 << sId << "] and text ["
				 << sText << "]" << endl;
		}
	}


	cout << "   Cache : loaded  ("
		 << hmp_TaskToResponse.size () << ", "
		 << hmp_DomainToId.size () << ", "
		 << hmp_ProblemToId.size ()
		 << ") states." << endl;
	return true;
}



//																
bool Cache::SaveThreadUnsafe (String& _rFileName)
{
	time_t t = time (NULL);
	char zTime [201];
	#ifdef NDEBUG
	strftime (zTime, 200, "%Y-%m-%d-%H-%M-%S", localtime (&t));
	#else
	size_t iTimeLen = strftime (zTime, 200, "%Y-%m-%d-%H-%M-%S", localtime (&t));
	assert (iTimeLen < 200);
	#endif

	String sTempPath = (config)"temp_cache_path";
	_rFileName << sTempPath << "/env.cache.tmp." << zTime;

	File file (_rFileName, ios_base::out);

	file << "[DOMAINS]" << endl;
	ITERATE (DomainToId_hmp_t, hmp_DomainToId, ite)
	{
		file << ite->second << "\n\x10\n"
			 << ite->first << "\n\x11\n";
	}
	file << endl;

	file << "[PROBLEMS]" << endl;
	ITERATE (ProblemToId_hmp_t, hmp_ProblemToId, ite)
	{
		const CompressedBuffer& rCompressedProblem = ite->first;
		String sProblem;
		if (false == rCompressedProblem.Uncompress (&sProblem))
		{
			cerr << "[ERROR] Failed to compressed problem while saving!"
				 << endl;
			continue;
		}

		file << ite->second << "\n\x10\n"
			 << sProblem << "\n\x11\n";
	}
	file << endl;

	file << "[PLANS]" << endl;
	ITERATE (TaskToResponse_hmp_t, hmp_TaskToResponse, ite)
	{
		file << ite->first << "\n\x10\n"
			 << ite->second << "\n\x11\n";
	}
	file << endl;

	file.flush ();
	file.close ();

	return true;
}


//																
bool Cache::Backup (void)
{
	if (false == Cache::Save ())
		return false;

	time_t t = time (NULL);
	char zTime [201];
	#ifdef NDEBUG
	strftime (zTime, 200, "%Y-%m-%d-%H-%M-%S", localtime (&t));
	#else
	size_t iTimeLen = strftime (zTime, 200, "%Y-%m-%d-%H-%M-%S", localtime (&t));
	assert (iTimeLen < 200);
	#endif

	String sCacheFileName = (config)"cache_file_name";
	String sBackupFileName (sCacheFileName);
	sBackupFileName << '.' << zTime << ".backup-on-clear";

	if (false == Path::MoveFile (sCacheFileName, sBackupFileName))
		return false;
	
	return true;
}

