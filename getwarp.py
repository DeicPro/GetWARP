from datetime import datetime
from time import sleep

script_version = 'v1.1.7'
script_title = f"GetWARP {script_version} by Deiki"

from functools import partial
tolog = partial(print, "[{}]".format(datetime.now()), file=open('getwarp.log', 'w'))
printr = partial(print, end='', flush=True)

from os import system, name
system('title ' + script_title if name == 'nt' else 'PS1="\[\e]0;' + script_title + '\a\]"; echo $PS1')
system('cls' if name == 'nt' else 'clear')

print (f'''
	<> {script_title} <>

 [i] Get free WARP+ GB bandwidth for 1.1.1.1 app.

 # GitHub: github.com/DeicPro/GetWARP
 # Telegram: @Deiki
''')

def invalidParam(param):
	print(f" [!] \'{param}\' is not a valid parameter.")

def newID():
	while True:
		referrer = input(" [#] Enter your client ID\n > ")
		user_input = input(f" [?] ID = {referrer}, sure? [y/n]\n > ")
		if user_input == "y":
			save_id = input(" [?] Do you want to save your ID? [y/n]\n > ")
			if save_id == "y":
			    with open("client_id.txt","w") as file:
				    file.write(referrer)
			    return referrer
			elif save_id == "n":
				return referrer
			else:
			    invalidParam(save_id)
		elif user_input == "n":
			user_input = None
		else:
			invalidParam(user_input)

def progressBar():
	animation = ["▱▱▱▱▱▱▱▱▱▱","▰▱▱▱▱▱▱▱▱▱","▰▰▱▱▱▱▱▱▱▱", "▰▰▰▱▱▱▱▱▱▱", "▰▰▰▰▱▱▱▱▱▱", "▰▰▰▰▰▱▱▱▱▱", "▰▰▰▰▰▰▱▱▱▱", "▰▰▰▰▰▰▰▱▱▱", "▰▰▰▰▰▰▰▰▱▱", "▰▰▰▰▰▰▰▰▰▱"]
	progress_anim = 0
	save_anim = animation[progress_anim % len(animation)]
	percent = 0
	while True:
		for _ in range(10):
			percent += 1
			printr(f"\r Sending request...  " + save_anim + f" {percent}%")
			if result.is_alive():
				sleep(0.1)
			else:
				sleep(0.005)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 75 and result.is_alive == True:
				while result.is_alive:
					for _ in range(10):
						printr(f"\r Sending request...  " + save_anim + f" {percent}% (it is taking longer than usual)")
						sleep(1)
					#result.abort()
					break
		elif percent == 100:
			printr("\r Received response.  ▰▰▰▰▰▰▰▰▰▰ 100%")
			break

from string import ascii_letters, digits
from random import choice
def genString(stringLength, charsType):
	try:
		chars = charsType
		return ''.join(choice(chars) for i in range(stringLength))
	except Exception as error:
		tolog(error)

url = f'https://api.cloudflareclient.com/v0a{genString(3, digits)}/reg'

from threading import Thread
from json import dumps
from urllib import request
class sendRequest(Thread):
	def run(self):
		try:
			install_id = genString(22, ascii_letters)
			body = {"key": "{}=".format(genString(43, ascii_letters)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134, ascii_letters)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.now().isoformat()[:-3] + "+07:00",
				"type": "Android",
				"locale": "zh-CN"}
			data = dumps(body).encode('utf8')
			headers = {'Content-Type': 'application/json; charset=UTF-8',
				'Host': 'api.cloudflareclient.com',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'User-Agent': 'okhttp/3.12.1'}
			req = request.Request(url, data, headers)
			resp = request.urlopen(req)
			self.status = resp.getcode()
		except Exception as error:
			tolog(error)
			self.status = error

from pathlib import Path
if Path("client_id.txt").exists():
	while True:
		user_input = input(" [?] Do you want to use saved client ID? [y/n]\n > ")
		if user_input == "y":
			with open("client_id.txt","r") as file:
				referrer = file.read().strip()
			break
		elif user_input == "n":
			referrer = newID()
			break
		else:
			invalidParam(user_input)
else:
	referrer = newID()

g = 0
f = 0

while True:
	system('cls' if name == 'nt' else 'clear')
	print(f"\n	<> {script_title} <>\n")
	result = sendRequest()
	result.start()
	print(f" # Current ID: {referrer}")
	progressBar()
	if result.status == 200:
		g += 1
		print(f"\n\n [i] You've got {g} GB (failed: {f})")
		for i in range(18,0,-1):
			printr(f"\r * Sending a new request in {i} seconds...")
			sleep(1)
	else:
		f += 1
		print(f'''\n\n [i] You've got {g} GB (failed: {f})\n [!] Has been occurred some problem when sent the request:\n''' + str(result.status) + "\n")
		for i in range(18,0,-1):
			printr(f"\r * Retrying again in {i} seconds...")
			sleep(1)
