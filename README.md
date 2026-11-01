# Moonlighter 2D Action Study

Python과 pico2d로 문라이터의 던전 전투를 구현해 보는 2D 액션 학습 프로젝트.

| 항목 | 내용 |
|---|---|
| 기술 | Python, pico2d |
| 화면 | 800 × 500 |
| 진입점 | Moonlighter.py |
| 구현 범위 | 던전 전투·플레이어 행동·몬스터·방 진행 |

> 문서 기준: 2026-11-01. 구현 상태는 소스 검토 기준이며, 이 문서 갱신 과정에서 빌드·플레이·성능 실험을 새로 실행하지 않았습니다.

## 1. 프로젝트 소개

이동·공격·방어·구르기와 몬스터 충돌을 구현하며, 게임 루프와 상태 전환을 학습하는 프로젝트입니다. 문라이터 모작을 목표로 한 자료가 포함되어 있지만, 현재 소개 범위는 소스에서 확인되는 던전 전투입니다.

상점 운영이나 원작 전체 시스템의 구현을 의미하지 않습니다.

## 2. 실행·시연 방법

1. Python 3와 pico2d가 동작하는 환경을 준비합니다. 정확한 검증 버전은 아직 기록하지 않았습니다.
2. 이미지·폰트 파일을 유지하고 저장소 루트를 작업 디렉터리로 사용합니다.
3. 다음 명령으로 시작합니다.

```powershell
python Moonlighter.py
```

| 키 | 동작 |
|---|---|
| W / A / S / D | 이동 |
| J | 공격 |
| K | 방어 |
| Space | 구르기 |

실행 절차는 [진입점](https://github.com/Han-g/2DGP_Proj_2019180043/blob/main/Moonlighter.py)과 [입력 처리](https://github.com/Han-g/2DGP_Proj_2019180043/blob/main/character.py) 기준입니다. 현재 환경에서 실행하거나 패키지 버전 호환성을 검증하지 않았습니다.

## 3. 현재 구현된 기능

| 영역 | 소스에서 확인한 구현 |
|---|---|
| 프레임워크 | 상태 진입·갱신·그리기, 프레임 시간 |
| 플레이어 | Move·Attack·Dffense·Roll 상태와 애니메이션 |
| 무기 | 검·창의 표현과 공격 범위 |
| 몬스터 | 생성·이동·근접 관계·체력 관련 처리 |
| 상호작용 | 공격·접촉·낙하 검사 |
| 방 진행 | 몬스터 제거와 조건에 따른 재진입 처리 |

몬스터의 별도 Attack 상태는 빈 함수가 남아 있으며, 모든 상태가 완성된 것은 아닙니다.

## 4. 담당 범위와 사용 자료

문라이터의 던전 전투를 대상으로 한 학습 프로젝트이며 Python과 pico2d를 사용합니다.

개인 담당 범위, 수업 제공 프레임워크와의 차이, 스프라이트·폰트 자료의 출처는 추가로 정리할 예정입니다. 원작 전체 시스템을 구현한 프로젝트로 소개하지 않습니다.

## 5. 핵심 구조와 설계

```text
Moonlighter.py
  → Framework.play(Game_State)
  → Game_State의 enter / update / draw / 입력 처리
  → Game_World의 객체 목록
  → Character / Monster / Weapon / Background
  → 충돌·피해·제거·방 진행
```

| 파일 | 역할 |
|---|---|
| [Framework.py](https://github.com/Han-g/2DGP_Proj_2019180043/blob/main/Framework.py) | 메인 루프와 상태 실행 |
| [Game_State.py](https://github.com/Han-g/2DGP_Proj_2019180043/blob/main/Game_State.py) | 객체 구성, 충돌, 진행 |
| [character.py](https://github.com/Han-g/2DGP_Proj_2019180043/blob/main/character.py) | 플레이어 상태와 입력 |
| [monster.py](https://github.com/Han-g/2DGP_Proj_2019180043/blob/main/monster.py) | 몬스터 동작 |
| [weapon.py](https://github.com/Han-g/2DGP_Proj_2019180043/blob/main/weapon.py) | 무기 표현과 범위 |

행동별 상태를 나누지만 객체 간 연결은 refer_object의 전역 참조를 많이 사용합니다.

## 6. 문제 해결과 검증 기록

| 주제 | 현재 확인 내용 | 추가할 자료 |
|---|---|---|
| 상태 전환 | 이동·공격·방어·구르기 분리 | 실제 입력별 상태 전이 그림 |
| 시간 기반 처리 | 프레임 시간을 사용한 이동·애니메이션 | 프레임 조건을 바꿨을 때의 동작 기록 |
| 피해 판정 | Game_State의 무기·몬스터·캐릭터 충돌 검사 | 한 번의 공격이 적용되는 조건 설명 |
| 미완성 상태 | monster.py의 Attack에 pass 잔존 | 구현 범위와 알려진 제한 표시 |

발견한 문제와 수정 완료한 문제를 구분해 기록합니다. 성능이나 버그 해결 결과는 아직 첨부하지 않았습니다.

## 7. 현재 제한과 다음 작업

- [ ] Python·pico2d 검증 버전과 실행 화면 기록
- [ ] 플레이어 상태 전이 그림과 조작법 정리
- [ ] 구현한 전투 범위와 미완성 몬스터 상태를 명확히 표시
- [ ] 보완할 경우 몬스터 공격 준비·실행·회복 흐름 추가
- [ ] 사용 에셋 출처와 개인 작성 범위 정리

---

저장소: [2DGP_Proj_2019180043](https://github.com/Han-g/2DGP_Proj_2019180043)
