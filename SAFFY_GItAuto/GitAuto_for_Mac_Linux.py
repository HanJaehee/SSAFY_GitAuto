#-*- coding: utf-8 -*-
import requests as req
import json
import os
import time
import subprocess as sp

private_key = "m522bRJaYpBv_BXiUGZ3"
user_name = "gkswogml23" # lab.ssafy.com/KimSSAFY/hw_200918 => KIMSSAFY 
prof_name = 'ssafy7'
work_path = '/Users/hindsight/ssafy/work_java' # your workspace or git path

# mgr = gitAuto('private_key', 'gkswogml23', 'ssafy7', 'C:\\ssafy\\work_java')
"""
워크 스페이스에 깃 init하고 생성하는 방식 ( 이클립스에서 권장하지 않는 방식, 하지만 편하고 파일이 깔끔하게 올라감 )
1. 이클립스 숙제 프로젝트 생성하고 숙제 완성
2. gitAuto 실행 => gitlab에 프로젝트 생성 및 푸시, 멤버추가 까지 완료된 상태
3. 이후 수정사항이 있다면, 이클립스에서 add existing local repository 누르고, 서칭 경로를 work_java로 바꿔주고 깃 추가 후 자유롭게 커밋 푸시
"""
# mgr = gitAuto('private_key', 'gkswogml23', 'ssafy7', 'C:\\users\\user\\git')
"""
워크스페이스와 분리된 git 폴더에서 init 후 생성 하는 방식( 이클립스에서 권장하는 방식, 다소 불편한 부분들이 있고 파일이 중복된다 )
1. 이클립스 숙제 프로젝트 생성
2. 파일 실행
3. add existing local respository에서 서칭 경로를 git 폴더로(아마 디폴트 일거에요)
4. 이후 자유롭게 커밋 푸시
"""

class gitAuto:
    def __init__(self, _private_token, _user_name, _prof_id, _work_space):
        self.private_token = _private_token
        self.user_name = _user_name
        # self.prof_name = _prof_name # chk
        self.work_space = _work_space
        self.repo_name = 'hw_' + time.strftime('%y%m%d', time.localtime(time.time()))
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


mgr = gitAuto(private_key, user_name, prof_name, work_path)

if not mgr.chkRepo():
    mgr.makeDir()

mgr.makeProject()
mgr.makeMember()
mgr.chkMember()