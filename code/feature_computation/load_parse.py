import sys, os, re

rgx_Tags = re.compile ('[^()]+ [^()]+')


#											
def remove_sentence_markers (_lstLines):
	lstCleaned = []
	i = 0
	while i < len (_lstLines):
		if True == _lstLines [i].startswith ('(ROOT'):
			if '<SENTENCE' in _lstLines [i+1]:
				i += 2
				continue
		lstCleaned.append (_lstLines [i])
		i += 1
	return lstCleaned


#											
def load_deps (_sFileName):
	file = open (_sFileName)
	_lstLines = remove_sentence_markers (map (lambda x: x.rstrip (), file.readlines ()))
	file.close ()

	lstAll = []
	lstSentence = []
	sSentence = ''
	bInBlock = False
	d = 0
	for sLine in _lstLines:
		d = len (lstAll)
		if '(ROOT' in sLine:
			# if len (lstSentence) > 0:
			if True == bInBlock:
				lstAll.append ((lstSentence, sSentence))
				lstSentence = []
				sSentence = ''
			bInBlock = True

		if '' == sLine.strip ():
			sSentence += sLine + '\n'
			continue

		if '(' == sLine.strip ()[0]:
			sSentence += sLine + '\n'
			continue

		if ',-' in sLine:
			sSentence += sLine + '\n'
			continue

		sSentence += sLine + '\n'
		sLine = sLine.strip ()
		sLine = sLine.replace (')', '')
		(sType, words) = sLine.split ('(', 1)
		(iFrom, iTo) = map (lambda x: int (x.rsplit ('-', 1)[-1].replace ("'", '')), words.split (','))
		(sFrom, sTo) = map (lambda x: x.rsplit ('-', 1)[0].strip (), words.split (','))

		tpl = (sType, iFrom-1, iTo-1, sFrom, sTo)
		lstSentence.append (tpl)

	if len (lstSentence) > 0:
		lstAll.append ((lstSentence, sSentence))

	return lstAll



#													
def load_tags (_sFileName):
	file = open (_sFileName)
	_lstLines = remove_sentence_markers (map (lambda x: x.strip (), file.readlines ()))
	file.close ()


	lstTrees = []
	sTree = ''
	for sLine in _lstLines:
		if '' == sLine:
			continue
		if '(' != sLine [0]:
			continue
		if '(ROOT' in sLine:
			if '' != sTree:
				lstTrees.append (sTree)
				sTree = ''

		sTree += sLine + ' '

	if '' != sTree:
		lstTrees.append (sTree)

	lstValidTrees = filter (lambda x: '<SENTENCE-' not in x, lstTrees)

	lstSentenceTags = []
	for sTree in lstValidTrees:
		lstTags = map (lambda x: x.lower ().split (), rgx_Tags.findall (sTree))
		lstSentenceTags.append (lstTags)

	return lstSentenceTags


