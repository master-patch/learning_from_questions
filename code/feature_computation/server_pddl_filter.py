import sys, os, socket, select, time
from pddl_filter_lib import *;


#
def RunFF (_sDomain, _sProblem, _lstTasks, _sTime, _sServer, _iPort):

    lstGoodPred = [];

    soc_Client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    soc_Client.connect ((_sServer, _iPort))

    sResponse = ''
    sTaskBeingSent = ''

    iCurrentTask = 0
    setTaskIds = set ()

    while True:
        #if '' == sTaskBeingSent:
            # sys.stderr.write (str(len (setTaskIds)));

        if (iCurrentTask == len (_lstTasks)) and \
           (0 == len (setTaskIds)) and \
           ('' == sTaskBeingSent):
            return lstGoodPred

        lstReadReady = []
        lstWriteReady = []
        lstInError = []


        if (iCurrentTask < len (_lstTasks)) or (len (sTaskBeingSent) > 0):
            lstReadReady, lstWriteReady, lstInError =\
                select.select ([soc_Client], \
                               [soc_Client], \
                               [soc_Client], 10000)
        else:
            lstReadReady, lstWriteReady, lstInError =\
                select.select ([soc_Client], \
                               [], \
                               [soc_Client], 10000)


        if soc_Client in lstInError:
            soc_Client.shutdown (socket.SHUT_RDWR)
            soc_Client.close ()
            soc_Client = None
            print 'client socket error'
            break


        if soc_Client in lstWriteReady:
            if ('' == sTaskBeingSent) and \
               (len (_lstTasks) > iCurrentTask):
                # time.sleep (0.01)
                sys.stderr.write ('.')
                sys.stderr.flush ()
                #(sDomainFile, sProblemFile, sLogFile) = _lstTasks [iCurrentTask]
                iSentTask = iCurrentTask
                iCurrentTask += 1

                #file = open (sDomainFile)
                #sDomain = file.read ()
                #file.close ()
                sDomain = _sDomain;

                #file = open (sProblemFile)
                #sProblem = file.read ()
                #file.close ()
                sProblem = GenerateTestProblem(_sProblem, _lstTasks[iSentTask]);

                sTaskBeingSent = '?\x01' + str(iSentTask) + '\x01' +\
                                 _sTime + '\x01' +\
                                 sDomain + '\x01' +\
                                 sProblem + '\x01\x05'
                setTaskIds.add (iSentTask)

            sBlock = sTaskBeingSent [:1024]
            sTaskBeingSent = sTaskBeingSent [1024:]
            soc_Client.send (sBlock)


        if soc_Client in lstReadReady:
            sResponse += soc_Client.recv (40960)
            if (None == sResponse) or (len(sResponse) <= 0):
                soc_Client.shutdown (socket.SHUT_RDWR)
                soc_Client.close ()
                soc_Client = None
                print 'client socket error'
                break

            while '\x05' in sResponse:
                (sMessage, sRemainder) = sResponse.split ('\x05', 1)
                if '' == sMessage:
                    continue
                if '\x01' == sMessage [0]:
                    lstValues = sMessage.split ('\x01')
                    # sys.stderr.write ('<' + str(len(lstValues)) + '>')
                    iPredId = int (lstValues [1]);
                    setTaskIds.discard (iPredId)
                    sProblem = GenerateTestProblem (_sProblem, _lstTasks[iPredId]);
                    write_output (lstGoodPred, _lstTasks[iPredId], lstValues [2], _sDomain, sProblem);

                elif '\x04' == sMessage [0]:
                    lstValues = sMessage.split ('\x04')
                    # sys.stderr.write ('<' + str(len(lstValues)) + '>')
                    iPredId = int (lstValues [1]);
                    setTaskIds.discard (iPredId);
                    sProblem = GenerateTestProblem (_sProblem, _lstTasks[iPredId]);
                    write_output (lstGoodPred, _lstTasks[iPredId], lstValues [2], _sDomain, sProblem);

                else:
                    print 'unknown response!'

                sResponse = sRemainder


#
def write_output (_lstGoodPred, _sPred, _sPlan, _sDomain, _sProblem):

    bGood, sError = CheckPredicatePlan(_sPlan);

    if bGood:
        sys.stderr.write (':')
        sys.stderr.flush ()
        _lstGoodPred.append(_sPred.strip ());
    elif sError:
        print '===================================='
        print _sPlan
        print '------------------------------------'
        print _sDomain
        print '------------------------------------'
        print _sProblem
        print '------------------------------------'

        sys.stderr.write ('#')
        sys.stderr.flush ()
        sys.stdout.write('\n');
        sys.stdout.write(_sPred + '\n' + sError + '\n');
        sys.stdout.flush();
        # time.sleep(2.0);
    else:
        sys.stderr.write ('-')
        sys.stderr.flush ()

#
def AlphaStrip (_sText):
    iStart = 0
    iEnd = len (_sText)
    lstC = list (enumerate (_sText))
    for i, c in lstC:
        if c.isdigit ():
            iStart = i
            break
    lstC.reverse ()
    for i, c in lstC:
        if c.isdigit ():
            iEnd = i+1
            break

    return _sText [iStart:iEnd]


#
def GetLogName (_sDomain, _sProblem):
    return 'd' + AlphaStrip (_sDomain) + '_p' + AlphaStrip (_sProblem) + '.log'


#
def main ():
    if len (sys.argv) < 6:
        print 'command line: [server] [port] [timelimit] [input_predicate_dict] [output_predicate_dict] (domain_file) (problem_template_file)';
        return;

    sServer = sys.argv [1]
    iPort = int (sys.argv [2])
    sTime = sys.argv [3]
    sPredDictFile = sys.argv [4];
    sOPredDictFile = sys.argv [5];
    sDomainFile = 'domain.v120.pddl';
    sProblemFile = 'template_problem.pddl';

    if len (sys.argv) > 6:
        sDomainFile = sys.argv [6];
    if len (sys.argv) > 7:
        sProblemFile = sys.argv [7];

    lstPred= ReadPredicateDict(sPredDictFile);
    sDomain = ReadPddlFile(sDomainFile);
    sProblem = ReadPddlFile(sProblemFile);
    lstFilteredPred = RunFF (sDomain, sProblem, lstPred, sTime, sServer, iPort);

    fout = open(sOPredDictFile, 'w');
    for sPred in lstFilteredPred:
        fout.write(sPred);
        fout.write('\n');
    fout.close();


if __name__ == '__main__':
    sys.exit (main ())
