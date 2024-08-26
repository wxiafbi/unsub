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



# 计算密码
def calculate_password(product_key, device_name, device_secret):
    def hmac_sha256(key, msg):
        return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

    def get_client_id():
        return device_name + "|securemode=3,signmethod=hmacsha256|"

    def get_username():
        return device_name + "&" + product_key

    def get_password():
        content = (
            "clientId"
            + device_name
            + "deviceName"
            + device_name
            + "productKey"
            + product_key
        )
        return base64.b64encode(
            hmac_sha256(device_secret.encode("utf-8"), content)
        ).decode("utf-8")

    client_id = get_client_id()
    username = get_username()
    password = get_password()
    print("client_id: ", client_id)
    print("username: ", username)
    print("password: ", password)
    return client_id, username, password


client_id, username, password = calculate_password(
    product_key, device_name, device_secret
)

# MQTT连接参数
broker = product_key + ".iot-as-mqtt.cn-shanghai.aliyuncs.com"  # 根据实际情况修改区域
port = 1883

# 创建MQTT客户端
client = mqtt.Client(
    client_id='Mi98|securemode=2,signmethod=hmacsha1,timestamp=1724677486310|', callback_api_version=mqtt_enums.CallbackAPIVersion.VERSION2
)
client.username_pw_set(username, password='B731FEF9FAD6D4F1B920332707CB510A630F19F7')


# 连接回调函数
def on_connect(client, userdata, flags, rc,ling):
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
