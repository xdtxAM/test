import RPi.GPIO as GPIO  # 引入RPi.GPIO模块，并实例化为GPIO，简化后面的模块调用
import time


def get_temperature_humidity():  # 定义获取温湿度数据的函数
    """
    解释：此函数用以获取dht11的温湿度数据，返回值为一个列表，列表中的第一个元素为温度，第二个元素为湿度
    :return
    :return:
    """
    GPIO.setmode(GPIO.BCM)
    Bit = []  # 定义列表，用以存储接收到的数据
    Time = []  # 存储数字0和数字1的高电位持续时间
    K = 0  # 定义循环初始值
    time.sleep(2)  # 由于dht11的采样周期间隔为2s，此处防止dht无方响应
    Pin = 27  # 定义引脚，使用哪个就定义哪个
    GPIO.setup(Pin, GPIO.OUT)  # 将GPIO设置为输出模式
    GPIO.output(Pin, 0)  # 向dht11发送低电平（开始信号）（其中0可以用Flase、GPIO.low代替，下文的1同理）
    time.sleep(0.02)  # 低电平持续时间0.02s大于dht11要求的0.018s
    GPIO.output(Pin, 1)  # 向dht11发送高电平（理论上可以取消，但是实际使用中不发送高概率出错）
    GPIO.setup(Pin, GPIO.IN)  # 将GPIO转为输入模式，用以接收dht11的信号
    while GPIO.input(Pin) == 0:  # 采用轮训检测dht的响应信号，如果输入高电平将跳出此循环（不懂可以查阅python的while continue用法）
        continue
    while GPIO.input(Pin) == 1:  # 采用轮训检测dht的响应信号
        continue
    while K < 40:  # 循环40次用以接收dht11的40bit数据
        while GPIO.input(Pin) == 0:  # 因为每bit数据以低电平开始，故此。
            continue
        begin = time.time()  # 低电平循环结束故此时是高电平信号，因此开始计时
        while GPIO.input(Pin) == 1:  # 轮训高电平
            continue
        end = time.time()  # 获取高电平信号的结束时间
        # Time.append(end-begin)#此处为了确定0和1的高电平持续时间
        if (end - begin) < 0.00003:  # 检测高电平的持续时间判断输入是0还是1（0.00003可以自测一下，取一个适合你的时间）
            Bit.append(0)  # 高电平小于0.00003s证明是0
        else:
            Bit.append(1)  # 高电平大于0.00003s证明是1
        K = K + 1  # 记录循环次数
    # print(Time)				#观察时间特点以确定上文0.00003的取值
    humidity1bit = Bit[0:8]  # 根据dht11的信号原理获取所需的值（下同理）
    humidity2bit = Bit[8:16]
    temperature1bit = Bit[16:24]
    temperature2bit = Bit[24:32]
    checkbit = Bit[32:40]
    humidity1 = 0
    humidity2 = 0
    temperature1 = 0
    temperature2 = 0
    check = 0
    for i in range(0, 8):  # 循环8次，将二进制数转换为十进制数
        humidity1 += humidity1bit[i] * (2 ** (7 - i))
        humidity2 += humidity2bit[i] * (2 ** (7 - 1))
        temperature1 += temperature1bit[i] * (2 ** (7 - i))
        temperature2 += temperature2bit[i] * (2 ** (7 - i))
        check += checkbit[i] * (2 ** (7 - i))

    temperature = temperature1 + temperature2 * 0.1  # 获取温度值（注意dht11的使用说明中明文写到整数位后是小数位故应乘0.1）
    humidity = humidity1 + humidity2 * 0.1  # （网上大部分都没乘，他们的运行结果是整数，足可见网上的帖子都是复制粘着的水文）

    return temperature, humidity  # 返回温度和湿度值


if __name__ == '__main__':
    temp, hum = get_temperature_humidity()
    print("温度：%s℃，湿度：%s%%" % (temp, hum))
