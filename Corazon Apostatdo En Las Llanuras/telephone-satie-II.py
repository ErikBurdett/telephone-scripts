import pretty_midi
import numpy as np


cello_c_chord = pretty_midi.PrettyMIDI()


cello_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
cello = pretty_midi.Instrument(program=cello_program)


notes = ['C5', 'E5', 'G5', 'B5', 'C6', 'D6', 'F6', 'G6', 'A6', 'B6', 'C7']

start_time = 0
end_time = start_time + 1/80*60 
for note_name in notes:
    note_number = pretty_midi.note_name_to_number(note_name)
    note = pretty_midi.Note(
        velocity=100, pitch=note_number, start=start_time, end=end_time)
    cello.notes.append(note)
    start_time += 1/80*60
    end_time += 1/80*60


cello_c_chord.instruments.append(cello)

cello_c_chord.write('c-scale-1-min.midi')
