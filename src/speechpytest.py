import scipy.io.wavfile as wav
import numpy as np
import sys
import os
import speechpy


def run(file_path):
    lib_path = os.path.abspath(os.path.join('..'))
    sys.path.append(lib_path)

    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),file_path)
    fs, signal = wav.read(file_name)
    if signal.ndim > 1:
        signal = signal[:, 0]

    # Example of pre-emphasizing.
    signal_preemphasized = speechpy.processing.preemphasis(signal, cof=0.98)

    # Example of staching frames
    frames = speechpy.processing.stack_frames(signal, sampling_frequency=fs, frame_length=0.020, frame_stride=0.01, filter=lambda x: np.ones((x,)),
             zero_padding=True)

    # Example of extracting power spectrum
    power_spectrum = speechpy.processing.power_spectrum(frames, fft_points=512)
    import matplotlib.pyplot as plt
    plt.specgram(power_spectrum, Fs=fs)
    plt.show()
    print('power spectrum shape=', power_spectrum.shape)

    ############# Extract MFCC features #############
    mfcc = speechpy.feature.mfcc(signal, sampling_frequency=fs, frame_length=0.020, frame_stride=0.01,
                 num_filters=40, fft_length=512, low_frequency=0, high_frequency=None)


    mfcc_cmvn = speechpy.processing.cmvnw(mfcc,win_size=301,variance_normalization=True)
    print('mfcc(mean + variance normalized) feature shape=', mfcc_cmvn.shape)

    mfcc_feature_cube = speechpy.feature.extract_derivative_feature(mfcc)
    print('mfcc feature cube shape=', mfcc_feature_cube.shape)

    ############# Extract logenergy features #############
    logenergy = speechpy.feature.lmfe(signal, sampling_frequency=fs, frame_length=0.020, frame_stride=0.01,
                 num_filters=40, fft_length=512, low_frequency=0, high_frequency=None)
    logenergy_feature_cube = speechpy.feature.extract_derivative_feature(logenergy)

    print('logenergy features=', logenergy.shape)
    print('logenergy feature cube=', logenergy_feature_cube.shape)


if __name__ == "__main__":
    run('sourcefiles/3.wav')
