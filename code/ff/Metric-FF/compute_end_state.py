import sys, os, re

rgx_RF = re.compile ('^\\[rf[0-9]*\\]')

set_Predicates = set ()
set_NegatedPredicates = set ()
set_Functions = set ()
set_NegatedFunctions = set ()


def extract_predicates_and_fluents (_sFileName):
	file = open (_sFileName)

	bInPredicates = False
	bInFunctions = False
	for sLine in file:
		sLine = sLine.strip ().lower ()
		if ')' == sLine:
			bInPredicates = False
			bInFunctions = False
			continue
		if '(:predicates' == sLine:
			bInPredicates = True
			continue
		if '(:functions' == sLine:
			bInFunctions = True
			continue

		if True == bInPredicates:
			sName = sLine.split ()[0].replace ('(','').replace (')','').strip ()
			set_Predicates.add (sName)
			set_NegatedPredicates.add ('not-' + sName)
			continue
		if True == bInFunctions:
			sName = sLine.split ()[0].replace ('(','').replace (')','').strip ()
			set_Functions.add (sName)
			set_NegatedFunctions.add ('minus-' + sName)
			continue
	file.close ()

	print '\n'.join (set_Predicates)
	print
	print '\n'.join (set_Functions)
	print


def extract_end_state (_sFileName):
	file = open (_sFileName)

	set_State = set ()

	bInEndState = False
	for sLine in file:
		sLine = sLine.strip ().lower ()
		if '' == sLine:
			continue
		if '-----end-state-----' == sLine:
			if True == bInEndState:
				break
			bInEndState = True
			continue

		if True == bInEndState:

			sPredicateName = sLine.split ()[0].replace ('(','').replace (')','').strip ()
			if sPredicateName in set_NegatedPredicates:
				continue
			if sPredicateName in set_Predicates:
				set_State.add (sLine)
				continue

			# print '->' + sLine + '<-'
			sLine = rgx_RF.sub ('', sLine).replace ('_', ' ')
			# print '->' + sLine + '<-'
			sFunctionName = sLine.split ()[0].replace ('(','').replace (')','').strip ()
			if sFunctionName in set_NegatedFunctions:
				(sName, sValue) = sLine.split (':')
				sName = sName.replace (sFunctionName, sFunctionName [len('minus-'):])
				set_State.add ('(= ' + sName + ' ' + str (-1 * float(sValue)) + ')')
			if sFunctionName in set_Functions:
				(sName, sValue) = sLine.split (':')
				set_State.add ('(= ' + sName + ' ' + str (float (sValue)) + ')')


	lst_State = list (set_State)
	lst_State.sort ()
	print '----------------------------------'
	print '\n'.join (lst_State)


	file.close ()


def main ():
	sDomainFile = sys.argv [1]
	sFFOutput = sys.argv [2]

	extract_predicates_and_fluents (sDomainFile)
	extract_end_state (sFFOutput)


if __name__ == '__main__':
	sys.exit (main ())
