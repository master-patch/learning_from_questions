#include <assert.h>
#include <math.h>
#include <nlp_macros.h>
#include <nlp_config.h>
#include <nlp_filesystem.h>
#include "Feature.h"



//											
FeatureSpace::FeatureSpace (void)
{
	i_BagOfWordsOffset = 0;
	i_MaxIndex = 0;
	pthread_rwlock_init (&rwl_IndexMap, NULL);
}

FeatureSpace::~FeatureSpace (void)
{
	map_FeatureValueToIndex.clear ();
	pthread_rwlock_destroy (&rwl_IndexMap);
}


//											
int FeatureSpace::GetFeatureIndex (const String& _rName, bool _bCheckExists)
{
	pthread_rwlock_rdlock (&rwl_IndexMap);

	FeatureValueToIndex_map_t::iterator	ite;
	ite = map_FeatureValueToIndex.find (_rName);
	if (map_FeatureValueToIndex.end () != ite)
	{
		pthread_rwlock_unlock (&rwl_IndexMap);
		return ite->second;
	}
	pthread_rwlock_unlock (&rwl_IndexMap);
    if (true == _bCheckExists)
		return 0;
    

	pthread_rwlock_wrlock (&rwl_IndexMap);
	int iIndex = map_FeatureValueToIndex.size ()
					+ i_BagOfWordsOffset;
	if (i_MaxIndex < iIndex)
		i_MaxIndex = iIndex;

	map_FeatureValueToIndex.insert (make_pair (_rName, iIndex));
	map_IndexToFeatureValue.insert (make_pair (iIndex, _rName));
	pthread_rwlock_unlock (&rwl_IndexMap);
	return iIndex;
}


String FeatureSpace::GetFeatureString(int _iIndex) const
{
    return map_IndexToFeatureValue.find(_iIndex)->second;
}




//											
void FeatureSpace::SetBagOfWordsOffset (int _iOffset)
{
	assert ((0 == i_BagOfWordsOffset) || (i_BagOfWordsOffset == _iOffset));
	i_BagOfWordsOffset = _iOffset;
}


//											
bool FeatureSpace::SaveFeatureMapping (String _sName)
{
	File file;
	if (false == file.Open((config)(_sName + ":feature_mapping_file"), ios_base::out))
		return false;

	ITERATE (FeatureValueToIndex_map_t, map_FeatureValueToIndex, ite)
		file << ite->second << '\x01' << ite->first << endl;
	
	file.Close ();
	return true;
}


//											
bool FeatureSpace::LoadFeatureMapping (String _sName)
{
	String_dq_t dqLines;
	if (false == File::ReadLines ((config)(_sName + ":feature_mapping_file"), dqLines))
		return false;

	map_FeatureValueToIndex.clear ();
	ITERATE (String_dq_t, dqLines, ite)
	{
		String_dq_t dqValues;
		ite->Split (dqValues, '\x01');
		map_FeatureValueToIndex.insert (make_pair (dqValues [1], (int)dqValues [0]));
	}
	return true;
}




//											
Features::Features (void)
{
	i_Current = 0;
    i_MaxSize = 0;
}

Features::Features (const Features& _rFeatures)
{
	vec_Indices.Copy (_rFeatures.vec_Indices);
	vec_Features.Copy (_rFeatures.vec_Features);
	i_Current = _rFeatures.i_Current;
	#ifndef NDEBUG
	set_Indices = _rFeatures.set_Indices;
	#endif
}




Features::~Features (void)
{
	i_Current = 0xDEADBEEF + 1;
	i_MaxSize = 0xDEADBEEF;
}


//											
void Features::SetSize (int _iSize)
{
	assert (0 == i_Current);
	
	vec_Indices.Reserve (_iSize);
	vec_Features.Reserve (_iSize);
	i_MaxSize = _iSize;
}

//											
void Features::IncreaseSizeBy (int _iSize)
{
    //NK: using resize here because Branvan's Vector class doesn't allow reserve to resize
	vec_Indices.Resize (vec_Indices.Size() + _iSize);
	vec_Features.Resize (vec_Features.Size() + _iSize);
	i_MaxSize += _iSize;
}


//											
Features& Features::operator= (const Features& _rFeatures)
{
	vec_Indices.Copy (_rFeatures.vec_Indices);
	vec_Features.Copy (_rFeatures.vec_Features);
	i_Current = _rFeatures.i_Current;
	assert (i_Current < i_MaxSize);

	#ifndef NDEBUG
	set_Indices = _rFeatures.set_Indices;
	#endif
	return *this;
}


