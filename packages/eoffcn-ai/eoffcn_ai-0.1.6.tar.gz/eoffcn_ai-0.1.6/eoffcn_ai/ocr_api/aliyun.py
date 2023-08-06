import json

from ._ocr_base import OCRBase


class Aliyun(OCRBase):
    products = {
        # 通用文字识别
        "general": "https://tysbgpu.market.alicloudapi.com/api/predict/ocr_general",
        # 通用高精度版
        "advanced":"https://ocrapi-advanced.taobao.com/ocrservice/advanced",
        # 发票识别
        "invoice": "https://ocrapi-invoice.taobao.com/ocrservice/invoice",
        "handwriting": None
    }

    def __init__(self, appcode):
        """
        :param appcode: 阿里云提供的appcode值
        """
        self.appcode = appcode

    def set_header(self, **kwargs):
        headers = {
            'Authorization': 'APPCODE ' + self.appcode,
            'Content-Type': 'application/json; charset=UTF-8'
        }
        return headers

    def set_body(self, file_path, **kwargs):
        product = kwargs['product']
        body = dict()
        image = "image" if product == "general" else "img"
        body[image] = self.base64_img(file_path).decode("utf-8")
        if product == "general":
            body["configure"] = {"main_size": 16, "output_prob": True}
        if product == "advanced":
            body["prob"] = "true"  # 显示每一行的置信度
            body["charInfo"] = "false"  # 单字识别
            body["rotate"] = "true"  # 自动旋转
            body["table"] = "false"  # 表格识别
        return json.dumps(body)
