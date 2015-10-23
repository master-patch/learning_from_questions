#include "Probability.h"


//											
LogProbability::LogProbability (size_t _iSize)
{
	vec_LogProb.Reserve (_iSize);
}


LogProbability::LogProbability (void)
{
}


//											
LogProbability::~LogProbability (void)
{
}


//											
void LogProbability::Create (size_t _iSize)
{
	vec_LogProb.Reserve (_iSize);
}


//											
void LogProbability::RemoveOffset (void)
{
	double dMaxLogProb = vec_LogProb.Max ();
	for (size_t i = 0; i < vec_LogProb.Size (); ++ i)
		vec_LogProb [i] -= dMaxLogProb;
}


//											
void LogProbability::Normalize (void)
{
	double dMaxLogProb = vec_LogProb.Max ();
	double dSum = 0;
	for (size_t i = 0; i < vec_LogProb.Size (); ++ i)
	{
		vec_LogProb [i] -= dMaxLogProb;
		double dProb = exp (vec_LogProb [i]);
		dSum += dProb;
	}

	if (0 != dSum)
	{
		for (size_t i = 0; i < vec_LogProb.Size (); ++ i)
			vec_LogProb [i] -= log (dSum);
	}
	else
	{
		double dLogUniform = log (1 / (double) vec_LogProb.Size ());
		for (size_t i = 0; i < vec_LogProb.Size (); ++ i)
			vec_LogProb [i] = dLogUniform;
	}
}


//											
LogProbability& LogProbability::operator= (const Probability& _rProb)
{
	size_t iSize = _rProb.vec_Prob.Size ();
	if (0 == iSize)
		return *this;

	vec_LogProb.Reserve (iSize);
	for (size_t i = 0; i < iSize; ++ i)
		vec_LogProb [i] = log (_rProb.vec_Prob [i]);

	return *this;
}


//											
LogProbability& LogProbability::operator= (const LogProbability& _rLogProb)
{
	size_t iSize = _rLogProb.vec_LogProb.Size ();
	if (0 == iSize)
		return *this;

	vec_LogProb.Reserve (iSize);
	for (size_t i = 0; i < iSize; ++ i)
		vec_LogProb [i] = _rLogProb.vec_LogProb [i];

	return *this;
}


//											
LogProbability& LogProbability::operator+= (const LogProbability& _rLogProb)
{
	size_t iSize = _rLogProb.vec_LogProb.Size ();
	if (0 == iSize)
		return *this;

	if (0 == vec_LogProb.Size ())
		*this = _rLogProb;
	else if (vec_LogProb.Size () == iSize)
	{
		for (size_t i = 0; i < iSize; ++ i)
			vec_LogProb [i] += _rLogProb.vec_LogProb [i];
	}
	else
		cerr << "[ERROR] Size mismatch between LogProbability objects during assignment."
			 << endl;

	return *this;
}


//											
double LogProbability::Entropy (void)
{
	Probability oProb (*this);
	return oProb.Entropy ();
}


//											
double LogProbability::MaxMinDiff (void)
{
	Probability oProb (*this);
	return oProb.MaxMinDiff ();
}


//											
Probability::Probability (size_t _iSize)
{
	vec_Prob.Reserve (_iSize);
}


//											
Probability::Probability (const LogProbability& _rLogProb)
{
	size_t iSize = _rLogProb.vec_LogProb.Size ();
	if (0 == iSize)
		return;

	vec_Prob.Reserve (iSize);
	double dMaxLogProb = _rLogProb.vec_LogProb.Max ();
	double dSum = 0;
	for (size_t i = 0; i < iSize; ++ i)
	{
		double dProb = exp (_rLogProb.vec_LogProb [i] - dMaxLogProb);
		vec_Prob [i] = dProb;
		dSum += dProb;
	}

	for (size_t i = 0; i < iSize; ++ i)
		vec_Prob [i] /= dSum;
}


Probability::Probability (void)
{
}


//											
Probability::~Probability (void)
{
}


//											
void Probability::Create (size_t _iSize)
{
	vec_Prob.Reserve (_iSize);
}


//											
void Probability::Normalize (void)
{
	double dSum = 0;
	for (size_t i = 0; i < vec_Prob.Size (); ++ i)
		dSum += vec_Prob [i];

	if (0 != dSum)
	{
		for (size_t i = 0; i < vec_Prob.Size (); ++ i)
			vec_Prob [i] /= dSum;
	}
	else
	{
		double dUniform = 1 / (double) vec_Prob.Size ();
		for (size_t i = 0; i < vec_Prob.Size (); ++ i)
			vec_Prob [i] = dUniform;
	}
}


//											
Probability& Probability::operator= (const Probability& _rProb)
{
	size_t iSize = _rProb.vec_Prob.Size ();
	if (0 == iSize)
		return *this;

	vec_Prob.Reserve (iSize);
	for (size_t i = 0; i < iSize; ++ i)
		vec_Prob [i] = _rProb.vec_Prob [i];

	return *this;
}


//											
Probability& Probability::operator= (const LogProbability& _rLogProb)
{
	size_t iSize = _rLogProb.vec_LogProb.Size ();
	if (0 == iSize)
		return *this;

	vec_Prob.Reserve (iSize);
	double dMaxLogProb = _rLogProb.vec_LogProb.Max ();
	double dSum = 0;
	for (size_t i = 0; i < iSize; ++ i)
	{
		double dProb = exp (_rLogProb.vec_LogProb [i] - dMaxLogProb);
		vec_Prob [i] = dProb;
		dSum += dProb;
	}

	for (size_t i = 0; i < iSize; ++ i)
		vec_Prob [i] /= dSum;

	return *this;
}


//											
double Probability::Entropy (void)
{
	double dEntropy = 0;
	for (size_t i = 0; i < vec_Prob.Size (); ++ i)
	{
		if (0 == vec_Prob [i])
			continue;
		dEntropy -= vec_Prob [i] * log (vec_Prob [i]);
	}
	
	return dEntropy;
}


//											
double Probability::MaxMinDiff (void)
{
	double dMin = 1;
	double dMax = 0;
	for (size_t i = 0; i < vec_Prob.Size (); ++ i)
	{
		if (dMin > vec_Prob [i])
			dMin = vec_Prob [i];
		if (dMax < vec_Prob [i])
			dMax = vec_Prob [i];
	}
	
	return dMax - dMin;
}

