<h1 align="center">✌️SSAFY GitAuto✌️</h1>

<h2 align="center">SSAFY 과제 제출용 GitLab Repository 자동생성기</h2>


<h4 align="center">OS 지원 : Windows , Mac, Linux</h4>

Usage
---

 * Eclipse Work Space에 깃 init 하고 생성하는 방식 ( eclipse에서 권장하진 않음 but 편하고 파일이 깔끔하게 올라감 )<br>
 work_path = "eclipse work space" ex) C:\\ssafy\\work_java   ||  /users/kimssafy/ssafy/work_java
<ol style="list-style-type : decimal;">
  <li>이클립스 숙제 프로젝트 생성하고 숙제 완성</li>
  <img width="594" alt="createProject" src="https://user-images.githubusercontent.com/38396374/93661491-2e2c1980-fa93-11ea-9f65-30b475ceea45.png">
  <li>GitAuto 실행, 이후 수정사항 없다면 끝! ( gitlab에 프로젝트 생성 및 푸시, 멤버 추가 까지 완료된 상태)
  <img width="578" alt="niceGitAuto" src="https://user-images.githubusercontent.com/38396374/93661493-31bfa080-fa93-11ea-9f04-790db91b7bd2.png">
  <li>이후 수정사항이 생겼다면, 이클립스에서 add existing local respository 클릭, 서칭 경로를 work_java로 바꿔준다.
  <img width="273" alt="addLocal" src="https://user-images.githubusercontent.com/38396374/93661499-35532780-fa93-11ea-8592-a80648540290.png"><br>
  <img width="592" alt="로컬레포지토리에추가하는것" src="https://user-images.githubusercontent.com/38396374/93661494-32f0cd80-fa93-11ea-8bdb-a41a993b65da.png">
  <img width="435" alt="추가된gitRepo" src="https://user-images.githubusercontent.com/38396374/93661495-33896400-fa93-11ea-9e40-7bc8f1ccc037.png"><br>
  <img width="284" alt="따로연결안해도자동으로잡혀있음" src="https://user-images.githubusercontent.com/38396374/93661496-3421fa80-fa93-11ea-8627-3e1c4671af1e.png"><br>
  <img width="591" alt="자동으로gitStaging에잡히는모습" src="https://user-images.githubusercontent.com/38396374/93661497-34ba9100-fa93-11ea-9e5d-791ab9fef1df.png">

</ol>


windows issue

install requests administrator

Git Credential Manager for Windows 에 lab.ssafy.com에 대한 계정 정보 입력 시
영어 입력했을 때, 한글로 바뀔 경우
외부 에디터 또는 브라우저 주소창에 영어입력후 복사 + 붙여넣기


위의 Manager에서 lab.ssafy.com 계정 실수 입력시
win + R 누른 후 rundll32.exe keymgr.dll,KRShowKeyMgr 입력,
그리고 lab.ssafy.com 삭제 후 재시도
