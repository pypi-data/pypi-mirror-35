import numpy as np
import pandas as pd


def feature_creators(list_functions, history_size):
    feature_creators.res = pd.DataFrame()

    def feats_and_concat(small_df):
        small_df.index = small_df.index.get_level_values(0)
        index = small_df.index[-1]
        line = pd.DataFrame()
        for func in list_functions:
            tmp = func(small_df)
            line = pd.concat([line, tmp], axis=1)
        line.index = [index]
        feature_creators.res = pd.concat([feature_creators.res, line])

    def run(df):
        for i in range(len(df.index) - history_size + 1):
            sub_df = df[i:i + history_size]
            feats_and_concat(sub_df)
        # _roll_big_data(df, history_size=history_size).apply(feats_and_concat)
        return feature_creators.res

    return run


def fe_get_day_of_week(name_of_feature):
    def get_day_of_week(df_small):
        return pd.DataFrame({name_of_feature: [df_small.index[-1].weekday()]})

    return get_day_of_week


def _roll(df, history_size, **kwargs):
    roll_array = np.dstack([df.values[i:i + history_size, :] for i in range(len(df.index) - history_size + 1)]).T
    panel = pd.Panel(roll_array,
                     items=df.index[history_size - 1:],
                     major_axis=df.columns, minor_axis=pd.Index(range(history_size), name='roll'))
    df_group = panel.to_frame().unstack().T.groupby(level=0, **kwargs)
    return df_group


def _roll_big_data(df, history_size, **kwargs):
    sub_df = pd.DataFrame()
    return sub_df
