import os
import shutil

root_folder = lambda:"./.tests"

def init_folder():
    if os.path.exists(root_folder()):
        remove_folder()
        
    os.makedirs(root_folder())

def remove_folder():
    shutil.rmtree(root_folder())
    
def create_folder(folder_name, parent_folder = None):
    def create(folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return folder_path

    return create(os.path.join(parent_folder or root_folder(), folder_name))
                
def create_file(file_name, parent_folder, content):
    with open(os.path.join(parent_folder, file_name), 'w') as fileobj:
        fileobj.write(content)

def do_nothing():
    pass
