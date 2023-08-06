import abc
import json
import base64

import requests


class OCRBase:
    # 当请求失败时用于记录重复请求的次数
    _n = 0
    # 用于存放不同产品对应的url
    products = {}

    @abc.abstractmethod
    def set_header(self, **kwargs):
        """
        设置请求头
        :return: 请求头
        """
        pass

    @abc.abstractmethod
    def set_body(self, file_path, **kwargs):
        """
        设置body
        :param file_path: 文件路径
        :return: body
        """
        pass

    def get_access_token(self):
        """
        获取控制访问权限的加密串
        :return:
        """
        pass

    def get_url(self, product):
        """
        获取接口url
        :param product: 产品类型
        :return: url
        """
        return self.products.get(product, None)

    def ocr(self, file_path, product):
        """
        调用第三方接口
        :param file_path: 文件路径
        :param product: 请求的产品类型
        :return: 以字典形式返回第三方接口返回的内容
        """
        headers = self.set_header()
        body = self.set_body(file_path, product=product)
        url = self.get_url(product)
        if url is None:
            return {"error_code": "暂无此功能"}
        response = requests.post(url, data=body, headers=headers)
        content = json.loads(response.text)
        return content

    def get(self, file_path, product, code_key, right_value=None, abnormal_re_requests=3):
        """
        获取第三方返回值的入口
        :param file_path: 文件路径
        :param product: 产品类型
                        "handwriting": 手写体(暂时仅支持此值)
        :param code_key: 存放异常码的keys, 多层用 "." 隔开
        :param right_value: 请求正常的code值
        :param abnormal_re_requests: 请求失败后重新请求的次数(包括第一次)
        :return: 是否请求成功, 第三方返回的内容(dict)
        """
        content = self.ocr(file_path, product)
        if self.get_code(content, code_key) != right_value:
            self._n += 1
            if self._n >= abnormal_re_requests:
                return False, content
            else:
                self.get_access_token()
                return self.get(file_path, product, code_key, right_value, abnormal_re_requests)
        return True, content

    @staticmethod
    def get_code(content, code_key):
        """
        获取异常码, 无异常返回None, 或给定正常码
        :param content: 第三方接口的返回值(dict)
        :param code_key: 存放异常码的key
        :return: 返回异常码
        """
        keys = code_key.split('.')
        for i in keys:
            content = content.get(i, None)
            if content is None:
                return content
        return content

    @staticmethod
    def base64_img(img_path_or_bytes):
        """
        读取文件
        :param img_path_or_bytes: 文件路径
        :return: 返回经过base64编码的二进制字符串
        """
        if isinstance(img_path_or_bytes, bytes):
            return img_path_or_bytes
        with open(img_path_or_bytes, 'rb') as f:
            return base64.b64encode(f.read())
