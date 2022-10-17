from genericpath import exists
from unittest.mock import patch
import pymongo
import os

  
from tkinter import messagebox  

#global variables
available_commit_id=""
current_commit_id=""

#Checking if git folder exists
# Specify path
git_folder_path = './.git'
#git refs folder
git_refs_path="/refs/heads/master"
# Check whether the specified
# path exists or not
is_Git_Folder_Exist = os.path.exists(git_folder_path)
if(not is_Git_Folder_Exist):
    messagebox.showinfo("Error","Not a git repository")
else:
    is_ref_folder_exists = os.path.isfile(git_folder_path+git_refs_path)
    if(not is_ref_folder_exists):
        messagebox.showinfo("Error","Could not find git references file in the specified")

    else:
        with open(git_folder_path+git_refs_path) as ref:
            #Reading commit id
            available_commit_id=ref.readline()

#check if the current_commit_id is in the project folder
#This will never be pushed to server
current_commit_id_file_path="./current_red_id"
is_current_commit_id_file_exists=os.path.isfile(current_commit_id_file_path)
if(not is_current_commit_id_file_exists and is_Git_Folder_Exist):
    with open(current_commit_id_file_path,'w') as file:
        file.writelines(available_commit_id)
        print("File created")


