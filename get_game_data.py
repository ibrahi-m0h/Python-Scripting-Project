import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIRECTORY_PATTERN = "game"

def find_game_directories(source):
    game_paths = []
    for root, dirs, files in os.walk(source):
        

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and a target directory - only")
    
    source, target = args[1:]
    main(source, target)
    
    