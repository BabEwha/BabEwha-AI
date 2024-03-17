# 🍚 밥이화(BabEwha) 🍚
### OCR 기반 배달 어플리케이션 **🍚** **밥이화(BabEwha) 🍚** AI 레포지토리입니다.
#### 1️⃣ Client 레포지토리 링크: https://github.com/BabEwha/BabEwha-Client
#### 2️⃣ Backend 레포지토리 링크: https://github.com/BabEwha/BabEwha-Backend

<br/>

## 🍙 프로젝트 소개

### 🍘 기존에 이화인끼리 진행하던 ‘배달톡방’을 어플화하여 직관적이고 신속한 배달을 가능하게 하는 ‘배달 공구 서비스’

### 🍘 문제 상황 및 솔루션
1️⃣ 식사권이 보장되지 않는 상황
2️⃣ 넓은 부지를 소유하고 있는 우리 학교지만, 상권은 정문 위주로 형성되어 있으며
언덕이 심한 특성으로 인해 한 번 각 건물로 등교하면 다른 장소로의 이동이 어려움- 공대, 연협, 중도 등 정문과 거리가 있는 건물의 학생들은 근방에 음식점이 없어 편의점이나 배달을 통해 식사를 해결하고 있음. - 편의점의 경우 영양 불균형 문제가 심각하게 발생함. 그러나 배달의 경우 오르는
배달팁이 부담됨. 2. 배달 공구를 이용하고 있으나, 현존하는 배달 공구는 카카오톡 오픈채팅을 이용하기에 여러 불편이 따르는 상황
3️⃣ 공구를 할 때마다 새로 오픈채팅방을 파야 하고, 알림이나 입장/퇴장 등 배달 공구
경험을 방해하는 여러 요소들이 존재함. - 이로 인해 배달 공구를 포기하는 인원이 다수 발생하여 공구 리젠이 줄어듦. => 직관적인 UI/UX로, 사용자로 하여금 신속하고 긍정적인 배달 공구 경험을 쌓게
함. 이를 통해 배달 공구를 활성화하고, 교내 이화 학생들의 식사권 보장 및 배달팁
감소를 통한 금전적 이득 보장을 가능케 함. 

### 🍘 가치
1️⃣ '이화’라는 공간 내에서 공동 생활을 하는 이화인이 공동 구매 경험을 통해 서로의 이익 증진과 권리 보장을 도모할 수 있음

### 🍘 가치
1️⃣ 실제 사용자 리서치를 통해 얻은 결과로, 사용자 맞춤형 UI/UX 제안
- 총 응답 324개를 바탕으로 신뢰성 향상
- 사용자가 진정으로 원하는 서비스임을 확인
2️⃣ 배달 공구의 신속성을 위하여 AI (OCR) 기술 적용
- 공구 참여자, 공구 개설자의 주문내역 및 영수증을 확인하여 신속하고 안전한 정산

- 개발 기간: 2023.03.15(금) ~ 2023.03.17(일) <br/>
- 예상 사용자 설문조사: 3.15(금) 21:00 ~ 3.17(일) 14:00<br/>
- 설문 링크 (현재 폐쇄): https://docs.google.com/forms/d/e/1FAIpQLSfulZbuCy8cGD-FTW601AuBbd7FedH7zUMOYdtjfu-iqWXjSw/viewform?usp=sf_link

<br/><br/>

## 🍙 프로젝트 구조

<img width="800" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/adda6865-b0f4-4f80-9cad-79eb534990bb"/>

- Client: Swift(iOS)
- Server: Django, MySQL, AWS EC2, AWS S3
- AI: Google Vision, Flask, AWS EC2

<br/><br/>

## 🍙 팀원 소개

| <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/1a77ca56-1b72-48cc-81e1-09d2d2ee1688"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/0c997a4a-b942-457a-8c20-fb8bdd0a7277"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/f1414b85-9269-4aae-a121-af8e01090579"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/6b676f0c-d5e1-44e9-ab1d-1d00d7c48046"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/4be5a2b8-fd32-4ccc-b89c-00d4269c77ce"/> |
| --- | --- | --- | --- | --- |
| **엄채은** | **양연우** | **허혜민** | **김원정** | **이남영** |
| 기획 | 디자이너 | 프론트엔드 | 백엔드 | IT기술(AI) |

<br/><br/>

## 🍙 AI 사용 기술

| <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/075295ea-6122-458d-991e-a4a95ab8221d"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/941f9767-efb6-4950-8647-01a987f7708c"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/7fc0098a-47e4-4af4-a167-8defc53d5920"/> |
| --- | --- | --- |
| **OCR** | **서버** | **배포** |
| Google Vision | Flask | AWS EC2 |

