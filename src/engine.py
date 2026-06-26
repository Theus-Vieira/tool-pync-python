import socket
from time import sleep


class Engine:
    @staticmethod
    def server_tcp(ip: str, port: int, v: bool):
        sleep(1)
        v and print("Iniciando um servidor TCP")
        sleep(0.5)
        v and print(f"IP: {ip}")
        sleep(0.5)
        v and print(f"PORTA: {port}")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        s.listen(1)

        v and print("""
                    [*] Aguardando conexão...
                    """)

        try:
            conn, addr = s.accept()

            v and print(f"[*] Conexão estabelecida com {addr}")

            conn.send(f"Você está conectado ao servidor TCP em {ip}:{port}\n".encode())
            conn.send("Aguardando a sua mensagem...\n".encode())
        except KeyboardInterrupt:
            exit(0)
        except Exception as e:
            v and print("[!] Algo deu errado na tentativa de conexão.")
            v and print(e)
            exit(1)

        while True:
            print("")

            try:
                res = conn.recv(4096).decode()

                print(res)

                msg = input(">: ")

                if msg == "exit":
                    v and print("[*] Encerramento manual do servidor...")
                    break

                conn.send(f"{msg}\n".encode())

            except KeyboardInterrupt:
                v and print("[*] Encerramento manual do servidor...")
                break
            except Exception as e:
                v and print("[!] Algo deu errado no recebimento das mensagens.")
                v and print(e)
                conn.close()
                s.close()
                exit(1)
                break

        conn.close()
        s.close()
        exit(0)

    def server_udp():
        print("")

    def client_tcp():
        print("")

    def client_udp():
        print("")
