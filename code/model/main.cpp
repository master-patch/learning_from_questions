#include <iostream>
#include "Learner.h"
#include "Problems.h"
#include <nlp_string.h>
#include <nlp_filesystem.h>
#include <nlp_config.h>

using namespace std;

Problem_dq_t	Problem::dq_Problems;


//													
String GetFileName (String _sPath)
{
	String sTarget;
	size_t iNameStart = _sPath.ReverseFind ("/");
	if (string::npos != iNameStart)
		sTarget << _sPath.substr (iNameStart);
	else
		sTarget << _sPath;
	return sTarget;
};


//													
void TestPddlLibrary (void)
{
    PddlDomain* domain;
    PddlProblem* problem;
    PddlPlan* plan = NULL;
    {
        String_dq_t	dqLines;
        File::ReadLines ((config)"test_domain", dqLines);
        String sPddl;
        sPddl.Join (dqLines, '\n');
        domain = PddlInterface::ParseDomainPddl (sPddl);
        // cout << *domain << endl;
        //delete domain;
    } 
    {
        String_dq_t	dqLines;
        File::ReadLines ((config)"test_problem", dqLines);
        String sPddl;
        sPddl.Join (dqLines, '\n');
        problem = PddlInterface::ParseProblemPddl (sPddl);
        // cout << *problem << endl;
        //delete problem;
    }
    {
        String_dq_t dqLines;
        File::ReadLines ((config)"test_plan", dqLines);
        String sPlan;
        sPlan.Join(dqLines, '\n');
        FFPlaningOutcome_e eOutcome = FFInterface::FFExtractOutcome(sPlan);
        if (eOutcome == po_plan_found || eOutcome == po_goal_already_satisfied)
        {
            sPlan = FFInterface::ExtractPlan(sPlan);
            plan = PddlInterface::ParsePlan(*domain, sPlan);
        }
    }

    if (plan != NULL)
    {
		PddlPredicate_dq_t dqPredicates;
        PddlState* endState = PddlInterface::ComputeEndStateFast (*problem, *plan, dqPredicates);
        String sNextPddl = endState->GetPddlString();
        cout << sNextPddl << endl;
    }
    // String sPlan = "move m0_0 m0_1\nmove m0_1 m1_1\n";
    // PddlPlan* plan = PddlInterface::ParsePlan(*domain, sPlan);
    
    //cout << "Computing end state.." << endl;
    // PddlState* endState = PddlInterface::ComputeEndStateFast (*domain, *problem, *plan);
    //cout << "The end state is: " << endl;
    // cout << endState->GetPddlString () << endl;
    // cout << endState->s_Preamble << endl;
}


//													
int main (int argc, const char** argv)
{
	Config::SetCommandLine (argc, argv);

	// pddl readup test code...		
	if (1 == (int)(config)"test_pddl")
	{
		TestPddlLibrary ();
		return 1;
	}


	cout << "High-level planning learner. Version "
		 << __DATE__ << ' ' << __TIME__ << endl;

	
	// copy run configuration to output path.
	{
		// copy config file to output path ...	
		{
			String sConfigFile (Config::GetConfigFileName ());
			String sTarget;
			sTarget << (config)"output_path" << '/'
					<< GetFileName (sConfigFile);
			if (true == Path::Exists (sTarget))
				Path::RemoveFile (sTarget);
			Config::WriteConfig (sTarget);
		}

		// copy binary to output path ...		
		if (1 == (int)(config)"copy_binary_to_output_path")
		{
			String sTarget;
			sTarget << (config)"output_path" << '/'
					<< GetFileName (argv [0]);
			if (true == Path::Exists (sTarget))
				Path::RemoveFile (sTarget);
			Path::CopyFile (argv [0], sTarget);
		}
	}


	// test feature computation...	
    if(1 == (int)(config)"test_pddl_features")
	{
        // SubgoalPolicy policy;
        // policy.Init();
        // policy.Test();
        return 1;
    }
    

	// learner...					
	SubgoalLearner	o_Learner;
	if (false == Problem::Load ())
		return 1;
	cout << "Learner init..." << endl;
	if (false == o_Learner.Init ())
		return 1;
  cout << "Trying to plan on a sequence with questions" << endl;
  o_Learner.TryLinkingSubgoals ();
	cout << "Trying planning on full tasks..." << endl;
	o_Learner.TryPlanningOnFullTasks ();
    int iSolutionLogPeriod = (config)"solution_log_period";
	if (iSolutionLogPeriod > 0)
		Problem::LogSolutions ((config)"solution_log_path");

	cout << "Learning..." << endl;
    int iLearningIterations = (config)"learning_iterations";
    int iTestingPeriod = (config)"test_period";


	Time oTimer;
	oTimer.StartTimer ();
	for (int i = 1; i < iLearningIterations + 1; ++ i)
	{
		cout << i << ' ' << flush;
		bool bTestMode = (0 == (i % iTestingPeriod));
		o_Learner.Iterate (i, bTestMode);

		o_Learner.SaveWeights (i);
		if ((iSolutionLogPeriod > 0) && (0 == (i % iSolutionLogPeriod)))
			Problem::LogSolutions ((config)"solution_log_path");

		cout << '[' << oTimer.sTimeToCompletion (i, iLearningIterations)
			 << "]  [" << oTimer.sTotalRunTime () << ']' << endl;
	}

	o_Learner.SaveWeights (iLearningIterations);
	if (iSolutionLogPeriod > 0)
		Problem::LogSolutions ((config)"solution_log_path");

	cout << "----------------------------------------------" << endl;
	cout << " List of solved problems " << endl;
	cout << "----------------------------------------------" << endl;
	Problem::PrintSolvedProblems ();
	cout << "----------------------------------------------" << endl;

	Problem::Clear ();
}

