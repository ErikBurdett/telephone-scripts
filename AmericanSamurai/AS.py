import mido
from mido import MidiFile, MidiTrack, Message

def create_drum_track(tempo=120, length=4):
    # MIDI note numbers for standard drum kit elements
    kick = 36  # C1
    snare = 38 # D1
    hihat = 42 # F#1

    # Create a new MIDI file and track
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Set the tempo (microseconds per beat)
    microseconds_per_beat = mido.bpm2tempo(tempo)
    track.append(mido.MetaMessage('set_tempo', tempo=microseconds_per_beat))

    # Define the basic pattern
    for i in range(length):
        # Add a kick on beats 1 and 3
        if i % 2 == 0:
            track.append(Message('note_on', note=kick, velocity=64, time=0))
            track.append(Message('note_off', note=kick, time=480)) # 480 ticks for a quarter note

        # Add a snare on beats 2 and 4
        else:
            track.append(Message('note_on', note=snare, velocity=64, time=0))
            track.append(Message('note_off', note=snare, time=480))

        # Add a closed hi-hat on each beat
        track.append(Message('note_on', note=hihat, velocity=64, time=0))
        track.append(Message('note_off', note=hihat, time=480))

    return mid

# Create a drum track and save as a MIDI file
drum_track = create_drum_track()
drum_track.save('drum_track.mid')
