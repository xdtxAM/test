import RPi.GPIO as GPIO
import time
import threading

# 定义舵机引脚
servo_pin = 15

# 使用BCM引脚编号模式
GPIO.setmode(GPIO.BCM)

# 设置舵机引脚为输出模式
GPIO.setup(servo_pin, GPIO.OUT)

# 创建舵机PWM对象
pwm = GPIO.PWM(servo_pin, 50)  # 频率设置为50Hz

# 启动PWM
pwm.start(0)

angle = 0  # 当前角度为0度
duty_cycle = 0.5  # 初始占空比为0.5%
pwm.ChangeDutyCycle(duty_cycle)
time.sleep(1)  # 等待1秒钟
