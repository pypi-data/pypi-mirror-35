import cv2
import numpy as np
from PIL import ImageDraw

from .tool import ImageTools


class ImageProcess(ImageTools):
    @staticmethod
    def _near(data, nn=0, difference=5):
        """
        去除data中开头元素且相邻不超过difference的值
        比如[1, 2, 3, 4, 20, 21, 22]
        nn 跟 1 比较, 不超过 5 则 1 被剔除
        接下来依次, 2 跟 1 比较, 3 跟 2 比较
        直到 20 跟 4 比较大于 5 结束
        :param data: 一维有序数据结构
        :param nn: 首次判断时比较的值
        :param difference: 最大跨度
        :return: 过滤后的列表
        """
        data_copy = list(data)
        for ii in data:
            if -difference <= ii - nn <= difference:
                data_copy = data_copy[1:]
                nn = ii
            else:
                break
        return data_copy

    def correction(self, src, max_angle=5, threshold=100, angle=0.0):
        """
        对图片自动旋转矫正
        :param src: 要旋转的图片(二值, 背景黑色, 0, 255)
        :param max_angle: 允许的最大旋转角度
        :param threshold: 初始判断阈值, 当某一行的平均值小于此值将会继续进行
        :param angle: 初始旋转角度, 若指定则会先旋转此角度, 后进行继续判断
        :return: 旋转角度, 结束时阈值, 白色点最少的行
        """
        src_ = src
        if angle > max_angle or angle < -max_angle:
            return None, None, None
        if angle != 0:
            src = self.rotate_bound(src, angle)
        row_mean = src.mean(axis=1).round(2)
        row_min = row_mean.min()
        min_index = np.where(row_mean == row_min)[0]

        min_index = self._near(min_index, 0)
        min_index.reverse()
        min_index = self._near(min_index, src.shape[0])
        min_count = len(min_index)
        threshold_ = (row_min + 1) * 1. / (min_count + 1)
        if threshold_ <= threshold:
            result1 = result2 = 0.0, None, None
            if angle >= 0:
                result1 = self.correction(src_, threshold=threshold_, angle=angle + 0.5)
            if angle <= 0:
                result2 = self.correction(src_, threshold=threshold_, angle=angle - 0.5)
            if result1[1] is None:
                return (0.0, None, None) if result2[1] is None else result2
            else:
                if result2[1] is None:
                    return result1
                else:
                    return result1 if result1[1] < result2[1] else result2
        else:
            return angle, threshold_, min_index

    @staticmethod
    def _judging_the_edge(arr_1d, threshold=0, expansion=0):
        """
        返回去除两端小于阈值的索引范围
        :param arr_1d: 一维数组
        :param threshold: 阈值
        :param expansion: 扩展值(结果范围向两端扩展)
        :return: 索引开始值, 索引结束值
        """
        r = len(arr_1d)
        x1 = 0
        for x1 in range(r):
            if arr_1d[x1] > threshold:
                break
        x2 = r - 1
        for x2 in range(r - 1, 0, -1):
            if arr_1d[x2] > threshold:
                break
        x1 = 0 if x1 - expansion < 0 else x1 - expansion
        x2 = r if x2 + 1 + expansion > r else x2 + 1 + expansion
        return x1, x2

    def remove_the_edg(self, src, threshold=255 * 20, expansion=20):
        """
        去除二维矩阵边缘零值的索引范围
        :param src: 二维数组
        :param threshold: 阈值
        :param expansion: 扩展值(结果范围向两端扩展)
        :return: ((行开始, 行结束), (列开始, 列结束))
        """
        row = src.sum(axis=1)
        x1, x2 = self._judging_the_edge(row, threshold, expansion)
        column = src.sum(axis=0)
        y1, y2 = self._judging_the_edge(column, threshold, expansion)
        return (x1, x2), (y1, y2)


