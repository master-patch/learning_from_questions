#include "Problems.h"
#include "PddlInterface.h"
#include <assert.h>


//											
Problem::Problem (String& _rProblem, String& _rFileName)
{
	s_FileName = _rFileName;
	s_Problem = _rProblem;
	b_SubgoalsNotNeeded = false;
	p_SolutionSequence = NULL;
	d_SolutionReward = 0;
	i_SolutionIteration = -100;

	PddlProblem* pPddl = PddlInterface::ParseProblemPddl (s_Problem);
	s_PddlPreamble = pPddl->o_StartState.s_Preamble;
	delete pPddl;
	p_PddlProblem = NULL;
}


//											
Problem::~Problem (void)
{
	delete p_PddlProblem;
	delete p_SolutionSequence;
	p_PddlProblem = (PddlProblem*)0x1;
}


//											
PddlProblem& Problem::GetPddlProblem (void)
{
	if (NULL == p_PddlProblem)
		p_PddlProblem = PddlInterface::ParseProblemPddl (s_Problem);

	return *p_PddlProblem;
}


//									
bool Problem::AddSolution (SubgoalSequence* _pSequence,
						   double _dReward,
						   int _iIteration)
{
	String sSolution = _pSequence->ToLogString ();
	SolutionsToCount_map_t::iterator	ite;
	ite = map_SolutionsToCount.find (sSolution);
	if (map_SolutionsToCount.end () == ite)
		map_SolutionsToCount [sSolution] = 1;
	else
		++ ite->second;

	if (d_SolutionReward >= _dReward)
		return false;

	delete p_SolutionSequence;
	p_SolutionSequence = _pSequence;
	d_SolutionReward = _dReward;
	i_SolutionIteration = _iIteration;

	return true;
}


//									
bool Problem::Load (void)
{
	cout << "Loading planning problems..." << endl;
	String sPath ((config)"problems_path");

	String_dq_t dqFiles;
	if (false == Path::GetFileList (sPath, dqFiles))
	{
		cerr << "[ERROR] Failed to get problem file list."
			 << endl;
		return false;
	}

	ITERATE (String_dq_t, dqFiles, ite)
	{
		String sFilePath;
		sFilePath << sPath << '/' << *ite;
		if (false == Path::IsRegularFile (sFilePath))
			continue;

		String_dq_t dqLines;
		if (false == File::ReadLines (sFilePath, dqLines))
			continue;

		String sProblem;
		sProblem.Join (dqLines, '\n');
		dq_Problems.push_back (Problem (sProblem, *ite));
	}

	cout << "   " << dq_Problems.size () << " problems loaded." << endl;
	return true;
}


//									
long Problem::TotalSolvedProblems (void)
{
	long lTotalSolutions = 0;
	ITERATE (Problem_dq_t, dq_Problems, iteProblem)
	{
		Problem& rProblem = *iteProblem;
		if ((false == rProblem.b_SubgoalsNotNeeded) &&
			(true == rProblem.map_SolutionsToCount.empty ()))
			continue;
		++ lTotalSolutions;
	}
	return lTotalSolutions;
}


//									
bool Problem::LogSolutions (const char* _zPath)
{
	if (false == Path::Exists (_zPath))
		Path::CreatePath (_zPath, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
	if (false == Path::IsDirectory (_zPath))
	{
		cerr << "[ERROR] Output path for problem solutions is not a directory.\n"
			 << _zPath << endl;
		return false;
	}
	if (false == Path::Writable (_zPath))
	{
		cerr << "[ERROR] Output path for problem solutions is not writable.\n"
			 << _zPath << endl;
		return false;
	}

	ITERATE (Problem_dq_t, dq_Problems, iteProblem)
	{
		Problem& rProblem = *iteProblem;
		if (true == rProblem.map_SolutionsToCount.empty ())
			continue;

		String sFilePath;
		sFilePath << _zPath << '/' << rProblem.s_FileName;

		File file;
		if (false == file.Open (sFilePath, ios_base::out))
		{
			cerr << "[ERROR] Failed to open file for writing : " 
				 << sFilePath << endl;
			continue;
		}

		file << rProblem.p_PddlProblem->o_PartialGoalState.GetPredicatePddlString ()
			 << "\n===========================\n";
		if (true == rProblem.b_SubgoalsNotNeeded)
			file << "[SUBGOALS NOT NEEDED]" << endl;
		else
		{
			ITERATE (SolutionsToCount_map_t, rProblem.map_SolutionsToCount, ite)
			{
				file << ite->second << '\n'
					 << ite->first
					 << "\n---------------------------\n";
			}
		}

		file.flush ();
		file.Close ();
	}
	return true;
}


//									
void Problem::PrintSolvedProblems (void)
{
	ITERATE (Problem_dq_t, dq_Problems, iteProblem)
	{
		Problem& rProblem = *iteProblem;
		cout << "   " << rProblem.s_FileName;

		if (true == rProblem.map_SolutionsToCount.empty ())
		{
			cout << "  [NOT SOLVED]" << endl;
			continue;
		}
		if (true == rProblem.b_SubgoalsNotNeeded)
		{
			cout << "  [SUBGOALS NOT NEEDED]" << endl;
			continue;
		}

		String sMostCommonSolution;
		int iCount = 0;
		ITERATE (SolutionsToCount_map_t, rProblem.map_SolutionsToCount, ite)
		{
			if (iCount >= ite->second)
				continue;
			iCount = ite->second;
			sMostCommonSolution = ite->first;
		}

		sMostCommonSolution.Replace ("\n", " ");
		cout << "  " << sMostCommonSolution << endl;
	}
}



