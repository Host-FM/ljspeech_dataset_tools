import csv
import random
import os

def make_dataset():
    """This fuction creates a dataset with 80% training and 20% validation ratio."""
    with open('metadata.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        train = []
        val = []
        for line in data:
            if random.random() < 0.2:
                val.append(line[0].replace('./wavs/', ''))
            else:
                train.append(line[0].replace('./wavs/', ''))
        with open('trainfiles.txt', 'w') as f:
            for line in train:
                f.write(line + '\n')
        with open('valfiles.txt', 'w') as f:
            for line in val:
                f.write(line + '\n')

    dataset = os.mkdir("dataset")
    wav_dir = os.mkdir("dataset/wavs")
    for file in os.listdir("trimmed_wavs"):
        abs_path = os.path.join("trimmed_wavs", file)
        input_path = os.path.join("dataset/wavs", file)
        os.rename(abs_path, input_path)

    os.rename("trainfiles.txt", "dataset/trainfiles.txt")
    os.rename("valfiles.txt", "dataset/valfiles.txt")

if __name__ == "__main__":
    make_dataset()
    print('done')