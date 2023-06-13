from pydub import AudioSegment

# Load the audio files (assumes you have .wav files of wind and bird sounds)
wind = AudioSegment.from_wav("wind.wav")
birds = AudioSegment.from_wav("birds.wav")

# Lower the volume of the bird sounds
birds = birds - 10

# Overlay the sounds
combined = wind.overlay(birds)

# Export the result
combined.export("prairie.wav", format='wav')
