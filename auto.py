import os
import time

"""
************************** PLEASE README ******************************
usage
repo_name : don't touch
private_token : input your private_token
user_name : input your user_name
work_space = input your local git repository path
"""

#repo_name = 'hw_' + time.strftime('%y%m%d', time.localtime(time.time()))
repo_name = 'hw_200915'
private_token = 'm522bRJaYpBv_BXiUGZ3'
user_name = 'gkswogml23'
work_space = '/Users/hindsight/git/'

print(repo_name)
os.chdir(work_space)
os.system('mkdir ' + repo_name)
os.chdir('./'+ repo_name)
os.system('git init')
os.system('touch README')
os.system('git add .')
os.system('git commit -m \'created by gitlab-auto HJH\'')
os.system('git push --set-upstream https://lab.ssafy.com/gkswogml23/' + repo_name + '.git master')

member_add = 'curl --request POST --header "PRIVATE-TOKEN: ' + private_token + '" --data "user_id=487&access_level=30" "https://lab.ssafy.com/api/v4/projects/' + user_name + '%2F' + repo_name + '/members"'
os.system(member_add)
member_chk = 'curl --request GET --header "PRIVATE-TOKEN: ' + private_token + '" \'https://lab.ssafy.com/api/v4/projects/' + user_name + '%2F' + repo_name +'/members\''
os.system(member_chk)


