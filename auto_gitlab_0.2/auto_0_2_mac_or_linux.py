import os
import time

"""
************************** PLEASE README ******************************

Auto GitLab ver 0.1 for Mac or Linux

Usage

private_token : Input your private_token
user_name : Input your user_name
work_space = input your local git repository path

"""

repo_name = 'hw_' + time.strftime('%y%m%d', time.localtime(time.time()))

private_token = 'Private Token' # Input your Private Token
user_name = 'username' # Input your Username ex) lab.ssafy.com/kimssafy <-- kimssafy
work_space = 'your workspace path' # ex) '/Users/kimssafy/ssafy/work_java'
print(repo_name)

# init repository and commit
os.chdir(work_space)
os.system('mkdir ' + repo_name)
os.chdir('./'+ repo_name)
os.system('git init')
os.system('touch README')
os.system('git add .')
os.system('git commit -m \'created by gitlab-auto HJH\'')

# git push
git_push = 'git push --set-upstream https://lab.ssafy.com/' + user_name + '/' + repo_name + '.git master'
os.system(git_push)

# add Member ssafy7
member_add = 'curl --request POST --header "PRIVATE-TOKEN: ' + private_token + '" --data "user_id=487&access_level=30" "https://lab.ssafy.com/api/v4/projects/' + user_name + '%2F' + repo_name + '/members"'
os.system(member_add)

# check Members. If you can check ssafy7 in lines, good
member_chk = 'curl --request GET --header "PRIVATE-TOKEN: ' + private_token + '" \'https://lab.ssafy.com/api/v4/projects/' + user_name + '%2F' + repo_name +'/members\''
os.system(member_chk)


