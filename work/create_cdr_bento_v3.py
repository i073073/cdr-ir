import json, re, hashlib
from pathlib import Path

SHELL_SRC = Path('/mnt/c/Users/USER/Downloads/CDR_System_IR_v2_pdf_reflected.bento.html')
OUT = Path('/mnt/c/Users/USER/Downloads/CDR_System_IR_v3_consistent_story.bento.html')
LOCAL = Path('/home/termi/work/cdr-bento/CDR_System_IR_v3_consistent_story.bento.html')

html = SHELL_SRC.read_text(encoding='utf-8')
m = re.search(r'(<script type="application/bento\+json" id="bento-doc">)\s*(.*?)\s*(</script>)', html, re.S)
if not m:
    raise SystemExit('bento-doc block not found')
base = json.loads(m.group(2))
assets = dict(base.get('assets', {}))

W,H=1280,720
BG='#111827'; FG='#F9FAFB'; MUTED='#D1D5DB'; MUTED2='#9CA3AF'; ACC='#2DD4BF'; BLUE='#60A5FA'; AMBER='#FBBF24'; RED='#F87171'
SURF='rgba(255,255,255,0.058)'; SURF2='rgba(255,255,255,0.085)'; BORDER='rgba(255,255,255,0.16)'
FONT='Inter, Pretendard, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif'

def txt(id,x,y,w,h,html,size=32,weight=700,color=FG,align='left',line=1.15,fx=None):
    o={'id':id,'type':'text','x':x,'y':y,'w':w,'h':h,'rotation':0,'opacity':1,'html':html,'fontSize':size,'fontFamily':FONT,'fontWeight':weight,'color':color,'align':align,'valign':'top','lineHeight':line}
    if fx: o['fx']=fx
    return o

def rect(id,x,y,w,h,fill=SURF,stroke=BORDER,sw=1,r=22,op=1,fx=None):
    o={'id':id,'type':'shape','shape':'rect','x':x,'y':y,'w':w,'h':h,'fill':fill,'stroke':stroke,'strokeWidth':sw,'radius':r,'rotation':0,'opacity':op}
    if fx: o['fx']=fx
    return o

def line(id,x,y,w,h,color=ACC,op=1):
    return {'id':id,'type':'shape','shape':'line','x':x,'y':y,'w':w,'h':h,'fill':color,'stroke':'none','strokeWidth':0,'radius':0,'rotation':0,'opacity':op}

def img(id,x,y,w,h,key,fit='contain',op=1,r=16,fx=None):
    o={'id':id,'type':'image','x':x,'y':y,'w':w,'h':h,'src':'asset:'+key,'fit':fit,'radius':r,'rotation':0,'opacity':op}
    if fx: o['fx']=fx
    return o

def footer(n):
    return [txt(f'foot{n}',96,672,520,24,'CDR System · coherent IR v3',16,500,MUTED2), txt(f'pg{n}',1118,672,66,24,f'{n:02d}',16,700,MUTED2,'right')]

def slide(id,name,els,n,notes='',transition='morph'):
    return {'id':id,'name':name,'background':BG,'transition':transition,'notes':notes,'elements':els+footer(n)}

def pill(id,x,y,label,color=ACC,w=188):
    return [rect(id+'b',x,y,w,44,'rgba(255,255,255,0.07)',color,1,22), txt(id+'t',x+16,y+11,w-32,24,label,17,700,color,'center')]

def metric(id,x,y,num,label,color=ACC,w=220):
    return [rect(id+'b',x,y,w,124,'rgba(255,255,255,0.072)',color,1,24), txt(id+'n',x+22,y+24,w-44,38,num,34,800,color,'center'), txt(id+'l',x+22,y+76,w-44,34,label,18,500,MUTED,'center')]

def bullet_block(id,x,y,w,items,color=ACC,gap=52,fs=23):
    els=[]
    for i,it in enumerate(items):
        yy=y+i*gap
        els += [rect(f'{id}dot{i}',x,yy+8,12,12,color,color,0,6), txt(f'{id}t{i}',x+28,yy,w-28,40,it,fs,600,FG,line=1.23)]
    return els

def product_card(id,x,y,title,sub,body,color):
    return [rect(id+'card',x,y,250,248,'rgba(255,255,255,0.058)',BORDER,1,26), txt(id+'title',x+24,y+26,202,34,title,33,800,color,'center'), txt(id+'sub',x+22,y+78,206,52,sub,23,700,FG,'center',1.15), txt(id+'body',x+24,y+154,202,58,body,18,500,MUTED,'center',1.25)]

