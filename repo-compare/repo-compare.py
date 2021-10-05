from git import Repo
from deepdiff import DeepDiff
import difflib, filecmp

file_dict = {}
path1 = "<first-repo>"
path2 = "<second-repo>"

def compare(repo_path):
    repo = Repo(repo_path)
    repo_list = []
    repo_files = repo.git.ls_files().split("\n")
    for el in repo_files:
        path = "{}/{}".format(repo.working_dir, el)
        repo_list.append(path)
        file_dict[el.split("/")[-1]] = path
    return file_dict
        
path1_files = compare(path1)
path2_files = compare(path2)
same_files = set(path1_files.keys()) & set(path2_files.keys())
removed_files = set(path1_files.keys()) - set(path2_files.keys())

for i in same_file:
    path1_dict = dict1[i]
    path2_dict = dict2[i]
    with open(path1_dict) as f1:
        f1_text = f1.read()
    with open(path2_dict) as f2:
        f2_text = f2.read()
    ext = filecmp.cmp(path1_dict,path2_dict)
    if ext:
        print(path1_dict)
        pass

