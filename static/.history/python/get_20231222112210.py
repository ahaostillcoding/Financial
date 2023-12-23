import requests
import json

url = "http://127.0.0.1:8800/json"  # 替换为服务器的实际地址

# 构造请求的JSON数据
json_data = {
    "data": [
        {
            "_id": "657bfa0b466d41a5849052a0",
            "money": "23",
            "datetime": "2023-12-15 15:02:29",
            "tagUrl": "https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/study.png",
            "tag": "学习",
            "remark": "22"
        },
        {
            "_id": "657c060f6e5d2d335af56425",
            "money": "100",
            "datetime": "2023-12-15 15:53:37",
            "tagUrl": "https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/bus.png",
            "tag": "交通",
            "remark": "跳转测试"
        }
    ]
}

# 发送POST请求
response = requests.post(url, json=json_data)

# 检查响应状态码
if response.status_code == 200:
    # 解析响应数据
    data = response.json()
    print(data)
else:
    print("请求失败:", response.status_code)