def table(id,x,y,w,h,headers,rows,font=18):
    return {'id':id,'type':'table','x':x,'y':y,'w':w,'h':h,'rotation':0,'opacity':1,'header':True,
            'columns':[{'w':1} for _ in headers],
            'rows':[{'cells':[{'html':c,'align':'center'} for c in headers]}]+[{'cells':[{'html':str(c),'align':'center'} for c in r]} for r in rows],
            'style':{'headerBg':'#1F2937','headerColor':'#FFFFFF','zebra':'rgba(255,255,255,0.04)','borderColor':BORDER,'borderWidth':1,'cellPadX':10,'cellPadY':9,'fontSize':font,'color':FG,'radius':14}}

slides=[]
# 1. v1 style cover; history as quiet confidence chips, not main message
slides.append(slide('s1','Cover',[
    img('hero',0,0,W,H,'hero','cover',0.62,0,{'ambient':'kenburns','ken':{'dir':'drift','scale':1.07,'duration':24}}),
    rect('scrim',0,0,W,H,'linear-gradient(90deg, rgba(17,24,39,0.96), rgba(17,24,39,0.52))','none',0,0),
    img('logo',88,66,220,82,'ci'),
    txt('eyebrow',96,170,720,34,'CDR SYSTEM · ROBOT SERVICE PLATFORM',22,800,ACC),
    txt('headline',96,224,920,150,'Customized Robot Services<br>for Real Industry',68,800,FG,line=1.02,fx={'enter':'fade-up'}),
    txt('sub',100,416,790,80,'로봇을 직접 제조하기보다, 고객 현장에 맞는 로봇 서비스와 디지털트윈 기반 활용 역량을 설계합니다.',28,500,MUTED,line=1.28),
    *pill('p1',96,552,'Simulation First',ACC), *pill('p2',306,552,'Sim2Real',BLUE), *pill('p3',516,552,'Physical AI',AMBER),
    txt('proof',96,622,640,28,'Since 2020 · NVIDIA N-Up · DIPS 1000+ · Series A-ready',18,600,MUTED2)
],1,'v1 홈페이지 기반 메시지를 메인으로 복원. v2 히스토리는 보조 proof chip으로만 사용.', 'none'))

# 2. problem, from v1
slides.append(slide('s2','Problem',[
    txt('k',96,68,600,32,'현장의 질문',22,800,ACC),
    txt('h',96,110,920,92,'로봇 도입의 병목은 “기계”가 아니라 “사용 역량”입니다',48,800),
    rect('q1',96,250,330,218,'rgba(255,255,255,0.058)',ACC,1,24), txt('q1t',124,286,270,86,'최선의 로봇 파트너를 만날 확률은?',30,800), txt('q1b',124,386,270,44,'선택과 셋업이 어렵습니다.',20,500,MUTED),
    rect('q2',475,250,330,218,'rgba(255,255,255,0.058)',BLUE,1,24), txt('q2t',503,286,270,96,'담당자는 현장을 충분히 이해했는가?',30,800), txt('q2b',503,396,270,44,'현장 지식이 성패를 좌우합니다.',20,500,MUTED),
    rect('q3',854,250,330,218,'rgba(255,255,255,0.058)',AMBER,1,24), txt('q3t',882,286,270,96,'시스템은 계속 업데이트되는가?',30,800), txt('q3b',882,396,270,44,'도입 이후 활용도가 문제입니다.',20,500,MUTED),
    rect('bottom',150,540,980,70,'rgba(45,212,191,0.10)',ACC,1,22), txt('bt',184,560,912,30,'그래서 로봇은 “현장을 아는 사람이 쉽게 사용할 수 있는 도구”가 되어야 합니다.',26,700,FG,'center')
],2,'v1의 세 가지 질문 구조 유지.'))

