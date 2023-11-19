import pretty_midi
import numpy as np

# Initialize PrettyMIDI object with a slower tempo for lo-fi
midi = pretty_midi.PrettyMIDI(initial_tempo=80)

# Define piano program and create piano instrument
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)

# Define piano melody notes and patterns
# Using C major scale for simplicity: C4, D4, E4, F4, G4, A4, B4, C5
notes = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86]
melody_pattern = [0, 5, 8, 11, 12, 7, 4, 1, 0, 5, 8, 11, 14, 15, 12, 9]  # Index into notes array

eight_bars_time_melody = np.linspace(0, 8 * 4, 16)  # 8 bars at 2 units per bar for melody

for i, time_unit in enumerate(eight_bars_time_melody):
    note_number = notes[melody_pattern[i]]
    note = pretty_midi.Note(velocity=70, pitch=note_number, start=time_unit, end=time_unit + 0.5)
    piano.notes.append(note)

# Add piano instrument to PrettyMIDI object
midi.instruments.append(piano)

# Write MIDI to disk
midi.write("lofi_hiphop_piano_track.midi")
