import pandas as pd
import fastapi

# JSON数据
json_data = [
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
    },
    {
        "_id": "657edf678b0da41d314a7cd0",
        "money": "11",
        "datetime": "2023-12-17 19:45:34",
        "tagUrl": "https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/shop.png",
        "tag": "购物",
        "remark": "1"
    },
    {
        "_id": "657ee6d4bd02205a530e495c",
        "money": "1",
        "datetime": "2023-12-16 20:17:19",
        "tagUrl": "https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/food.png",
        "tag": "餐饮",
        "remark": "测试"
    },
    {
        "_id": "657fdd52bd02205a53302a58",
        "money": "111",
        "datetime": "2023-12-18 13:45:47",
        "tagUrl": "https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/bus.png",
        "tag": "交通",
        "remark": "12.18"
    },
    {
        "_id": "6580e5b921821b5c0fb3b9e8",
        "money": "250",
        "datetime": "2023-12-19 08:37:01",
        "tagUrl": "https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/food.png",
        "tag": "餐饮",
        "remark": "测试"
    },
    {
        "_id": "6580fbd721821b5c0fb86140",
        "money": "122",
        "datetime": "2023-12-19 10:11:25",
        "tagUrl": "https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/food.png",
        "tag": "餐饮",
        "remark": "分类"
    },
    {
        "_id": "6581c068652341901b8aef83",
        "money": "12",
        "datetime": "2023-12-20 00:10:05",
        "tagUrl": "https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/shop.png",
        "tag": "购物",
        "remark": "12.20"
    },
    {
        "_id": "658314ee65234188b3aad251",
        "money": "11",
        "datetime": "2023-12-21 00:23:02",
        "tagUrl": "https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/shop.png",
        "tag": "购物",
        "remark": "1"
    }
]

# 将JSON数据转换为数据帧
dfdf = pd.DataFrame(json_data)

# 将数据保存为Excel文件
dfdf.to_excel('data.xlsx', index=False)

print('数据保存成功')