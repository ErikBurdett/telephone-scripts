import pretty_midi


midi = pretty_midi.PrettyMIDI()


synth = pretty_midi.Instrument(program=89)


notes = ['C4', 'G3', 'G#3', 'G3', 'C4', 'G3', 'F3', 'G3']


for i, note_name in enumerate(notes):

    note_number = pretty_midi.note_name_to_number(note_name)
    
    start_time = i * 0.5
    end_time = (i + 1) * 0.5

    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start_time, end=end_time)
    synth.notes.append(note)


midi.instruments.append(synth)


midi.write('breathless-synth.midi')
