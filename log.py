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
        # 取消订阅所有topic
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/property/desired/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/topo/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/topo/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/event/property/history/post_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/event/property/history/post_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/service/+")  # 注意：+ 通配符
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/service/+")  # 注意：+ 通配符
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/reset")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/reset")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/sub/unregister_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/sub/unregister_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/job/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/job/get_reply")
        client.unsubscribe("/a1bw1zXB8k4/Mi98/user/get")
        client.unsubscribe("/a1bw1zXB8k4/Mi98/user/get")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/config/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/config/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/deviceinfo/delete_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/deviceinfo/delete_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/topo/change")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/topo/change")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/reset_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/reset_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/job/notify")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/job/notify")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/bootstrap/notify")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/bootstrap/notify")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/ota/firmware/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/ota/firmware/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/lan/prefix/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/lan/prefix/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/lan/blacklist/update_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/lan/blacklist/update_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/disable_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/disable_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/job/update_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/job/update_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/lan/prefix/update")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/lan/prefix/update")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/awss/enrollee/match_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/awss/enrollee/match_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/cipher/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/cipher/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/service/property/set")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/service/property/set")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/model/down_raw")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/model/down_raw")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/config/log/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/config/log/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/topo/delete_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/topo/delete_reply")
        client.unsubscribe("/ota/device/request/a1bw1zXB8k4/Mi98")
        client.unsubscribe("/ota/device/request/a1bw1zXB8k4/Mi98")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/awss/enrollee/found_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/awss/enrollee/found_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/gateway/permit")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/gateway/permit")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/_thing/service/post_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/_thing/service/post_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/event/+/post_reply")  # 注意：+ 通配符
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/event/+/post_reply")  # 注意：+ 通配符
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/property/desired/delete_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/property/desired/delete_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/config/push")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/model/up_raw_reply")
        client.unsubscribe("/ota/device/upgrade/a1bw1zXB8k4/Mi98")
        client.unsubscribe("/ota/device/upgrade/a1bw1zXB8k4/Mi98")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/rrpc/request/+")  # 注意：+ 通配符
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/rrpc/request/+")  # 注意：+ 通配符
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/sub/register_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/config/log/push")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/dynamicTsl/get_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/awss/device/switchap")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/awss/enrollee/checkin")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/bootstrap/config/push")
        client.unsubscribe("/shadow/get/a1bw1zXB8k4/Mi98")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/proxy/provisioning/product_register_reply")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/service/property/get")
        client.unsubscribe("/sys/a1bw1zXB8k4/Mi98/thing/dsltemplate/get_reply")
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
