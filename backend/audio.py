import librosa
import matplotlib.pyplot as plt
import numpy as np

def plot_waveform(file_path):
    y, sr = librosa.load(file_path)

    plt.figure()
    plt.plot(y)
    plt.title("Waveform")
    plt.savefig("waveform.png")
    plt.close()

    return "waveform.png"

def plot_spectrogram(file_path):
    y, sr = librosa.load(file_path)

    D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)

    plt.figure()
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.savefig("spectrogram.png")
    plt.close()

    return "spectrogram.png"

def get_tempo(file_path):
    y, sr = librosa.load(file_path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return tempo