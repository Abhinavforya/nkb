def generate_ascii(midi_data):
    if not midi_data:
        return "Error parsing MIDI file. Please ensure it is a valid .mid file."
    
    ascii_result = "=== MIDI ASCII ART ===\n"
    for instrument in midi_data.instruments:
        ascii_result += f"\nInstrument: {instrument.program}\n"
        if instrument.is_drum:
            ascii_result += "[Drums]\n"
            continue
        
        # Simple rendering for first 20 notes
        for note in instrument.notes[:20]:
            bar = "#" * max(1, (note.pitch // 5))
            ascii_result += f"{note.pitch:03} | {bar}\n"
            
    return ascii_result
