import os
import re

from .zxing import BarCodeReader


def qrdecode(qrcode_path, delete=True):
    result = None
    if os.name == 'nt':
        # 使用zbar识别二维码, 暂仅支持Windows
        zbarimg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ZBar_Win", "bin", "zbarimg.exe")
        barcode = os.popen(f"{zbarimg_path} -D {qrcode_path}").read()
        if barcode:
            result = barcode[8:]
    elif os.environ.get('JAVA_HOME'):
        # 使用zxing识别二维码, 基于Java环境
        try:
            zx = BarCodeReader()
            barcode = zx.decode(qrcode_path)
            if barcode:
                result = barcode.data
        except:
            pass
    else:
        # 使用php识别二维码, 基于php环境
        qrcode_decode_path = os.path.dirname(os.path.abspath(__file__)) + '/php_qrdecode'
        barcode = os.popen(f"php {qrcode_decode_path}/decode.php {qrcode_path}").read()
        if re.match(r"\d\d,\d\d", barcode):
            result = barcode
    if delete:
        os.remove(qrcode_path)
    return result
