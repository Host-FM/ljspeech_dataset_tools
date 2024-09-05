import os
from pydub import AudioSegment, effects

def normalize_wavs(input_dir="converted_wavs", output_dir="normalized_wavs"):

    for file in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file)
        audio = AudioSegment.from_file(input_path)
        audio = audio.set_channels(1)
        audio = audio.set_sample_width(2)
        audio = audio.set_frame_rate(22050)
        normalized_audio = effects.normalize(audio)
        output_path = os.path.join(output_dir, file)
        normalized_audio.export(output_path)

    print(f"Normalization complete. Normalized wavs are in {output_dir} folder.")

normalize_wavs()
