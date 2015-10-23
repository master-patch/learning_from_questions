import sys, os


def main ():
	if False == os.access ('GNUmakefile', os.F_OK):
		print 'make file not found'
		return
	file = open ('GNUmakefile')
	sLines = '\n'.join (map (lambda x: x.strip (), file.readlines ()))
	file.close ()

	sLines = sLines.replace (' ', '')
	if 'ENABLE_SOURCE_DUMP=1' not in sLines:
		print "make file doesn't have source dump flag"
		return


	sExePath = './'
	if len (sys.argv) > 1:
		sExePath = sys.argv [1]
	print 'getting svn information'
	pipe = os.popen ('date > info.svn')
	pipe.close ()
	pipe = os.popen ('echo "----------------------------" >> info.svn')
	pipe.close ()
	pipe = os.popen ('echo >> info.svn')
	pipe.close ()
	pipe = os.popen ('svn status >> info.svn')
	pipe.close ()
	pipe = os.popen ('echo "----------------------------" >> info.svn')
	pipe.close ()
	pipe = os.popen ('echo >> info.svn')
	pipe.close ()

	lstFiles = os.listdir ('./')
	for sFileName in lstFiles:
		if 'core' == sFileName:
			continue
		if 'SourceDump.cpp' in sFileName:
			continue
		if (True == sFileName.endswith ('.h')) or \
			(True == sFileName.endswith ('.cpp')) or \
			(True == sFileName.endswith ('.c')) or \
			(True == sFileName.endswith ('.g')) or \
			('GNUmakefile' in sFileName):
			pipe = os.popen ('svn info ' + sFileName + ' >> info.svn')

	pipe.close ()
	pipe = os.popen ('echo "----------------------------" >> info.svn')
	pipe.close ()

	print 'preprocessing source for source dump'

	fileCpp = open (sExePath + '/SourceDump.cpp', 'w')
	fileCpp.write ('#include <iostream>\n')
	fileCpp.write ('#include <fstream>\n')
	fileCpp.write ('using namespace std;\n')
	fileCpp.write ('\n\n')
	fileCpp.write ('void DumpSource (void)\n{\n')

	lstFiles = os.listdir ('./')
	for sFileName in lstFiles:
		if 'SourceDump.cpp' in sFileName:
			continue
		if 'core' == sFileName:
			continue

		if (True == sFileName.endswith ('.h')) or \
			(True == sFileName.endswith ('.cpp')) or \
			(True == sFileName.endswith ('.c')) or \
			(True == sFileName.endswith ('.g')) or \
			('GNUmakefile' in sFileName) or \
			('info.svn' in sFileName):
	
			file = open (sFileName)
			lstLines = map (lambda x: x.rstrip (), file.readlines ())

			fileCpp.write ('\t{\n')
			fileCpp.write ('\t\tofstream file ("' + sFileName + '", ios_base::out);\n')

			for sLine in lstLines:	
				sLine = sLine.replace ('\\', '\\\\')
				sLine = sLine.replace ('"', '\\"')
				sLine = sLine.replace ('??', '?\\?')
				fileCpp.write ('\t\tfile << "' + sLine + '\\n";\n')

			fileCpp.write ('\t\tfile.close ();\n')
			fileCpp.write ('\t}\n')
			fileCpp.write ('\n\n\n')
	fileCpp.write ('}\n\n')
	fileCpp.close ()




if __name__ == '__main__':
	sys.exit (main ())
