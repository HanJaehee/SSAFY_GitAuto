#-*- coding: utf-8 -*-
import json
import sys
import os
import time
import subprocess as sp
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QFileDialog, QLabel)


# mgr = gitAuto('privateKey', 'username', 'ssafy7', 'C:\\ssafy\\work_java')
"""
워크 스페이스에 깃 init하고 생성하는 방식 ( 이클립스에서 권장하지 않는 방식, 하지만 편하고 파일이 깔끔하게 올라감 )
1. 이클립스 숙제 프로젝트 생성하고 숙제 완성
2. gitAuto 실행 => gitlab에 프로젝트 생성 및 푸시, 멤버추가 까지 완료된 상태
3. 이후 수정사항이 있다면, 이클립스에서 add existing local repository 누르고, 서칭 경로를 work_java로 바꿔주고 깃 추가 후 자유롭게 커밋 푸시
"""
# mgr = gitAuto('privateKey', 'username', 'ssafy7', 'C:\\users\\gkswo\\git')
"""
워크스페이스와 분리된 git 폴더에서 init 후 생성 하는 방식( 이클립스에서 권장하는 방식, 다소 불편한 부분들이 있고 파일이 중복된다 )
1. 이클립스 숙제 프로젝트 생성
2. 파일 실행
3. add existing local respository에서 서칭 경로를 git 폴더로(아마 디폴트 일거에요)
4. 이후 자유롭게 커밋 푸시
"""

origin_path = os.path.dirname(os.path.realpath(__file__))

