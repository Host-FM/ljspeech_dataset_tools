import os
import whisper

def transcribe(language="English", input_dir="trimmed_wavs"):

    model = whisper.load_model("models/base.en.pt")
    metadata = []

    for file in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file)
        #transcription = ""
        transcription = model.transcribe(input_path, language=language)
        transcription = transcription["text"]
        print(f"{file} | {transcription}")
        metadata.append(f"{file} |{transcription}")

    metadata_txt = '\n'.join(metadata)

    with open("metadata.csv", "w") as text_file:
        text_file.write(metadata_txt)

    print(f"Wavs have been transcribed. Transcription has been saved in {text_file.name}.")
        

transcribe()
