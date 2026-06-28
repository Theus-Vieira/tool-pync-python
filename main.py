import src.flow as flow
import src.engine as engine
import sys


def main():
    args = sys.argv
    f = flow.Flow()
    e = engine.Engine()

    if "--help" in args:
        f.help()
        exit(0)

    f.banner()

    type, ip, port, verbose = f.flags(args)

    match type:
        case "client-tcp":
            e.client_tcp(ip, port, verbose)
        case "client-udp":
            print("CLIENTE UDP")
        case "server-tcp":
            e.server_tcp(ip, port, verbose)
        case "server-udp":
            e.server_udp(ip, port, verbose)


main()
