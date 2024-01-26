import mido
from mido import MidiFile, MidiTrack, Message

def create_trap_drum_track(tempo=133, length=16):
    # MIDI note numbers for standard drum kit elements in trap music
    kick = 36  # C1
    snare = 38 # D1
    hi_hat = 42 # F#1

    # Create a new MIDI file and track
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Set the tempo (microseconds per beat)
    microseconds_per_beat = mido.bpm2tempo(tempo)
    track.append(mido.MetaMessage('set_tempo', tempo=microseconds_per_beat))

    # Define the basic pattern
    for i in range(length):
        # Add a kick on specific beats for the trap feel
        if i % 4 == 0:
            track.append(Message('note_on', note=kick, velocity=100, time=0))
            track.append(Message('note_off', note=kick, time=240)) # 1/8 note

        # Add a snare on the 3rd beat of every bar
        if i % 4 == 2:
            track.append(Message('note_on', note=snare, velocity=100, time=0))
            track.append(Message('note_off', note=snare, time=480)) # 1/4 note

        # Hi-hat pattern
        for j in range(4):  # Fast hi-hat hits
            track.append(Message('note_on', note=hi_hat, velocity=80, time=0 if j==0 else 120))
            track.append(Message('note_off', note=hi_hat, time=120))

    return mid

# Create the drum track and save as a MIDI file
trap_drum_track = create_trap_drum_track()
trap_drum_track.save('trap_drum_track.midi')
