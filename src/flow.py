class Flow:
  @staticmethod
  def banner():
    print(f""""
       _____          _    _                    _   _        _     _____         _
      |  __ \        | |  | |                  | \ | |      | |   / ____|       | |
      | |__) | _   _ | |_ | |__    ___   _ __  |  \| |  ___ | |_ | |       __ _ | |_
      |  ___/ | | | || __|| '_ \  / _ \ | '_ \ | . ` | / _ \| __|| |      / _` || __|
      | |     | |_| || |_ | | | || (_) || | | || |\  ||  __/| |_ | |____ | (_| || |_
      |_|      \__, | \__||_| |_| \___/ |_| |_||_| \_| \___| \__| \_____| \__,_| \__|
                __/ |                                                      By: Theus
                |___/ 

        """)
    
  @staticmethod
  def flags(items: list[str]):
    type = None
    ip = None
    port = None
    verbose = None

    # seleciona o tipo. padrão: Servidor TCP
    if "--server-udp" in items:
      type = "server-udp"
    elif "--client-tcp" in items:
      type = "client-tcp"
    elif "--client-udp" in items:
      type = "client-udp"
    else:
      type = "server-tcp"

    # seleciona o ip
    if "-h" in items:
      idx = items.index("-h") + 1
      ip = items[idx]
    else:
      ip = "0.0.0.0"

    # seleciona a porta
    if "-p" in items:
      idx = items.index("-p") + 1
      port = int(items[idx])
    else:
      port = 1234

    # seleciona verbosidade
    if "-v" in items:
      verbose = True
    else:
      verbose = False

    return (type, ip, port, verbose)