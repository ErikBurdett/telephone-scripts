# import pretty_midi
# # Set up instrument and tempo
# instrument = pretty_midi.PrettyMIDI() # Load MIDI file into instrument
# tempo = 120
# # Define drum track notes
# kick = 36
# snare = 38
# closed_hihat = 42
# notes = [pretty_midi.Note(velocity=75, pitch=kick) for _ in range(1)] + \
#           [pretty_midi.Note(velocity=70, pitch=snare) for _ in range(8)] + \
#           [pretty_midi.Note(velocity=65, pitch=closed_hihat) for _ in range(4)]
# # Create drum track instrument and add notes to it
# drums = pretty_midi.PrettyMIDI() # Load MIDI file into instrument
# for note in notes:
#     start, end = pretty_midi.get_note_times(instrument, kick)
#     drums.add_note(pretty_midi.Note(velocity=75, pitch=kick), start=start, end=end)
    
# # Add drum track to MIDI file
# with open('breathless_drum_track.mid', 'wb') as midi_file:
#     pretty_midi.write_midi(drums, output=midi_file, tempo=tempo)