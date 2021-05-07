import os
import os.path


def getDirList(curr_path):
    file_names = os.listdir(curr_path)
    dir = []
    file = []
    for name in file_names:
        if os.path.isdir(name):
            dir.append(name)
        else:
            file.append(name)
    return {"dir":dir, "file":file}


path = './'
result = getDirList(path)
print(result)
