#ifndef __FEATURES__
#define __FEATURES__

#include <map>
#include <deque>
#include <vector>
#include <hash_map>
#include <nlp_string.h>
#include <nlp_vector.h>
using namespace std;


class Features;
typedef map <String, int>		FeatureValueToIndex_map_t;
typedef map <int, String>       IndexToFeatureValue_map_t;
typedef Vector <int>			int_Vec_t;
typedef Vector <float>			float_Vec_t;
typedef vector <double>			double_vec_t;
typedef vector <Features*>		Feature_vec_t;
typedef deque <Features*>		Feature_dq_t;
typedef hash_map <int, float>	int_float_map_t;
typedef set<int> int_set_t;

class SubgoalSequenceState;


//													
class FeatureSpace
{
	friend class SubgoalSequenceState;
  
	private:
		FeatureValueToIndex_map_t	map_FeatureValueToIndex;
		IndexToFeatureValue_map_t	map_IndexToFeatureValue;
		int							i_BagOfWordsOffset;
		int							i_MaxIndex;
		pthread_rwlock_t			rwl_IndexMap;

	public:
		FeatureSpace (void);
		~FeatureSpace (void);

        String GetFeatureString(int _iIndex) const;
		int GetFeatureIndex (const String& _rName, bool _bAssertExists = false);
		int MaxIndex (void) const
		{ return ((0 != i_MaxIndex)? i_MaxIndex : i_BagOfWordsOffset); };
		int BagOfWordsOffset (void) const
		{ return i_BagOfWordsOffset; };

		void SetBagOfWordsOffset (int _iOffset);

		bool SaveFeatureMapping (String _sName);
		bool LoadFeatureMapping (String _sName);
};



//													
class Features
{
	private:
		int_Vec_t	vec_Indices;
		float_Vec_t	vec_Features;
		size_t		i_Current;
		size_t		i_MaxSize;
		#ifndef NDEBUG
		int_set_t	set_Indices;
		#endif

	public:
		Features (void);
		Features (const Features& _rFeatures);
		~Features (void);

		void SetSize (int _iSize);
        void IncreaseSizeBy (int _iSize);

		void Set (FeatureSpace& _rSpace, int _iIndex, float _fValue);
		void Set (int _iIndex, float _fValue, bool _bCheckDuplicate = true);
		void Set (const Features& _rFeatures);

		void SetBagOfWords (FeatureSpace& _rSpace,
							const char* _zFeature,
							float _fValue = 1);
		void SetBagOfWords (FeatureSpace& _rSpace,
							String& _rFeature,
							float _fValue = 1);
		void SetBagOfWords (FeatureSpace& _rSpace,
							String_dq_t& _rdqFeatures,
							float _fValue = 1);
		void SetBagOfWords (FeatureSpace& _rSpace,
							const char* _zPrefix,
							char* _zFeatures,
							float _fValue = 1);
		void SetBagOfWords (FeatureSpace& _rSpace,
							const char* _zPrefix,
							zchar_dq_t& _rdqFeatures,
							float _fValue = 1);
		void SetBagOfWords (FeatureSpace& _rSpace,
							const char* _zPrefix,
							String_dq_t& _rdqFeatures,
							float _fValue = 1);

		Features& operator= (const Features& _rFeatures);

		int Size (void) const
		{ return i_Current; };
		int Index (int _i) const
		{
			assert (vec_Indices [_i] >= 0);
			assert ((size_t)_i < i_Current);
			return vec_Indices [_i];
		};
		float Feature (int _i) const
		{
			assert (_i >= 0);
			assert ((size_t)_i < i_Current);
			return vec_Features [_i];
		};

		double DotProduct (double_vec_t& _rvecWeights);
		bool Check (void) const;
		bool HasNan (void) 
		{
			for (size_t i = 0; i < i_Current; ++ i)
			{
				if (true == isnan (vec_Features [i]))
					return true;
			}
			return false;
		}
		bool HasLargeValue (float _fLarge)
		{
			for (size_t i = 0; i < i_Current; ++ i)
			{
				if ((vec_Features [i] < - _fLarge) ||
					(vec_Features [i] > _fLarge))
					return true;
			}
			return false;
		}

		void Normalize (void);

        void From(const int_set_t & _setFeatures);
};

ostream& operator<< (ostream& _rStream, const Features& _rFeatures);
ostream& operator<< (ostream& _rStream, const double_vec_t& _rvecValues);

#endif
