from fastapi import FastAPI, UploadFile, File
import shutil
from audio import plot_waveform, plot_spectrogram, get_tempo

app = FastAPI()

@app.post("/analyse/")
async def analyse(file: UploadFile = File(...)):
    file_location = f"temp.wav"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    waveform = plot_waveform(file_location)
    spectrogram = plot_spectrogram(file_location)
    tempo = get_tempo(file_location)

    return {
        "waveform": waveform,
        "spectrogram": spectrogram,
        "tempo": tempo
    }