# 3. solution narrative
slides.append(slide('s3','Solution',[
    txt('k',96,68,600,32,'CDR의 해법',22,800,ACC),
    txt('h',96,110,800,82,'Simulation First,<br>Sim2Real로 검증하는 로봇 서비스',50,800,line=1.05),
    txt('body',98,228,610,118,'실제 공정 그대로의 시뮬레이터에서 먼저 배우고, 검증하고, 현장에 적용합니다. 교육은 일회성 납품이 아니라 플랫폼 사업으로 축적됩니다.',29,500,MUTED,line=1.3),
    rect('a',100,430,232,116,'rgba(45,212,191,0.10)',ACC,1,22), txt('at',124,462,184,36,'현장 이해',29,800,ACC,'center'),
    line('l1',354,488,130,4,ACC), rect('b',506,430,232,116,'rgba(96,165,250,0.10)',BLUE,1,22), txt('bt',530,462,184,36,'시뮬레이션',29,800,BLUE,'center'),
    line('l2',760,488,130,4,BLUE), rect('c',912,430,232,116,'rgba(251,191,36,0.10)',AMBER,1,22), txt('ct',936,462,184,36,'현장 적용',29,800,AMBER,'center'),
    txt('aside',760,220,380,120,'PDF 근거: RwRP는 “실제 로봇 공정 그대로”의 디지털트윈 교육을 목표로 합니다.',28,700,FG,line=1.25)
],3,'v1 솔루션 흐름 유지 + v2 RwRP 정의를 보조 문장으로 통합.'))

# 4 portfolio from v1, less table-heavy
slides.append(slide('s4','Portfolio',[
    txt('k',96,68,600,32,'기술과 제품',22,800,ACC), txt('h',96,110,740,66,'One platform, four service routes',50,800),
    *product_card('rw',96,230,'RwRP','Robot with Real Programming','디지털트윈 기반 로봇교육 / 1인 1로봇',ACC),
    *product_card('cdr',376,230,'CDR','Custom-Designed Robot','현장 맞춤 로봇 SI / 공정 최적화',BLUE),
    *product_card('crc',656,230,'CRC','Customized Robot Café','F&B 자동화 / RMS / QR 주문결제',AMBER),
    *product_card('csr',936,230,'CSR','Customized Service Robot','AI 모바일 서비스로봇 / 방역 등 확장',FG),
    txt('bottom',146,552,990,42,'모든 제품과 서비스의 C는 Customized — 고객 현장 Needs를 가장 잘 이해하는 로봇 서비스 회사',28,700,ACC,'center')
],4,'v1 Products를 메인으로 유지하고 PDF 세부 정의만 정제해 반영.'))

# 5 RwRP as core technology, but not PDF-looking
slides.append(slide('s5','Core Technology',[
    txt('k',96,64,600,32,'핵심 기술',22,800,ACC), txt('h',96,106,860,70,'RwRP는 “로봇을 배우고 쓰는 방식”을 바꿉니다',48,800),
    rect('left',96,210,560,330), *bullet_block('r',132,248,500,['이기종·다수·다관절 로봇 직접 프로그래밍','실제 공정 그대로의 시뮬레이터 모델 사용','비주얼 노드 그래프 UI로 초보자 접근성 확보','고가 실습장비 없이 노트북 기반 실습 가능'],ACC,56,23),
    rect('proofbox',720,218,420,290,'rgba(255,255,255,0.052)',BORDER,1,24), txt('pt',752,250,356,34,'Sub proof',22,800,MUTED2,'center'),
    *metric('m1',758,300,'특허등록','10-2426456',ACC,164), *metric('m2',946,300,'N-Up','NVIDIA 협업',BLUE,164),
    txt('pd',760,448,350,38,'디지털트윈 → AI 로봇 모션플래닝으로 확장',24,700,AMBER,'center')
],5,'v2 기술 근거를 v1 스타일 proof box로 변환.'))

