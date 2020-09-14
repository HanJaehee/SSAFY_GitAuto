import os


path = os.getcwd()
repo_name = 'hw_testet'
os.system('mkdir ' + repo_name)
os.system('cd ' + repo_name)
os.system('git init')
os.system('touch README')
os.system('git add .')
os.system('git commit -m \'created by gitlab-auto\'')
os.system('git push --set-upstream https://lab.ssafy.com/gkswogml23/' + repo_name + '.git master')

member_add = 'curl --request POST --header "PRIVATE-TOKEN: m522bRJaYpBv_BXiUGZ3" --data "user_id=487&access_level=30" "https://lab.ssafy.com/api/v4/projects/gkswogml23%2F' + repo_name + '/members"'
os.system(member_add)
member_chk = 'curl --request GET --header "PRIVATE-TOKEN: m522bRJaYpBv_BXiUGZ3" \'https://lab.ssafy.com/api/v4/projects/gkswogml23%2F\'' + repo_name +'/members\''
result = os.system(member_chk)
print(result)


