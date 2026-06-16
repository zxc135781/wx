# 微信 Android 更新配置抓取工具

一个简单的 Python 脚本，用于从腾讯 CDN 获取微信 Android 版的更新配置信息。

## 功能

- 从腾讯官方 CDN 抓取微信 Android 版的更新配置
- 获取 APK 下载链接、版本号、MD5 校验值等信息
- 支持 arm32 和 arm64 架构

## 使用方法

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行脚本

```bash
python wx.py
```

脚本会抓取配置并保存到 `demofile3.txt` 文件中。

## 输出示例

输出为 JSONP 格式（`cb({...})`），包含微信 Android 版的更新配置信息，如：

- APK 下载地址
- 版本号
- 文件 MD5 校验值
- 支持的 CPU 架构 (arm32/arm64)

## 许可证

MIT License