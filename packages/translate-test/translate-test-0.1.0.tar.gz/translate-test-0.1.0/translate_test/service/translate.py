import json
import string

import requests
import html

from translate_test import settings


def sogou_translate(text):
    if type(text) is list:
        text = [sogou_translate(i).strip(string.punctuation) for i in text]
        return text
    data = {'from_lang': 'zh-CHS', 'to_lang': 'en',
            'trans_frag': [{'text': text}]}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url=settings.TRANSLATE_URL, headers=headers, data=json.dumps(data))
    json_response = response.json()
    if json_response.get('status', 0) < 0:
        raise Exception(json_response.get('error_string'))
    text = html.unescape(json_response['trans_result'][0]['trans_text'])
    return text.strip(string.punctuation)


if __name__ == '__main__':
    sogou_translate.run()
