import pretty_midi

midi = pretty_midi.PrettyMIDI()

drum = pretty_midi.Instrument(program=0, is_drum=True)


kick = 36
snare = 38
closed_hi_hat = 42


for i in range(16):
   
    if i in [0, 10]:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=i*0.25, end=(i*0.25) + 0.25)
        drum.notes.append(note)
   
    elif i in [4, 12]:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=i*0.25, end=(i*0.25) + 0.25)
        drum.notes.append(note)
   
    note = pretty_midi.Note(velocity=70, pitch=closed_hi_hat, start=i*0.25, end=(i*0.25) + 0.1)
    drum.notes.append(note)


midi.instruments.append(drum)


midi.write('breathless_drum_track.midi')
