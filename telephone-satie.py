import pretty_midi
import numpy as np

midi = pretty_midi.PrettyMIDI()


piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)


scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C Major scale in MIDI numbers


for i in range(8):
    note_number = scale[np.random.randint(0, 7)]
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=i*0.5, end=(i+1)*0.5)
    piano.notes.append(note)


for i in range(8, 16):
    note_number = scale[np.random.randint(0, 7)]
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=i*0.5, end=(i+1)*0.5)
    piano.notes.append(note)

for i in range(16, 24):
    note_number = scale[np.random.randint(0, 7)]
    note = pretty_midi.Note(velocity=60, pitch=note_number, start=i*0.5, end=(i+1)*0.5)
    piano.notes.append(note)


for i in range(24, 32):
    note_number = scale[np.random.randint(0, 7)]
    note = pretty_midi.Note(velocity=40, pitch=note_number, start=i*0.5, end=(i+1)*0.5)
    piano.notes.append(note)


midi.instruments.append(piano)


midi.write('t-s-0.midi')
