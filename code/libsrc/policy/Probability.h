#ifndef __PROB_LOGPROB__
#define __PROB_LOGPROB__

#include <nlp_vector.h>
#include <iostream>
using namespace std;


class LogProbability;
typedef Vector<double>	double_Vec_t;


//												
class Probability
{
	friend class LogProbability;
	private:
		double_Vec_t	vec_Prob;

	public:
		Probability (const LogProbability& _rLogProb);
		Probability (size_t _iSize);
		Probability (void);
		~Probability (void);

		void Create (size_t _iSize);
		void Normalize (void);
		void Memset (size_t _iValue)
		{ vec_Prob.Memset (_iValue); };
		size_t Size (void)
		{ return vec_Prob.Size (); };
		double& operator[] (size_t _iIndex)
		{
			assert (_iIndex < vec_Prob.Size ());
			return vec_Prob [_iIndex];
		};
		Probability& operator= (const Probability& _rProb);
		Probability& operator= (const LogProbability& _rLogProb);

		void PrintToStream (ostream& _rStream) const
		{ _rStream << vec_Prob; };

		double* GetData (void)
		{ return vec_Prob; };

		double Entropy (void);
		double MaxMinDiff (void);
};

inline ostream& operator<< (ostream& _rStream, const Probability& _rProb)
{
	_rProb.PrintToStream (_rStream);
	return _rStream;
}



//												
class LogProbability
{
	friend class Probability;
	private:
		double_Vec_t	vec_LogProb;

	public:
		LogProbability (size_t _iSize);
		LogProbability (void);
		~LogProbability (void);

		void Create (size_t _iSize);
		void RemoveOffset (void);
		void Normalize (void);
		void Memset (size_t _iValue)
		{ vec_LogProb.Memset (_iValue); };
		size_t Size (void) const
		{ return vec_LogProb.Size (); };
		double& operator[] (size_t _iIndex)
		{
			assert (_iIndex < vec_LogProb.Size ());
			return vec_LogProb [_iIndex];
		};
		LogProbability& operator= (const Probability& _rProb);
		LogProbability& operator= (const LogProbability& _rLogProb);
		LogProbability& operator+= (const LogProbability& _rLogProb);

		void PrintToStream (ostream& _rStream) const
		{ _rStream << vec_LogProb; };

		double* GetData (void)
		{ return vec_LogProb; };

		double Entropy (void);
		double MaxMinDiff (void);
};

inline ostream& operator<< (ostream& _rStream, const LogProbability& _rLogProb)
{
	_rLogProb.PrintToStream (_rStream);
	return _rStream;
}


#endif

