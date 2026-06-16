import requests
import json
import re

url = 'https://dldir1.qq.com/weixin/android/weixin_android_alpha_config.json'
output_file = "demofile3.txt"
parsed_file = "config.json"

try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()
except requests.RequestException as e:
    print(f"请求失败: {e}")
    exit(1)

raw = res.text
print(raw)

with open(output_file, "w") as f:
    f.write(raw)

arch_blocks = re.findall(r'(arm32|arm64)\s*:\s*\{([^}]+)\}', raw)

result = {}
for arch, block in arch_blocks:
    url_m = re.search(r'url\s*:\s*"([^"]+)"', block)
    md5_m = re.search(r'md5\s*:\s*"([^"]+)"', block)
    ver_name_m = re.search(r'versionName\s*:\s*"([^"]+)"', block)
    ver_m = re.search(r'version\s*:\s*"(\d+)"', block)
    text_m = re.search(r'textList\s*:\s*\[([^\]]*)\]', block)
    recent_m = re.search(r'recentList\s*:\s*\[([^\]]*)\]', block)

    def parse_str_list(s):
        if not s:
            return []
        return re.findall(r'"([^"]*)"', s)

    result[arch] = {
        'url': url_m.group(1) if url_m else '',
        'md5': md5_m.group(1) if md5_m else '',
        'versionName': ver_name_m.group(1) if ver_name_m else '',
        'version': ver_m.group(1) if ver_m else '',
        'textList': parse_str_list(text_m.group(1)) if text_m else [],
        'recentList': parse_str_list(recent_m.group(1)) if recent_m else [],
    }

with open(parsed_file, "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"\n解析完成，已保存到 {parsed_file}")
