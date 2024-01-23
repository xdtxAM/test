import RPi.GPIO as GPIO
import time

# 设置GPIO口编号模式
GPIO.setmode(GPIO.BCM)

# 定义GPIO口
sensor_pin = 15

# 设置GPIO口为输入模式
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        # 读取GPIO口的数值
        sensor_value = GPIO.input(sensor_pin)

        if sensor_value == GPIO.HIGH:
            # 当有人靠近时
            print("有人靠近")
        else:
            # 当没有人靠近时
            print("没有人靠近")

        # 延时一段时间
        time.sleep(5)
except KeyboardInterrupt:
    # 当用户按下Ctrl+C时，退出程序
    pass

# 清理GPIO口
GPIO.cleanup()
