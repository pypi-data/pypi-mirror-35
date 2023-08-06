import pandas as pd


def rolling_median(emg, window, min_periods=None, freq=None, center=False):
    """

    :param emg:
    :param window:
    :param min_periods:
    :param freq:
    :param center:
    :return:
    """

    new_header = emg.header.copy()
    new_data = pd.rolling_median(emg.data, window, min_periods=min_periods, freq=freq, center=center)
    new_emg = Emg()
    new_emg.header = new_header
    new_emg.data = new_data
    new_emg.name = "{}_median".format(emg.name)
    return new_emg
