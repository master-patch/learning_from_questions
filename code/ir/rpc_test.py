import socket
import sys
import struct

def recv_size(the_socket, recv_length=8192):
    print "IR: receiving a message"
    # data length is packed into 4 bytes
    total_len = 0
    total_data = []
    size = sys.maxint
    size_data = sock_data = ''
    recv_size = recv_length
    while total_len < size:
        print total_len, size
        sock_data = the_socket.recv(recv_size)
        print "IR: partial message", sock_data
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

def send_size():
    print "sending", sys.argv[2]
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('localhost', int(sys.argv[1])))
    sock.sendall(struct.pack('>i', len(sys.argv[2]))+sys.argv[2])
    recv_size(sock)
    sock.close()

send_size()
