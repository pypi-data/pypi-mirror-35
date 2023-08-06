import pandas as pd

from ..tool import get_value


def filter_(df):
    return df


def get_df(dict_, data_key, word_key,
           left_key, top_key,
           right_key=None, bottom_key=None,
           height_key=None, width_key=None):
    """
    将字典转换为DataFrame
    :param dict_: 字典
    :param data_key: 获取行数据的key, "data.block.0.line"
    :param word_key: "word.0.content"
    :param left_key: "location.top_left.x"
    :param top_key: "location.top_left.y"
    :param right_key: "location.right_bottom.x"
    :param bottom_key: "location.right_bottom.y"
    :param height_key:
    :param width_key:
    :return: DataFrame
    """
    if right_key is None and width_key is None:
        raise ValueError("right_key与width_key至少有一个不为空")
    if bottom_key is None and height_key is None:
        raise ValueError("bottom_key与height_key至少有一个不为空")
    data_df = pd.DataFrame(columns=['word', 'left', 'top', 'right', 'bottom', 'height', 'width'])
    data = get_value(dict_, data_key)
    for n, row in enumerate(data):
        data_df.at[n, 'word'] = get_value(row, word_key)
        data_df.at[n, 'left'] = get_value(row, left_key)
        data_df.at[n, 'top'] = get_value(row, top_key)
        data_df.at[n, 'right'] = get_value(row, right_key)
        data_df.at[n, 'bottom'] = get_value(row, bottom_key)
        data_df.at[n, 'height'] = get_value(row, height_key)
        data_df.at[n, 'width'] = get_value(row, width_key)
        if data_df.at[n, 'height'] is None:
            data_df.at[n, 'height'] = data_df.at[n, 'bottom'] - data_df.at[n, 'top']
        else:
            data_df.at[n, 'bottom'] = data_df.at[n, 'top'] + data_df.at[n, 'height']
        if data_df.at[n, 'width'] is None:
            data_df.at[n, 'width'] = data_df.at[n, 'right'] - data_df.at[n, 'left']
        else:
            data_df.at[n, 'right'] = data_df.at[n, 'left'] + data_df.at[n, 'width']
    return data_df


def block(df, left=80, scope=(80, 200), filter_height=0.7):
    """
    分段
    :param df: get_df的返回值
    :param left: 求所有左侧坐标小于此值的平均值
    :param scope: 用于判断段首的位置, 在此范围内将被判断为段首
    :param filter_height: 行高小于 平均行高*filter_height 的行将被过滤
    :return: 含换行符的string
    """
    df = filter_(df)
    height_mean = df['height'].mean()
    df = df[df['height'] > height_mean * filter_height]
    left_mean = df['left'][df['left'] < left].mean()
    paragraph = (df['left'] > left_mean + scope[0]) & (df['left'] < left_mean + scope[1])
    paragraph_index = paragraph[paragraph].index
    for i in paragraph_index:
        df.at[i, 'word'] = '\n  ' + df.at[i, 'word']
    return df['word'].str.cat(sep='')


if __name__ == "__main__":
    print(get_value({"a": [1, {"b": 2}]}, "a.1.b"))
