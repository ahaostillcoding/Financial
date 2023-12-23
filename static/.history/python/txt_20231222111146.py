import json

def save_json_to_txt(json_data, file_path):
    # 将JSON数据转换为字符串
    json_string = json.dumps(json_data)
    
    # 写入TXT文件
    with open(file_path, 'w') as file:
        file.write(json_string)

# 示例用法
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

file_path = 'data.txt'
save_json_to_txt(data, file_path)