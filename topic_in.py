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
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/rrpc/request/+")
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/job/notify")
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/config/push")
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/config/log/push"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/bootstrap/config/push"
    )
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/reset")
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/sub/register_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/property/desired/delete_reply"
    )
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/service/+")
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/model/down_raw")
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/awss/enrollee/found_reply"
    )
    topic_list.append("/ota/device/upgrade/" + productKey + "/" + deviceName)
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/topo/delete_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/deviceinfo/update_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/property/desired/get_reply"
    )
    topic_list.append("/ota/device/request/" + productKey + "/" + deviceName)
    topic_list.append(
        "/sys/"
        + productKey
        + "/"
        + deviceName
        + "/thing/event/property/history/post_reply"
    )
    topic_list.append(
        "/sys/"
        + productKey
        + "/"
        + deviceName
        + "/thing/proxy/provisioning/product_register_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/dynamicTsl/get_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/sub/unregister_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/awss/enrollee/checkin"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/bootstrap/notify"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/service/property/set"
    )
    topic_list.append("/sys/" + productKey + "/" + deviceName + "/thing/topo/change")
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/awss/enrollee/match_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/awss/device/switchap"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/ota/firmware/get_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/lan/prefix/update"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/thing/event/+/post_reply"
    )
    topic_list.append(
        "/sys/" + productKey + "/" + deviceName + "/rrpc/request/+"
    )

    print(topic_list)
    return topic_list


build_topic_list("a1bw1zXB8k4", "Mi206")
