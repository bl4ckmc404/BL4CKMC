#!/usr/bin/env python
# Autor : Michael Doruelo
# Tool Name : BL4CKMC v1.0
# Dont change this code :D

import os
import sys

def banner():
 print """
             \033[1;36m_________________________________
\033[1;33m0\033[1;35m===========\033[1;33m[]\033[1;36m_______________________________/
\033[1;31m _____ __    ___ _____ _____ _____ _____
|  _  |  |  | | |     |  |  |     |     |
|  _ -|  |__|_  |   --|    -| | | |   --|
|_____|_____| |_|_____|__|__|_|_|_|_____| \033[1;35mv1.0
\033[1;32m==============================================
\033[1;33m**********************************************
       \033[1;37mMade with \033[1;31m<3 \033[1;37mby Michael Doruelo
    Github : http://github.com/bl4ckmc404
\033[1;33m**********************************************"""

def menu():
 print """Select from menu:
 
 \033[1;37m[\033[1;31m01\033[1;37m] \033[32mFacebook group hijack
 \033[1;37m[\033[1;31m02\033[1;37m] \033[32mFacebook Page hijack
 \033[1;37m[\033[1;31m03\033[1;37m] \033[32mDeface page maker
 \033[1;37m[\033[1;31m04\033[1;37m] \033[32mAdmin Panel Finder

 \033[1;37m[\033[1;31m00\033[1;37m] \033[32mExit
 """

def restart():
 python = sys.executable
 os.execl(python,python, * sys.argv)
 
def back_to_menu():
 print """
 \033[1;37m[\033[1;31m99\033[1;37m] \033[32mBack to menu
 \033[1;37m[\033[1;31m00\033[1;37m] \033[32mExit.
 """
 try:
  select = int(input("\033[1;33mSelect \033[1;31m>\033[1;37m "))
 except:
  restart()
 else:
  if select == 0:
   print "\033[1;31mExit."
   sys.exit()
  else:
   restart()

 