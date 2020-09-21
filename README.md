<h1 align="center">✌️SSAFY GitAuto✌️</h1>

<h2 align="center">SSAFY 과제 제출용 GitLab Repository 자동생성기</h2>


<h4 align="center">OS 지원 : Windows , Mac, Linux</h4>
<h4 align="center">❗Python 3.x 버전 필요 !❗</h4>

Usage
---
 <h3>👋 pip3 install requests || pip install requests ( Python 버전 체크하시고 명령어 입력하세요! )
 <br>
 <h3>👏 필수 !! Private Key 생성<br></h3>
 <ol style="list-style-type : decimal;">
 <li> lab.ssafy.com 에 로그인 한 후 우측 상단의 '설정' 또는 'Setting' 접속</li>
  <img width="276" alt="우측상단 설정접속" src="https://user-images.githubusercontent.com/38396374/93663795-49078980-faa5-11ea-893a-767a630af14f.png"><br>
 <li> 액세스 토큰 탭에서 이름과 기한, 그리고 'api' 체크 후 personal access token 생성 ( 🚫 공유하지 마세요 ! 🚫 )</li>
  <img width="1003" alt="액세스토큰접속" src="https://user-images.githubusercontent.com/38396374/93663792-45740280-faa5-11ea-80f1-fc903fb48eb5.png"><br>
 <li> 액세스 토큰 획득 한 것을 GitAuto 내 private_key에 넣기</li>
  <img width="1051" alt="액세스토큰획득" src="https://user-images.githubusercontent.com/38396374/93663794-486ef300-faa5-11ea-8680-6697ff124e12.png"><br>
 <li> 이제 하단의 설명 잘 읽어보시고 원하는 방법으로 자동화하기! </li>
</ol>
 
 
 <br><br>
 두 가지의 사용법이 존재해요.<br>
 👆 Eclipse Work Space에 git 생성하는 방식 ( eclipse에서 권장하진 않음 but 편하고 파일이 깔끔하게 올라감 )<br>
 ✌ git 폴더에 git 생성하는 방식 ( eclipse에서 권장하는 방식 but 파일이 이중화되어 올라가고, 첫번째에 비교해서 여러번의 클릭 ( 아마 기존에 많이 사용하시던 방법일거에요 ! )<br>
 
 먼저,<br>
 👆 Eclipse Work Space에 깃 init 하고 생성하는 방식 ( eclipse에서 권장하진 않음 but 편하고 파일이 깔끔하게 올라감 )<br>
 work_path = "eclipse work space" ex) C:\\ssafy\\work_java   ||  /users/kimssafy/ssafy/work_java
<ol style="list-style-type : decimal;">
  <li>이클립스 숙제 프로젝트 생성하고 숙제 완성</li>
  <img width="594" alt="createProject" src="https://user-images.githubusercontent.com/38396374/93661491-2e2c1980-fa93-11ea-9f65-30b475ceea45.png">
  <li>GitAuto 실행, 이후 수정사항 없다면 끝! ( gitlab에 프로젝트 생성 및 프로젝트 Push, 멤버 추가 까지 완료된 상태)
  <img width="578" alt="niceGitAuto" src="https://user-images.githubusercontent.com/38396374/93661493-31bfa080-fa93-11ea-9f04-790db91b7bd2.png">
  <li>이후 수정사항이 생겼다면, 이클립스에서 add existing local respository 클릭, 서칭 경로를 work_java로 바꿔준다.
  <img width="273" alt="addLocal" src="https://user-images.githubusercontent.com/38396374/93661499-35532780-fa93-11ea-8592-a80648540290.png"><br>
  <img width="592" alt="로컬레포지토리에추가하는것" src="https://user-images.githubusercontent.com/38396374/93661494-32f0cd80-fa93-11ea-8bdb-a41a993b65da.png">
  <img width="435" alt="추가된gitRepo" src="https://user-images.githubusercontent.com/38396374/93661495-33896400-fa93-11ea-9e40-7bc8f1ccc037.png"><br>
  <img width="284" alt="따로연결안해도자동으로잡혀있음" src="https://user-images.githubusercontent.com/38396374/93661496-3421fa80-fa93-11ea-8627-3e1c4671af1e.png"><br>
  <img width="591" alt="자동으로gitStaging에잡히는모습" src="https://user-images.githubusercontent.com/38396374/93661497-34ba9100-fa93-11ea-9e5d-791ab9fef1df.png">

</ol>
<br><br>
이제 두번째 ! <br>
✌ git 폴더에 git 생성하는 방식 ( eclipse에서 권장하는 방식 but 파일이 이중화되어 올라가고, 첫번째에 비교해서 여러번의 클릭 ( 아마 기존에 많이 사용하시던 방법일거에요 ! )<br>
work_path = "git path" ex) C:\\Users\\KimSSAFY\\git || /users/kimssafy/git
<ol style="list-style-type : decimal;">
 <li>이클립스 프로젝트 생성 및 숙제 완성</li>
 <img width="594" alt="createProject" src="https://user-images.githubusercontent.com/38396374/93661491-2e2c1980-fa93-11ea-9f65-30b475ceea45.png"><br/>
 <li>GitAuto 실행, ( gitlab 프로젝트에 생성, 멤버 추가까지 완료된 상태 )</li>
 <img width="580" alt="success git" src="https://user-images.githubusercontent.com/38396374/93664294-a51fdd00-faa8-11ea-9253-008dcc39bb55.png">
 <li>git repository 탭에서 git 추가 </li>
 <img width="596" alt="addgit" src="https://user-images.githubusercontent.com/38396374/93664296-a8b36400-faa8-11ea-9aa3-43edae7b66de.png">
 <li>이클립스 프로젝트에서 우클릭 -> Team 탭 -> Share Project... 선택한 후 git repository 선택</li>
 <img width="514" alt="selectTeam" src="https://user-images.githubusercontent.com/38396374/93664297-a94bfa80-faa8-11ea-838a-f3f4ea7cb7b6.png">
 <img width="760" alt="selectgitrepo" src="https://user-images.githubusercontent.com/38396374/93664298-ab15be00-faa8-11ea-9165-9e9ffa6923bb.png">
 <li>git Staging 탭에서 연동된 것 확인 가능 ! 이제 커밋, 푸시 하시면 됩니다! 끝!</li>
 <img width="927" alt="addandpush" src="https://user-images.githubusercontent.com/38396374/93664300-abae5480-faa8-11ea-8c3d-c2baeafb00ea.png">
</ol>
<br><br>




windows issue

install requests administrator

Git Credential Manager for Windows 에 lab.ssafy.com에 대한 계정 정보 입력 시
영어 입력했을 때, 한글로 바뀔 경우
외부 에디터 또는 브라우저 주소창에 영어입력후 복사 + 붙여넣기


위의 Manager에서 lab.ssafy.com 계정 실수 입력시
win + R 누른 후 rundll32.exe keymgr.dll,KRShowKeyMgr 입력,
그리고 lab.ssafy.com 삭제 후 재시도
