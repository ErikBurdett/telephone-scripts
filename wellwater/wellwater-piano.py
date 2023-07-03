import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=60)  # Erik Satie often used free tempo, but let's assume 60 BPM for simplicity.

# Create an Instrument instance for a piano instrument
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)

# Define the notes and their start/end times in seconds
notes = [
    ('A3', 'E4'),
    ('A3', 'C4'),
    ('G3', 'B3', 'E4'),
    ('G3', 'B3', 'D4'),
    ('F3', 'A3', 'D4'),
    ('E3', 'G3', 'C4'),
    ('D3', 'F3', 'A3'),
    ('C3', 'E3', 'G3'),
    ('B2', 'D3', 'F3'),  # Hypothetical additional bars
    ('A2', 'C3', 'E3')   # Hypothetical additional bars
]

# Create a time array using NumPy
time_array = np.arange(0, len(notes)*2, 2)

# Add notes to the piano instrument
for time, chord in zip(time_array, notes):
    for note_name in chord:
        note_number = pretty_midi.note_name_to_number(note_name)
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time+2)
        piano.notes.append(note)

# Add the piano instrument to the PrettyMIDI object
midi.instruments.append(piano)

# Write out the MIDI data
midi.write('gymnopedie_3_excerpt.midi')