import pandas as pd
from fastapi import FastAPI, HTTPException
import uvicorn


app = FastAPI()

@app.post("/json")
async def process_json(json_data: list):
    try:
        # 将JSON数据转换为数据帧
        df = pd.DataFrame(json_data)

        # 将数据保存为Excel文件
        df.to_excel('data.xlsx', index=False)

        return {"message": "数据保存成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("change:app", host="127.0.0.0", port=7800, reload=True)