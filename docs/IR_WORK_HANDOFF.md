# CDR System Bento IR 작업 핸드오프

## 목적
보스가 나중에 “IR 작업하자”, “CDR IR 이어서”, “Bento IR 업데이트”라고 하면 이 파일을 먼저 읽고 이어간다.

## 주요 파일
- 최신 Bento IR: `/mnt/c/Users/USER/Downloads/CDR_System_IR_v4_product_videos.bento.html`
- 직전 일관 시나리오본: `/mnt/c/Users/USER/Downloads/CDR_System_IR_v3_consistent_story.bento.html`
- 직전 자료반영본: `/mnt/c/Users/USER/Downloads/CDR_System_IR_v2_pdf_reflected.bento.html`
- 이전 디자인 버전: `/mnt/c/Users/USER/Downloads/CDR_System_IR_v1_design.bento.html`
- 최초 초안: `/mnt/c/Users/USER/Downloads/CDR_System_IR_v0.bento.html`
- 작업 디렉터리: `/home/termi/work/cdr-bento`
- v2 생성 스크립트: `/home/termi/work/cdr-bento/create_cdr_bento_v2.py`
- v1 개선 스크립트: `/home/termi/work/cdr-bento/improve_cdr_bento_v1.py`
- 홈페이지 추출 텍스트: `/home/termi/work/cdr-bento/home_text.txt`
- PDF 추출 결과: `/home/termi/work/cdr-bento/pdf_extract/ir.txt`
- PDF 페이지 이미지: `/home/termi/work/cdr-bento/pdf_extract/ir_pages/`

## 원천 자료
- 홈페이지: `https://www.cdrsystem.com/`
- 업로드 PDF 1: `/home/termi/.hermes/profiles/myafast/cache/documents/doc_b6ec780171f1_IR_CDR System.pdf`
- 업로드 PDF 2: `/home/termi/.hermes/profiles/myafast/cache/documents/doc_8408c98759ec_2025년 CDR System 소개 자료.pdf`
  - 두 PDF는 pymupdf 텍스트 추출 기준 동일한 23p 내용으로 확인됨.
- UI 참고: Adham Dannaway UI Design Tips — `https://www.adhamdannaway.com/blog/ui-design/ui-design-tips`

## 현재 최신본 상태
`CDR_System_IR_v4_product_videos.bento.html`

- 슬라이드 수: 11
- 파일 크기: 1,627,718 bytes
- SHA256: `3d0daeaf5ec2950f686210f278f62492e695c21a99d0b80e42c3a8ba42ce4416`
- 로컬 HTTP 검증: `HTTP/1.0 200 OK`
- Bento JSON 파싱 검증 완료: `format=bento/slides`
- 구성 원칙: v1 홈페이지 기반 내러티브를 메인으로, v2 PDF의 회사 히스토리/검증 지표는 보조 근거로만 사용.
- v4 변경: 제품별 홈페이지 원본 MP4를 링크형 Bento `media` 요소로 삽입. 큰 영상은 파일에 임베드하지 않음.

## v3 슬라이드 구성
1. Cover — Customized Robot Services for Real Industry
2. Problem — 로봇 도입 병목은 사용 역량
3. Solution — Simulation First, Sim2Real
4. Portfolio — RwRP / CDR / CRC / CSR
5. Product Videos — 제품별 홈페이지 영상 1개씩 삽입
6. Core Technology — RwRP 핵심 기술과 특허/NVIDIA 보조 근거
7. Why Now — 회사 히스토리는 메인 스토리의 증거
8. Use Cases — 교육, 스마트팩토리, F&B, 서비스로봇
9. Business Model — 교육 콘텐츠 → 실습 환경 → 플랫폼
10. Roadmap — 2025~2027 매출 계획과 성장축
11. Next Step — 투자 계획과 연락처

## v4 제품 영상 매핑
- RwRP: CDR 페이지의 Sim2Real 검증 영상 (`New Robot - ENCY simul & CDR real`, 34,242,471 bytes)
- CDR: CDR 페이지의 EncyManager GUI 순차 조각 테스트 영상 (12,929,944 bytes)
- CRC: CRC 페이지의 `CRC 서빙2차_텀블러250807.mp4` (140,878,289 bytes)
- CSR: CSR 페이지의 도슨트 모드 영상 (445,067,288 bytes)
- 주의: RwRP 전용 페이지에서는 `<video>`를 찾지 못해 CDR 페이지의 Sim2Real 검증 영상을 RwRP 관련 영상으로 매핑함.

## 디자인 원칙
Adham Dannaway UI tips를 반영:
- 명확한 시각 계층
- 목적 있는 색상 사용
- 충분한 대비
- 단일 sans-serif 계열
- 굵기 단계 단순화
- 긴 본문 왼쪽 정렬
- 카드/푸터/번호 스타일 일관화

## 다음에 할 만한 작업
- v3: 투자자용 10장 압축본
- v3-product: 제품/서비스 소개용 버전
- v3-sales: 고객 제안/영업용 버전
- v3-english: 영문 버전
- PDF 원본의 핵심 시각자료를 더 정교하게 재사용
- 매출/투자 표를 차트 중심으로 개선
- Bento 애니메이션/morph/state slide 강화

## 이어서 작업할 때 권장 절차
1. 이 파일과 최신 Bento 파일을 읽는다.
2. `#bento-doc` JSON을 추출한다.
3. 요청 방향에 따라 JSON만 수정하고 shell/runtime은 유지한다.
4. 새 파일은 `/mnt/c/Users/USER/Downloads/CDR_System_IR_v{N}_*.bento.html`로 저장한다.
5. JSON 파싱, 슬라이드 수, 파일 크기, SHA256, HTTP 200 검증 후 보고한다.
