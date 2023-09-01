os.system("cls")
        print(f"{Fore.GREEN}")
        printSlow("loading..............")
        os.system("cls")
        print(f'''{Fore.GREEN} 

                ██╗██╗  ██╗ ██████╗  █████╗     ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗
                ██║██║ ██╔╝██╔════╝ ██╔══██╗    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
                ██║█████╔╝ ██║  ███╗███████║    ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  
                ██║██╔═██╗ ██║   ██║██╔══██║    ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  
                ██║██║  ██╗╚██████╔╝██║  ██║    ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗
                ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝

            
''')
        print('''

                    [1] JOIN SERVER  |  [2] Bypass Emoji |  [3] SPAM MESSAGE
              
                    [4] LEAVE SERVER |  [5] SPAM DM      |  [6] SPAM VC (เข้าห้องแชร์จอ + ส่งเสียงตามกำหนด)



''')
        print(f"{Fore.RED}")
        ikga = input('[+] ==> : ')

    if ikga == '':
        os.system('cls')
        Main_Program()

    if ikga == '1':
        os.system('cls')
        print(f'''{Style.BRIGHT}{Fore.BLACK}
                        
            ██╗██╗  ██╗ ██████╗  █████╗     ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗
            ██║██║ ██╔╝██╔════╝ ██╔══██╗    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
            ██║█████╔╝ ██║  ███╗███████║    ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  
            ██║██╔═██╗ ██║   ██║██╔══██║    ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  
            ██║██║  ██╗╚██████╔╝██║  ██║    ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗
            ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝

            
            +--------------------------------------+
            || DISCORD : https://discord.gg/ikgas ||
            || SYSTEM  :      Join server         ||
            +--------------------------------------+

        ''')
        print(f'''{Style.BRIGHT}{Fore.YELLOW}Token Stock: {len(open('tokens.txt', 'r').read().splitlines())}''' + Fore.RESET)
        menu()
        Main_Program()

    if ikga == '2':
        os.system('cls')
        print(f'''{Fore.RED} 

    ██╗██╗  ██╗ ██████╗  █████╗     ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗
    ██║██║ ██╔╝██╔════╝ ██╔══██╗    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
    ██║█████╔╝ ██║  ███╗███████║    ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  
    ██║██╔═██╗ ██║   ██║██╔══██║    ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  
    ██║██║  ██╗╚██████╔╝██║  ██║    ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗
    ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝

              
                                [ERROR : กรุณาติดต่อแอดมิน !!]
                                [DISCORD : discord.gg/ikgas]
                                [User : jajahummus.]
''')
        input('กด ENTER เพื่อกลับไปหน้าหลัก')
        Main_Program()







    if ikga == '3':
        tokens = open("tokens.txt", "r").read().splitlines()
        os.system("cls")
        clear = lambda: os.system('cls')
        print(f'''{Fore.MAGENTA} 

              
    ██╗██╗  ██╗ ██████╗  █████╗     ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗
    ██║██║ ██╔╝██╔════╝ ██╔══██╗    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
    ██║█████╔╝ ██║  ███╗███████║    ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  
    ██║██╔═██╗ ██║   ██║██╔══██║    ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  
    ██║██║  ██╗╚██████╔╝██║  ██║    ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗
    ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝

      
              +--------------------------------------+
              || DISCORD : https://discord.gg/ikgas ||
              || SYSTEM  :      SPAM MESSAGE        ||
              +--------------------------------------+

            
''')
        #server = input(f'GUILD ID : ')
        channel = input(f'CHANNEL ID : ')
        mess = input(f'MESSAGES : ')
        delay = float(input(f'DELAY : '))
        ch = input('BYPASS ANTI SPAM y/n : ').lower()
        os.system('cls')



        def spam(token, mess):
            pass

            if ch == 'y':
                mess += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))

            elif ch == 'n':
                pass

            else:
                pass

            url = 'https://discord.com/api/v10/channels/' + channel + '/messages'
            payload = {"content": mess, "tts": False}
            header = mainHeader(token)

            while True:
                sleep(delay)
                src = requests.post(url, headers=header, json=payload)

                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print(f"{Fore.LIGHTRED_EX} DELAY",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    sleep(float(ratelimit['retry_after']))

                elif src.status_code == 200:
                    sleep(delay)
                    print(f'{Fore.GREEN}[*]{Fore.GREEN} ATTACK [+]')

        def thread():
            text = mess
            for token in tokens:
                threading.Thread(target=spam, args=(token, text)).start()

       # start = input(f'{Fore.LIGHTCYAN_EX} ENTER TO START SPAM MESSAGE ')
        start = thread()
        

    if ikga == '4':
        os.system('cls')
        token = open("tokens.txt", "r").read().splitlines()

        ID = input(f'{Fore.RED}GULID ID : ')

        apilink = "https://discord.com/api/v10/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

                }
                requests.delete(apilink, headers=headers)
            print(f'{Fore.GREEN}[*]{Fore.GREEN}LEAVER {token}')

        sleep(1)
        exit = input(f'{Fore.GREEN} SUCCEED ENTER ')
        exit = clear()
        exit = spammer()



    if ikga == '5':
        os.system('cls')
        print(f'''{Fore.RED} 

    ██╗██╗  ██╗ ██████╗  █████╗     ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗
    ██║██║ ██╔╝██╔════╝ ██╔══██╗    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
    ██║█████╔╝ ██║  ███╗███████║    ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  
    ██║██╔═██╗ ██║   ██║██╔══██║    ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  
    ██║██║  ██╗╚██████╔╝██║  ██║    ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗
    ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝

              
                                [ERROR : กรุณาติดต่อแอดมิน !!]
                                [DISCORD : discord.gg/ikgas]
                                [User : jajahummus.]
''')

        input('กด ENTER เพื่อกลับไปหน้าหลัก')
        Main_Program()

    if ikga == '6':
        os.system('cls')
        print(f'''{Fore.RED} 

    ██╗██╗  ██╗ ██████╗  █████╗     ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗
    ██║██║ ██╔╝██╔════╝ ██╔══██╗    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
    ██║█████╔╝ ██║  ███╗███████║    ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  
    ██║██╔═██╗ ██║   ██║██╔══██║    ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  
    ██║██║  ██╗╚██████╔╝██║  ██║    ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗
    ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝

              
                                [ERROR : กรุณาติดต่อแอดมิน !!]
                                [DISCORD : discord.gg/ikgas]
                                [User : jajahummus.]
''')

        input('กด ENTER เพื่อกลับไปหน้าหลัก')
        Main_Program()
