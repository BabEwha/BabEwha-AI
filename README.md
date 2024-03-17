# 🍚 밥이화(BabEwha) 🍚
### OCR 기반 배달 애플리케이션 **🍚** **밥이화(BabEwha) 🍚** AI 레포지토리입니다.
#### 1️⃣ Client 레포지토리 링크: https://github.com/BabEwha/BabEwha-AI
#### 2️⃣ Backend 레포지토리 링크: https://github.com/BabEwha/BabEwha-AI

<br/>

## 🍙 프로젝트 소개


개발 기간: 2023.03.15(금) ~ 2023.03.17(일) <br/>
예상 사용자 설문조사 링크: https://docs.google.com/forms/d/e/1FAIpQLSfulZbuCy8cGD-FTW601AuBbd7FedH7zUMOYdtjfu-iqWXjSw/viewform?usp=sf_link

<br/><br/>

## 🍙 프로젝트 구조

<img width="800" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/adda6865-b0f4-4f80-9cad-79eb534990bb"/>

- Client: Swift(iOS)
- Server: Django, MySQL, AWS EC2, AWS S3
- AI: Google Vision, Flask, AWS EC2



<br/><br/>

## 🍙 팀원 소개

| <img width="200" src=""/> | <img width="200" src=""/> | <img width="200" src=""/> | <img width="200" src=""/> | <img width="200" src=""/> |
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

<br/>

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

웹 서비스 주소(배포 완료): http://18.118.254.47:5000/cart

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

웹 서비스 주소(배포 완료): http://18.118.254.47:5002/receipt

<br/><br/><br/><br/>
