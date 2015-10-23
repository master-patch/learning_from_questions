import sys, os, socket, select, tempfile, multiprocessing


#												
def construct_command (_sPathToFF, _sTimelimit, _sDomainFile, _sProblemFile):
	sCommand = 'runtime=' + _sTimelimit + ' ; ' +\
				_sPathToFF + ' -o ' + _sDomainFile + ' -f ' + _sProblemFile + ' 2>&1 & ' +\
				'cpid=$! ; ' +\
				'trap \'kill -9 $cpid; exit 1\' 1 2 9 15 ;  ' +\
				'for x in `seq $runtime`; do   ' +\
					'sleep 1 ;  ' +\
					'kill -0 $cpid > /dev/null  2>&1;  ' +\
					'if [ $? -eq 1 ]; then   ' +\
						'break;  ' +\
					'fi;  ' +\
				'done;  ' +\
				'kill -0 $cpid > /dev/null  2>&1;  ' +\
				'if [ $? -eq 0 ]; then  ' +\
					'kill -9 $cpid ;  ' +\
					'echo "[killed planner on timeout]" ;  ' +\
				'fi;   '

	return sCommand


#												
def start_client (_sPathToFF, _sServer, _iPort):

	soc_Client = None
	sRequest = ''

	while True:
		if None == soc_Client:
			soc_Client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
			soc_Client.connect ((_sServer, _iPort))

		lstReadReady, lstWriteReady, lstInError =\
			select.select ([soc_Client], [], [soc_Client], 60)

		if soc_Client in lstInError:
			soc_Client.shutdown (socket.SHUT_RDWR)
			soc_Client.close ()
			soc_Client = None
			continue


		if soc_Client in lstReadReady:
			sRequest += soc_Client.recv (1024)

			if (None == sRequest) or (len(sRequest) <= 0):
				soc_Client.shutdown (socket.SHUT_RDWR)
				soc_Client.close ()
				soc_Client = None
				continue
			
			if (len (sRequest) > 0) and ('\x02' == sRequest [0]):
				return

			if '\x05' in sRequest:
				if '\x02\x05' == sRequest:
					return

				(sTimelimit, sDomain, sProblem) = sRequest.split ('\x01')[:3]

				(fdDomain, sDomainFile) = tempfile.mkstemp ('.pddl', 'dom', '/tmp', True)
				os.write (fdDomain, sDomain)
				os.close (fdDomain)

				(fdProblem, sProblemFile) = tempfile.mkstemp ('.pddl', 'prb', '/tmp', True)
				os.write (fdProblem, sProblem)
				os.close (fdProblem)

				sys.stdout.write ('.')
				sys.stdout.flush ()
				sCommand = construct_command (_sPathToFF, \
											  sTimelimit, \
											  sDomainFile, \
											  sProblemFile)
				pipe = os.popen (sCommand)
				lstFFOutput = pipe.readlines ()
				pipe.close ()

				sFFOutput = ''.join (lstFFOutput)
				soc_Client.send (sFFOutput + '\x05')

				if 'syntax error' in sFFOutput:
					print '[ERROR] Syntax error in pddl files.'
					print '        Retaining files as [' + sDomainFile +\
						  '] and [' + sProblemFile + ']'
				else:
					os.remove (sDomainFile)
					os.remove (sProblemFile)
				sRequest = ''

				sys.stdout.write ('\x08')
				sys.stdout.write (' ')
				sys.stdout.write ('\x08')
				sys.stdout.flush ()



#												
def main ():
	if len (sys.argv) < 5:
		print 'command line: [threads] [path to ff] [server ip] [port]'
		return

	iThreads = int (sys.argv [1])
	sPathToFF = sys.argv [2]
	sServer = sys.argv [3]
	iPort = int (sys.argv [4])

	sys.stdout.write ('>')
	sys.stdout.flush ()

	lstThreads = []
	for t in xrange (iThreads):
		p = multiprocessing.Process (target=start_client, args=(sPathToFF, sServer, iPort))
		p.start ()
		lstThreads.append (p)

	for p in lstThreads:
		p.join ()

	


if __name__ == '__main__':
	sys.exit (main ())
