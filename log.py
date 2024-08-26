import time
import hashlib
import hmac
import base64
import paho.mqtt.client as mqtt
import paho.mqtt.enums as mqtt_enums

# 阿里云物联网平台设备三元组
product_key = "a1bw1zXB8k4"
device_name = "Mi98"
device_secret = "290b3479cc2604418db6011596b7e9c8"


def generate_credentials(productKey, deviceName, deviceSecret):
    # 生成客户端ID
    secure_mode = 3
    sign_method = "hmacsha1"
    client_id = f"{deviceName}|securemode={secure_mode},signmethod={sign_method}|"

    # 生成用户名
    username = f"{deviceName}&{productKey}"

    # 生成密码
    signature = hmac.new(
        deviceSecret.encode("utf-8"),
        msg=username.encode("utf-8"),
        digestmod=hashlib.sha1,
    ).digest()
    password = signature.hex()

    return client_id, username, password


client_id, username, password = generate_credentials(
    product_key, device_name, device_secret
)

print("Client ID:", client_id)
print("Username:", username)
print("Password:", password)
# 计算密码


client_id, username, password = generate_credentials(
    product_key, device_name, device_secret
)

# MQTT连接参数
broker = product_key + ".iot-as-mqtt.cn-shanghai.aliyuncs.com"  # 根据实际情况修改区域
port = 1883

# 创建MQTT客户端
client = mqtt.Client(
    client_id='Mi98|securemode=2,signmethod=hmacsha1,timestamp=1724677486310|', callback_api_version=mqtt_enums.CallbackAPIVersion.VERSION2
)
# client.username_pw_set(username, password='B731FEF9FAD6D4F1B920332707CB510A630F19F7')
# client = mqtt.Client(
#     client_id, callback_api_version=1, callback_api_version_tuple=(2, 0, 0)
# )
client.username_pw_set(username, password)


# 连接回调函数
def on_connect(client, userdata, flags, rc, ling):
    if rc == 0:
        print("Connected to broker")
        # 取消订阅所有topic
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/topo/add_reply")
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