class SelectQrcode(ImageTools):
    @staticmethod
    def _select_area(array):
        """
        选择数组中有值的正方形区域
        :param array: 数组
        :return: 边长, 正方形位置(左上角)
        """
        index = list(zip(*np.where(array == 255)))
        if index:
            min_index = min(index, key=lambda x: x[0] + x[1])
            max_index = max(index, key=lambda x: x[0] + x[1])
            side_leng = ((max_index[0] - min_index[0]) + (max_index[1] - min_index[1])) // 2
            return side_leng, min_index[0], min_index[1]
        return 0, 0, 0

    def img_qrcode(self, src, show=False, binary_picture=False):
        """
        截取及标记二维码
        :param src: 灰度图
        :param show: 是否展示图片
        :param binary_picture: 是否展示处理过程图
        :return: 二维码图片数组, 及二维码位置
        """
        src_ = self.binarization(src, 40)

        ll = int(np.sqrt(self.h * self.w / 10000) + 5)
        src = self.area(src_, 30, gap_filling=(ll, ll))

        # 腐蚀和膨胀
        n = 0
        while True:
            src = cv2.erode(src, None, iterations=5)
            n += 1
            if n > 5 and src.sum() < 255 * 20 ** 2:
                break
        src = cv2.dilate(src, None, iterations=5 * n + 5)

        if binary_picture:
            self.show_from_array(src)

        sid_length, x, y = self._select_area(src)

        image_3 = self.array_to_image(self.image)

        position = [y, x, sid_length, sid_length]
        qrcode = False
        if sid_length:
            if src_[x - 10:x + sid_length + 10, y - 10:y + sid_length + 10].mean() > 255 * 0.1:
                qrcode = self.image[x - 10:x + sid_length + 10, y - 10:y + sid_length + 10]
        if show:
            draw = ImageDraw.Draw(image_3)
            self.rectangle(draw, *position, expand=7)
            image_3.show()
        return qrcode, position


class Segmentation(ImageTools):
    """
    未使用, 暂留
    """
    @staticmethod
    def is_blank(src, coordinate, is_img=False, threshold=0.00005, multiple=5):
        x1, x2, y1, y2 = coordinate
        if is_img:
            if ((x2 - x1) // (y2 - y1) >= multiple) \
                    or ((y2 - y1) // (x2 - x1) >= multiple):
                return True
        array = src[x1:x2, y1:y2]
        return array.mean() < 255 * threshold

    def segmentation(self, src, coordinate, dividing_line=50, *, h=False, w=False):
        if h ^ w:
            raise ValueError("需要h与w有且只有一个为True")
        x1, x2, y1, y2 = coordinate
        _h, _w = src[x1:x2, y1:y2].shape
        h, w = _h * h, _w * w
        h_center, w_center = h // 2, w // 2
        for i in range(dividing_line, h_center+w_center, dividing_line):
            h_effective = i if h else 0
            w_effective = i if h else 0
            coordinate_ = (
                x1 + h_center - h_effective, x1 + h_center - h_effective + dividing_line,
                y1 + w_center - w_effective, y1 + w_center - w_effective + dividing_line)
            if self.is_blank(src, coordinate_):
                out = h_center + w_center - i
                break
            coordinate_ = (
                x1 + h_center + h_effective - dividing_line, x1 + h_center + h_effective,
                y1 + w_center + w_effective - dividing_line, y1 + w_center + w_effective)
            if self.is_blank(src, coordinate_):
                out = h_center + w_center + i
                break
        else:
            return () if self.is_blank(src, coordinate, True) else (coordinate,)
        if w == 0:
            coordinate_1, coordinate_2 = (x1, x1 + out, y1, y2), (x1 + out, x2, y1, y2)
        else:
            coordinate_1, coordinate_2 = (x1, x2, y1, y1 + out), (x1, x2, y1 + out, y2)
        if self.is_blank(src, coordinate_1, True):
            return self.segmentation(src, coordinate_2, dividing_line, h=h, w=w)
        if self.is_blank(src, coordinate_2, True):
            return self.segmentation(src, coordinate_1, dividing_line, h=h, w=w)
        result = (*self.segmentation(src, coordinate_1, dividing_line, h=h, w=w),
                  *self.segmentation(src, coordinate_2, dividing_line, h=h, w=w))
        return result

    def run(self, src):
        h, w = src.shape[:2]
        s = self.segmentation(src, (0, h, 0, w), h=True)
        for i in s:
            for i2 in self.segmentation(src, i, w=True):
                for j in self.segmentation(src, i2, h=True):
                    image_array = self.image[j[0]:j[1], j[2]:j[3]]
                    self.show_from_array(image_array)
