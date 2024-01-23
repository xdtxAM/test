import RPi.GPIO as GPIO
import time

# 设置GPIO口的编号方式，这里使用BCM编号方式
GPIO.setmode(GPIO.BCM)

# 定义可燃气体检测模块的引脚
gas_pin = 18

# 设置GPIO口为输入模式
GPIO.setup(gas_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(gas_pin):
            print("检测到可燃气体!")
        else:
            print("未检测到可燃气体")

        # 延时一段时间
        time.sleep(1)
except KeyboardInterrupt:
    # 当用户按下Ctrl+C时，退出程序
    pass

# 清理GPIO口状态
GPIO.cleanup()
