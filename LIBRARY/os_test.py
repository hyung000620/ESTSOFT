import os

folder_path = "C:\\Users\\dksms\\OneDrive\\Desktop\\estsoft\\est"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"폴더 '{folder_path}'를 생성했습니다.")
else:
    print(f"폴더 {folder_path}에 존재합니다. O")