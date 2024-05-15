import requests

from creds import get_creds 
from config import *

iam_token, folder_id = get_creds()  

def speech_to_text(data):
    iam_token = IAM_TOKEN
    folder_id = FOLDER_ID

    params = "&".join([
        "topic=general",  
        f"folderId={folder_id}",
        "lang=ru-RU"  
    ])

    headers = {
        'Authorization': f'Bearer {iam_token}',
    }


    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data
    )

    decoded_data = response.json()
    if decoded_data.get("error_code") is None:
        return True, decoded_data.get("result") 
    else:
        return False, "При запросе в SpeechKit возникла ошибка"


def text_to_speech(text: str):
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
    }
    data = {
        'text': text,  
        'lang': 'ru-RU',  
        'voice': 'filipp',  
        'folderId': FOLDER_ID,
    }
    response = requests.post('https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize', headers=headers, data=data)

    if response.status_code == 200:
        return True, response.content  
    else:
        return False, "При запросе в SpeechKit возникла ошибка"