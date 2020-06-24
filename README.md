# 과학과소프트웨어적사고 Pygame 실습

## 권장사항

virtualenv를 사용하여 라이브러리를 설치, 실행하는 것을 권장함.

VisualStudio Code를 사용할 것을 권장함. 본 Repo의 모든 환경은 VSCode에 최적화되어있음.

## 실행

### 1. VirtualEnv 활성화

```bash
python3 -m venv .
```

### 2. Package 설치

```bash
pip install -r requirements.txt
```

### 3. Python Script 실행

```bash
./Scripts/python(.exe) main.py
```

## Mission

1. [x] [5점] 비행기가 총알에 맞았을 때 효과음이 발생하도록 한다.
1. [x] [5점] 비행기가 총알에 맞았을 때 터지는 그림 효과가 나타나도록 한다.
1. [x] [5점] 배경그림이 비행기의 움직임에 반응하여 같이 움직이도록 한다.
1. [x] [15점] 비행기가 총알과 여러번 충돌해야 게임이 종료되도록 한다
    – 즉, '생명력' 개념을 도입한다.
    – 참고: 총알에 맞으면 일정시간동안 무적이 되어야 정상적으로 작동한다.
1. [ ] [5점] 무적시간동안 비행기가 반짝거리도록 한다.
1. [ ] [10점] 남은 생명력을 막대기(5점)와 숫자(5점)로 표시한다.
1. [ ] [10점] 총알을 여러 종류로 만들고, 종류별로 크기와 색깔을 다르게 표현한다.
1. [ ] [5점] 총알의 종류마다 플레이어와 충돌했을 때 차감되는 생명력을 다르게 한다.
1. [ ] [10점] 사용자의 가장 오래 버틴 생존 시간을 최대 10개까지 파일에 기록한다.
1. [ ] [5점] 게임오버시에 기록된 생존시간을 화면에 출력한다.
1. [ ] [5점] 게임오버시에 기록된 생존시간을 화면에 출력하며, 현재 기록이 순위권에 있을 경우 강조하여 표시한다.

## Resources
- effect sound: https://freesound.org/people/sandyrb/sounds/95078/
- effect image: https://pixabay.com/vectors/boom-bang-explosion-explode-burst-42441/