import json

from fastapi import FastAPI, HTTPException
import uvicorn
import uuid
import oss2

app = FastAPI()

access_key_id = "LTAI5t6A3MfeDTCMkvR4vevV"
access_key_secret = "s4CLZLvPZvMaF0AXdc55ENgQ6msQOu"
bucket_name = "digitalhuman1"
endpoint = "oss-cn-beijing.aliyuncs.com"


@app.post("/json")
async def process_json(json_data: dict):
    try:
        data = json_data.get("data", [])
        # 将数据转换为JSON字符串
        json_string = json.dumps(data)
        # 用uuid生成一个唯一的文件名
        filename = f"txt_{str(uuid.uuid4())}.txt"
        # 将数据保存为TXT文件在本地
        with open(filename, 'w') as file:
            file.write(json_string)
        # 上传OSS
        # auth = oss2.Auth(access_key_id, access_key_secret)
        # bucket = oss2.Bucket(auth, endpoint, bucket_name)
        # bucket.put_object_from_file(filename, filename)
        # # 文件URL
        # url = f"https://{bucket_name}.{endpoint}/{filename}"
        # print(url)

        # return {"url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("txt:app", host="127.0.0.1", port=7800, reload=True)