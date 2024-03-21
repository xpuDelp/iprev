import requests
import re
from multiprocessing.dummy import Pool
import random
import sys


def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

ef reverse_ip(url):
    try:
        with requests.Session() as session:
            req = session.get('https://api.webscan.cc/?action=query&ip=' + url).text
        if '"domain":' in req:
            ree = re.findall('"domain": "(.*?)"', req)
            for r in ree:
                dom = r.replace("'", "").replace('cpanel.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('webmail.', '').replace('webdisk.', '').replace('hostmaster.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '')
                print('IP -> ' + url + ' OK \n')
                with open('grab.txt', 'a') as file:
                    file.write('http://' + dom + '\n')
        else:
            print('IP -> ' + url + ' NOT WORKING \n')
    except Exception as e:
        print('IP -> ' + url + ' ERROR: ' + str(e) + '\n')

def generate_and_reverse_ips():
    ips = int(input("Enter the number of IPs to generate and reverse: "))
    ip_list = [generate_ip() for _ in range(ips)]
    
    # Reverse IPs with multiple threads
    num_threads = int(input("Enter the number of threads: "))
    pp = Pool(num_threads)
    pr = pp.map(reverse_ip, ip_list)

def main():
    print("""
Menu:    
1) Generate and Reverse IPs
2) Exit
""")
    choice = input("Choice: ")
    if choice == '1':
        generate_and_reverse_ips()
    elif choice == '2':
        sys.exit()

if __name__ == "__main__":
    main()
