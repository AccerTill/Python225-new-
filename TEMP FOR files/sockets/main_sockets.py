

# --------------------------------------------------------- 1 -----------------------------------
# import socket
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1', 2000))                            # adding address 'local host', port
# server.listen(4)                                            # учим слушать (принимать инфо)
# print('Starting working...')
# client_socket, address = server.accept()                    # учим принимать запросы и разделять на клиента и адрес
# data = client_socket.recv(1024).decode('utf-8')             # получаем содержимое запроса
# print("DATA: ", data)
# HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
# content = 'Hello @@@ .......'.encode('utf-8')               # ответ
# client_socket.send(HDRS.encode('utf-8') + content)          # метод ответа
# print('Shutdown here....')


# #---------------------------------------------------
# # or possible create server via:
# server = socket.create_server(('127.0.0.1', 2000))
# #---------------------------------------------------

# some_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#----------------------------------------------------------- 2 -----------------------------------
#
import socket

def start_my_server():
    try:

        server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 2000))                        # adding address 'local host', port
        server.listen(4)                                        # учим слушать (принимать инфо)
        while True:
            print('Starting working...')
            client_socket, address = server.accept()             # учим принимать запросы и разделять на клиента и адрес
            data = client_socket.recv(1024).decode('utf-8')      # получаем содержимое запроса
            content = load_page_from_request(data)               # ответ
            client_socket.send(content)                          # метод ответа
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('Shutdown here....')

def load_page_from_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ' '
    try:
        with open('views' + path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + "ERROR...no page").encode('utf-8')



if __name__=="__main__":
    start_my_server()


#------------------------------------------------ 3 --------------------------------------















