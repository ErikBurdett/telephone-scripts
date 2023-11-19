import pretty_midi
import numpy as np

# Initialize PrettyMIDI object with a slower tempo for lo-fi
midi = pretty_midi.PrettyMIDI(initial_tempo=80)

# Define drum program and create instrument
drum_program = 0  # You can use any number, it's not important for drum tracks

drum = pretty_midi.Instrument(program=drum_program, is_drum=True)

# Define drum sounds
kick = 36
snare = 40
hihat_closed = 42
hihat_open = 46
tom_low = 41
tom_mid = 43
tom_high = 48
clap = 39
rimshot = 37
shaker = 82
tambourine = 54
ride_cymbal = 51
crash_cymbal = 49
splash_cymbal = 55
cowbell = 56
triangle = 81

# Define intricate 8-bar patterns
kick_pattern = [1, 0, 0, 0, 1, 0, 0, 0] * 16
snare_pattern = [0, 0, 0, 0, 0, 0, 1, 0] * 16
hihat_closed_pattern = [1, 1, 1, 1, 1, 1, 1, 1] * 16
clap_pattern = [0, 0, 0, 0, 0, 0, 0, 1] * 16
rimshot_pattern = [0, 1, 0, 0, 0, 0, 0, 0] * 16
tambourine_pattern = [0, 0, 0, 1, 0, 0, 0, 0] * 16
tom_low_pattern = [0, 0, 1, 0, 0, 0, 0, 0] * 16
tom_mid_pattern = [0, 0, 0, 0, 0, 1, 0, 0] * 16
tom_high_pattern = [0, 0, 0, 0, 0, 0, 0, 1] * 16
cowbell_pattern = [1, 0, 0, 0, 0, 0, 0, 0] * 16
shaker_pattern = [1, 1, 1, 1, 1, 1, 0, 1] * 16
triangle_pattern = [0, 0, 0, 0, 1, 0, 0, 0] * 16
ride_cymbal_pattern = [1, 0, 1, 0, 1, 0, 1, 0] * 16
crash_cymbal_pattern = [0, 0, 0, 0, 1, 0, 0, 0] * 16
splash_cymbal_pattern = [0, 0, 0, 0, 0, 1, 0, 0] * 16
hihat_open_pattern = [0, 0, 0, 1, 0, 0, 0, 0] * 16

# Generate MIDI notes based on patterns
patterns = [
    (kick, kick_pattern),
    (snare, snare_pattern),
    (hihat_closed, hihat_closed_pattern),
    (clap, clap_pattern),
    (rimshot, rimshot_pattern),
    (tambourine, tambourine_pattern),
    (tom_low, tom_low_pattern),
    (tom_mid, tom_mid_pattern),
    (tom_high, tom_high_pattern),
    (cowbell, cowbell_pattern),
    (shaker, shaker_pattern),
    (triangle, triangle_pattern),
    (ride_cymbal, ride_cymbal_pattern),
    (crash_cymbal, crash_cymbal_pattern),
    (splash_cymbal, splash_cymbal_pattern),
    (hihat_open, hihat_open_pattern)
]

eight_bars_time = np.linspace(0, 8 * 4, 128)  # 8 bars at 16 units per bar

for sound, pattern in patterns:
    for i, time_unit in enumerate(eight_bars_time):
        if pattern[i]:
            note = pretty_midi.Note(velocity=70, pitch=sound, start=time_unit, end=time_unit + 0.1)
            drum.notes.append(note)

# Add drum instrument to PrettyMIDI object
midi.instruments.append(drum)

# Write MIDI to disk
midi.write("loafy_drum_track.midi")
