import hashlib
import base64
import requests


def send_image(url, img_path):
    with open(img_path, 'rb') as fp:
        content = fp.read()
        base64_data = base64.b64encode(content)
        md5 = hashlib.md5(content).hexdigest()

    headers = {'Content-Type': 'application/json'}
    body = {
         "msgtype": "image",
        "image": {
            "base64": base64_data,
            "md5": md5
        }
    }
    r = requests.post(url=url, json=body, headers=headers, verify=False)
    print(r.text)
    res = r.json()
    assert res['errcode'] == 0

if __name__ == '__main__':
    img_path = '/Users/zengze/Downloads/test.png'
    url = 'http://in.qyapi.weixin.qq.com/cgi-bin/webhook/send?key=af4d309d-0a16-4959-b83e-40ce4a57a7c5'
    send_image(url, img_path)