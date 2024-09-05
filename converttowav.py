import os
from pydub import AudioSegment

def convert_to_wav(input_dir="put_audio_files_here", output_dir = "converted_wavs"):

    index = 1

    for file in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file)
        audio = AudioSegment.from_file(input_path)
        ouput_path = os.path.join(output_dir, str(index) + ".wav")
        audio.export(ouput_path, format="wav")

        index += 1
    
    print(f"{index - 1} files have been converted to wav.")

convert_to_wav()