<br/><br/>

## 🍙 코드 설명
### 1️⃣ cart.py
- 장바구니 캡쳐본의 text를 추출하여 'menu: 주문 음식 메뉴'와 'price: 메뉴 가격'을 json으로 반환
### 2️⃣ receipt_combined.py
- 주문내역 캡쳐본의 text를 추출하여 'fee: 배달팁과 정액 할인 금액을 합산한 금액', 'discount: % 할인 값'을 json으로 반환
### 3️⃣ receipt_separate.py
- 주문내역 캡쳐본의 text를 추출하여 'delivery: 배달팁', 'coupon: 정액 할인 금액', 'discount: % 할인 값'을 json으로 반환
<br/>

<img width="600" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/b36edf38-7659-44fe-a5f0-f8c5d9ea1512"/>

### *receipt.py(2,3번)의 경우 서버 배포 후 github 파일명만 편의를 위해 수정
##### ✔ 밥이화(BabEwha) 서비스에서는 receipt_separate.py 사용
##### ✔ 과금 문제로 서버를 닫게 될 경우를 대비해 캡쳐 증명

<br/><br/>

## 🍙 장바구니, 주문내역 이미지 분석

### OCR을 통한 text 추출 후 필요 요소 추출을 위한 탐색 과정

### 1. 장바구니
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/41f517cc-b0da-4fe5-8a0c-5ed57ae6959e"/> |
| --- |
| 장바구니의 2가지 구성 <br/> 🟥 메뉴 (menu) <br/> 🟦 가격 (price) |

<br/>

### 2. 주문내역
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/92de8380-1b91-454e-a40c-6bb78ba2bfd5"/> |
| --- |
| 주문내역의 3가지 구성 <br/> 🟩 배달팁 (delivery) <br/> 🟥 % 할인 쿠폰 (discount) <br/> 🟦 정액 할인 쿠폰 (coupon) |

<br/>

### 3. 할인 (4가지 요소)
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/56052773-1171-4688-8924-634fb28e2f46"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/0bbc4676-d64e-4db4-abb7-cfdc70eb19dc"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/374fa377-0d0a-4dac-bfac-e888f97ca9ea"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/a07c564a-34d5-454e-a250-6107ee88407b"/> |
| --- | --- | --- | --- |
| 🟥 % 할인 (discount) | 🟦 정액 할인 (coupon) | 🟥🟦 %할인 + 정액할인 | ✖ 할인 없음 |

<br/><br/>

## 🍙 장바구니(메뉴, 가격) 분석

| <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/4831d60f-4719-496f-a43f-39a17e95835d"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/018cdeeb-8cc5-4deb-bcd0-2882799c1499"/> |
| --- | --- |
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/bb22b3b9-f7f8-4364-8faa-6c3a6fec4554"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/d2f78841-cbdf-4a60-a5b0-cf45373c7add"/> |
| **1️⃣ 메뉴 1개** | **2️⃣ 메뉴 2개** |

<br/>

### 🍘 장바구니에 담긴 모든 음식 메뉴와 메뉴별 개별 가격 분석
### 1. 스크롤 캡쳐/풀페이지 캡쳐 등 모든 형태의 캡쳐본 취급
### 2. 메뉴의 개수와 옵션 제한 없이 분석 가능

✔ 웹 서비스 주소(배포 완료): http://18.118.254.47:5000/cart

<br/><br/>

## 🍙 주문내역(배달팁, % 할인, 정액 할인) 분석

| <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/2d306c90-cf27-453a-abd5-1d0ac78a7a2b"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/8b01f011-026c-4bbd-a88b-9f62470b4e46"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/45f51eb5-551b-44cc-a9be-70d41b24f8ff"/> |
| --- | --- | --- |
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/893d9ee4-bea4-4ecd-b8ab-939eaa327d3c"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/819132f5-37d2-4770-9a37-15a7aa001477"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/c873a8c2-a32b-4b93-8ce0-f8ca2a87bad5"/> |
| **1️⃣ % 할인** | **2️⃣ 정액 중복 할인** | **3️⃣ % 할인 + 정액 할인** |


<br/>

### 🍘 배달팁과 할인 쿠폰 종류 2가지(% 할인, 정액 할인) 분석
### 1. %할인시 각 사용자의 결제 금액에 따라 차등 할인 적용
### 2. 중복 할인도 모두 적용해서 배달팁과 정액 할인 금액 1/n

✔ 웹 서비스 주소(배포 완료): http://18.118.254.47:5002/receipt

<br/><br/><br/><br/>
