import sys
import struct
sys.path.append(sys.path[0] + '/../')

from ir import BagOfWords
from feature_computation.Sentence import ReadSentencesFromTextFileSimple
import socket

EOM = '---EOM'


def start_ir(host, port, ir, max_connections=1, recv_length=8192):
    # Setup socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print "IR: ({}) started {}:{}".format(ir.name, host, port)
    s.listen(max_connections)
    conn, addr = s.accept()

    # Keep on listening
    while True:
        # accept new message
        newsock, address = s.accept()

        # receive questions from new connection
        message = recv_size(newsock, recv_length)
        type, question = message.split(" ", 1)
        answers = ir.question(type, question)
        print "IR: question is ({}, {})".format(type, question)
        print "IR found {} question/s".format(len(answers))

        # formatting the answer
        '''
        12
        This is an example of a sentence all in one line .
        PathDep::nsubj::0::0::Forw::::|1|84|270|12
        PathDep::nsubj::0::0::Forw::::|1|84|271|12
        ---
        13
        This is an example of a sentence all in one line .
        PathDep::nsubj::0::0::Forw::::|1|84|270|13
        ---
        14
        This is an example of a sentence all in one line .

        ---
        '''
        formatted_answers = "\n---\n".join(
            ["\n".join([str(a[0]), a[1], a[2]])
                for a in answers]) + "\n"
        length = struct.pack('>i', len(formatted_answers))
        conn.send(length + formatted_answers)


def recv_size(the_socket, recv_length=8192):
    # data length is packed into 4 bytes
    total_len = 0
    total_data = []
    size = sys.maxint
    size_data = sock_data = ''
    recv_size = recv_length
    while total_len < size:
        sock_data = the_socket.recv(recv_size)
        if not total_data:
            if len(sock_data) > 4:
                size_data += sock_data
                size = struct.unpack('>i', size_data[:4])[0]
                recv_size = size
                if recv_size > 524288:
                    recv_size = 524288
                total_data.append(size_data[4:])
            else:
                size_data += sock_data
        else:
            total_data.append(sock_data)
        total_len = sum([len(i) for i in total_data])
    return ''.join(total_data)


# Crete an IR instance using wiki
print "IR: Starting IR.."
sSentenceFile = sys.path[0] + '/../../data/minecraft_text.raw'
lSentences = ReadSentencesFromTextFileSimple(sSentenceFile)

sentences = [sentence.lWords for sentence in lSentences]
ids = [sentence.iIndex for sentence in lSentences]
ir = BagOfWords(sentences, ids)
start_ir(sys.argv[1], int(sys.argv[2]), ir)
