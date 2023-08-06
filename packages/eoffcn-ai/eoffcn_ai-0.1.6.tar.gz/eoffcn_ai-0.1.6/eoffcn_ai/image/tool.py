import io
import base64

import cv2
import numpy as np
from PIL import Image


class ImageTools:
    def __init__(self, src_or_bytes):
        # 转换为灰度图
        self.image = self.open_from_bytes(src_or_bytes) if isinstance(src_or_bytes, bytes) else src_or_bytes
        self.grayscale = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.h, self.w = self.grayscale.shape

    def area(self, src, thresh=None, gap_filling=(0, 0), erode_and_dilate=(0, 0)):
        """
        用于突出明暗变化密集的区域
        :param src: 灰度图
        :param thresh: 用于边缘检测的阈值
        :param gap_filling: 缝隙填充的像素
        :param erode_and_dilate: 腐蚀及膨胀的像素数
        :return: 二值化后的数组
        """
        src = cv2.Canny(src, thresh, 255)  # canny边缘检测
        if np.sum(gap_filling):
            src = self.gap_filling(src, *gap_filling)
        if np.sum(erode_and_dilate):
            src = self.erode_and_dilate(src, *erode_and_dilate)
        return src

    @staticmethod
    def binarization(src, thresh):
        """
        图片二值化为 0, 255 (黑, 白)并进行颜色反转
        :param src: 要处理的图像数组
        :param thresh: 阈值, 推荐 w // 15
        :return: 处理完的图像数组
        """
        _, src = cv2.threshold(src, thresh, 255, cv2.THRESH_BINARY_INV)
        return src

    @staticmethod
    def erode_and_dilate(src, erode, dilate):
        """
        腐蚀和膨胀
        :param src: 要处理的图像数组
        :param erode: 腐蚀的像素数
        :param dilate: 膨胀的像素数
        :return: 处理完的图像数组
        """
        src = cv2.erode(src, None, iterations=erode)
        src = cv2.dilate(src, None, iterations=dilate)
        return src

    @staticmethod
    def gap_filling(src, landscape, vertical):
        """
        消除图像缝隙
        :param src: 要处理的图像数组
        :param landscape: 横向填充的像素数
        :param vertical: 纵向填充的像素数
        :return: 处理完的图像数组
        """
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (landscape, vertical))
        src = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)
        return src

    @staticmethod
    def rotate_bound(src, angle, expand=True):
        """
        将图像逆时针旋转一定角度
        :param src: 要旋转的图片
        :param angle: 旋转角度
        :param expand: 是否保证原图的完整性, 否则保持像素不变, 旋转后角落内容丢失
        :return: 旋转后的图片
        """
        h, w = src.shape[:2]
        x_center, y_center = w / 2., h / 2.
        # 旋转中心, 旋转角度, 缩放比例
        m = cv2.getRotationMatrix2D((x_center, y_center), angle, 1)
        if not expand:
            src = cv2.warpAffine(src, m, (h, w))
            return src
        cos = np.abs(m[0, 0])
        sin = np.abs(m[0, 1])
        n_w = int((h * sin) + (w * cos))
        n_h = int((h * cos) + (w * sin))
        m[0, 2] += (n_w / 2) - x_center
        m[1, 2] += (n_h / 2) - y_center
        src = cv2.warpAffine(src, m, (n_w, n_h))
        return src

    def show_from_array(self, src):
        """
        图片显示
        :param src: 图片数组
        :return: None
        """
        self.array_to_image(src).show()

    @staticmethod
    def image_to_array(pil_img):
        """
        将PIL读取的图片转换为数组
        :param pil_img: PIL图片
        :return: ndarray
        """
        src = cv2.cvtColor(np.asarray(pil_img), cv2.COLOR_RGB2BGR)
        return src

    @staticmethod
    def array_to_image(src):
        """
        将数组转换为PIL格式的图片
        :param src: 图片数组, ndarray
        :return: PIL.Image
        """
        if src.ndim == 3:
            src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        return Image.fromarray(src)

    @staticmethod
    def open_from_bytes(byte, b64=True):
        """
        将字节码转换为图片数组
        :param byte: 图片字节码
        :param b64: 是否是base64编码的字节码
        :return: image
        """
        if b64:
            byte = base64.b64decode(byte)
        with io.BytesIO(byte) as f:
            image = Image.open(f)
            # 为了避免image离开with或函数将处于close状态
            src = __class__.image_to_array(image)
        return src

    @staticmethod
    def image_to_bytes(image, b64=True):
        """
        将图片转换为字节码
        :param image: image
        :param b64: 是否使用b64编码
        :return: 图片字节码
        """
        with io.BytesIO() as f:
            image.save(f, format="jpeg")
            byte = f.getvalue()
        if b64:
            byte = base64.b64encode(byte)
        return byte

    @staticmethod
    def point_rotate(point, center, angle):
        """
        图像(左上角为 0,0)上某个点point沿点center旋转angle角度后的坐标值
        :param point: 要旋转的点
        :param center: 旋转中心
        :param angle: 旋转角度
        :return: 旋转后的坐标
        """
        angle = -angle
        x = (point[0] - center[0]) * np.cos(np.pi / 180. * angle) \
            - (point[1] - center[1]) * np.sin(np.pi / 180. * angle) + center[0]
        y = (point[0] - center[0]) * np.sin(np.pi / 180. * angle) \
            + (point[1] - center[1]) * np.cos(np.pi / 180. * angle) + center[1]
        return x, y

    @staticmethod
    def rectangle(draw, left, top, width, height, angle=0, line_width=4, expand=2, fill="red"):
        """
        在图像上画一个矩形
        :param draw: 图像的可编辑对象 PIL.ImageDraw.Draw(img)
        :param left: 矩形左上角离图像左边的距离
        :param top: 矩形左上角离图像上边的距离
        :param width: 矩形宽度
        :param height: 矩形高度
        :param angle: 矩形旋转角度(沿矩形中心旋转)
        :param line_width: 线宽
        :param expand: 矩形向外扩大的像素数
        :param fill: 颜色
        :return: None
        """
        expand += line_width / 2.
        center = (left + width / 2., top + height / 2.)
        top_left = (left - expand, top - expand)
        bottom_left = (left - expand, top + height + expand)
        top_right = (left + width + expand, top - expand)
        bottom_right = (left + width + expand, top + height + expand)
        if angle != 0:
            top_left = __class__.point_rotate(top_left, center, angle)
            bottom_left = __class__.point_rotate(bottom_left, center, angle)
            top_right = __class__.point_rotate(top_right, center, angle)
            bottom_right = __class__.point_rotate(bottom_right, center, angle)
        draw.line([top_left, top_right],
                  fill=fill, width=line_width)  # 横线 1
        draw.line([bottom_left, bottom_right],
                  fill=fill, width=line_width)  # 横线 2
        draw.line([top_left, bottom_left],
                  fill=fill, width=line_width)  # 竖线 1
        draw.line([top_right, bottom_right],
                  fill=fill, width=line_width)  # 竖线 2
