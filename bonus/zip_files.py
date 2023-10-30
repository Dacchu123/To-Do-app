import zipfile
import pathlib


def zip_file(filepath, direction):
    dir_name = pathlib.Path(direction, "output.zip")
    with zipfile.ZipFile(dir_name, 'w') as files:
        for filepaths in filepath:
            filepaths = pathlib.Path(filepaths)
            files.write(filepaths, arcname=filepaths.name)


if __name__ == "__main__":
    zip_file(filepath=["content.py", "dictionary.py"], direction="files")
