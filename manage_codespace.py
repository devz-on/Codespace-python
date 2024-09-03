import requests
import time
from keep_alive import keep_alive  # Import keep_alive.py

# Configuration
GITHUB_TOKEN = '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'  # Replace with your GitHub token
GITHUB_USER = 'Devvzone'    # Replace with your GitHub username
CODESPACE_NAME = 'Dosfish'  # Replace with your Codespace name

API_URL = 'https://api.github.com'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_codespace_status():
    url = f'{API_URL}/user/codespaces/{CODESPACE_NAME}'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    return data['state']

def start_codespace():
    url = f'{API_URL}/user/codespaces/{CODESPACE_NAME}/start'
    response = requests.post(url, headers=HEADERS)
    response.raise_for_status()
    print('Codespace is starting...')

def stop_codespace():
    url = f'{API_URL}/user/codespaces/{CODESPACE_NAME}/stop'
    response = requests.post(url, headers=HEADERS)
    response.raise_for_status()
    print('Codespace is stopping...')

def manage_codespace():
    while True:
        try:
            status = get_codespace_status()
            print(f'Current Codespace status: {status}')
            
            if status == 'running':
                print('Stopping and restarting Codespace...')
                stop_codespace()
                time.sleep(30)  # Wait a bit to ensure the Codespace is stopped
                start_codespace()
            elif status == 'stopped':
                start_codespace()
            else:
                print(f'Codespace is in an unexpected state: {status}')
        
        except requests.RequestException as e:
            print(f'An error occurred: {e}')
        
        time.sleep(230 * 60)  # Wait for 230 minutes before checking again

if __name__ == "__main__":
    keep_alive()  # Ensure the Heroku dyno stays awake
    manage_codespace()
    