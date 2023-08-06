from lztools.git import load_file, save_file, list_files

class GitRepo(object):
    path = None

    def __init__(self, path:str):
        self.path = path

    def load_file(self, path):
        load_file(self.path, path)

    def save_file(self, path):
        save_file(self.path, path)

    def list_files(self):
        return list_files()
