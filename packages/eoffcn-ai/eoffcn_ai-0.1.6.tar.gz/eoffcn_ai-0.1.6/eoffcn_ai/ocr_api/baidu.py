import json
import requests

from ._ocr_base import OCRBase


class Baidu(OCRBase):
    __url = "https://aip.baidubce.com/rest/2.0/ocr/v1"
    products = {
        # 二维码识别
        "qrcode": f"{__url}/qrcode",
        # 发票识别
        "vat_invoice": f"{__url}/vat_invoice",
        # 通用文字识别(高精度, 含位置信息)
        "accurate": f"{__url}/accurate",
        # 手写体识别
        "handwriting": f"{__url}/handwriting"
    }

    def __init__(self, client_id, client_secret):
        """
        值由百度提供
        :param client_id:
        :param client_secret:
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = self.get_access_token()

    def get_access_token(self):
        url = "https://aip.baidubce.com/oauth/2.0/token"
        grant_type = "client_credentials"
        url = f"{url}?grant_type={grant_type}&client_id={self.client_id}&client_secret={self.client_secret}"
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        response = requests.get(url, headers=headers)
        content = json.loads(response.text)
        return content["access_token"]

    def get_url(self, product):
        return f'{self.products[product]}?access_token={self.access_token}'

    def set_header(self, **kwargs):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        return headers

    def set_body(self, file_path, **kwargs):
        img = self.base64_img(file_path)
        return {"image": img}
