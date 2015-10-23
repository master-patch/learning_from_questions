import sys, os


def main ():
	sBinary = sys.argv [1]
	sPathPrefix = sys.argv [2]
	iStartIndex = int (sys.argv [3])
	iCount = int (sys.argv [4])
	sConfigFile = sys.argv [5:]

	for i in xrange (iStartIndex, iStartIndex+iCount):
		sPath = sPathPrefix + '_' + str(i)
		if False == os.path.exists (sPath):
			os.path.mkdir (sPath)
		else:
			os.path.rmdir (sPath)
			os.path.mkdir (sPath)
		sCmd = sBinary + ' run=' + sPath + ' ' + sConfigFile + ' 2>&1 | tee ' + sPath + '/run.log'
		pipe = os.popen (sCmd)
		for sLine in pipe:
			print sLine.rstrip ()
		pipe.close ()





if __name__ == '__main__':
	sys.exit (main ())
