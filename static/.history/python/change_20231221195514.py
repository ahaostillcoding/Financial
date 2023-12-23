import pandas as pd
from fastapi import FastAPI, HTTPException
import uvicorn
import uuid

app = FastAPI()

@app.post("/json")
async def process_json(json_data: dict):
    try:
        # 从字典中提取"data"键对应的列表
        data = json_data.get("data", [])

        # 将JSON数据转换为数据帧
        df = pd.DataFrame(data)

        # 生成唯一的文件名
        filename = f"data_{str(uuid.uuid4())}.xlsx"


        # 将数据保存为Excel文件
        df.to_excel(filename, index=False)
        
        return {"message": "数据保存成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("change:app", host="127.0.0.1", port=7800, reload=True)