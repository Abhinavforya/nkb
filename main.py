from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from midi_parser import parse_midi
from ascii_generator import generate_ascii
from mp3_parser import generate_mp3_ascii
import io
import os
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "MIDI to ASCII Server is running. Visit /docs to test the API."}

@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    filename = file.filename.lower()
    
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        # Save temp file for librosa processing
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Process audio to ASCII
        ascii_art = generate_mp3_ascii(temp_path)
        
        # Remove original
        os.remove(temp_path)
        return {"ascii": ascii_art}
    else:
        # Default midi processing
        content = await file.read()
        midi_data = parse_midi(io.BytesIO(content))
        ascii_art = generate_ascii(midi_data)
        return {"ascii": ascii_art}
