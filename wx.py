import requests

res = requests.get('https://dldir1.qq.com/weixin/android/weixin_android_alpha_config.json?t=1740760055')

f = open("demofile3.txt", "w")
f.write(res.text)
f.close()
