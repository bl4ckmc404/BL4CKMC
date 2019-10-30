#!/usr/bin/env python
# Autor : Michael Doruelo
# Tool Name : BL4CKMC v1.0
# Dont change this code :D

import os
import sys
from core.misc import *
from core.bl4ckmc import *

os.system("clear")
banner()
menu()
try:
 select = int(input("\033[1;33mSelect \033[1;31m>\033[1;37m "))
except:
 restart()
else:
 if select == 1:
  os.system("clear")
  banner()
  facebook_group_hijack()
  back_to_menu()
 elif select == 2:
  os.system("clear")
  banner()
  facebook_page_hijack()
  back_to_menu()
 elif select == 3:
  os.system("clear")
  banner()
  deface_page_maker()
  back_to_menu()
 elif select == 4:
  os.system("clear")
  banner()
  admin_finder()
  back_to_menu()
 elif select == 0:
  print "\033[31mExit!"
  sys.exit()
 else:
  restart()