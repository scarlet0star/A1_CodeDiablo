import json
import keyboard
import time
import os

# 추가적인 기능들을 위한 파일입니다. 현재는 json파일을 불러오고 리턴해주는 함수밖에 없습니다.

def load_files(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        file_data = json.load(f)
    return file_data

def pick(options, subscription):
    selected_index = 0
    display_list = ["▶ " + options[0]] + \
        ["  " + option for option in options[1:]]

    def print_list():
        os.system("cls" if os.name == "nt" else "clear")
        print(subscription)
        for item in display_list:
            print(item)

    print_list()

    while True:
        if keyboard.is_pressed("up") and selected_index > 0:
            display_list[selected_index] = "  " + options[selected_index]
            selected_index -= 1
            display_list[selected_index] = "▶ " + options[selected_index]
            print_list()
            time.sleep(0.15)

        if keyboard.is_pressed("down") and selected_index < len(options) - 1:
            display_list[selected_index] = "  " + options[selected_index]
            selected_index += 1
            display_list[selected_index] = "▶ " + options[selected_index]
            print_list()
            time.sleep(0.15)

        if keyboard.is_pressed("enter"):
            time.sleep(0.15)
            break

    return options[selected_index], selected_index