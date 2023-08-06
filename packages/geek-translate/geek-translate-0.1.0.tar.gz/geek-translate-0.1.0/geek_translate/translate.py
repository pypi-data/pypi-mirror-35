import json
import string

import requests
import html


def sogou_translate(text):
    if type(text) is list:
        text = [sogou_translate(i).strip(string.punctuation) for i in text]
        return text
    sogou_api_url = "http://snapshot.sogoucdn.com/engtranslate"
    data = {'from_lang': 'zh-CHS', 'to_lang': 'en',
            'trans_frag': [{'text': text}]}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url=sogou_api_url, headers=headers, data=json.dumps(data))
    json_response = response.json()
    if json_response.get('status', 0) < 0:
        raise Exception(json_response.get('error_string'))
    text = html.unescape(json_response['trans_result'][0]['trans_text'])
    return text.strip(string.punctuation)


text = '我想吃饭'
sogou_translate(text)

if __name__ == '__main__':
    pass
