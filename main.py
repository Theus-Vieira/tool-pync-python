import src.flow as flow
import sys


def main():
    args = sys.argv
    f = flow.Flow()

    if "--help" in args:
        f.help()
        exit(0)

    f.banner()

    type, ip, port, verbose = f.flags(args)

    match type:
        case "client-tcp":
            print("CLIENTE TCP")
        case "client-udp":
            print("CLIENTE UDP")
        case "server-tcp":
            print("SERVIDOR TCP")
        case "server-udp":
            print("SERVIDOR UDP")


main()
