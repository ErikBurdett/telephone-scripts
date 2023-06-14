import pretty_midi
import numpy as np

midi = pretty_midi.PrettyMIDI(initial_tempo=80)  # 80 BPM

piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)

whole_tone_scale = ['C4', 'D4', 'E4', 'F#4', 'G#4', 'A#4', 'C5']

notes = (whole_tone_scale * 14)[:80]

start_time = 0
end_time = 1 / 1.33
note_duration = end_time - start_time
for note_name in notes:
    note_number = pretty_midi.note_name_to_number(note_name)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start_time, end=end_time)
    piano.notes.append(note)
    start_time += note_duration
    end_time = start_time + note_duration

midi.instruments.append(piano)

midi.write('wholetone.midi')
