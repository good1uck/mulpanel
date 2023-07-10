import tkinter as tk
import subprocess

# 启动批处理文件
def start_bat_file(file_path):
    subprocess.Popen(file_path)

# 停止批处理文件
def stop_bat_file(process):
    process.kill()

# 创建主窗口
window = tk.Tk()
window.title("STEAM-CSGO 多开面板")
window.geometry("294x258")

# 创建启动按钮
start_csgo_button = tk.Button(window, text="启动 CS:GO", command=lambda: start_bat_file("CSGO多开.BAT"))
start_csgo_button.pack(pady=10)
# 创建停止按钮
stop_csgo_button = tk.Button(window, text="停止 CS:GO", command=lambda: start_bat_file("CSGO结束进程.BAT"))
stop_csgo_button.pack(pady=10)
# 
start_steam_button = tk.Button(window, text="启动 STEAM", command=lambda: start_bat_file("STEAM多开.bat"))
start_steam_button.pack(pady=10)
# 
stop_steam_button = tk.Button(window, text="停止 STEAM", command=lambda: start_bat_file("STEAM结束进程.BAT"))
stop_steam_button.pack(pady=10)
# 创建退出按钮
quit_button = tk.Button(window, text="退出", command=window.quit)
quit_button.pack(padx=10)
# 运行主循环
window.mainloop()
