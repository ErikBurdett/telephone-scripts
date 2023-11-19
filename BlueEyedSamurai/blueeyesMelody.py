import pretty_midi

def create_ambient_piano_track():
    # Create a PrettyMIDI object
    midi_data = pretty_midi.PrettyMIDI(initial_tempo=80)

    # Create an Instrument instance for a piano
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)

    # Define the scale and key (C Major for simplicity)
    scale = [0, 2, 4, 5, 7, 9, 11]  # C Major scale
    key = 60  # Middle C

    # Generate a simple melody and chords in Erik Satie's style
    start_time = 0
    duration = 1  # 1 second per note for a calm, sustained feel
    for note_number in scale:
        # Create a note instance for the melody
        note = pretty_midi.Note(
            velocity=100, pitch=key + note_number, start=start_time, end=start_time + duration
        )
        piano.notes.append(note)

        # Create overlapping notes for echo effect
        echo_note = pretty_midi.Note(
            velocity=60, pitch=key + note_number, start=start_time + 0.5, end=start_time + duration + 0.5
        )
        piano.notes.append(echo_note)

        start_time += 0.5  # Move to the next note position

    # Add the piano instrument to the PrettyMIDI object
    midi_data.instruments.append(piano)

    # Save the MIDI file
    midi_file_name = 'ambient_piano.midi'
    midi_data.write(midi_file_name)

    return midi_file_name

# Create and save the ambient piano track
ambient_piano_midi = create_ambient_piano_track()
print(f"MIDI file created: {ambient_piano_midi}")
