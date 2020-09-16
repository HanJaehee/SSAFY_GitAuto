import requests as req
import json
import os
import time
import subprocess as sp


class gitAuto:
    def __init__(self, _private_token, _user_name, _prof_id, _work_space):
        self.private_token = _private_token
        self.user_name = _user_name
        # self.prof_name = _prof_name # chk
        self.work_space = _work_space
        #self.repo_name = 'hw_' + time.strftime('%y%m%d', time.localtime(time.time()))
        self.repo_name = 'hw010'
        self.prof_id = '487'

    def chkRepo(self):
        return os.path.isdir(self.work_space + self.repo_name)

    def makeDir(self):
        print("[*] Start to make " + self.repo_name)
        os.chdir(self.work_space)
        os.system('mkdir ' + self.repo_name)
        print("[+] Success")

    def makeProject(self):
        try:
            print("[*] Start to make the Local Repository")
            os.chdir(self.work_space + self.repo_name)
            init_out = sp.check_output(['git init'], shell=True, encoding='utf-8')
            print("[+] Success")
            print("[*] Start to make README && add all files && commit ")
            touch_out = sp.check_output(
                ['touch README'], shell=True, encoding='utf-8')
            add_out = sp.check_output(['git add .'], shell=True, encoding='utf-8')
            commit_out = sp.check_output(
                ['git commit -m \'created by GitAuto\''], shell=True, encoding='utf-8')
            print("[+] Success")
            
            print("[*] Start to push https://lab.ssafy.com/" + self.user_name + '/' + self.repo_name + '.git')
            push_msg = 'git push --set-upstream https://lab.ssafy.com/' + \
                self.user_name + '/' + self.repo_name + '.git master'
            push_out = sp.check_output([push_msg], shell=True, encoding='utf-8')
            print("[+] Success")
        except Exception as e:
            print("[-] Error in makeProject")
            print("ErrorMsg : ", e)

    def makeMember(self):
        try:
            member_add = 'curl --request POST --header "PRIVATE-TOKEN: ' + self.private_token
            member_add += '" --data "user_id=' + self.prof_id + '&access_level=30" "https://lab.ssafy.com/api/v4/projects/'
            member_add += self.user_name + '%2F' + self.repo_name + '/members"'

            print("------------------------------------------------")
            print("[*] Start to add " + self.prof_id + " in members")
            out = sp.check_output([member_add], shell=True, encoding='utf-8')
            result = json.loads(out)
            if 'message' in list(result.keys()):
                print("[*] " + result['message'])
            else:
                print("[+] Success to add " + self.prof_id + " in members")
            # print(type(result))
            # print(type(out))
        except Exception as e:
            print("[-] Error in makeMember()")
            print("ErrorMsg : ", e)

    def chkMember(self):
        try:
            member_chk = 'curl --request GET --header "PRIVATE-TOKEN: ' + self.private_token
            member_chk += '" \'https://lab.ssafy.com/api/v4/projects/' + self.user_name + '%2F' + self.repo_name +'/members\''
            out = sp.check_output([member_chk], shell=True, encoding='utf-8')
            result = json.loads(out)

            print("\n------------ All members ---------------")
            for idx, dic in enumerate(result):
                print(str(idx+1) + ". " + "id : " + str(dic['id']) +  " username : " + dic['username'] + " access_level : " + str(dic['access_level']))
            print("\n* Access Level *\n Maintainer = 40\nDeveloper = 30\n")
            print("[+] The End")
            # print(result[0]['id'])
            # print(result[1]['id'])
        except Exception as e:
            print("[-] Error in chkMember()")
            print("ErrorMsg : ", e)

mgr = gitAuto('m522bRJaYpBv_BXiUGZ3', 'gkswogml23', 'ssafy7', '/Users/hindsight/ssafy/work_java/')
#mgr = gitAuto('m522bRJaYpBv_BXiUGZ3', 'gkswogml23', 'ssafy7', '/Users/hindsight/git/')

if not mgr.chkRepo():
    mgr.makeDir()

mgr.makeProject()
mgr.makeMember()
mgr.chkMember()
