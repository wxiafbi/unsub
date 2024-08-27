# 构建topic列表
def build_topic_list(productKey, deviceName):
    topic_list = []
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/model/up_raw_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/deviceinfo/delete_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/cipher/get_reply"
    )
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/topo/add_reply")
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/config/log/get_reply"
    )
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/gateway/permit")
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/_thing/service/post_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/lan/blacklist/update_reply"
    )
    topic_list.append("/shadow/get/" + productKey + "/" + deviceName)
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/job/get_reply")
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/reset_reply")
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/topo/get_reply")
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/service/property/get"
    )
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/rrpc/request/+")
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/disable_reply")
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/dsltemplate/get_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/job/update_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/lan/prefix/get_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/config/get_reply"
    )

    print(topic_list)
    return topic_list


build_topic_list("a1bw1zXB8k4", "Mi206")