class gitAuto:
    def __init__(self, _private_token, _user_name, _repo_name, _prof_id, _work_space):
        self.private_token = _private_token
        self.user_name = _user_name
        # self.prof_name = _prof_name # chk
        self.work_space = _work_space
        self.repo_name = _repo_name
        #self.repo_name = 'hw31'
        self.prof_id = '487'

    def chkRepo(self):
        return os.path.isdir(self.work_space + self.repo_name)

    def makeDir(self):
        print("[*] Start to make " + self.repo_name)
        os.chdir(self.work_space)
        os.system('mkdir ' + self.repo_name)
        print("[+] Success")

    def makeProject(self):
        #try:
        #git init
        print("[*] Start to make the Local Repository")
        os.chdir(self.work_space + '\\' + self.repo_name)
        init_out = sp.check_output('git init', shell=True)
        print("[+] Success")

        #create README and commit
        print("[*] Start to make README && add all files && commit ")
        touch_out = sp.check_output(
            'type NUL > README.md', shell=True, encoding='utf-8')
        add_out = sp.check_output('git add .', shell=True, encoding='utf-8')
        try:
            commit_out = sp.check_output('git commit -m \"create by GitAuto\"', shell=True, encoding='utf-8')
        except Exception as e:
            print(e)
        print("[+] Success")
        
        #push 
        print("[*] Start to push https://lab.ssafy.com/" + self.user_name + "/" + self.repo_name + '.git')
        push_msg = 'git push --set-upstream https://lab.ssafy.com/' + \
            self.user_name + '/' + self.repo_name + '.git master'
        push_out = sp.check_output(push_msg, shell=True, encoding='utf-8')
        print("[+] Success")

        return True
        #except Exception as e:
        #    print("[-] Error in makeProject")
        #    print("ErrorMsg : ", e)
         #   return False

    def makeMember(self):
        try:
            member_add = 'curl --request POST --header "PRIVATE-TOKEN: ' + self.private_token
            member_add += '" --data "user_id=' + self.prof_id + '&access_level=30" "https://lab.ssafy.com/api/v4/projects/'
            member_add += self.user_name + '%2F' + self.repo_name + '/members"'

            print("------------------------------------------------")
            print("[*] Start to add " + self.prof_id + " in members")
            out = sp.check_output(member_add, shell=True, encoding='utf-8')
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
            member_chk += '" ' + 'https://lab.ssafy.com/api/v4/projects/' + self.user_name + '%2F' + self.repo_name +'/members'
            print(member_chk)
            out = sp.check_output(member_chk, shell=True, encoding='utf-8')
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


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        try:
            a = open('info.txt', 'r')
        except Exception as e:
            os.system('fsutil file createnew info.txt 0')
            a = open('info.txt', 'r')
        a = a.read()
        data = a.split('\n')
        self.initUI(data)

    def initUI(self, data):
        if data[0]:
            api_keys, userid, profid, file_path = data
        else:
            api_keys = None
            userid = None
            profid = None
            file_path = None

        self.ulbl = QLabel('GITLAB ID', self)
        self.ulbl.move(20, 40)
        self.userid = QLineEdit(self)
        self.userid.move(110, 35)
        self.userid.resize(170, 20)
        if userid:
            self.userid.setText(userid)

        self.plbl = QLabel('PROF ID', self)
        self.plbl.move(20, 75)
        self.profid = QLineEdit(self)
        self.profid.move(110, 70)
        self.profid.resize(170, 20)
        if profid:
            self.profid.setText(profid)

        self.rlbl = QLabel('REPOSITORY', self)
        self.rlbl.move(20, 110)
        self.repo_name = QLineEdit(self)
        self.repo_name.move(110, 105)
        self.repo_name.resize(170, 20)
        self.repo_name.setText('hw_' + time.strftime('%y%m%d', time.localtime(time.time())))

        self.api_lbl = QLabel('API KEYS', self)
        self.api_lbl.move(20, 145)
        self.api_keys = QLineEdit(self)
        self.api_keys.move(110, 140)
        self.api_keys.resize(170, 20)
        if api_keys:
            self.api_keys.setText(api_keys)

        self.dir_lbl = QLabel('FILE PATH', self)
        self.dir_lbl.move(20, 180)
        self.dir_location = QLineEdit(self)
        self.dir_location.move(20, 210)
        self.dir_location.resize(260, 20)
        self.dir_location.setEnabled(False)
        self.dir_btn = QPushButton('경로 설정', self)
        self.dir_btn.move(110, 175)
        self.dir_btn.clicked.connect(self.setFilePath)
        if file_path:
            self.dir_location.setText(file_path)

        self.repo_btn = QPushButton('레포지토리 생성 밎 GIT AUTO PUSH', self)
        self.repo_btn.move(50, 240)
        self.repo_btn.clicked.connect(self.execFile)

        self.lbl = QLabel('AUTOGIT_SSAFY_한재희_박종한', self)
        self.lbl.move(60, 280)

        self.setWindowTitle('AUTOGIT_SSAFY')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def execFile(self):
        print(self.userid.text())
        try:
            mgr = gitAuto(self.api_keys.text(), self.userid.text(), self.repo_name.text(), self.profid.text(), self.dir_location.text())
            if not mgr.chkRepo():
                mgr.makeDir()
            mgr.makeProject()
            mgr.makeMember()
            mgr.chkMember()
            os.chdir(origin_path)
            print(origin_path)
            a = open('info.txt', 'w+')
            a.write(self.api_keys.text()+'\n'+self.userid.text()+'\n'+self.profid.text()+'\n'+self.dir_location.text())
            print(self.api_keys.text()+'\n'+self.userid.text()+'\n'+self.profid.text()+'\n'+self.dir_location.text())
            print("[+] success in writeFile")
            print("유저 아이디, 교수 아이디, API 키, 마지막으로 경로가 info.txt파일에 저장되었습니다.")
            print("info.txt를 지우지 않으면 계속 같은 정보를 사용할 수 있습니다. 삭제시 정보가 초기화 됩니다")
            print("git clone 혹은 push가 완료되었습니다. 프로그램을 종료하셔도 됩니다.")
            a.close()
        except Exception as e:
            print("[-] Error in execFile()")
            print("ErrorMsg : ", e)

    def setFilePath(self, loc):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            dirName = dialog.selectedFiles()
            self.dir_location.setText(dirName[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
