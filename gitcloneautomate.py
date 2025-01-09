import os
import sys
import json

# file_name = 'gitdata.json'
if len(sys.argv) < 2:
    print("Usage: pass the json file as an input in arg1")
    sys.exit()

file_name = sys.argv[1]


def file_processing():
    with open(file_name, 'r') as file:
        str_data = file.read()
    return json.loads(str_data)


file_processing_fun = file_processing()
clone_dir = file_processing_fun.get('gitinfo').get('clone_directory')
repo_list = file_processing_fun.get('gitinfo').get('repo_list')
username = file_processing_fun.get('gitinfo').get('username')

try:
    os.mkdir(clone_dir)
except Exception as WinError:
    print(f"The Directory is already present")

if clone_dir:
    for repo in repo_list:
        os.system(
            f'git clone https://github.com/{username}/{repo}.git {clone_dir}/{repo}')
