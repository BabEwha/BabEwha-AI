# 🍚 밥이화(BabEwha) 🍚
AI 기반 배달 애플리케이션 **🍚** **밥이화(BabEwha) 🍚** AI 레포지토리입니다.

<br/><br/>

## 🍙 프로젝트 소개


개발 기간: 2023.03.15(금) ~ 2023.03.17(일) <br/>
예상 사용자 설문조사 링크: https://docs.google.com/forms/d/e/1FAIpQLSfulZbuCy8cGD-FTW601AuBbd7FedH7zUMOYdtjfu-iqWXjSw/viewform?usp=sf_link

<br/><br/>

## 🍙 프로젝트 구조

<img width="1000" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/f6506a8e-f22c-4177-b4d2-108bcf0e0f30"/>



- Client: Swift(iOS)
- Server: Django, MySQL, AWS EC2, AWS S3
- AI: Google Vision, Flask, AWS EC2



<br/><br/>

## 🍙 팀원 소개

| <img width="200" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/8e36d672-d586-4d3f-987e-97ddeed88a3b"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/8e36d672-d586-4d3f-987e-97ddeed88a3b"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/8e36d672-d586-4d3f-987e-97ddeed88a3b"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/8e36d672-d586-4d3f-987e-97ddeed88a3b"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/8e36d672-d586-4d3f-987e-97ddeed88a3b"/> |
| --- | --- | --- | --- | --- |
| **엄채은** | **양연우** | **허혜민** | **김원정** | **이남영** |
| 기획 | 디자이너 | 클라이언트 | 백엔드 | AI |




<br/><br/>

## 🍙 AI 사용 기술

| <img width="150" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/7ea4f409-f7c3-481a-9013-221a8bf43702"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/7073637a-d185-42fc-975e-1da2ab4962a0"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/8495377d-7f0b-4f80-8b6f-b78b6e5064fb"/> |
| --- | --- | --- |
| **OCR** | **서버** | **배포** |
| Google Vision | Flask | AWS EC2 |

<br/><br/>

## 🍙 장바구니, 주문내역 이미지 분석



### 1. 장바구니
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/c60cd8db-af5b-47b0-8bf3-55ab2dbea4ae"/> |
| --- |
| 장바구니의 2가지 구성 <br/> 🟥 메뉴 (menu) <br/> 🟦 가격 (price) |

<br/>

### 2. 주문내역
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/10ccf5c4-b1f2-4ae7-901c-4f4260cf5e45"/> |
| --- |
| 주문내역의 3가지 구성 <br/> 🟩 배달팁 (delivery) <br/> 🟥 %할인 쿠폰 (discount) <br/> 🟦 정액 할인 쿠폰 (coupon) |

<br/>

### 3. 할인 (4가지 요소)
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/878364ac-a9f1-409f-b5f4-89bb896b5cf6"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/79c71158-e486-45d6-a9d6-5970eafa5157"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/d7d4d3fc-d579-4446-af89-9227b29cc001"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/4685fdb0-7568-410c-bb82-3377a10406b2"/> |
| --- | --- | --- | --- |
| 🟥 % 할인 (discount) | 🟦 정액 할인 (coupon) | 🟥🟦 %할인 + 정액할인 | 할인 없음 |

<br/><br/>

## 🍙 장바구니(메뉴, 가격) 분석

| <img width="200" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/c4204670-8d5d-4893-801a-93fb8721d955"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/9475c583-3b3e-44f8-9e88-ef368f03684f"/> |
| --- | --- |
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/f4637396-72fc-4a24-a709-1c7c7825cca3"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/5fbaf07b-efc5-4cbb-96eb-d8d31e843c4d"/> |
| **메뉴 1개** | **메뉴 2개** |

<br/>

### 🍘 장바구니에 담긴 모든 음식 메뉴와 메뉴별 개별 가격 분석
### 1. 스크롤 캡쳐/풀페이지 캡쳐 등 모든 형태의 캡쳐본 취급
### 2. 메뉴의 개수와 옵션 제한 없이 분석 가능

웹 서비스 주소(배포 완료): http://18.118.254.47:5000/cart

<br/><br/>

## 🍙 주문내역(배달팁, % 할인, 정액 할인) 분석

| <img width="200" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/dc98624e-3873-4163-8903-7c5794ad7413"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/2e5b37f5-08f7-4a01-b81c-ca7617bc1c4b"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/86e8dc8a-762b-47f7-a91e-2088d5c85840"/> |
| --- | --- | --- |
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/a44795b6-80c8-419a-9914-b3b1476fbe7a"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/b5aa4fac-1fe1-4be8-90b1-8c050fb45412"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai/assets/91009436/b09bb878-8d75-4cf1-a5f7-2429e268f707"/> |
| **% 할인** | **정액 중복 할인** | **% 할인 + 정액 할인** |


<br/>

### 🍘 배달팁과 할인 쿠폰 종류 2가지(% 할인, 정액 할인) 분석
### 1. %할인시 각 사용자의 결제 금액에 따라 차등 할인 적용
### 2. 중복 할인도 모두 적용해서 배달팁과 정액 할인 금액 1/n

웹 서비스 주소(배포 완료): http://18.118.254.47:5002/receipt

