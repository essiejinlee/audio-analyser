import librosa
import matplotlib.pyplot as plt
import numpy as np

# Generate and save waveform plot
def plot_waveform(file_path):
    # Load audio file as time-series signal
    y, sr = librosa.load(file_path)

    # Create waveform plot
    plt.figure()
    plt.plot(y)
    plt.title("Waveform")
    # Save image
    plt.savefig("waveform.png")
    plt.close()

    return "waveform.png"

# Generate and save spectrogram
def plot_spectrogram(file_path):
    # Load audio file
    y, sr = librosa.load(file_path)

    # Compute Short-Time Fourier Transform (STFT)
    D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)

    # Create spectrogram plot
    plt.figure()
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    # Save image
    plt.savefig("spectrogram.png")
    plt.close()

    return "spectrogram.png"

# Generate pitch contour (pitch over time)
def plot_pitch(file_path):
    y, sr = librosa.load(file_path)

    # Extract fundamental frequency using YIN algorithm
    f0 = librosa.yin(y, fmin=50, fmax=2000)

    # Create time axis for plotting
    times = np.arange(len(f0)) * (len(y)/sr) / len(f0)

    # Create pitch contour plot
    plt.figure()
    plt.plot(times, f0)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Pitch (Hz)")
    plt.title("Pitch Contour")

    # Save image
    plt.savefig("pitch.png")
    plt.close()

    return "pitch.png"

# Estimate tempo (BPM)
def get_tempo(file_path):
    y, sr = librosa.load(file_path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return tempo

# Estimate average pitch using spectral peaks
def get_pitch(file_path):
    y, sr = librosa.load(file_path)

    # Extract pitch candidates and magnitudes
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    pitch_values = []

    # Select strongest pitch for each frame
    for i in range(pitches.shape[1]):
        index = magnitudes[:, i].argmax()
        pitch = pitches[index, i]
        if pitch > 0:
            pitch_values.append(pitch)

    # Return mean pitch value
    if len(pitch_values) == 0:
        return 0
    
    return float(np.mean(pitch_values))