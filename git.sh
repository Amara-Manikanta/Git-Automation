#!/usr/bin/env sh


echo "performing pull in main brach"
git pull

branch_name=$(date +"%m-%d-%Y")
echo"\n Present branch name : $branch_name \n"

git checkout -b $branch_name

echo -e "Checkout is done"
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

echo -e " Everything is done "