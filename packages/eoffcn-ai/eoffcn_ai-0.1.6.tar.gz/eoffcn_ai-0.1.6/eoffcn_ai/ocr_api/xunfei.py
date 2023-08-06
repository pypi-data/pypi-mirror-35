import json
import time
import base64
import hashlib

from ._ocr_base import OCRBase


class XunFei(OCRBase):
    __url = "http://webapi.xfyun.cn/v1/service/v1/ocr"
    products = {
        "general": f"{__url}/general",
        "handwriting": f"{__url}/handwriting"
    }
    image = None

    def __init__(self, appid, api_key):
        """
        值由讯飞提供
        :param appid:
        :param api_key:
        """
        self.appid = appid
        self.api_key = api_key

    def set_header(self, **kwargs):
        headers = dict()
        headers["X-Appid"] = self.appid
        headers["X-CurTime"] = f"{int(time.time())}"
        param = json.dumps({"language": "cn|en", "location": "true"}).encode("utf8")
        headers["X-Param"] = base64.b64encode(param).decode("utf8")
        headers["X-CheckSum"] = f"{self.api_key}{headers['X-CurTime']}{headers['X-Param']}"
        h = hashlib.md5()
        h.update(headers["X-CheckSum"].encode("utf8"))
        headers["X-CheckSum"] = h.hexdigest()
        return headers

    def set_body(self, file_path, **kwargs):
        body = dict()
        self.image = self.base64_img(file_path).decode("utf8") if self.image is None else self.image
        body["image"] = self.image
        return body