//											
void Features::Set (FeatureSpace& _rSpace, int _iIndex, float _fValue)
{
	assert (false == isnan (_fValue));
	assert (_iIndex < _rSpace.BagOfWordsOffset ());
	assert (_iIndex >= 0);
	if (0 == _fValue)
		return;
	#ifdef NAN_CHECK
	if ((_fValue < -100) || (_fValue > 100))
	{
		cout << "[WARNING] large feature value Features::Set (): " << _fValue << endl;
		abort ();
	}
	#endif

	assert (i_Current < i_MaxSize);
	vec_Indices [i_Current] = _iIndex;
	vec_Features [i_Current] = _fValue;
	#ifndef NDEBUG
	assert (set_Indices.end () == set_Indices.find (_iIndex));
	set_Indices.insert (_iIndex);
	#endif

	++ i_Current;
}


//											
void Features::Set (int _iIndex, float _fValue, bool _bCheckDuplicate)
{
	assert (false == isnan (_fValue));
	assert (_iIndex >= 0);
	if (0 == _fValue)
		return;
	#ifdef NAN_CHECK
	if ((_fValue < -100) || (_fValue > 100))
	{
		cout << "[WARNING] large feature value Features::Set (): " << _fValue << endl;
		abort ();
	}
	#endif

	assert (i_Current < i_MaxSize);
	vec_Indices [i_Current] = _iIndex;
	vec_Features [i_Current] = _fValue;
	#ifndef NDEBUG
	if (true == _bCheckDuplicate)
		assert (set_Indices.end () == set_Indices.find (_iIndex));
	set_Indices.insert (_iIndex);
	#endif

	++ i_Current;
}


//											
void Features::Set (const Features& _rFeatures)
{
	size_t iNewFeatures = _rFeatures.Size ();
	assert (i_Current + iNewFeatures <= i_MaxSize);

	#ifdef NAN_CHECK
	if (i_Current + iNewFeatures > i_MaxSize)
	{
		cout << i_Current << " + " << iNewFeatures << " > " << i_MaxSize << endl;
		abort ();
	}
	#endif

	vec_Indices.InsertDataBlock (i_Current,
								 (int*)((Features&)_rFeatures).vec_Indices,
								 iNewFeatures);
	vec_Features.InsertDataBlock (i_Current,
								  (float*)((Features&)_rFeatures).vec_Features,
								  iNewFeatures);
	i_Current += iNewFeatures;
}


//											
void Features::SetBagOfWords (FeatureSpace& _rSpace, const char* _zFeature, float _fValue)
{
	String sFeature (_zFeature);
	int iIndex = _rSpace.GetFeatureIndex (sFeature);
	assert (iIndex >= 0);

	#ifdef NAN_CHECK
	if ((_fValue < -100) || (_fValue > 100))
	{
		cout << "[WARNING] large feature value Features::SetBagOfWords (): "
			 << _fValue << endl;
		abort ();
	}
	#endif

	assert (i_Current < i_MaxSize);
	vec_Indices [i_Current] = iIndex;
	vec_Features [i_Current] = _fValue;
	#ifndef NDEBUG
	assert (set_Indices.end () == set_Indices.find (iIndex));
	set_Indices.insert (iIndex);
	#endif

	++ i_Current;
}


//											
void Features::SetBagOfWords (FeatureSpace& _rSpace, String& _rFeature, float _fValue)
{
	int iIndex = _rSpace.GetFeatureIndex (_rFeature);
	assert (iIndex >= 0);

	#ifdef NAN_CHECK
	if ((_fValue < -100) || (_fValue > 100))
	{
		cout << "[WARNING] large feature value Features::SetBagOfWords (): "
			 << _fValue << endl;
		abort ();
	}
	#endif

	assert (i_Current < i_MaxSize);
	vec_Indices [i_Current] = iIndex;
	vec_Features [i_Current] = _fValue;
	#ifndef NDEBUG
	assert (set_Indices.end () == set_Indices.find (iIndex));
	set_Indices.insert (iIndex);
	#endif

	++ i_Current;
}


//											
void Features::SetBagOfWords (FeatureSpace& _rSpace, String_dq_t& _rdqFeatures, float _fValue)
{
	#ifdef NAN_CHECK
	if ((_fValue < -100) || (_fValue > 100))
	{
		cout << "[WARNING] large feature value Features::SetBagOfWords (): " << _fValue << endl;
		abort ();
	}
	#endif

	ITERATE (String_dq_t, _rdqFeatures, iteValue)
	{
		int iIndex = _rSpace.GetFeatureIndex (*iteValue);
		assert (iIndex >= 0);
		assert (i_Current < i_MaxSize);

		vec_Indices [i_Current] = iIndex;
		vec_Features [i_Current] = _fValue;
		#ifndef NDEBUG
		assert (set_Indices.end () == set_Indices.find (iIndex));
		set_Indices.insert (iIndex);
		#endif

		++ i_Current;
	}
}


