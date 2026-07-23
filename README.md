- Obsidian vault must have all screenshots inside a single folder
1. Generate wordlist of all screenshot file names
2. Search every single .md file for file name in text
3. If no match, move screenshot to the specified folder

```
python3 .\dead_screenies.py -h
usage: dead_screenies.py [-h] -r RESOURCES -v VAULT -f FOLDER
Script to identify, remove and preserve unused screenshots ('Dead Screenies') from your obsidian vault
options:
  -h, --help                show this help message and exit
  -r, --resources RESOURCES Folder containing all of your screenshots
  -v, --vault VAULT         Obsidian vault folder
  -f, --folder FOLDER       Folder to create with your dead screenies
  ```
