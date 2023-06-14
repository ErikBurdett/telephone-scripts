import pretty_midi
import numpy as np

midi = pretty_midi.PrettyMIDI(initial_tempo=89)  

piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)


scale = [60, 62, 64, 65, 67, 69, 71, 72]  


note_duration = 0.8  
note_interval = 1.0  

#
fade_in_duration = 10  
fade_out_duration = 10  
max_velocity = 100  


total_duration = 60  


time = 0
while time < total_duration:

    if time < fade_in_duration:
        velocity = int((time / fade_in_duration) * max_velocity)
    elif time > total_duration - fade_out_duration:
        velocity = int(((total_duration - time) / fade_out_duration) * max_velocity)
    else:
        velocity = max_velocity


    note_number = scale[np.random.randint(0, 7)]


    note = pretty_midi.Note(
        velocity=velocity,
        pitch=note_number,
        start=time,
        end=time + note_duration
    )


    piano.notes.append(note)


    time += note_interval


midi.instruments.append(piano)


midi.write('t-s-i.midi')