//											
void Features::SetBagOfWords (FeatureSpace& _rSpace, const char* _zPrefix, char* _zFeatures, float _fValue)
{
	assert (false);
	// zchar_dq_t dqValues = String::DestructiveSplit (_zFeatures, LCP_BOW_SEPARATOR);
	// SetBagOfWords (_rSpace, _zPrefix, dqValues, _fValue);
}


//											
void Features::SetBagOfWords (FeatureSpace& _rSpace, const char* _zPrefix, zchar_dq_t& _rdqFeatures, float _fValue)
{
	#ifdef NAN_CHECK
	if ((_fValue < -100) || (_fValue > 100))
	{
		cout << "[WARNING] large feature value Features::SetBagOfWords (): " << _fValue << endl;
		abort ();
	}
	#endif

	ITERATE (zchar_dq_t, _rdqFeatures, iteValue)
	{
		String sName;
		sName << _zPrefix << '\x01' << *iteValue;

		int iIndex = _rSpace.GetFeatureIndex (sName);
		assert (iIndex >= 0);

		#ifdef NAN_CHECK
		if (i_Current >= i_MaxSize)
		{
			cout << "array bounds : " << i_Current << " >= " << i_MaxSize << endl;
			ITERATE (zchar_dq_t, _rdqFeatures, ite)
				cout << '[' << *ite << "], ";
			cout << endl;
			abort ();
		}
		#endif

		vec_Indices [i_Current] = iIndex;
		vec_Features [i_Current] = _fValue;
		#ifndef NDEBUG
		assert (set_Indices.end () == set_Indices.find (iIndex));
		set_Indices.insert (iIndex);
		#endif

		++ i_Current;
	}
}


//											
void Features::SetBagOfWords (FeatureSpace& _rSpace, const char* _zPrefix, String_dq_t& _rdqFeatures, float _fValue)
{
	#ifdef NAN_CHECK
	if ((_fValue < -100) || (_fValue > 100))
	{
		cout << "[WARNING] large feature value Features::SetBagOfWords (): " << _fValue << endl;
		abort ();
	}
	#endif

	ITERATE (String_dq_t, _rdqFeatures, iteValue)
	{
		String sName;
		sName << _zPrefix << '\x01' << *iteValue;

		int iIndex = _rSpace.GetFeatureIndex (sName);
		assert (iIndex >= 0);
		assert (i_Current < i_MaxSize);

		vec_Indices [i_Current] = iIndex;
		vec_Features [i_Current] = _fValue;
		#ifndef NDEBUG
		assert (set_Indices.end () == set_Indices.find (iIndex));
		set_Indices.insert (iIndex);
		#endif

		++ i_Current;
	}
}


//											
double Features::DotProduct (double_vec_t& _rvecWeights)
{
	double dResult = 0;
	for (int i = 0; i < Size (); ++ i)
		dResult += vec_Features [i] * _rvecWeights [vec_Indices [i]];
	
	return dResult;
}


//											
void Features::Normalize (void)
{
	double dSum = 0;
	for (int i = 0; i < Size (); ++ i)
		dSum += vec_Features [i];

	if (0 == dSum)
		return;
	for (int i = 0; i < Size (); ++ i)
		vec_Features [i] /= dSum;
}


//											
ostream& operator<< (ostream& _rStream, const Features& _rFeatures)
{
	if (0 == _rFeatures.Size ())
		return _rStream;

	_rStream << _rFeatures.Index (0) << ':' << _rFeatures.Feature (0);
	for (int i = 1; i < _rFeatures.Size (); ++ i)
		_rStream << ", " << _rFeatures.Index (i) << ':' << _rFeatures.Feature (i);
	return _rStream;
}


//											
ostream& operator<< (ostream& _rStream, const double_vec_t& _rvecValues)
{
	if (true == _rvecValues.empty ())
		return _rStream;

	_rStream << _rvecValues [0];
	for (size_t i = 1; i < _rvecValues.size (); ++ i)
		_rStream << ", " << _rvecValues [i];
	return _rStream;
}


bool Features::Check (void) const
{
	for (size_t i = 0; i < i_Current; ++ i)
	{
		if (vec_Indices [i] < 0)
			return false;
	}
	return true;
}

    
void Features::From(const int_set_t& _setFeatures)
{
    this->IncreaseSizeBy(_setFeatures.size());

    CONST_ITERATE(int_set_t, _setFeatures, iter){
        this->Set(*iter, 1);
    }
}

