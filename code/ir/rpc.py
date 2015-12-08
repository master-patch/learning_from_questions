import sys
import struct
sys.path.append(sys.path[0] + '/../')
import feature_computation.config as config

# from pdb import set_trace as bp

from ir import BagOfWords
from feature_computation.Sentence import ReadSentencesFromTextFileSimple
import socket

EOM = '---EOM'


def start_ir(
        host, port, ir, max_connections=1, recv_length=8192, write_file=False):
    # Setup socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print "IR:\t({}) started {}:{}".format(ir.name, host, port)
    s.listen(max_connections)
    newsock, address = s.accept()
    print "IR: new connection", newsock, address
    # Keep on listening
    while True:
        # accept new message
        # # print "IR: waiting for new questions"

        # receive questions from new connection
        message = recv_size(newsock, recv_length)
        if not message:
            exit(0)
        type, question = message.split(" ", 1)
        answers = ir.question(type, question)
        # # print "IR: question is ({}, {})".format(type, question)
        print "IR found {} answer/s".format(len(answers))
        # This is sent via RPC
        formatted_answers = "\n---\n".join(
            ["\n".join([str(a[0]), a[1], a[2]])
                for a in answers])

        formatted_answers = "1"
        length = struct.pack('i', len(formatted_answers))
        # # print "IR: Answering with a message of length", length

        # This is written to the file
        # TODO: if this works, then we can have a long opened file
        if write_file:
            s_features = "".join([a[2] for a in answers])
            with open(write_file, 'a') as f:
                f.write(s_features)
                f.close()
                # # print "IR: Successfully written answers to file"

        try:
            newsock.sendall(length + formatted_answers)
        except:
            print "IR: client had an error"
            continue


def recv_size(the_socket, recv_length=8192):
    # data length is packed into 4 bytes
    total_len = 0
    total_data = []
    size = sys.maxint
    size_data = sock_data = ''
    recv_size = recv_length
    while total_len < size:
        print total_len, size
        sock_data = the_socket.recv(recv_size)
        if len(sock_data) == 0:
            print "IR: 0 data received, now disconnect"
            the_socket.close()
            return None
        # bp()
        print "IR: received something", sock_data
        if not total_data:
            if len(sock_data) > 4:
                size_data += sock_data
                size = struct.unpack('i', size_data[:4])[0]
                recv_size = size
                print "IR: size is ", size
                if recv_size > 524288:
                    recv_size = 524288
                print "IR: partial data is ", size_data[4:]
                total_data.append(size_data[4:])
            else:
                size_data += sock_data
                print "IR: data is", size_data
        else:
            total_data.append(sock_data)
        total_len = sum([len(i) for i in total_data])
    return ''.join(total_data)


sSentenceFile = sys.path[0] + '/../../data/minecraft_text.raw'
lSentences = ReadSentencesFromTextFileSimple(sSentenceFile)

sentences = [sentence.lWords for sentence in lSentences]
ids = [sentence.iIndex for sentence in lSentences]

config.load_config(sys.argv)
host = config.get_string("ir_host")

if (not host):
    print "IR: not starting"
    exit(0)

text_connection = sys.path[0]
text_connection += '/../../'
text_connection += config.get_string("text_connection_file")

ir = BagOfWords(
    sentences,
    ids,
    k=config.get_int("ir:num_answers"),
    shuffle=config.get_int("ir:random"))

print "IR: Starting IR..", config.get_string("text_connection_file")
start_ir(
    config.get_string("ir_host"),
    config.get_int("ir_service"),
    ir,
    write_file=text_connection)