# 6 proof/history as sub narrative
slides.append(slide('s6','Why Now',[
    txt('k',96,64,600,32,'회사 히스토리는 메인 스토리의 증거입니다',22,800,ACC), txt('h',96,108,830,70,'검증된 팀이 이제 플랫폼 단계로 이동합니다',48,800),
    line('base',138,360,1000,4,BORDER),
    rect('y20',126,310,120,98,'rgba(255,255,255,0.06)',ACC,1,20), txt('y20t',142,326,88,26,'2020',23,800,ACC,'center'), txt('y20b',142,360,88,34,'법인 설립',16,500,MUTED,'center'),
    rect('y22',308,310,120,98,'rgba(255,255,255,0.06)',BLUE,1,20), txt('y22t',324,326,88,26,'2022',23,800,BLUE,'center'), txt('y22b',324,360,88,34,'교육 매출<br>5.8억',16,500,MUTED,'center'),
    rect('y23',490,310,120,98,'rgba(255,255,255,0.06)',AMBER,1,20), txt('y23t',506,326,88,26,'2023',23,800,AMBER,'center'), txt('y23b',506,360,88,34,'매출<br>10.3억',16,500,MUTED,'center'),
    rect('y24',672,310,120,98,'rgba(255,255,255,0.06)',BLUE,1,20), txt('y24t',688,326,88,26,'2024',23,800,BLUE,'center'), txt('y24b',688,360,88,34,'NVIDIA<br>N-Up',16,500,MUTED,'center'),
    rect('y25',854,310,120,98,'rgba(255,255,255,0.06)',ACC,1,20), txt('y25t',870,326,88,26,'2025',23,800,ACC,'center'), txt('y25b',870,360,88,34,'DIPS<br>선정',16,500,MUTED,'center'),
    rect('now',1018,288,150,142,'rgba(251,191,36,0.10)',AMBER,1,24), txt('nowt',1042,315,102,34,'Now',31,800,AMBER,'center'), txt('nowb',1040,366,106,40,'Series A<br>ready',18,600,FG,'center'),
    txt('caption',170,500,940,58,'히스토리는 독립된 자랑이 아니라, “시장 증명 → 글로벌/플랫폼 확장”으로 이어지는 신뢰 근거입니다.',30,700,FG,'center')
],6,'v2 회사 히스토리를 서브 proof slide로 재배치.'))

# 7 projects/use cases, v1 with proof
slides.append(slide('s7','Use Cases',[
    txt('k',96,64,600,32,'적용 사례',22,800,ACC), txt('h',96,108,820,66,'로봇 서비스는 공정과 매장으로 확장됩니다',48,800),
    rect('u1',96,230,500,92,'rgba(255,255,255,0.058)',ACC,1,22), txt('u1t',126,258,220,34,'교육 / RwRP',28,800,ACC), txt('u1b',360,258,190,38,'Pick & Place, 로봇카페, FMS 등',20,500,MUTED,'right'),
    rect('u2',684,230,500,92,'rgba(255,255,255,0.058)',BLUE,1,22), txt('u2t',714,258,220,34,'스마트팩토리',28,800,BLUE), txt('u2b',948,258,190,38,'출판·인쇄 자동화 / 제본 공정',20,500,MUTED,'right'),
    rect('u3',96,360,500,92,'rgba(255,255,255,0.058)',AMBER,1,22), txt('u3t',126,388,220,34,'F&B 자동화',28,800,AMBER), txt('u3b',360,388,190,38,'로봇카페 · 라면 · 생맥주',20,500,MUTED,'right'),
    rect('u4',684,360,500,92,'rgba(255,255,255,0.058)',FG,1,22), txt('u4t',714,388,220,34,'서비스 로봇',28,800,FG), txt('u4b',948,388,190,38,'모바일 / 방역 / 필드서비스',20,500,MUTED,'right'),
    rect('proof',200,530,880,70,'rgba(45,212,191,0.10)',ACC,1,22), txt('prooft',230,552,820,28,'F&B 사례: 아이스아메리카노 1잔 52초 → 24초 단축',26,800,ACC,'center')
],7,'v1 projects 느낌 + v2 F&B/공정 근거 통합.'))

# 8 business model coherent: education -> platform
slides.append(slide('s8','Business Model',[
    txt('k',96,64,600,32,'사업 모델',22,800,ACC), txt('h',96,108,900,66,'교육 콘텐츠는 플랫폼 사업으로 축적됩니다',48,800),
    rect('b1',112,246,270,160,'rgba(45,212,191,0.10)',ACC,1,26), txt('b1t',136,284,222,34,'교육 콘텐츠',30,800,ACC,'center'), txt('b1d',136,334,222,38,'직훈급 로봇교육<br>과정·교재 판매',20,500,MUTED,'center'),
    line('a1',410,322,110,4,ACC), rect('b2',548,246,270,160,'rgba(96,165,250,0.10)',BLUE,1,26), txt('b2t',572,284,222,34,'실습 환경',30,800,BLUE,'center'), txt('b2d',572,334,222,38,'디지털트윈 기반<br>1인 1로봇 실습',20,500,MUTED,'center'),
    line('a2',846,322,110,4,BLUE), rect('b3',984,246,170,160,'rgba(251,191,36,0.10)',AMBER,1,26), txt('b3t',1004,280,130,58,'공정거래<br>플랫폼',27,800,AMBER,'center'), txt('b3d',1000,350,138,34,'CoboticLAB',19,600,MUTED,'center'),
    *metric('mv',240,500,'5.6억','RwRP 누적매출(’22~’24)',ACC,240), *metric('gx',520,500,'12,000 Pax','동남아 교육 수요 추정',BLUE,240), *metric('rev',800,500,'12억대','온라인 교육 고정매출 예상',AMBER,240)
],8,'v2 사업모델 숫자를 v1 스타일 메트릭으로 보조화.'))

