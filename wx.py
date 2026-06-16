import requests

url = 'https://dldir1.qq.com/weixin/android/weixin_android_alpha_config.json'
output_file = "demofile3.txt"

try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()
except requests.RequestException as e:
    print(f"请求失败: {e}")
    exit(1)

print(res.text)

with open(output_file, "w") as f:
    f.write(res.text)
