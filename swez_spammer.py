import threading
import time
import colorama
import requests.exceptions
import os
import requests
from colorama import Fore, Style

colorama.init()
os.system('title Swez Webhook S')

fiery_effect = f'''
{Fore.BLUE}
   swez  :)
   bypass rate limit :3
{Fore.RESET}
'''

print(fiery_effect)
message = input(f'{Fore.RED}message: {Fore.LIGHTYELLOW_EX}')
image_path = 'nuke.jpg'

with open('webhooks.txt') as file:
    webhooks_list = file.read().splitlines()

with open('proxies.txt') as file:
    proxies_list = file.read().splitlines()

def send_webhook(message, image_path, webhook_url, proxy, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            proxies = {'http': proxy}
            payload = {"content": message}  # Construct the payload with the message content
            
            # Open and attach the image file
            with open(image_path, 'rb') as image_file:
                files = {'file': image_file}
                response = requests.post(webhook_url, data=payload, files=files, proxies=proxies)
            
            if response.status_code == 204:
                print(f'{Fore.RED}sent webk...{Fore.LIGHTYELLOW_EX}')
            else:
                print(f'{Fore.RED}error send webook {response.status_code}{Fore.LIGHTYELLOW_EX}')
        except (requests.exceptions.ConnectionError, Exception) as e:
            print(f'{Fore.RED}error send webook {e}{Fore.LIGHTYELLOW_EX}')
            retries += 1
            time.sleep(1)  # Wait for a short duration before retrying

threads = []
for webhook_url in webhooks_list:
    for proxy in proxies_list:
        thread = threading.Thread(target=send_webhook, args=(message, image_path, webhook_url, proxy))
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()