import requests
import fake_useragent
ua = fake_useragent.UserAgent()
headers = {
    'User-Agent': ua.random
}
for i in range(1000):
    response = requests.get(url, headers=headers)
    url = 'https://api.suyanw.cn/api/hs.php'
    with open(f'test/test{i}.jpg', 'wb') as f:
        f.write(response.content)