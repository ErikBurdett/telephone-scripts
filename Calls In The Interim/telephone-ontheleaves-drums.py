import mido
from mido import Message, MidiFile, MidiTrack


mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)


track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(172)))

for i in range(4): 

    track.append(Message('note_on', channel=10, note=36, velocity=64, time=0))
    track.append(Message('note_off', channel=10, note=36, velocity=64, time=480))

    # Snare drum
    track.append(Message('note_on', channel=10, note=38, velocity=64, time=0))
    track.append(Message('note_off', channel=10, note=38, velocity=64, time=480))

    # High tom
    track.append(Message('note_on', channel=10, note=50, velocity=64, time=0))
    track.append(Message('note_off', channel=10, note=50, velocity=64, time=480))

    # Mid tom
    track.append(Message('note_on', channel=10, note=47, velocity=64, time=0))
    track.append(Message('note_off', channel=10, note=47, velocity=64, time=480))

mid.save('telephone-repeater-beat.mid')
