import os

def make_dataset():
    dataset = os.mkdir("dataset")
    wav_dir = os.mkdir("dataset/wavs")
    for file in os.listdir("trimmed_wavs"):
        abs_path = os.path.join("trimmed_wavs", file)
        input_path = os.path.join("dataset/wavs", file)
        os.rename(abs_path, input_path)

    os.rename("metadata.csv", "dataset/metadata.csv")


make_dataset()
print('Dataset has been created.')