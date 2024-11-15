import requests
import json

# JSONデータの読み込み
json_file_path = './tmp/tmp.json'

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)


# 1つ目のリクエスト：JSONデータを送信
url_1 = 'http://takaryo1010.site:8080/foods'
headers_1 = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

response_1 = requests.post(url_1, headers=headers_1, data=json.dumps(json_data))
print("Response from foods API:", response_1.status_code, response_1.text)

# 2つ目のリクエスト：画像ファイルを送信
url_2 = 'http://takaryo1010.site:8080/images'
headers_2 = {
    'accept': 'application/json',
}

# ファイルを送信する際は、'files' パラメータを使用
image_path = './tmp/tmp.png'

with open(image_path, 'rb') as image_file:
    files = {
        'image': (json_data["name"]+'.png', image_file, 'image/png')
    }
    response_2 = requests.post(url_2, headers=headers_2, files=files)

print("Response from images API:", response_2.status_code, response_2.text)
