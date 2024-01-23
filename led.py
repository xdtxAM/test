import RPi.GPIO as GPIO
import time


# 设置GPIO模式为BCM编码方式
GPIO.setmode(GPIO.BCM)

# 设置GPIO引脚
led_pin = 16
GPIO.setup(led_pin, GPIO.OUT)


def led_on():
    # 点亮LED
    try:
        # 点亮LED
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED点亮了，按Ctrl+C可以停止程序")

        # 程序会一直运行，直到按下Ctrl+C
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        # 当按下Ctrl+C时，清理GPIO设置
        print("程序被用户中断")
        GPIO.cleanup()


def led_off():
    # 关闭LED
    try:
        # 点亮LED
        GPIO.output(led_pin, GPIO.LOW)
        print("LED关闭了，按Ctrl+C可以停止程序")

        # 程序会一直运行，直到按下Ctrl+C
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        # 当按下Ctrl+C时，清理GPIO设置
        print("程序被用户中断")
        GPIO.cleanup()


def led_blink():
    # led 闪烁
    try:
        # 点亮LED
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED点亮了，按Ctrl+C可以停止程序")

        # 程序会一直运行，直到按下Ctrl+C
        while True:
            time.sleep(0.3)
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(0.3)
            GPIO.output(led_pin, GPIO.HIGH)

    except KeyboardInterrupt:
        # 当按下Ctrl+C时，清理GPIO设置
        print("程序被用户中断")
        GPIO.cleanup()


if __name__ == '__main__':
    # led_blink()
    # led_off()
    led_on()
