import webbrowser
from wonderwords import RandomSentence
import time
import schedule
import sys
import subprocess
import datetime
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

game_aumid = 'Innersloth.AmongUs_fw5x688tam7rm!Game'
game_proc_name = 'Among Us.exe'


def openSearch():
    # search_url = f"https://www.bing.com/search?q={uuid.uuid4()}&qs=SS&pq=pink&sk=LS1&sc=10-4&FORM=QBRE&sp=2&ghc=1&lq=0"

    r = RandomSentence()
    search_url = f"https://www.bing.com/search?q={r.sentence()}&qs=SS&pq=pink&sk=LS1&sc=10-4&FORM=QBRE&sp=2&ghc=1&lq=0"
    webbrowser.open(search_url)

    # # 新建第二个窗口
    # driver.execute_script("window.open('');")
    # # 切换到第二个窗口
    # driver.switch_to.window(driver.window_handles[1])
    # # 在第二个窗口中打开网页
    # driver.get(search_url)


# # ----------------------------------------test----------------------------------------
# # 设置Selenium使用Edge浏览器
# options = Options()
# options.use_chromium = True
# # 这里设置了以User Data结尾的配置文件路径
# options.add_argument(
#     "user-data-dir=C:\\Users\\fwzy_\\AppData\\Local\\Microsoft\\Edge\\User Data")
# # 指定特定的配置文件夹
# options.add_argument("profile-directory=Profile 1")
# options.binary_location = r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

# # 启动Edge浏览器
# driverEdge = webdriver.Edge(
#     options=options, executable_path="EdgeDriver\\msedgedriver.exe")
# # driverEdge = webdriver.Edge(service=Service(
# #     EdgeChromiumDriverManager().install()), options=options)

# openSearch(driverEdge)
# time.sleep(1000)
# openSearch(driverEdge)
# time.sleep(5000)
# driverEdge.quit()
# # --------------------------------------test end--------------------------------------


def daily(bigCD: bool):
    # 启动XGP PC游戏
    subprocess.Popen(
        ['explorer.exe', 'shell:appsFolder\\' + game_aumid], shell=True)
    start_time = datetime.datetime.now()

    # # 设置Selenium使用Edge浏览器
    # options = Options()
    # options.use_chromium = True
    # driverEdge = webdriver.Edge(service=Service(
    #     EdgeChromiumDriverManager().install()), options=options)

    if (not bigCD):
        # for Normal CD
        print("\n强国时间到 - 普通模式")
        interval = 10
        for i in range(32):
            openSearch(driverEdge)
            print(f"已强国{i+1}次")
            time.sleep(interval)
    else:
        # for Big CD
        print("\n强国时间到 - Big CD模式")
        roundcount = 8
        roundinterval = 15*60
        interval = 10
        count = 4
        for i in range(roundcount):
            for j in range(count):
                openSearch(driverEdge)
                print(f"第{i}轮，本轮已强国{j+1}次，共{i*count+j+1}次")
                time.sleep(interval)
            time.sleep(roundinterval)

    # # 关闭所有搜索窗
    # driverEdge.quit()

    # 计算启动XGP PC游戏的时长
    end_time = datetime.datetime.now()
    time_difference = end_time - start_time
    print(f"XGP PC 游戏已运行{time_difference.total_seconds()}秒")
    # 如果未达到16分钟，需等待16分钟过后再关闭，以确保强国任务交付（强国任务：运行XGP PC游戏15分钟）
    if time_difference.total_seconds() < 16 * 60:
        wait_sec = 16 * 60-time_difference.total_seconds()
        print(f"等待{wait_sec}秒")
        time.sleep(wait_sec)

    # 关闭XGP PC游戏
    print("关闭XGP PC游戏")
    subprocess.run(f'taskkill /f /im "{game_proc_name}"', shell=True)


# 定义每天下午16:00执行的任务
bigCD: bool = len(sys.argv) > 1 and sys.argv[1] == '-bigcd'
if (bigCD):
    print("强国开启 - Big CD模式")
else:
    print("强国开启 - 普通模式")
schedule.every().day.at("16:00").do(daily, bigCD=bigCD)

# 无限循环，以确保调度任务持续运行
while True:
    schedule.run_pending()
    time.sleep(60)
