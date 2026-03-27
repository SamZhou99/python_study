# 无需安装任何库！Python 自带功能
import plistlib


def decodedPlist(bplist_data):
    # 核心：用系统自带 plistlib 解码
    try:
        result = plistlib.loads(bplist_data)
        return (result, None)
        # print("✅ 解码成功！")
        # print("数据内容：", result)

        # # 直接取值演示
        # print("\n单独字段：")
        # print("shouldForceToSMS =", result.get("shouldForceToSMS"))
        # print(
        #     "numberOfTimesRespondedtoThread =",
        #     result.get("numberOfTimesRespondedtoThread"),
        # )
    except Exception as e:
        # print("❌ 解码失败：", e)
        return (None, e)


def demo():
    # 提取二进制数据
    bplist_data = b"bplist00\xd3\x01\x02\x03\x04\x05\x06TLSMD_\x10\x10shouldForceToSMS_\x10\x1enumberOfTimesRespondedtoThread3A\xc3\xcbF\nfa\xc4\x08\x10\x01\x08\x0f\x14'HQR\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00T"
    res, err = decodedPlist(bplist_data)
    if err:
        print(err)
    else:
        print(res)


if __name__ == "__main__":
    demo()
