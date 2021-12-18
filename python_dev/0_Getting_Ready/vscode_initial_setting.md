## VSCode 초기설정

### 폴더 만들고 시작하기

VSCode를 실행하면 다음과 같은 창이 뜰텐데, `Open folder`를 선택해줍니다.

![image](https://user-images.githubusercontent.com/50950237/146644344-b481c09b-b222-404a-9bc6-922abcba8c8d.png)

그럼 열 폴더를 선택해야하는데, 바탕화면에서 `우클릭 > 새로 만들기 > 폴더`를 통해 `PythonWorkspace`라는 폴더를 만들어줍니다.   
앞으로 `PythonWorkspace`라는 폴더는 저희가 연습하는 모든 코드를 저장할 것입니다.

![image](https://user-images.githubusercontent.com/50950237/146644383-543ed3b6-9d1e-4c26-9b49-fee8e3db2b79.png)

다음과 같이 폴더를 생성한 뒤, PythonWorkspace를 선택한 상태로 열기를 누르면 됩니다.   
그러면 다음과 같은 창이 나오게 됩니다.   
여기서는 `Yes, I trust the authors`라고 선택해주시면 됩니다.

![image](https://user-images.githubusercontent.com/50950237/146644502-269336a4-b4da-44a0-ba5a-70a2fb422d76.png)

다음과 같이 창이 뜨면 정상적으로 준비가 된 것입니다.
- 왼쪽 상단에 `PythonWorkspace`라고 표시
- 상단에 `Get Started`창 표시

![image](https://user-images.githubusercontent.com/50950237/146644663-d9016f97-cea5-49f2-ad65-ae46ed8b6ee5.png)

### Python 관련 플러그인 다운받기

VSCode는 Python뿐만아니라 다양한 프로그래밍 언어에 대한 코드 에디터입니다. 따라서 Python을 사용하기 위해서는 Python 관련 플러그인을 다운받아야 합니다.   
우선 왼쪽 툴바에 있는 아이콘들 중 가장 아래에 있는 아이콘을 클릭하고, Python이라고 검색합니다.   
그러면 다음과 같이 상단에 `Python`, `Python for VSCode`, `Python Extension Pack`이 있습니다.   
위 세가지를 모두 `Install`버튼을 눌러 다운받아주도록 합시다.

![image](https://user-images.githubusercontent.com/50950237/146644791-89d3b816-e4e0-4e69-a07c-ce03a34e6dd0.png)

잘 설치되어있는지 확인하기 위해 단순히 확인해보도록 합시다.   
다시 왼쪽 툴바의 맨 위 아이콘(Explorer)를 클릭하고, 작은 종이모양 아이콘을 클릭해 파일을 생성합시다. 이름은 `test.py`라고 입력한 뒤 엔터를 누릅니다.

![image](https://user-images.githubusercontent.com/50950237/146644911-bdac499c-ece4-4ede-a594-a76c1428d99f.png)

그러면 입력할 수 있는 창이 나타나게 됩니다.   
상단에 `test.py`가 보이고, 그 밑에는 코드를 입력할 수 있는 공간이 주어집니다.   
입력할 수 있는 공간에 다음 코드를 입력하도록 하겠습니다.   

```
print('hello world!')
```

입력한 뒤 다음과 같은 화면이면 됩니다.

![image](https://user-images.githubusercontent.com/50950237/146644993-9122a541-539a-4403-a5b2-d9efdad9c116.png)


마지막으로 코드를 실행시켜보도록 하겠습니다.    
코드를 실행시키는 방법은 여러 가지가 있지만, 일단은 우측 상단에 있는 세모 버튼을 눌러서 실행시키도록 합시다.   
그러면 하단에 Terminal창이 뜨면서 뭔가 막 뜰텐데, 아래 캡쳐처럼 `hello world!`라는 문구가 출력되면 성공적으로 실행된 것입니다.

![image](https://user-images.githubusercontent.com/50950237/146645073-40153d00-2708-4f58-a3c0-906454129549.png)

여기까지 문제없이 완료했다면 끝입니다. 수업시간에 만나요!
