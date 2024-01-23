import RPi.GPIO as GPIO
import time

# 设置 GPIO 模式为 BCM 模式
GPIO.setmode(GPIO.BCM)

# 设置舵机控制引脚
servo_pin = 15

# 设置 GPIO 15 为输出
GPIO.setup(servo_pin, GPIO.OUT)

# 创建 PWM 对象，频率设为50Hz
pwm = GPIO.PWM(servo_pin, 50)


def set_angle(angle):
    # 将角度映射到 PWM 范围内
    duty_cycle = 2.5 + (angle / 180.0) * (12.5 - 2.5)
    pwm.ChangeDutyCycle(duty_cycle)


def gradual_change(current_angle, target_angle, duration=1, steps=50):
    step_angle = (target_angle - current_angle) / steps
    step_duration = duration / steps

    for _ in range(steps):
        current_angle += step_angle
        set_angle(current_angle)
        time.sleep(step_duration)


try:
    pwm.start(0)  # 初始化 PWM

    # 从90度到0度，持续2秒

    # 下面两行是归位到 90
    set_angle(90)
    gradual_change(90, 90, duration=2)

    gradual_change(90, 85, duration=1)

except KeyboardInterrupt:
    # 通过键盘中断停止舵机运动
    pwm.stop()

finally:
    # 清理 GPIO 资源
    GPIO.cleanup()
