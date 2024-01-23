import RPi.GPIO as GPIO
import time
# 设置GPIO口编号模式
GPIO.setmode(GPIO.BCM)

# 定义GPIO口
sensor_pin = 14

# 设置GPIO口为输入模式
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        # 读取GPIO口的数值
        sensor_value = GPIO.input(sensor_pin)

        # 根据电阻值计算水位百分比（示例）
        water_level = (sensor_value / 1023) * 100

        # 打印水位百分比
        print("水位百分比：{:.2f}%".format(water_level))
        time.sleep(1)

except KeyboardInterrupt:
    # 当用户按下Ctrl+C时，退出程序
    pass

# 清理GPIO口
GPIO.cleanup()
