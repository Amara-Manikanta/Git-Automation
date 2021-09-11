#!/usr/bin/env sh


echo "performing pull in main brach"
git pull


#"$(date "+%Y%d-%m-%Y")"
branch_name="${PWD##*/}$RANDOM"
echo" Present branch name : $branch_name \n"

git checkout -b $branch_name

echo -e "Checkout is done"

echo -e "Please press enter once files are added" 
read varname
echo -e" Checking the status of the files "

git status

echo -e " Adding the files to the branch "

git add .

echo -e " Please eneter commit statement "

read commit_statement

git commit -m $commit_statement

echo -e " Commit is done "

echo -e " Pushing  "

git push --set-upstream origin $branch_name
 

git push

echo -e "Please press enter once merge is done"
read varname1

git checkout main

echo -e "checkedout to main branch"
git branch

echo -e "Deleting the branch"

git branch -D $branch_name

echo -e " Everything is done "