import os
from git import Repo
local_repo_directory = os.path.join(os.getcwd())

def clone_repo():
    Repo.clone_from("https://github.com/JuanCorvus/PruevaCorvus-.git",local_repo_directory)

def chdirectory(path):
    os.chdir(path)
def update_file():
    chdirectory(local_repo_directory)


def main():
    update_file()

if __name__=="__main__":
    main()


