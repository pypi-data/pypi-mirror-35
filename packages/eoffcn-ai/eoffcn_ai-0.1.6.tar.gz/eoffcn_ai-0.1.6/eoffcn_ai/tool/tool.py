class Tool:
    __conf = {
        "壹": 1, "贰": 2, "叁": 3,
        "肆": 4, "伍": 5, "陆": 6,
        "柒": 7, "捌": 8, "玖": 9, "零": 0,
        "拾": 10, "佰": 100, "仟": 1000,
        "万": 10000, "亿": 100000000,
        "圆": 1, "角": 0.1, "分": 0.01
    }

    @staticmethod
    def get(dict_or_list, key):
        """
        获取对应键或索引的值
        :param dict_or_list: dict/list
        :param key: 索引/键
        :return: value
        """
        value = None
        if isinstance(dict_or_list, dict):
            if key[0] == "_" == key[-1] and key[1:-1].isnumeric():
                key = int(key[1:-1])
            value = dict_or_list.get(key, None)
        elif isinstance(dict_or_list, list):
            if key.isnumeric():
                index = int(key)
                if len(dict_or_list) > index:
                    value = dict_or_list[index]
        return value

    @staticmethod
    def get_value(dict_or_list, keys):
        """
        获取字典中对应key(多层嵌套)的值
        :param dict_or_list: 嵌套字典或列表
        :param keys: 多个key使用 "." 隔开
                     字典中想使用数字索引则需在两端加上 "_", 如 "_2_"
        :return: 按给定key取到的值
        """
        if keys is None:
            return None
        keys = keys.split(".")
        for key in keys:
            dict_or_list = __class__.get(dict_or_list, key)
            if dict_or_list is None:
                break
        return dict_or_list

    @staticmethod
    def __conversion(string):
        value = __class__.__conf[string[0]]
        for i in string[1:]:
            value *= __class__.__conf[i]
        return value

    @staticmethod
    def amount_conversion(string, level="圆"):
        """
        大写数字转换为数值
        :param string: 大写数字
        :param level: 起始单位, 只能是 "圆角分"
        :return: 转换结果
        """
        if string == "":
            return 0

        values = []
        for n, i in enumerate(string):
            if i in "圆角分":
                level = i
                string = string[n+1:]
                break
            v = __class__.__conf[i]
            if v < 10 or len(values) == 0 or len(values[-1]) == 2:
                values.append(i)
            else:
                values[-1] += i
        else:
            string = ""

        if not values:
            return 0

        value = __class__.__conversion(values[0])
        for i in values[1:]:
            v = __class__.__conversion(i)
            if v > value:
                value *= v
            else:
                value += v
        _level = "圆角分零零"["圆角分零".find(level)+1]
        return value * __class__.__conf[level] + __class__.amount_conversion(string, _level)
