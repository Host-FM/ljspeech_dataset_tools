import os
from pydub import AudioSegment, silence

def trim_silence(input_dir="normalized_wavs", output_dir="trimmed_wavs"):

    for file in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file)
        audio = AudioSegment.from_file(input_path)

        silence_threshold = audio.dBFS - 14  # Adjust this value as needed
        min_silence_len = 500  # Minimum length of silence in milliseconds
        silence_segments = silence.detect_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_threshold)

        non_silent_audio = AudioSegment.empty()
        previous_end = 0
        for start, end in silence_segments:
            non_silent_audio += audio[previous_end:start]
            previous_end = end

        non_silent_audio += audio[previous_end:]

        output_path = os.path.join(output_dir, file)
        non_silent_audio.export(output_path)

    print(f"Silence has been removed from wavs. Trimmed wavs are in {output_dir} folder")

trim_silence()
