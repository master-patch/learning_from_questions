#include "LogLinearPolicy.h"
#include "Feature.h"
#include <nlp_config.h>
#include <nlp_filesystem.h>



//											
LogLinearModel::LogLinearModel (void)
{
	i_Features = 0;
	d_LearningRate = 0;
	d_RegularizationFactor = 0;
	d_MaxWeightCeiling = 0;
}


//											
LogLinearModel::~LogLinearModel (void)
{
	i_Features = 0;
}


//											
void LogLinearModel::Init (String _sName)
{
	d_LearningRate = (config)(_sName + ":learning_rate");
	d_RegularizationFactor = (config)(_sName + ":regularization_factor");
	if (1 == (int)(config)(_sName + ":load_weights"))
		LoadWeights (_sName);
	else if (true == Path::Exists ((config)(_sName + ":weights_file")))
		Path::RemoveFile ((config)(_sName + ":weights_file"));
	d_MaxWeightCeiling = (config)(_sName + ":max_weight_ceiling");

	cout << "Initializing log-linear model (" << _sName << ')' << endl;
	cout << "   Learning rate  : " << d_LearningRate << endl;
	cout << "   Regularization : " << d_RegularizationFactor << endl;
}


//											
double LogLinearModel::ComputeLogProb (Features& _rFeatures)
{
	double dResult = 0;

	for (int i = 0; i < _rFeatures.Size (); ++ i)
	{
		int iIndex = _rFeatures.Index (i);
		if (iIndex >= i_Features)
			continue;
		dResult += _rFeatures.Feature (i) * vec_Weights [iIndex];
	}
	
	return dResult;
}


//											
void LogLinearModel::InitializeFeatureExpectationVector (double_Vec_t& _rvecExpectedFeatures,
														 int _iFeatureCount)
{
	// _rvecExpectedFeatures.Create (_iFeatureCount);
	_rvecExpectedFeatures.Resize (_iFeatureCount);
	_rvecExpectedFeatures.Memset (0);
}


//											
void LogLinearModel::ComputeNegativeFeatureExpectation (LogProbability& _rLogProb,
														Features_vec_t& _rvecFeatures, 
														double _dReward,
														double_Vec_t& _rvecExpectedFeatures)
{
	size_t iProbs = _rLogProb.Size ();
	if (0 == iProbs)
		return;

	Probability oProb (_rLogProb);
	for (size_t i = 0; i < iProbs; ++ i)
	{
		Features* pFeatures = _rvecFeatures [i];
		double dProb = oProb [i] * _dReward;

		for (int f = 0; f < pFeatures->Size (); ++ f)
		{
			size_t iIndex = pFeatures->Index (f);
			if (iIndex >= _rvecExpectedFeatures.Size ())
				cerr << "[ERROR] out-of-bounds " << iIndex
					 << " >= " << _rvecExpectedFeatures.Size () 
					 << endl;
			_rvecExpectedFeatures [pFeatures->Index (f)] -= dProb * pFeatures->Feature (f);
		}
	}
}


//											
void LogLinearModel::UpdateWeights (double _dReward, 
									double_Vec_t& _rvecTrace)
{
	int iSize = _rvecTrace.Size ();
	if ((int)vec_Weights.Size () < iSize)
		vec_Weights.Resize (iSize, 0);
	i_Features = iSize;

	int iLastNonZeroWeight = 0;
	for (int i = 0; i < iSize; ++ i)
	{
		#ifdef NAN_CHECK
		double dOldWeights = vec_Weights [i];
		#endif

		vec_Weights [i] += d_LearningRate * 
							(_dReward * _rvecTrace [i]
							- d_RegularizationFactor * vec_Weights [i]);
		if (0 != vec_Weights [i])
			iLastNonZeroWeight = i;

		#ifdef NAN_CHECK
		if (true == isnan (vec_Weights [i]))
		{
			cout << "[ERROR] LogLinearModel::UpdateWeights (). Weight vector has NAN."
				 << endl;
			cout << "weights[i]    : " << vec_Weights [i] << endl;
			cout << "learning rate : " << d_LearningRate << endl;
			cout << "reward        : " << _dReward << endl;
			cout << "trace[i]      : " << _rvecTrace [i] << endl;
			cout << "regularization: " << d_RegularizationFactor << endl;
			cout << "old weights[i]: " << dOldWeights << endl;
			cout << endl;
		}
		#endif
	}

	i_Features = iLastNonZeroWeight + 1;
}


//											
void LogLinearModel::ResetWeights (double _dRatio)
{
	if (i_Features > 0)
	{
		if (0 == _dRatio)
			vec_Weights.Memset (0);
		else
		{
			for (size_t i = 0; i < vec_Weights.Size (); ++ i)
				vec_Weights [i] *= _dRatio;
		}
	}
}


//											
bool LogLinearModel::SaveWeights (const char* _zName)
{
	// LogLinearModelFeatures::SaveIndices (_zName);
	ios_base::openmode eMode = ios_base::out;
	{
		String sName;
		sName << _zName << ":retain_weight_history";
		if (1 == (int)(config)sName)
			eMode |= ios_base::app;
	}

	{
		if (0 == vec_Weights.Size ())
			return true;

		String sName;
		sName << _zName << ":weights_file";
		CsvFile file;
		if (false == file.Open ((config)sName, eMode))
			return false;

		file << vec_Weights [0];
		for (int i = 1; i < i_Features; ++ i)
			file << ',' << vec_Weights [i];
		file << endl;
		file.Close ();
	}

	return true;
}


//											
bool LogLinearModel::LoadWeights (const char* _zName)
{
	cout << "Loading weights for log linear model : "
		 << _zName << endl;
	// LogLinearModelFeatures::LoadIndices (_zName);

	String sName;
	sName << _zName << ":weights_file";

	File file;
	if (false == file.Open ((config)sName))
		return false;
	String sLine;
	if (false == file.ReadLastLine (sLine))
		return false;

	String_dq_t dqValues;
	sLine.Split (dqValues, ',');

	i_Features = dqValues.size ();
	vec_Weights.Resize (i_Features, 0);
	for (int i = 0; i < i_Features; ++ i)
		vec_Weights [i] = dqValues [i];

	return true;
}


//														
void LogLinearModel::CheckForNan (const char* _zId)
{
	bool bHasNan = false;
	for (int i = 0; i < i_Features; ++ i)
	{
		if (true == isnan (vec_Weights [i]))
		{
			bHasNan = true;
			break;
		}
	}
	if (true == bHasNan)
	{
		cout << "[ERROR] {" << _zId << "} weigths has nan:" << endl;
		for (int i = 0; i < i_Features; ++ i)
		{
			cout << vec_Weights [i] << ", ";
		}
		cout << endl << endl;
		abort ();
	}
}


//														
double LogLinearModel::WeightVectorNorm (void)
{
	double dSum = 0;
	for (int i = 0; i < i_Features; ++ i)
		dSum += vec_Weights [i] * vec_Weights [i];
	return sqrt (dSum);
}





