import socket
import time


class Engine:
    def server_tcp(ip: str, port: int, v: bool):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen(1)

        conn, addr = s.accept()

        while True:
            try:
                conn.send(
                    f"Você está conectado ao servidor TCP em {ip}:{port}".encode()
                )
                conn.send("Aguardando a sua mensagem...".encode())

                res = conn.recv(4096).decode()

                print(res)

                msg = input(">: ")

                if msg == "exit":
                    break

                conn.send(msg.encode())

            except KeyboardInterrupt:
                break
            except Exception as e:
                break

        exit(0)
        conn.close()
        s.close()

    def server_udp():
        print("")

    def client_tcp():
        print("")

    def client_udp():
        print("")
