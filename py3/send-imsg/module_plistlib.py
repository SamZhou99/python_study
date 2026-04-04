# 无需安装任何库！Python 自带功能
import plistlib
import typedstream
from bpylist2 import archiver


def parseImessageText(blob: bytes) -> str:
    """自动解析 iMessage attributedBody 二进制数据"""
    if not blob:
        return None

    # 1. 尝试解析 typedstream（你现在这种）
    try:
        data = typedstream.loads(blob)
        if isinstance(data, dict) and "NS.string" in data:
            return data["NS.string"]
    except:
        pass

    # 2. 尝试解析 bplist（新版 iOS/macOS）
    try:
        data = archiver.unarchive(blob)
        return data.get("NS.string", "")
    except:
        pass

    # 3. 尝试解析 plist（旧版 iOS）
    try:
        data = plistlib.loads(blob)
        return data
    except:
        pass

    # 4. 尝试解析 typedstream（旧版 iOS）
    try:
        data = parse_attributedBody_fast(blob)
        return data
    except:
        pass

    return None


def parse_attributedBody_fast(blob: bytes) -> str:
    """快速提取 iMessage attributedBody 文本（typedstream）"""
    if not blob or b"streamtyped" not in blob:
        return ""
    try:
        idx = blob.find(b"+")
        if idx == -1:
            return ""
        length = blob[idx + 1]
        text = blob[idx + 2 : idx + 2 + length]
        return text.decode("utf8")
    except:
        return "<无法解析>"


def demo():
    # 提取二进制数据
    # blob_data = b"bplist00\xd3\x01\x02\x03\x04\x05\x06TLSMD_\x10\x10shouldForceToSMS_\x10\x1enumberOfTimesRespondedtoThread3A\xc3\xcbF\nfa\xc4\x08\x10\x01\x08\x0f\x14'HQR\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00T"
    blob_data = b"\x04\x0bstreamtyped\x81\xe8\x03\x84\x01@\x84\x84\x84\x19NSMutableAttributedString\x00\x84\x84\x12NSAttributedString\x00\x84\x84\x08NSObject\x00\x85\x92\x84\x84\x84\x0fNSMutableString\x01\x84\x84\x08NSString\x01\x95\x84\x01+\x05hello\x86\x84\x02iI\x01\x05\x92\x84\x84\x84\x0cNSDictionary\x00\x95\x84\x01i\x01\x92\x84\x98\x98\x1d__kIMMessagePartAttributeName\x86\x92\x84\x84\x84\x08NSNumber\x00\x84\x84\x07NSValue\x00\x95\x84\x01*\x84\x9b\x9b\x00\x86\x86\x86"
    res = parseImessageText(blob_data)
    print("Demo 解析结果：", res)


if __name__ == "__main__":
    demo()
