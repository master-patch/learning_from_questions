#ifndef __NLP_MACROS__
#define __NLP_MACROS__


#define ITERATE(type,lst,ite)	\
			for (type::iterator ite = lst.begin (), \
				 ite##_end = lst.end (); \
				 ite != ite##_end; \
				 ++ ite)

#define CONST_ITERATE(type,lst,ite)\
  for (type::const_iterator ite = lst.begin (), \
	 ite##_end = lst.end ();		\
       ite != ite##_end;			\
       ++ ite)


#endif
