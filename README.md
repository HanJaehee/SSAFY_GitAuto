<h1 align="center">✌️SSAFY GitAuto✌️</h1>

<h2 align="center">SSAFY 과제 제출용 GitLab Repository 자동생성기</h2>


<h4 align="center">OS 지원 : Windows , Mac, Linux</h4>

Usage
---
>if : Nobase로 실행 시<br />
>>=> 로컬 레포지토리가 생성되어있지 않을 경우 <br />
>>1. git proejct 폴더에 오늘의 Homework폴더 생성 <br />
>>2. README 파일 생성<br />

>if else : 오늘의 Homework폴더가 생성되어 있고, 내부에 Homework가 작성되어있을 경우<br />
>>=> 로컬 레포지토리가 생성되어 있는 경우<br />

>1. git add .<br />
>2. git commit -m "GitAuto of SSAFY"<br />
>3. 오늘의 Homework 프로젝트 생성 및 git push origin <br />
>4. 교수님 멤버(as Developer) 추가<br />
>5. 멤버 확인<br />


windows issue

install requests administrator

Git Credential Manager for Windows 에 lab.ssafy.com에 대한 계정 정보 입력 시
영어 입력했을 때, 한글로 바뀔 경우
외부 에디터 또는 브라우저 주소창에 영어입력후 복사 + 붙여넣기


위의 Manager에서 lab.ssafy.com 계정 실수 입력시
win + R 누른 후 rundll32.exe keymgr.dll,KRShowKeyMgr 입력,
그리고 lab.ssafy.com 삭제 후 재시도
