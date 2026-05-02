import librosa
import numpy as np

def generate_mp3_ascii(file_path):
    try:
        # Load audio file -> y is the audio time series, sr is sampling rate
        # We load a short snippet to avoid massive processing time and output
        y, sr = librosa.load(file_path, duration=10.0) 
        
        # Extract melspectrogram to visualize frequencies
        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=20)
        # Convert to decibels (log scale)
        S_dB = librosa.power_to_db(S, ref=np.max)
        
        # Scale to ASCII characters based on intensity
        chars = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
        # Normalize between 0 and len(chars)-1
        S_normalized = (S_dB - S_dB.min()) / (S_dB.max() - S_dB.min() + 1e-6)
        S_indices = (S_normalized * (len(chars) - 1)).astype(int)
        
        ascii_result = "=== MP3 SPECTROGRAM ASCII ===\n"
        
        # Iterate frequencies (top to bottom)
        for i in reversed(range(S_indices.shape[0])):
            row = ""
            for j in range(0, S_indices.shape[1], max(1, S_indices.shape[1] // 80)): # max 80 width
                idx = S_indices[i, j]
                row += chars[idx]
            ascii_result += row + "\n"
            
        return ascii_result
    except Exception as e:
        return f"Error processing MP3: {e}"
