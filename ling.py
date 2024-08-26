import hashlib
import paho.mqtt.client as mqtt
import paho.mqtt.enums as mqtt_enums

# 定义连接参数
product_key = "a1bw1zXB8k4"
device_name = "Mi98"
device_secret = "290b3479cc2604418db6011596b7e9c8"

# 生成密码
password = hashlib.sha256(device_secret.encode()).hexdigest()

# 定义客户端ID
client_id = f"{product_key}/{device_name}"

# 创建MQTT客户端
client = mqtt.Client(client_id=client_id,callback_api_version=mqtt_enums.CallbackAPIVersion.VERSION2)

# 设置用户名和密码
client.username_pw_set(username=client_id, password=password)

# 连接阿里云物联网平台
server_address = f"{product_key}.iot-as-mqtt.cn-shanghai.aliyuncs.com"  # 替换为实际的区域
client.connect(server_address, port=1883)

# 取消订阅所有主题
# 注意: MQTT协议本身不支持直接取消订阅所有主题，这里使用一个假设的通用主题来取消订阅
# 例如，如果所有主题都以相同的前缀开始，可以尝试取消订阅该前缀
unsubscribe_topic = "#"
client.unsubscribe(unsubscribe_topic)

# 开始网络循环
client.loop_start()

# 停止网络循环
client.loop_stop()