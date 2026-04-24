from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import shutil
from audio import plot_waveform, plot_spectrogram, plot_pitch, get_tempo, get_pitch

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/analyse/")
async def analyse(file: UploadFile = File(...)):
    file_location = f"temp.wav"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    waveform = plot_waveform(file_location)
    spectrogram = plot_spectrogram(file_location)
    pitch_plot = plot_pitch(file_location)
    tempo = get_tempo(file_location)
    pitch = float(get_pitch(file_location))

    return {
        "waveform": waveform,
        "spectrogram": spectrogram,
        "pitch_plot": pitch_plot,
        "tempo": tempo,
        "pitch": pitch
    }