import zipfile


def extract(arcpath, destpath):
    with zipfile.ZipFile(arcpath, 'r') as zip_file:
        zip_file.extractall(destpath)


