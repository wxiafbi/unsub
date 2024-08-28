import time
import hashlib
import hmac
import base64
import paho.mqtt.client as mqtt
import paho.mqtt.enums as mqtt_enums
import excel_read

# 阿里云物联网平台设备三元组
product_key = "a1bw1zXB8k4"
device_name = "Mi96"
device_secret = "fd8cecfb378836304cc48c26f7bb677a"
Value_s = (
    "clientId" + device_name + "deviceName" + device_name + "productKey" + product_key
)
print(Value_s)


def generate_credentials(productKey, deviceName, deviceSecret):
    # 生成客户端ID
    secure_mode = 3
    sign_method = "hmacsha1"
    client_id = f"{deviceName}|securemode={secure_mode},signmethod={sign_method}|"

    # 生成用户名
    username = f"{deviceName}&{productKey}"

    # 生成密码使用deviceSecret对Value_s进行哈希1加密
    timestamp = int(time.time() * 1000)
    value_s = f"clientId{deviceName}deviceName{deviceName}productKey{productKey}"
    print(value_s)
    # signature = hmac.new(
    #     bytes(deviceSecret, "utf-8"), bytes(value_s, "utf-8"), hashlib.sha1
    # ).digest()
    # signature = base64.b64encode(signature).decode()
    # print(signature)
    password = hmac.new(
        deviceSecret.encode("utf-8"),
        msg=value_s.encode("utf-8"),
        digestmod=hashlib.sha1,
    )
    print(password.hexdigest())
    password = password.hexdigest()

    return client_id, username, password


client_id1, username1, password1 = generate_credentials(
    product_key, device_name, device_secret
)

print("Client ID:", client_id1)
print("Username:", username1)
print("Password:", password1)
# 计算密码


# MQTT连接参数
broker = product_key + ".iot-as-mqtt.cn-shanghai.aliyuncs.com"  # 根据实际情况修改区域
port = 1883

# 创建MQTT客户端
# client = mqtt.Client(
#     client_id,
#     mqtt_enums.CallbackAPIVersion.VERSION2,
# )
client = mqtt.Client(
    client_id=client_id1,
    callback_api_version=mqtt_enums.CallbackAPIVersion.VERSION2,
)
# client.username_pw_set(username, password='B731FEF9FAD6D4F1B920332707CB510A630F19F7')
# client = mqtt.Client(
#     client_id, callback_api_version=1, callback_api_version_tuple=(2, 0, 0)
# )
client.username_pw_set(username1, password1)


# 连接回调函数
def on_connect(client, userdata, flags, rc, ling):
    if rc == 0:
        print("Connected to broker")
        topics = excel_read.read_excel('新建 XLSX 工作表.xlsx')
        # 取消订阅所有topic
        # print(topics)
        for topic in topics:
            print('正在取消订阅',topic) 
            client.unsubscribe(topic)

    else:
        print("Connection failed")


# 订阅回调函数

# 设置连接回调函数
client.on_connect = on_connect

# 连接到阿里云物联网平台
client.connect(broker, port, 60)

# 启动网络循环
client.loop_start()

# 保持连接
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting")
    client.disconnect()
    client.loop_stop()
