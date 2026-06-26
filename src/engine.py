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

    @staticmethod
    def server_udp(ip: str, port: int, v: bool):
        sleep(1)
        v and print("[*] Iniciando um servidor UDP")
        sleep(0.5)
        v and print(f"IP: {ip}")
        sleep(0.5)
        v and print(f"PORTA: {port}")

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))

        v and print("""
                    [*] Aguardando mensagem...
                    """)

        while True:
            try:
                data, addr = s.recvfrom(4096)

                if not data:
                    continue

                msg_client = f"[{addr[0]}:{addr[1]}] - {data.decode().strip()}\n"

                print(msg_client)

                msg_server = input(f"[Server] - ")

                s.sendto(f"{msg_server}\n".encode(), addr)

            except KeyboardInterrupt:
                v and print("[*] Encerramento manual do servidor...")
                break
            except Exception as e:
                v and print("[!] Algo deu errado no recebimento das mensagens.")
                v and print(e)
                s.close()
                exit(1)
                break

        s.close()
        exit(0)

    def client_tcp():
        print("")

    def client_udp():
        print("")
