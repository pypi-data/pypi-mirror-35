from PIL import Image

from .nlp import block
from .nlp.setting import xf_keys
from .image import ImageProcess
from .ocr_api import XunFei


def run(b64, adjust=True, **kwargs):
    process = ImageProcess(b64)
    img = process.array_to_image(process.image)
    if adjust:
        # 二值化
        w = process.w
        binarization = process.area(process.grayscale, w//15, gap_filling=(w//340, w//340), erode_and_dilate=(3, 3))
        # 去除边缘
        x, y = process.remove_the_edg(binarization, 0, 0)
        if binarization[x[0]:x[1], y[0]:y[1]].mean() > 11:
            # 获取应旋转的角度
            angle_ = process.correction(binarization)[0]
            # 旋转原始图片
            if angle_:
                color = process.image[:, 0].mean(axis=0)
                color = tuple(int(i) for i in color)
                img = img.rotate(angle_, Image.BICUBIC, expand=True, fillcolor=color)
                # img.show()
    # 将图片转换为b64编码的字节码
    b64 = process.image_to_bytes(img)

    # 调用讯飞的手写文字识别接口
    xf = XunFei(appid=kwargs["appid"], api_key=kwargs["api_key"])
    status, result = xf.get(b64, product="handwriting", code_key="code", right_value="0")

    if status:
        # 结果转换为DataFrame
        data_df = block.get_df(result, **xf_keys)
        # 返回分段结果
        string = block.block(data_df)
        if string:
            return string
        else:
            return result
    else:
        return result
