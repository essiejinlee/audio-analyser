async function upload() {
    const file = document.getElementById("fileInput").files[0];

    let formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/analyse/", {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    document.getElementById("waveform").src = data.waveform;
    document.getElementById("spectrogram").src = data.spectrogram;
    document.getElementById("tempo").innerText = "Tempo: " + data.tempo;
}