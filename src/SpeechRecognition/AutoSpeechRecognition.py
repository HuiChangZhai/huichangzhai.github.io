from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np


class SpeechRecognition:
    def __init__(self):
        # plt.specgram
        self.rate = None
        self.data = None
        self.length= None
        self.second = None
        self.channelCount = None

    def read(self, filename):
        self.rate, self.data = wavfile.read(filename)
        if self.data.ndim > 1:
            self.data = self.data[:,0]#np.array([item[0] for item in self.data])
        self.length = len(self.data)
        self.second = self.length / self.rate
        self.channelCount = self.data.ndim

    def write(self, filename):
        wavfile.write(filename, self.rate, self.data)

    def denoise(self, noise):
        self.data[abs(self.data) < noise] = 0

    def volume(self, volume):
        max_volume = max(abs(self.data))
        data = [item / max_volume * volume for item in self.data]
        self.data = np.array(data, dtype=self.data.dtype)

    def trim(self, noise):
        start, end = (0, self.length)
        i = 0

        for i in range(0, self.length, 1):
            start = i
            if abs(self.data[i]) > noise:
                break

        for i in range(self.length - 1, -1, -1):
            end = i
            if abs(self.data[i]) > noise:
                break
        pre = 200
        if start > pre:
            start = start - pre

        if end < self.length - pre:
            end = end + pre

        if start < end:
            self.data = self.data[start: end]
            self.length = len(self.data)

    def plot(self, *args, **kwargs):
        start = kwargs.pop("start", 0)
        stop = kwargs.pop("stop", self.length)
        title = kwargs.pop("title", None)
        filename = kwargs.pop("filename", None)
        dpi = kwargs.pop("dpi", 300)

        if title:
            fig, ax = plt.subplots()
            ax.set(title=title)


        # gcf = plt.gcf()
        # dpi=300
        # gcf.set_size_inches(xlen / dpi, xlen / 10 / dpi)
        plt.plot(np.arange(start=start, stop=stop), self.data[start:stop], *args, **kwargs)
        if filename:
            if not dpi:
                dpi=300
            plt.savefig(filename, dpi=dpi)
        plt.show()

    def saveimg(self, filename, width, height, dpi=None):
        gcf = plt.gcf()
        if not dpi:
            dpi = 300
        gcf.set_size_inches(width / dpi, height / dpi)
        plt.savefig(filename, dpi=dpi)

    def frequency(self, **kwargs):
        threshold = kwargs.pop('threshold', 0)

        wave_filter = [-1, 1, -1]

        data_length = len(self.data)
        list = [self.data[i] if self.data[i] - self.data[i - 1] > threshold and self.data[i] - self.data[i + 1] > threshold else 0 for i in range(1, data_length - 2) \
                #if self.data[i] - self.data[i - 1] > threshold \
                #if self.data[i] - self.data[i + 1] > threshold \
                ]
        y = np.array(list)
        x = np.array(range(0, len(y)))

        #avg = np.average([list[j] - list[j - 1] for j in range(1, len(list))])

        #list = [list[j] - list[j - 1] for j in range(1, len(list)) if list[j] - list[j - 1] < avg * 5]

        plt.plot(x, y)
        plt.show()

    def outer_line(self, deg):
        import scipy as sp
        # import scipy.optimize
        y = self.data
        x = np.array(range(0, len(y)))

        x1 = x[y > 0]
        y1 = y[y > 0]
        x2 = x[y < 0]
        y2 = y[y < 0]

        fp1, fp2, fp3, fp4, fp5 = sp.polyfit(x1, y1, deg, full=True)

        f1 = sp.poly1d(fp1)

        fp2, fp2, fp3, fp4, fp5 = sp.polyfit(x2, y2, deg, full=True)

        f2 = sp.poly1d(fp2)
        
        fx1 = sp.linspace(0, x1[-1])
        fx2 = sp.linspace(0, x2[-1])

        plt.plot(fx1, f1(fx1), fx2, f2(fx2))
        plt.show()
