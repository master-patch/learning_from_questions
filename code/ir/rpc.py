import socket

EOM = '---EOM'


def start_ir(host, port, ir, max_connections=1):
    # Setup socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(max_connections)
    conn, addr = s.accept()

    # Keep on listening
    while True:
        # accept new message
        newsock, address = s.accept()

        # receive questions from new connection
        message = recv_end(newsock)
        type, question = message.split(" ", 1)
        answers = ir.question(type, question)

        # format question
        formatted_answers = "\n---\n".join(
            ["\n".join([str(a[0]), a[1], a[2]])
                for a in answers]) + "\n---EOM"
        conn.send(formatted_answers)


# this makes sure that we receive a question in the following form:
#    any message here as long as it ends with---EOM
def recv_end(the_socket):
    total_data = []
    data = ''
    while True:
        data = the_socket.recv(8192)
        if EOM in data:
            total_data.append(data[:data.find(EOM)])
            break
        total_data.append(data)
        if len(total_data) > 1:

            # check if end_of_data was split
            last_pair = total_data[-2] + total_data[-1]
            if EOM in last_pair:
                total_data[-2] = last_pair[:last_pair.find(EOM)]
                total_data.pop()
                break

    return ''.join(total_data)
