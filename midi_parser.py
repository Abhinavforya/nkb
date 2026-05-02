import pretty_midi

def parse_midi(file_obj):
    try:
        midi_data = pretty_midi.PrettyMIDI(file_obj)
        return midi_data
    except Exception as e:
        print(f"Error parsing MIDI: {e}")
        return None
