#!/bin/bash
git status
git add *
git commit -m "Upload new files"
git push origin master
echo 'Successfull!'