# 9 roadmap: compact chart, not table-heavy
slides.append(slide('s9','Roadmap',[
    txt('k',96,64,600,32,'성장 로드맵',22,800,ACC), txt('h',96,108,880,66,'시장 검증 이후, 매출 100억대로 가는 플랫폼 전환',46,800),
    {'id':'chart','type':'chart','x':96,'y':220,'w':600,'h':330,'rotation':0,'opacity':1,'preset':'bar','option':{'xAxis':{'type':'category','data':['2025','2026','2027']},'yAxis':{'type':'value'},'series':[{'type':'bar','data':[14.2,25.2,50.7],'itemStyle':{'color':ACC},'barWidth':72}],'tooltip':{'trigger':'item','formatter':'{b}: {c}억원'}},'fx':{'enter':'fade-up'}},
    rect('rbox',760,232,380,290,'rgba(255,255,255,0.058)',BORDER,1,24), txt('rt',792,266,316,34,'성장 축',28,800,ACC,'center'),
    *bullet_block('rb',800,326,300,['교육 RwRP set 확대','F&B 시스템 커스터마이징','모바일 서비스로봇 확장','로봇공정공유플랫폼 가동'],ACC,45,20),
    txt('cap',120,575,560,30,'PDF 계획: 2025 14.2억 → 2026 25.2억 → 2027 50.7억',22,600,MUTED,'center')
],9,'v2 매출계획을 하나의 깨끗한 차트로 압축.'))

# 10 ask/next step, consistent with v1 final
slides.append(slide('s10','Next Step',[
    img('logo',86,66,220,82,'ci'),
    txt('k',96,166,600,32,'Next Step',22,800,ACC),
    txt('h',96,210,850,112,'CDR은 로봇 사용의 시대를 위한<br>서비스 플랫폼을 만듭니다',52,800,line=1.08),
    txt('body',100,360,790,82,'필요한 것은 더 많은 로봇 제조가 아니라, 더 많은 현장이 로봇을 쉽게 배우고 적용하고 개선할 수 있는 체계입니다.',29,500,MUTED,line=1.28),
    rect('ask',96,500,1088,92,'rgba(96,165,250,0.10)',BLUE,1,24), txt('askt',130,527,1000,36,'투자 계획: 신규 20억원 · SI 파트너 10억 + VC Series A 10억 · Pre 150억원',29,800,FG,'center'),
    txt('contact',130,612,700,28,'contact@cdrsystem.com · www.cdrsystem.com',21,600,MUTED2)
],10,'마무리는 v1 Next Step 톤 유지 + v2 투자계획을 한 줄로 정리.'))

doc={'format':'bento/slides','version':1,'title':'CDR System IR v3 — Consistent Story','size':{'width':W,'height':H},'theme':{'background':BG,'color':FG,'accent':ACC,'fontFamily':FONT},'assets':assets,'slides':slides,'metadata':{'source':['https://www.cdrsystem.com/','IR_CDR System.pdf','2025년 CDR System 소개 자료.pdf'],'status':'draft-v3-consistent-story','strategy':'v1 homepage narrative as main; v2 company history/proof as supporting evidence','designReference':'Adham Dannaway UI Design Tips applied: hierarchy, spacing, contrast, purposeful color, consistency, readable alignment/fonts'}}
raw=json.dumps(doc,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
new_html=html[:m.start(1)] + m.group(1)+'\n'+raw+'\n'+m.group(3)+html[m.end(3):]
OUT.write_text(new_html,encoding='utf-8')
LOCAL.write_text(new_html,encoding='utf-8')
print('wrote', OUT)
print('local', LOCAL)
print('slides', len(slides), 'assets', len(assets), 'bytes', OUT.stat().st_size)
print('sha256', hashlib.sha256(OUT.read_bytes()).hexdigest())
