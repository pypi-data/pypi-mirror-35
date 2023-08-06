from .emg import EMG


def plot(emg, size):
    """

    :param emg:
    :param size:
    :return:
    """
    if isinstance(emg, (list, tuple)):
        emg_list = emg
    elif isinstance(emg, EMG):
        emg_list = [emg]
    else:
        raise

    for