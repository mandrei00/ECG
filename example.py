import scipy.datasets
import neurokit2
import sleepecg
import wfdb.processing
import wfdb


def example_neurokit2(ecg_signal):
    """

    Это пример использования библиотеки neurokit2 для поиска пиков.

    :param ecg_signal: numpy массив с размерностью 1
    :return:
    """
    _, r_peaks = neurokit2.ecg_peaks(ecg_signal, sampling_rate=360)
    return r_peaks


def example_sleepecg(ecg_signal):
    """

    Это пример использования библиотеки sleepecg для поиска пиков.

    :param ecg_signal:
    :return:
    """
    r_peaks = sleepecg.detect_heartbeats(ecg_signal, fs=360)
    return r_peaks


def example_wfdb(ecg_signal):
    """
    Это пример использования библиотеки wfdb для поиска пиков.
    :param ecg_signal:
    :return:
    """
    r_peaks = wfdb.processing.xqrs_detect(ecg_signal, fs=360, verbose=False)
    return r_peaks


def correct_r_peaks(ecg_signal, r_peaks):
    """
    Некоторые R пики сдвигаются в процессе обработки и их иногда нужно обработать
    :param r_peaks:
    :return:
    """
    return wfdb.processing.correct_peaks(ecg_signal, r_peaks, search_radius=36, smooth_window_size=50, peak_dir="up")


def main():
    ecg_signal = scipy.datasets.electrocardiogram()
    r_peaks = example_sleepecg(ecg_signal)
    # r_peaks = example_wfdb(ecg_signal)

    corrected_r_peaks = correct_r_peaks(ecg_signal, r_peaks)

    fig = wfdb.plot_items(
        ecg_signal,
        [corrected_r_peaks],
        fs=360,
        sig_name=["ECG"],
        sig_units=["mV"],
        time_units="seconds",
        # return_fig=True,
        ann_style="o",
    )



if __name__ == "__main__":
    main()

