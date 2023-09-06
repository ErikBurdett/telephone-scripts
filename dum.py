import pretty_midi
import numpy as np

# Initialize PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=89)

# Define drum program and create instrument
drum_program = pretty_midi.instrument_name_to_program('Synth Drum')
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

# Define more intricate patterns for a 4-bar loop
kick_pattern = [1, 0, 0, 0, 1, 0, 0, 1] * 8
snare_pattern = [0, 0, 0, 0, 0, 0, 1, 0] * 8
hihat_closed_pattern = [1, 1, 1, 1, 1, 1, 1, 1] * 8
clap_pattern = [0, 0, 0, 0, 0, 0, 1, 0] * 8
rimshot_pattern = [0, 0, 0, 1, 0, 0, 0, 0] * 8
tambourine_pattern = [0, 1, 0, 0, 0, 1, 0, 0] * 8

# Generate MIDI notes based on patterns
patterns = [
    (kick, kick_pattern),
    (snare, snare_pattern),
    (hihat_closed, hihat_closed_pattern),
    (clap, clap_pattern),
    (rimshot, rimshot_pattern),
    (tambourine, tambourine_pattern)
]

four_bars_time = np.linspace(0, 4 * 4, 64)  # 4 bars at 16 units per bar

for sound, pattern in patterns:
    for i, time_unit in enumerate(four_bars_time):
        if pattern[i]:
            note = pretty_midi.Note(velocity=100, pitch=sound, start=time_unit, end=time_unit + 0.1)
            drum.notes.append(note)

# Add drum instrument to PrettyMIDI object
midi.instruments.append(drum)

# Write MIDI to disk
midi.write("uhuh.midi")
