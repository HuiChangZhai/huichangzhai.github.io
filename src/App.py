import SpeechRecognition.AutoSpeechRecognition as asr
import numpy as np

source_folder = "sourcefiles"
destination_folder = "destfiles"


def run():
    pass

    # test_num()
    # speechpyrun()
    wav_plot("left.wav", noise=200)
    # test_frequency()
    # dir_abstract()
    # test_outer_line()
    # test_left()
    # wav_specgram('left.wav')
    # melspectrogram('left.wav')
    # mfcc_s('left.wav')
    #get_mfcc2('left.wav')

def melspectrogram(filename):
    import librosa

    y, sr = librosa.load(filename)
    librosa.feature.melspectrogram(y=y, sr=sr)

    D = np.abs(librosa.stft(y)) ** 2
    S = librosa.feature.melspectrogram(S=D)

    # Passing through arguments to the Mel filters
    #S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max),
                             y_axis='mel', fmax=8000,
                             x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel spectrogram')
    plt.tight_layout()
    plt.show()

def mfcc_s(filename):
    import librosa
    import scipy
    import matplotlib.pyplot as plt

    rate, signal_data = scipy.io.wavfile.read(filename)
    if signal_data.ndim > 1:
        signal = signal_data[:,0]
    mfccs = librosa.feature.mfcc(y=signal_data, sr=rate, n_mfcc=40)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mfccs, x_axis='time')
    plt.colorbar()
    plt.title('MFCC')
    plt.tight_layout()
    plt.show()


def get_mfcc2(filename):
    from scikits.talkbox.features import mfcc
    import os
    import scipy

    rate, signal = scipy.io.wavfile.read(filename)
    ceps, mspec, spec = mfcc(signal)
    base_filename, ext = os.path.splitext(filename)
    data_filename = base_filename + ".ceps"
    np.save(data_filename, ceps)
    print(" Written %s" % data_filename)


def wav_specgram(filename):
    import scipy
    import matplotlib.pyplot as plt

    rate, signal = scipy.io.wavfile.read(filename)
    if signal.ndim > 1:
        signal = signal[:, 0]

    plt.specgram(signal, Fs=rate, xextent=(0, 0.1))
    plt.show()


def test_outer_line():
    def run(filename, **kwargs):
        noise = kwargs.pop("noise", None)
        volume = kwargs.pop("volume", None)
        cut = kwargs.pop("cut", None)
        recognition = asr.SpeechRecognition()
        recognition.read(filename)

        if volume:
            recognition.volume(volume)

        if noise:
            recognition.denoise(500)

        if cut:
            recognition.trim(cut)

        recognition.outer_line(20)

    for i in range(0,10):
        run(source_folder + '/' + str(i) + '.wav', noise = 200, cut = 100, volume = 10000)


def dir_abstract():
    import os
    dirv1 = 'G:\speech_commands_v0.01'
    dirv2 = 'G:\speech_commands_v0.02'
    def display_dir(dir):
        files = os.listdir(dir)
        file_count = 0
        for item in files:
            if os.path.isdir(dir + '/' + item):
                display_dir(dir + '/' + item)
            else:
                file_count= file_count + 1

        print(dir + ':' + str(file_count))

    display_dir(dirv2)


def test_frequency():
    def run(filename, **kwargs):
        noise = kwargs.pop("noise", None)
        volume = kwargs.pop("volume", None)
        cut = kwargs.pop("cut", None)
        recognition = asr.SpeechRecognition()
        recognition.read(filename)

        if volume:
            recognition.volume(volume)

        if noise:
            recognition.denoise(500)

        if cut:
            recognition.trim(cut)

        frequency = recognition.frequency(threshold=0)
        if not frequency is None:
            print(frequency)

    for i in range(0,10):
        run(source_folder + '/' + str(i) + '.wav', noise = 200, cut = 100, volume = 10000)


def wav_plot(filename, **kwargs):
    import os
    saved_filename, ext = os.path.splitext(filename)
    # saved_filename = filename.replace(".wav", "")
    # saved_filename = saved_filename[saved_filename.rindex("/")+1:]
    noise = kwargs.pop("noise", None)
    volume = kwargs.pop("volume", None)
    cut = kwargs.pop("cut", None)

    recognition = asr.SpeechRecognition()
    recognition.read(filename)

    if volume:
        saved_filename = saved_filename + "_volume" + str(volume) + "_"
        recognition.volume(volume)

    if noise:
        saved_filename = saved_filename + "_noise" + str(noise) + "_"
        recognition.denoise(noise)

    if cut:
        saved_filename = saved_filename + "_cut" + str(cut) + "_"
        recognition.trim(cut)

    recognition.plot("-", title=filename)
    recognition.write(destination_folder + "/" + saved_filename + ".wav")


def test_left():
    wav_plot("../AudioListener/output.wav")


def test_num():
    files = [source_folder + "/" + str(i) + ".wav" for i in range(0, 10)]
    for file in files:
        wav_plot(file, noise=200, cut=100, volume=10000)


def speechpyrun():
    import speechpytest
    speechpytest.run('left.wav')
    #for i in range(0,10):
    #    speechpytest.run(source_folder + '/' + str(i) + '.wav')
    #    print('=============================================')

