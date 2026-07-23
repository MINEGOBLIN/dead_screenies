#!/usr/bin/python3

from pathlib import Path
from shutil import move
import argparse, re

"""
Python script that deletes unused screenshots (aka 'Dead Screenies') inside an obsidian vault
Only designed to work with vaults that have all their screenshots in a single folder
"""

# Make argparse for resources folder and vault to search
parser = argparse.ArgumentParser(
    description='Script to identify, remove and preserve unused screenshots (\'Dead Screenies\') from your obsidian vault',
    prog='dead_screenies.py')
parser.add_argument('-r', '--resources', required=True, help='Folder containing all of your screenshots')
parser.add_argument('-v', '--vault', required=True, help='Obsidian vault folder')
parser.add_argument('-f', '--folder', required=True, help='Folder to create with your dead screenies')
args = parser.parse_args()

# Generate wordlist from file names in resources directory
def resources_wordlist():
    resources_folder = Path(args.resources)
    print(f'Checking {resources_folder}')
    wordlist = []
    for item in resources_folder.iterdir():
        if item.is_file():
            wordlist.append(item.name)
    print('Screenshot wordlist generated')
    return wordlist

# Search obsidian .md files for file name in content
# Generate wordlist of .md files to inspect
def markdown_search():
    dead_files = []
    markdown_folder = Path(args.vault)
    markdown_files = list(markdown_folder.rglob('*.md'))
    print('Markdown wordlist generated')
    # Go through every .md file and check if filename appears in the text
    for word in resources_wordlist():
        print(f'Checking {word}')
        pattern = re.compile(str(word))
        word_found = False
        for file in markdown_files:
            with open(file, 'r', encoding='UTF-8') as markdown:
                if re.search(pattern, markdown.read()):
                    word_found = True
                    continue
        if not word_found:
            dead_files.append(Path(args.resources) / word)
    # Move dead files into separate folder
    print(f'All dead screenies have been identified, moving into separate folder')
    dead_files_folder = Path(args.folder)
    dead_files_folder.mkdir(exist_ok=True, parents=True)
    print(f'Moving dead screenies into {dead_files_folder}')
    for dead_file in dead_files:
        move(dead_file, dead_files_folder)

markdown_search()
