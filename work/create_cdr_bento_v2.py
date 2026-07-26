import base64, json, re, hashlib
from pathlib import Path
from PIL import Image

SHELL_SRC = Path('/mnt/c/Users/USER/Downloads/CDR_System_IR_v1_design.bento.html')
OUT = Path('/mnt/c/Users/USER/Downloads/CDR_System_IR_v2_pdf_reflected.bento.html')
LOCAL = Path('/home/termi/work/cdr-bento/CDR_System_IR_v2_pdf_reflected.bento.html')
PDF_IMG = Path('/home/termi/work/cdr-bento/pdf_extract/ir_pages')

html = SHELL_SRC.read_text(encoding='utf-8')
m = re.search(r'(<script type="application/bento\+json" id="bento-doc">)\s*(.*?)\s*(</script>)', html, re.S)
base_doc = json.loads(m.group(2))
assets = dict(base_doc.get('assets', {}))

# Downsample selected original PDF slides as visual proof/source thumbnails.
def asset_from_png(name, page_no, max_w=900):
    src = PDF_IMG / f'page_{page_no:02d}.png'
    im = Image.open(src).convert('RGB')
    if im.width > max_w:
        h = int(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    out = Path('/home/termi/work/cdr-bento') / f'{name}.webp'
    im.save(out, 'WEBP', quality=78, method=6)
    assets[name] = 'data:image/webp;base64,' + base64.b64encode(out.read_bytes()).decode('ascii')

for name, page in [('pdf_company',3),('pdf_rwrp',8),('pdf_biz',14),('pdf_roadmap',19),('pdf_invest',21)]:
    asset_from_png(name, page)

W,H=1280,720
BG='#111827'; FG='#F9FAFB'; MUTED='#D1D5DB'; MUTED2='#9CA3AF'; ACC='#2DD4BF'; BLUE='#60A5FA'; AMBER='#FBBF24'; RED='#F87171'
SURF='rgba(255,255,255,0.06)'; SURF2='rgba(255,255,255,0.09)'; BORDER='rgba(255,255,255,0.16)'
FONT='Inter, Pretendard, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif'

def txt(id,x,y,w,h,html,size=32,weight=700,color=FG,align='left',line=1.14):
    return {'id':id,'type':'text','x':x,'y':y,'w':w,'h':h,'rotation':0,'opacity':1,'html':html,'fontSize':size,'fontFamily':FONT,'fontWeight':weight,'color':color,'align':align,'valign':'top','lineHeight':line}
def rect(id,x,y,w,h,fill=SURF,stroke=BORDER,sw=1,r=20,op=1):
    return {'id':id,'type':'shape','shape':'rect','x':x,'y':y,'w':w,'h':h,'fill':fill,'stroke':stroke,'strokeWidth':sw,'radius':r,'rotation':0,'opacity':op}
def line(id,x,y,w,h,color=ACC):
    return {'id':id,'type':'shape','shape':'line','x':x,'y':y,'w':w,'h':h,'fill':color,'stroke':'none','strokeWidth':0,'radius':0,'rotation':0,'opacity':1}
def img(id,x,y,w,h,key,fit='contain',op=1,r=16):
    return {'id':id,'type':'image','x':x,'y':y,'w':w,'h':h,'src':'asset:'+key,'fit':fit,'radius':r,'rotation':0,'opacity':op}
def footer(n):
    return [txt(f'foot{n}',96,672,520,24,'CDR System · IR v2',16,500,MUTED2), txt(f'pg{n}',1118,672,66,24,f'{n:02d}',16,700,MUTED2,'right')]
def slide(id,name,els,n,notes='',transition='morph'):
    return {'id':id,'name':name,'background':BG,'transition':transition,'notes':notes,'elements':els+footer(n)}
def metric(id,x,y,num,label,color=ACC):
    return [rect(id+'b',x,y,230,132,'rgba(255,255,255,0.075)',color,1,24), txt(id+'n',x+24,y+24,182,42,num,36,800,color,'center'), txt(id+'l',x+24,y+78,182,36,label,18,500,MUTED,'center')]
def bullet_block(id,x,y,w,items,color=ACC):
    els=[]
    for i,it in enumerate(items):
        yy=y+i*58
        els += [rect(f'{id}dot{i}',x,yy+7,14,14,color,color,0,7), txt(f'{id}t{i}',x+30,yy,w-30,42,it,24,600,FG,line=1.22)]
    return els

def table(id,x,y,w,h,headers,rows):
    return {'id':id,'type':'table','x':x,'y':y,'w':w,'h':h,'rotation':0,'opacity':1,'header':True,
            'columns':[{'w':1} for _ in headers],
            'rows':[{'cells':[{'html':c,'align':'center'} for c in headers]}]+[{'cells':[{'html':str(c),'align':'center'} for c in r]} for r in rows],
            'style':{'headerBg':'#1F2937','headerColor':'#FFFFFF','zebra':'rgba(255,255,255,0.04)','borderColor':BORDER,'borderWidth':1,'cellPadX':10,'cellPadY':9,'fontSize':18,'color':FG,'radius':14}}

slides=[]
slides.append(slide('s1','Cover',[
    img('hero',0,0,W,H,'hero','cover',0.55,0), rect('scrim',0,0,W,H,'linear-gradient(90deg, rgba(17,24,39,0.96), rgba(17,24,39,0.58))','none',0,0), img('logo',88,66,220,82,'ci'),
    txt('eyebrow',96,168,760,34,'CDR SYSTEM · ROBOT SERVICE PLATFORM',22,800,ACC),
    txt('headline',96,222,920,150,'Make Robots<br>Easier to Use',74,800,FG,line=1.0),
    txt('sub',100,410,820,84,'우리는 Robot을 만들지 않는다. 고객을 위한 Robot Service를 Creation하여 Sales한다.',30,600,MUTED,line=1.3),
    *metric('m1',96,538,'5년차','2020.11 설립',ACC), *metric('m2',354,538,'10명','2025 직원수',BLUE), *metric('m3',612,538,'2.12억','자본금',AMBER)
],1,'PDF p1,p3 핵심 문구 반영.', 'none'))

slides.append(slide('s2','Company Snapshot',[
    txt('k',96,62,600,32,'기업개요 및 현황',22,800,ACC), txt('h',96,105,800,62,'고객이 원하는 로봇 서비스를 제공하는 로봇 SI 전문기업',44,800),
    rect('card',96,205,560,360), txt('c1',132,238,500,40,'Customized Robot Service',32,800,ACC),
    *bullet_block('bb',132,304,470,['고객 현장 Needs 기반 로봇 서비스 설계·구현·제공','주요 상품: 직훈급 로봇교육 콘텐츠, F&B 시스템, AI 모바일로봇','본사: 동탄 KAIST·화성시 사이언스허브'],ACC),
    img('src',720,188,420,420,'pdf_company'), txt('cap',720,622,420,28,'Source: 업로드 IR PDF p.3',16,500,MUTED2,'center')
],2,'PDF p3 기업개요 반영.'))

slides.append(slide('s3','Market Shift',[
    txt('k',96,64,600,32,'시장 패러다임',22,800,ACC), txt('h',96,108,820,70,'로봇 제조의 시대에서 로봇 사용의 시대로',50,800),
    *bullet_block('b',112,236,1000,['로봇을 개발·제조하는 것보다, 어떻게 효과적으로 활용할 것인가가 중요','고객의 로봇 도입 장벽: 높은 초기비용, 이해 부족, 유지보수 부담','CDR의 미션: Make Robots Easier to Use'],ACC),
    rect('q',96,500,1088,98,'rgba(45,212,191,0.10)',ACC,1,24), txt('qt',132,528,1000,38,'AI 기반 맞춤형 서비스로 생산성과 효율성을 높이고, 중소기업도 쉽게 로봇자동화를 구현하게 한다.',28,700,FG,'center')
],3,'PDF p4 시장기회/미션 반영.'))

slides.append(slide('s4','Traction Timeline',[
    txt('k',96,64,600,32,'연혁 및 검증',22,800,ACC), txt('h',96,108,760,64,'시장 증명 이후 글로벌 진출 단계',48,800),
    table('t',96,220,1088,310,['연도','핵심 이정표'],[
        ['2020.11','법인 설립 / 협동로봇·딥러닝 비전 시스템 자산 확보'],['2021','포항사무실·기업부설연구소·서울사무소'],['2022','로봇 바리스타 시스템 / 협동로봇 교육 매출 5.8억'],['2023','매출 10.3억 / 벤처기업 인정'],['2024','NVIDIA N-Up 선정 / 본사이전·공장등록 / 매출 9.8억'],['2025','초격차 스타트업 1000+ DIPS 선정']]),
    txt('note',132,570,980,44,'IR 동기: 시장 증명을 거쳐 글로벌 진출 단계 → 투자 포함 BM 완성을 위한 파트너 필요',28,700,AMBER,'center')
],4,'PDF p5,p7 반영.'))

slides.append(slide('s5','Technology: RwRP',[
    txt('k',96,62,600,32,'보유기술 1',22,800,ACC), txt('h',96,105,760,62,'RwRP: Robot with Real Programming',48,800),
    rect('left',96,198,548,380), *bullet_block('r',132,236,480,['이기종·다수·다관절 로봇 직접 프로그래밍','실제 공정 그대로의 시뮬레이터 모델 기반 교육','비주얼 노드 그래프 UI로 초보자도 접근 가능','고가 실습장비 없이 노트북으로 1인 1로봇 교육'],ACC),
    img('pdf',710,178,420,420,'pdf_rwrp'), txt('pat',132,586,520,28,'특허등록 10-2426456 + 국내/해외 출원 진행',22,700,AMBER), txt('cap',710,622,420,28,'Source: IR PDF p.8',16,500,MUTED2,'center')
],5,'PDF p8 RwRP 기술 반영.'))

slides.append(slide('s6','NVIDIA Digital Twin',[
    txt('k',96,64,600,32,'기술 로드맵',22,800,ACC), txt('h',96,108,780,70,'Simulation → Digital Twin → AI',54,800),
    rect('a',120,254,260,156,'rgba(255,255,255,0.07)',ACC,1,26), txt('at',145,292,210,36,'초기 RwRP',30,800,ACC,'center'), txt('ad',145,342,210,34,'일부 기능 SIM 구현',20,500,MUTED,'center'),
    line('l1',404,330,142,4,ACC), rect('b',570,254,260,156,'rgba(255,255,255,0.07)',BLUE,1,26), txt('bt',595,292,210,36,'24년 RwRP',30,800,BLUE,'center'), txt('bd',595,342,210,34,'NVIDIA 협업 / Omniverse',20,500,MUTED,'center'),
    line('l2',854,330,142,4,BLUE), rect('c',1020,254,160,156,'rgba(255,255,255,0.07)',AMBER,1,26), txt('ct',1040,286,120,48,'미래<br>RwRP',28,800,AMBER,'center'), txt('cd',1038,352,124,34,'Teaching-less',18,500,MUTED,'center'),
    txt('bottom',150,500,980,72,'NVIDIA Omniverse · Isaac SIM/Isaac LAB 생태계 진입, 한국/중국 로봇 이식 및 알고리즘 학습/모션플래닝으로 확장',30,700,FG,'center')
],6,'PDF p9,p10 반영.'))

slides.append(slide('s7','Portfolio',[
    txt('k',96,64,600,32,'제품·서비스 포트폴리오',22,800,ACC), txt('h',96,108,760,62,'교육에서 플랫폼까지 이어지는 4개 축',48,800),
    table('pt',96,220,1088,282,['축','정의','핵심 가치'],[
        ['RwRP','Robot with Real Programming','디지털트윈 기반 로봇교육 / 1인 1로봇'],['CDR','Custom-Designed Robot','현장 맞춤 로봇 SI / 공정 최적화'],['CRC','Customized Robot Café','F&B 자동화 / RMS / QR 주문결제'],['CSR','Customized Service Robot','AI 모바일 서비스로봇 / 방역 등 확장']]),
    txt('bottom',132,552,1000,42,'모든 제품과 서비스의 C는 Customized — 고객 현장 Needs를 가장 잘 이해하는 로봇 서비스 회사',28,700,ACC,'center')
],7,'PDF p11,p12 및 홈페이지 Products 반영.'))

slides.append(slide('s8','F&B Proof',[
    txt('k',96,64,600,32,'CRC / F&B 자동화',22,800,ACC), txt('h',96,108,860,62,'로봇카페·라면·생맥주로 검증되는 서비스 기술',46,800),
    *metric('f1',96,230,'52→24초','아이스아메리카노 1잔',ACC), *metric('f2',354,230,'RMS','장비·POS 연동',BLUE), *metric('f3',612,230,'QR','스마트폰 주문/결제',AMBER),
    rect('desc',96,420,1088,128), txt('dt',132,452,1008,64,'디지털트윈 기반 로봇 티칭으로 서비스 시간을 단축하고, IoT 기반 F&B 자동화로 매장 운영 효율을 극대화합니다.',32,700,FG,'center'),
    txt('pat',132,588,980,30,'로봇카페 시스템 외 2건 특허출원중 · SDR 차세대 로봇 공용플랫폼 기술개발사업 참여(’24~’27)',22,600,MUTED,'center')
],8,'PDF p12,p13 반영.'))

slides.append(slide('s9','Business Model',[
    txt('k',96,64,600,32,'Biz Model',22,800,ACC), txt('h',96,108,760,62,'교육 사업에서 플랫폼 사업으로 확장',48,800),
    img('pdf',760,176,360,360,'pdf_biz'),
    *bullet_block('biz',112,226,570,['물리 로봇이 아닌 시뮬레이션 기반 로봇교육','실물 구축 1/10 비용으로 1인 1로봇 교육 가능','CoboticLAB 도메인 확보 / 교육과정·교재 개발 판매','향후 로봇활용 공정개선 솔루션 거래플랫폼으로 발전'],ACC),
    txt('cap',760,562,360,28,'Source: IR PDF p.14',16,500,MUTED2,'center')
],9,'PDF p14 반영.'))

slides.append(slide('s10','Market Validation',[
    txt('k',96,64,600,32,'시장 검증',22,800,ACC), txt('h',96,108,800,62,'RwRP 교육 사업은 이미 3년간 시장에서 검증',46,800),
    table('sales',96,210,1088,270,['채널','내용','시기','금액'],[
        ['대학교','RTRS 2건-1세트','2021','40백만원'],['연구소','POC 1건-1세트','2022','120백만원'],['대학교','RwRP 제안 3건-25세트','2023','400백만원'],['대학교','공정교육용 로봇시스템','2024','180백만원'],['협회','RwRP 교육','2024','25백만원']]),
    rect('sum',226,532,828,78,'rgba(45,212,191,0.10)',ACC,1,22), txt('sumt',250,554,780,34,'누적매출 약 5.6억원 달성 (’22~’24)',30,800,ACC,'center')
],10,'PDF p15 반영.'))

slides.append(slide('s11','Global Expansion',[
    txt('k',96,64,600,32,'글로벌 확장',22,800,ACC), txt('h',96,108,820,62,'동남아 로봇교육 시장으로 확장 시작',48,800),
    *metric('g1',96,236,'12,000 Pax','연간 교육 수요 추정',ACC), *metric('g2',354,236,'12억대','온라인 교육 고정매출 예상',BLUE), *metric('g3',612,236,'SG Expert','싱가폴 파트너십',AMBER),
    rect('gb',96,440,1088,106), txt('gt',132,472,1000,44,'로봇교육 콘텐츠(SW) + RwRP 실습센터(HW) 구축, Study Tour to Korea 및 베트남 ODA 사업 협의',30,700,FG,'center')
],11,'PDF p16 반영.'))

slides.append(slide('s12','Roadmap & Revenue',[
    txt('k',96,64,600,32,'사업 로드맵',22,800,ACC), txt('h',96,108,840,62,'2025–2027 매출 14억 → 25억 → 50.7억 계획',46,800),
    {'id':'chart','type':'chart','x':96,'y':220,'w':590,'h':330,'rotation':0,'opacity':1,'preset':'bar','option':{'xAxis':{'type':'category','data':['2025','2026','2027']},'yAxis':{'type':'value'},'series':[{'type':'bar','data':[14.2,25.2,50.7],'itemStyle':{'color':ACC},'barWidth':70}],'tooltip':{'trigger':'item','formatter':'{b}: {c}억원'}},'fx':{'enter':'fade-up'}},
    img('pdf',750,190,370,370,'pdf_roadmap'), txt('mix',120,575,570,34,'교육 RwRP · F&B · 모바일서비스로봇 · 로봇공정공유플랫폼',24,600,MUTED,'center'), txt('cap',750,590,370,28,'Source: IR PDF p.19–20',16,500,MUTED2,'center')
],12,'PDF p19,p20 매출 로드맵 반영.'))

slides.append(slide('s13','Investment Ask',[
    txt('k',96,64,600,32,'투자유치 계획',22,800,ACC), txt('h',96,108,820,62,'CoboticLAB 구성 및 플랫폼 사업자금 확보',48,800),
    *metric('i1',96,232,'3.9억','기존 외부투자유치',ACC), *metric('i2',354,232,'20억','신규 유치 계획',BLUE), *metric('i3',612,232,'Pre 150억','목표 밸류에이션',AMBER),
    rect('ask',96,430,1088,120,'rgba(96,165,250,0.10)',BLUE,1,24), txt('askt',132,462,1000,50,'SI 투자 50% 이상 목표: SI 파트너 10억 + VC 시리즈A 10억',34,800,FG,'center'),
    img('pdf',934,178,210,210,'pdf_invest'), txt('cap',934,398,210,24,'Source: PDF p.21',14,500,MUTED2,'center')
],13,'PDF p21 투자유치 계획 반영.'))

doc={'format':'bento/slides','version':1,'title':'CDR System IR v2 — PDF Reflected','size':{'width':W,'height':H},'theme':{'background':BG,'color':FG,'accent':ACC,'fontFamily':FONT},'assets':assets,'slides':slides,'metadata':{'source':['https://www.cdrsystem.com/','IR_CDR System.pdf','2025년 CDR System 소개 자료.pdf'],'status':'draft-v2-pdf-reflected','designReference':'Adham Dannaway UI Design Tips applied'}}
raw=json.dumps(doc,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
new_html=html[:m.start(1)] + m.group(1)+'\n'+raw+'\n'+m.group(3)+html[m.end(3):]
OUT.write_text(new_html,encoding='utf-8')
LOCAL.write_text(new_html,encoding='utf-8')
print('wrote', OUT)
print('local', LOCAL)
print('slides', len(slides), 'assets', len(assets), 'bytes', OUT.stat().st_size)
print('sha256', hashlib.sha256(OUT.read_bytes()).hexdigest())
