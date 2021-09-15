import glob
import os
import shutil
import time
import random



def sleep_time():
    time.sleep(2)

def git_automation(repository_name,local_file_path,script_name,git_script_path):

    print('E:\\Github\\'+repository_name)
    os.chdir(r'E:\\Github\\'+repository_name)
    sleep_time()
    os.system('git checkout main')
    print("checkedout to main branch")
    sleep_time()
    os.system('git pull')
    sleep_time()
    print('pull completed for the main branch')
    print('copying the new file to repository')
    print(local_file_path)
    shutil.copy(local_file_path, git_script_path)
    sleep_time()
    print('creating new branch')
    branch_name = repository_name+'_'+script_name +'_'+str(random.randint(0,999999))
    os.system('git checkout -b '+str(branch_name))
    sleep_time()
    print('checking the status')
    os.system('git status')
    sleep_time()
    print('Adding the files to the branch')
    os.system('git add .')
    sleep_time()
    commit_statement=input('Please enter the commit statement:  ')
    os.system('git commit -m '+ commit_statement)
    sleep_time()
    os.system('git push --set-upstream origin '+str(branch_name))


    input('waiting')
    os.system('git checkout main')
    print("checkedout to main branch")
    sleep_time()
    os.system('git branch')
    sleep_time()
    print( "Deleting the branch")
    os.system('git branch -D '+str(branch_name))
    sleep_time()
    os.system('git branch')

    os.system('git pull')

    print(" Everything is done ")



def script_names_from_local_paths(files):
    script_names=[]
    for i in files:
        k = i.split('\\')
        script_names.append(k[-1])

    return script_names





git_files= glob.glob(r"E:\Github\*/*/*.py")
git_files1=glob.glob(r"E:\Github\*/*.py")
git_files.extend(git_files1)
git_files2=glob.glob(r"E:\Github\*/*.ipynb")
git_files.extend(git_files2)
git_files_without_path=script_names_from_local_paths(git_files)
l = len(git_files)
print(git_files)


local_files=glob.glob(r"E:\Manikanta\*/*.py")
local_files_without_path=script_names_from_local_paths(local_files)
print(local_files)
files_to_be_checked= []

for i in range(l):

    print(git_files_without_path[i])
    if git_files_without_path[i] in local_files_without_path:
        j = local_files_without_path.index(git_files_without_path[i])
        compare_output = os.system('FC '+git_files[i] +' '+local_files[j] )
        print(git_files_without_path[i], compare_output)

            #FC File1.txt File2.txt >NUL && Echo Same || Echo Different or error
            # -1 Invalid syntax(e.g.only one file passed)
            # 0 The files are identical.
            #1 The files are different.
            #2 Cannot find at least one of the files.

        if compare_output >= 1:
            repositorty_name = git_files[i].split('\\')
            time.sleep(5)
            print(repositorty_name)
            git_automation(repositorty_name[2],local_files[j],git_files_without_path[i],git_files[i])
            time.sleep(10)




