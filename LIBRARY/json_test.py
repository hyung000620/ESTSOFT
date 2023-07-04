import json

file_path = "C:\\Users\\dksms\\OneDrive\\Desktop\\estsoft\\est\\LIBRARY\\password.json"
with open(file_path,"r") as f:
    json_data = json.load(f)
    
print(json_data['password'])
json_data['delivery']="만두"

with open(file_path,"w",encoding="utf-8") as f:
    json.dump(json_data,f,ensure_ascii=False)