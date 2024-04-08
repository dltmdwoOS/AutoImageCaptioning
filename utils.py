import os
import json
import pyautogui
import datetime
from PIL import Image

def get_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def mkdir_unless_exist(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def find(folder_path, file_name):
    mkdir_unless_exist(folder_path)
    file_list = os.listdir(folder_path)
    if file_name in file_list:
        return True
    else:
        return False

def get_image(path):
    img = Image.open(path)
    return img

def take_screenshot(filename="image"):
    screenshot = pyautogui.screenshot()
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename_with_timestamp = f"{filename}_{timestamp}.png"
    screenshot.save(filename_with_timestamp)

    print(f"화면이 '{filename_with_timestamp}' 파일로 저장되었습니다.")
    return filename_with_timestamp