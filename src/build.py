s=open('orig.html',encoding='utf8').read()
old='family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&family=STIX+Two+Text:ital,wght@0,400;1,400'
new='family=IBM+Plex+Sans+Condensed:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500&family=JetBrains+Mono:wght@400;500;600&family=STIX+Two+Text:ital,wght@0,400;1,400'
assert s.count(old)==1; s=s.replace(old,new)
anchor='\n</style>\n\n<div class="wrap">'
assert s.count(anchor)==1
s=s.replace(anchor,'\n'+open('layer.css',encoding='utf8').read().rstrip()+anchor)
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
end='\n</script>\n\n</body></html>'
assert s.rstrip().endswith(end.strip()) and s.count(end)==1
s=s.replace(end,'\n'+open('motion.js',encoding='utf8').read().rstrip()+end)
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
o="i.style.width=Math.max(0,b.offsetWidth-2*ins)+'px';i.style.transform='translate('+(b.offsetLeft+ins)+'px,'+(b.offsetTop+b.offsetHeight-2)+'px)';"
assert s.count(o)==1
s=s.replace(o,"i.style.transform='translate('+(b.offsetLeft+ins)+'px,'+(b.offsetTop+b.offsetHeight-2)+'px) scaleX('+(Math.max(0,b.offsetWidth-2*ins)/100)+')';")
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
b='<button type="button" role="radio" data-th="eq">Law Lab</button>'
assert s.count(b)==1
s=s.replace(b,b+'<button type="button" role="radio" data-th="cx">Calc Lab</button>')
a='</section>\n<section class="sandbox"'
assert s.count(a)==1
s=s.replace(a,'</section>\n<section class="panel cxmp" id="cxMini" aria-label="Calc Lab mini views"><div class="vh"><h2>Mini views</h2></div><div class="mgrid" id="cxMg"></div></section>\n<section class="sandbox"')
o="MONO='\"IBM Plex Mono\",ui-monospace,monospace'"
assert s.count(o)==1
s=s.replace(o,"MONO='\"JetBrains Mono\",\"IBM Plex Mono\",ui-monospace,monospace'")
o="ta=st.alg==='fl'||"
assert s.count(o)==1
s=s.replace(o,"ta=st.alg==='fl'||st.alg==='cx'||")
import os
parts=[f for f in ['cx0.js','cx1.js','cx2.js','cx3.js','cx4.js','cx5.js','cx6.js','cx7.js','cx8.js','cx9.js','cxs.js','cxg.js','cb.js','q.js','ux.js','qg.js','press.js','slice.js'] if os.path.exists(f)]
code='\n'.join(open(f,encoding='utf8').read().strip() for f in parts)
a='const IIC={el:null'
assert s.count(a)==1
s=s.replace(a,code+'\n'+a)
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
P=[("depthStencil:{format:'depth24plus',depthWriteEnabled:!!dw,depthCompare:'less-equal'}","depthStencil:{format:'depth24plus',depthWriteEnabled:dw==='x'?false:!!dw,depthCompare:dw==='x'?'always':'less-equal'}"),
("dw=m.depthWrite!==false,","dw=m.depthTest===false?'x':m.depthWrite!==false,"),
("draws.push({p:gPipe('psh',1,0,'add',false,'none')","draws.push({p:gPipe('psh',1,0,'add',m.depthTest===false?'x':false,'none')"),
("function placeProbe(cx,cy){if(!GL){return}","function placeProbe(cx,cy){if(!GL||st.alg==='cx'){return}"),
("$('full').addEventListener('click',()=>{const el=$('gl');if(document.fullscreenElement){document.exitFullscreen()}else if(el.requestFullscreen){el.requestFullscreen().catch(()=>el.classList.toggle('full'))}else{el.classList.toggle('full')}});",
"function fsSet(on){const el=$('gl');el.classList.toggle('full',on);document.documentElement.classList.toggle('fsl',on);dispatchEvent(new Event('resize'))}\n$('full').addEventListener('click',()=>{const el=$('gl');if(document.fullscreenElement){document.exitFullscreen()}else if(el.classList.contains('full')){fsSet(false)}else if(el.requestFullscreen){el.requestFullscreen().catch(()=>fsSet(true))}else{fsSet(true)}});\n{const x=document.createElement('button');x.type='button';x.id='fsX';x.className='fsx';x.setAttribute('aria-label','Leave full screen');x.title='Leave full screen (Esc)';x.innerHTML='<svg viewBox=\"0 0 16 16\" aria-hidden=\"true\"><path d=\"M6 2.5V6H2.5M10 2.5V6h3.5M13.5 10H10v3.5M2.5 10H6v3.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.6\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/></svg>';for(const t of ['pointerdown','pointerup','pointermove']){x.addEventListener(t,ev=>ev.stopPropagation())}x.addEventListener('click',ev=>{ev.stopPropagation();if(document.fullscreenElement){document.exitFullscreen()}fsSet(false)});$('gl').appendChild(x);addEventListener('keydown',ev=>{if(ev.key==='Escape'&&$('gl').classList.contains('full')){fsSet(false)}});const f=$('full'),r=$('state')&&$('state').closest('.row');if(f&&r){r.appendChild(f);f.classList.add('fsb')}}")]
for a,b in P:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
a="if(xl){EQLB.push([g,xl,x0+w-2,y0+h-4,'right'])}if(yl){EQLB.push([g,yl,x0+4,y0+12,'left'])}"
assert s.count(a)==1
s=s.replace(a,"if(xl){EQLB.push([g,xl,x0+w-3,y0+h-4,'right'])}if(yl){EQLB.push([g,yl,x0+3,y0+11,'left'])}")
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
for a,c in [("f=110*Math.pow(2,3*clamp((v-lo)/den,0,1))","f=196*Math.pow(2,2.5*clamp((v-lo)/den,0,1))"),("SND.g.gain.setTargetAtTime(on?.05*APP.vol:0,t,.15)","SND.g.gain.setTargetAtTime(on?.12*APP.vol:0,t,.15)"),("f.type='lowpass';f.frequency.value=1500;","f.type='lowpass';f.frequency.value=2600;")]:
    assert s.count(a)==1,a
    s=s.replace(a,c)
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
a="}}const on=f>0&&st.play&&!document.hidden;"
assert s.count(a)==1
s=s.replace(a,"}}if(!f){const E=ENG[st.alg];let x=null;try{x=E&&E.sndv?E.sndv():null}catch(e){x=null}if(x===null||!isFinite(x)){x=.5+.5*Math.sin((RT.clk||0)*.6)}f=196*Math.pow(2,2.5*clamp(x,0,1))}const on=f>0&&st.play&&!document.hidden;")
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
QDEF="const QLV={potato:0,low:1,med:2,high:3,ultra:4,max:5},QG={p:(()=>{try{return (JSON.parse(localStorage.getItem('bitwistor-app')||'{}')||{}).perf||'auto'}catch(e){return 'auto'}})()};function qLv(){const v=QLV[QG.p];return v===undefined?(small?1:3):v}function QS(a,b){const L=qLv(),v=L===0?a*.6:L===1?a:L===2?(a+b)/2:L===3?b:L===4?b*1.5:b*2;return Number.isInteger(a)&&Number.isInteger(b)?Math.max(1,Math.round(v)):v}function QN(a,b){const L=qLv();return L<=1?a:L===2?Math.round((a+b)/2):b}function qMf(){return QG.p in QLV?[.55,.75,.9,1,1.5,2][QLV[QG.p]]:1}function QR(n){return Math.max(8,Math.round(n*qMf()))}function qDpr(){const d=Math.max(1,window.devicePixelRatio||1);return QG.p in QLV?[1,1,Math.min(1.5,d),Math.min(2,d),Math.min(3,Math.max(2,d*1.5)),Math.min(4,Math.max(3,d*2))][QLV[QG.p]]:Math.min(2,d)}function qGpr(g){const d=Math.max(1,window.devicePixelRatio||1);return QG.p in QLV?[.75,1,Math.min(1.5,d),Math.min(2,d),Math.min(3,Math.max(2,d*1.5)),Math.min(4,Math.max(3,d*2))][QLV[QG.p]]:Math.min(g?2:small?1.5:2,d)}"
P=[("small=Math.min(screen.width||800,innerWidth||800)<700;","small=Math.min(screen.width||800,innerWidth||800)<700;"+QDEF),
("dpr=Math.min(2,devicePixelRatio||1),W=M","dpr=qGpr(1),W=M"),
("Math.min(2,devicePixelRatio||1,Math.sqrt(","Math.min(qDpr(),Math.sqrt("),
("return P?Math.min(P.pr,d):Math.min(small?1.5:2,d)}","return qGpr(0)}"),
("function perfSet(v){APP.perf=v;","function perfSet(v){APP.perf=v;QG.p=v;"),
("toast('Performance: '+({auto:'automatic',low:'low',med:'medium',high:'high'})[v])","toast('Quality: '+({auto:'automatic',potato:'potato',low:'low',med:'medium',high:'high',ultra:'ultra',max:'maximum'})[v])"),
("seg('perf',[['auto','auto'],['low','low'],['med','medium'],['high','high']])","seg('perf',[['auto','auto'],['potato','potato'],['low','low'],['med','medium'],['high','high'],['ultra','ultra'],['max','max']])"),
("<span>Performance</span>","<span>Quality</span>"),
("const PERFV={low:","const PERFV={potato:{q:'0',pr:.75,n:24,nc:12,sg:32,qL:8,gm:2},ultra:{q:'3',pr:3,n:80,nc:32,sg:96,qL:24,gm:32},max:{q:'4',pr:4,n:96,nc:40,sg:96,qL:32,gm:64},low:"),
("high:'Full particle counts, 64³ lattices, sharp pixels on high-density screens.'}","high:'Full particle counts, 64³ lattices, sharp pixels on high-density screens.',potato:'Fastest possible: coarse grids and meshes, ¾× pixels in 3D, fewest particles. For very weak devices.',ultra:'Smoothest picture: up to 3× supersampled pixels, 1.5× finer grids, meshes and images, 80³ lattices. Needs a strong GPU.',max:'Best possible picture: up to 4× supersampled pixels, 2× finer grids, meshes and images, 96³ lattices, the most particles and field lines. For 2K and 4K screens on fast devices.'}"),
("function eqCap(k){const p=typeof APP!=='undefined'?APP.perf:'auto',lo=p==='low',md=p==='med'||p==='auto'&&small;return k==='g'?(lo?96:md?128:256):k==='n'?(lo?150:md?260:500):k==='m'?(lo?64:md?96:160):k==='c'?(lo?16:md?32:64):1}","function eqCap(k){const L=QG.p in QLV?QLV[QG.p]:small?2:3;return k==='g'?[64,96,128,256,320,400][L]:k==='n'?[100,150,260,500,800,1100][L]:k==='m'?[48,64,96,160,224,288][L]:k==='c'?[12,16,32,64,96,128][L]:1}"),
("function flCap(){const p=typeof APP!=='undefined'?APP.perf:'auto',lo=p==='low',md=p==='med'||p==='auto'&&small;return lo?160:md?224:320}","function flCap(){const L=QG.p in QLV?QLV[QG.p]:small?2:3;return [128,160,224,320,448,576][L]}"),
("(small?56:96)","QS(56,96)"),("(small?64:112)","QS(64,112)"),("small?1200:2400","QS(1200,2400)"),("(small?200:320)","QS(200,320)"),("N=small?3600:6000","N=QS(3600,6000)"),("fib(small?1100:1900)","fib(QS(1100,1900))"),("nC=small?380:620","nC=QS(380,620)"),("bud=small?7:11","bud=QS(7,11)"),("parts:small?650:1100","parts:QS(650,1100)"),("nlines:small?6:9","nlines:QS(6,9)"),
('aria-label="App settings: theme, text size, performance, tour"','aria-label="App settings: theme, text size, quality, tour"')]
for a,b in P:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
for a,b in [("VV('gmd',small?1.5:2)","VV('gmd',QS(1.5,2))"),("(small?.34:.5)","QS(.34,.5)")]:
    assert s.count(a)==2,a
    s=s.replace(a,b)
s=s.replace("Math.min(2,window.devicePixelRatio||1)","qDpr()").replace("Math.min(2,devicePixelRatio||1)","qDpr()")
a="const g=cv.getContext('2d');g.setTransform(d,0,0,d,0,0);return {g,w,h}}"
assert s.count(a)==1
s=s.replace(a,"const g=cv.getContext('2d');g.setTransform(d,0,0,d,0,0);g.imageSmoothingQuality=qLv()>=3?'high':'low';return {g,w,h}}")
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
a="['#appSet','App settings','Theme, text size, performance, sound, the glossary (G), an offline copy and this tour live here.']"
assert s.count(a)==1
s=s.replace(a,"['#qBtn','Quality','Pick how smooth the pictures are, from Potato (fastest) to Ultra (supersampled pixels and finer grids). Auto adapts to your device.'],['#appSet','App settings','Theme, text size, quality, sound, the glossary (G), an offline copy and this tour live here.']")
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
P=[("small=Math.min(screen.width||800,innerWidth||800)<700;","small=Math.min(screen.width||800,innerWidth||800)<700;function lbW(k){const b=Math.max(-2,Math.min(2,(typeof st!=='undefined'&&st&&st.lb)||0))/2;return k?(b<0?1+b:1):(b>0?1-b:1)}"),
("beta:0,lr:1,spd:1","beta:0,lr:1,lb:0,spd:1"),
("add(F[0],F[1],th*(1-lr)/2);add(F[2],F[3],th*(1+lr)/2)","add(F[0],F[1],Array.isArray(lr)?th*(lr[0]-lr[1])/2:th*(1-lr)/2);add(F[2],F[3],Array.isArray(lr)?th*(lr[0]+lr[1])/2:th*(1+lr)/2)"),
("rot4(u4,th*DEG,st.lr)}al=uq(rotU(th/720));be=uq(rotU(st.lr*th/720))","rot4(u4,th*DEG,[lbW(0),lbW(1)])}al=uq(rotU(lbW(0)*th/720));be=uq(rotU(lbW(1)*th/720))"),
("setT('ta1',f.th.toFixed(1)+'° ('+(st.lr*f.th).toFixed(1)+'°)')","setT('ta1',(lbW(0)*f.th).toFixed(1)+'° ('+(lbW(1)*f.th).toFixed(1)+'°)')"),
("Math.abs(st.lr-1)<1e-6?'yes: an ordinary 3D rotation'","Math.abs(st.lb||0)<1e-6?'yes: an ordinary 3D rotation'"),
("Math.abs(v-360)<6&&Math.abs(st.lr-1)<1e-6","Math.abs(v-360)<6&&Math.abs(st.lb||0)<1e-6"),
("$('lr').value=String(st.lr);$('lrOut').textContent=st.lr.toFixed(2);","$('lr').value=String(st.lb||0);$('lrOut').textContent=lbF();"),
("$('lr').addEventListener('input',e=>{st.lr=+e.target.value;$('lrOut').textContent=st.lr.toFixed(2);","function lbF(){const b=st.lb||0;return Math.abs(b)<.005?'0.00':(b>0?'+':'−')+Math.abs(b).toFixed(2)}\n$('lr').addEventListener('input',e=>{st.lb=+e.target.value;$('lrOut').textContent=lbF();"),
('<span class="lb">right ÷ left</span><input id="lr" type="range" min="-2" max="2" step="0.05" value="1"><output id="lrOut" for="lr">1.00</output>','<span class="lb">left ↔ right</span><input id="lr" type="range" min="-2" max="2" step="0.05" value="0"><output id="lrOut" for="lr">0.00</output>'),
("lr:'right ÷ left'","lr:'left ↔ right'"),
("lr:'Right ÷ left: a 4D rotation splits into a left and a right isoclinic part (SO(4) ≅ SU(2)×SU(2)/ℤ₂). 1 gives an ordinary rotation of ℝ³, −1 its mirror twin, 0 a pure left Hopf rotation.|ratio of the two angles'","lr:'Left ↔ right balance: a 4D rotation splits into a left and a right isoclinic part (SO(4) ≅ SU(2)×SU(2)/ℤ₂). 0 runs both equally, an ordinary rotation of ℝ³. Sliding right weakens the left part, sliding left weakens the right part; at ±2 that side is off, a pure Hopf rotation.|balance of the two parts'")]
for a,b in P:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
assert s.count("C.lr=0")==5
s=s.replace("C.lr=0","C.lb=-2")
open('Field_Lab.html','w',encoding='utf8').write(s)

s=open('Field_Lab.html',encoding='utf8').read()
P=[("const B=svBasis(),E=st.vw.sz,W=Math.min(200,Math.round(w/2)),H=Math.max(2,Math.round(W*h/w)),N=LT.N,hh=LT.h,off=LT.soff","const B=svBasis(),E=st.vw.sz,W=latSlW(w),H=Math.max(2,Math.round(W*h/w)),N=LT.N,hh=LT.h,off=LT.soff"),
("p=[0,1,2].map(k=>B.c[k]+u*B.a[k]+vv*B.b[k]),ix=p.map(x=>Math.round(x/hh+N/2-.5)),k4=(j*W+i)*4;if(ix.some(q=>q<0||q>=N)){D[k4]=6;D[k4+1]=8;D[k4+2]=12;D[k4+3]=255;continue}const s=ix[0]+N*(ix[1]+N*ix[2]),a=Math.min(1,Math.sqrt(V[4*s+3])*.9);D[k4]=V[4*s]*a*255;D[k4+1]=V[4*s+1]*a*255;D[k4+2]=V[4*s+2]*a*255;D[k4+3]=255}}",
 "p=[0,1,2].map(k=>(B.c[k]+u*B.a[k]+vv*B.b[k])/hh+N/2-.5),k4=(j*W+i)*4;if(p.some(q=>q<-.5||q>N-.5)){D[k4]=6;D[k4+1]=8;D[k4+2]=12;D[k4+3]=255;continue}const q=latTri(V,N,p),a=Math.min(1,Math.sqrt(Math.max(0,q[3]))*.9);D[k4]=q[0]*a*255;D[k4+1]=q[1]*a*255;D[k4+2]=q[2]*a*255;D[k4+3]=255}}"),
("const {g,w,h}=F,W=Math.min(200,Math.round(w/2)),H=Math.max(2,Math.min(400,Math.round(W*h/w)));LA.slReq={W,H};","const {g,w,h}=F,W=latSlW(w),H=Math.max(2,Math.min(2*W,Math.round(W*h/w)));LA.slReq={W,H};"),
("LA.SO=d.createBuffer({size:200*400*4,","LA.SO=d.createBuffer({size:560*1120*4,"),
("LA.SRB=d.createBuffer({size:200*400*4,","LA.SRB=d.createBuffer({size:560*1120*4,"),
("let ix=vec3i(round(p/hh+vec3f(f32(N)*.5-.5)));\n  var o=vec4f(6./255.,8./255.,12./255.,1.);if(all(ix>=vec3i(0))&&all(ix<vec3i(N))){let q=textureLoad(vT,ix,0);",
 "let f=p/hh+vec3f(f32(N)*.5-.5);let i0=vec3i(floor(f));let t=f-floor(f);\n  var o=vec4f(6./255.,8./255.,12./255.,1.);if(all(f>=vec3f(-.5))&&all(f<=vec3f(f32(N)-.5))){var q=vec4f(0.);for(var k=0;k<8;k++){let d=vec3i(k&1,(k>>1)&1,(k>>2)&1);let ii=clamp(i0+d,vec3i(0),vec3i(N-1));let w=select(1.-t.x,t.x,d.x==1)*select(1.-t.y,t.y,d.y==1)*select(1.-t.z,t.z,d.z==1);q+=w*textureLoad(vT,ii,0);}")]
for a,b in P:
    assert s.count(a)==1,a[:70]
    s=s.replace(a,b)
open('Field_Lab.html','w',encoding='utf8').write(s)

import ds,re
s=open('Field_Lab.html',encoding='utf8').read()
CMDEF="const CB={f:0,cur:0,r:null};const CMAP={k:(()=>{try{return (JSON.parse(localStorage.getItem('bitwistor-app')||'{}')||{}).cmap||'viridis'}catch(e){return 'viridis'}})()},CMS={viridis:[[.267,.004,.329],[.278,.176,.482],[.231,.322,.545],[.173,.447,.557],[.129,.569,.549],[.157,.682,.502],[.369,.788,.384],[.678,.863,.188],[.992,.906,.145]],cividis:[[0,.133,.306],[.122,.227,.431],[.294,.31,.424],[.42,.42,.439],[.541,.522,.471],[.675,.635,.467],[.812,.753,.42],[.941,.871,.361],[.996,.91,.22]],classic:[[.2,.1,.45],[.1,.45,.95],[.15,.85,.65],[.95,.8,.2],[.9,.2,.15]],cycRGB:[[244,146,138],[220,166,81],[155,192,106],[67,202,179],[83,191,239],[165,167,251],[223,148,209],[244,146,138]]};const CK=(()=>{let cs=null;try{cs=getComputedStyle(document.documentElement)}catch(e){cs=null}const tk=(n,d)=>{const v=cs?cs.getPropertyValue(n).trim():'';return v||d},rgb=h=>[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)).join(','),fg=tk('--dk-fg','#dfe3e8'),M={},F=rgb(fg);return {fg,dim:tk('--dk-dim','#a8b1bb'),faint:tk('--dk-faint','#8d97a2'),bg:tk('--dk-bg','#0d1013'),ax:['x','y','z','w'].map((n,i)=>tk('--dk-ax-'+n,['#ff6b6b','#7dff8a','#6bb8ff','#c9a6ff'][i])),pos:tk('--dk-pos','#ff6a5c'),neg:tk('--dk-neg','#62a6ff'),i:a=>M[a]||(M[a]='rgba('+F+','+a+')')}})();"
a="const QLV={potato:0"
assert s.count(a)==1
s=s.replace(a,CMDEF+a)
P=[("else{S=[[.2,.1,.45],[.1,.45,.95],[.15,.85,.65],[.95,.8,.2],[.9,.2,.15]]}","else{S=CMS[CMAP.k]||CMS.classic}"),
("if(PALK==='rainbow'){return hsl(h,.92,l)}const S=PALRGB[PALK],cyc=PALK==='aurora'||PALK==='neon';","const uni=PALK==='rainbow'&&CMAP.k!=='classic';if(PALK==='rainbow'&&!uni){return hsl(h,.92,l)}const S=uni?CMS.cycRGB:PALRGB[PALK],cyc=uni||PALK==='aurora'||PALK==='neon';"),
("s(I.COL,cm,RT.bHue,pal?pal.length:0,PALK==='aurora'||PALK==='neon'?1:0)","s(I.COL,cm,RT.bHue,pal?Math.min(8,pal.length):0,PALK==='aurora'||PALK==='neon'||PALK==='rainbow'?1:0)"),
("a[1]=PALK==='aurora'||PALK==='neon'?1:0;","a[1]=PALK==='aurora'||PALK==='neon'||PALK==='rainbow'?1:0;"),
("if(mode==='energy'){return pcol(250-250*e,.55)}","if(mode==='energy'){if(CMAP.k==='classic'){return pcol(250-250*e,.55)}const o=eqCm(null,clamp(e,0,1),[0,0,0]);return [o[0]*255,o[1]*255,o[2]*255]}"),
("const APP=Object.assign({theme:'dark',ts:'m',perf:'auto'}","const APP=Object.assign({theme:'dark',ts:'m',perf:'auto',cmap:'viridis'}"),
("'WebGL'+(GPU.st==='fail'||GPU.st==='lost'?' (WebGPU '+(GPU.st==='lost'?'lost':'unavailable')+')':'');if(el.textContent!==t){el.textContent=t}","'WebGL'+(GPU.st==='fail'?' (no WebGPU in this browser)':GPU.st==='lost'?' (WebGPU stopped)':'');if(el.textContent!==t){el.textContent=t;el.title=GPU.on?'Drawing with WebGPU':GPU.st==='fail'?'This browser has no WebGPU, so Field Lab draws with WebGL. Current Chrome and Edge include WebGPU.':GPU.st==='lost'?'WebGPU stopped responding, so Field Lab switched to WebGL. Reload the page to try WebGPU again.':'Drawing with WebGL'}"),
("class=\"chip\" data-ax=\"w\" id=\"axW\" aria-pressed=\"false\" style=\"color:#c9a6ff\"","class=\"chip dtx\" data-ax=\"w\" id=\"axW\" aria-pressed=\"false\" style=\"--c:var(--dk-ax-w)\""),
("<span class=\"lb\" style=\"color:#ff6b6b\">","<span class=\"lb dtx\" style=\"--c:var(--dk-ax-x)\">"),
("<span class=\"lb\" style=\"color:#7dff8a\">","<span class=\"lb dtx\" style=\"--c:var(--dk-ax-y)\">"),
("<span class=\"lb\" style=\"color:#6bb8ff\">","<span class=\"lb dtx\" style=\"--c:var(--dk-ax-z)\">"),
("<span class=\"lb\" style=\"color:#c9a6ff\">","<span class=\"lb dtx\" style=\"--c:var(--dk-ax-w)\">"),
("<span style=\"color:'+AXC[PLN[k][0]]+'\">","<span class=\"dtx\" style=\"--c:'+AXC[PLN[k][0]]+'\">"),
("<span style=\"color:'+AXC[PLN[k][1]]+'\">","<span class=\"dtx\" style=\"--c:'+AXC[PLN[k][1]]+'\">"),
("if(col){d.style.color=col}el.appendChild(d)","if(col){d.style.setProperty('--c',col);d.classList.add('dtx')}el.appendChild(d)"),
("<td class=\"ups\" style=\"color:'+unCss(o)+'\">","<td class=\"ups dtx\" style=\"--c:'+unCss(o)+'\">"),
("el.style.color=t?'#ff7a6b':''","el.style.color=t?'var(--bad)':''"),
("opts:[['rainbow','rainbow'],['plasma'","opts:[['rainbow','cyclic'],['plasma'"),
("<html>","<html lang=\"en\">"),
("m2.forEach((v,k)=>{const st8=2*Math.PI/m2.length","const RLB=[];m2.forEach((v,k)=>{const st8=2*Math.PI/m2.length"),
("R=Math.max(10,Math.min(w,h)/2-(nn>8?13:18))","R=Math.max(10,Math.min(w,h)/2-(nn>8?22:20))"),
("if(nn<=8||pc>=4){g.fillStyle=CC8(k);g.font=(nn>8?'9px ':'10px ')+UI;g.textAlign='center';g.fillText(pc+'%',clamp(cx+Math.cos(am)*(R+9),13,w-13),clamp(cy+Math.sin(am)*(R+9)+3,10,h-3))}});","if(nn<=8||pc>=4){RLB.push([pc,am,k])}});g.font='11px '+UI;g.textAlign='center';const RPB=[];RLB.sort((p,q)=>q[0]-p[0]);for(const [pc,am,k] of RLB){const t=pc+'%',tw=g.measureText(t).width/2+2;for(const d of [10,21]){const x=clamp(cx+Math.cos(am)*(R+d),tw+1,w-tw-1),y=clamp(cy+Math.sin(am)*(R+d)+4,12,h-3);if(!RPB.some(q=>Math.abs(q[0]-x)<q[2]+tw&&Math.abs(q[1]-y)<12)){RPB.push([x,y,tw]);g.fillStyle=CC8(k);g.fillText(t,x,y);break}}}"),
("cs=Math.min((w-40)/3/4.4,(h-34)/4)","cs=Math.min((w-40)/3/4.4,(h-58)/4)"),
("for(let fs=12;fs>7&&g.measureText(ct).width>w-16;fs--)","for(let fs=12;fs>11&&g.measureText(ct).width>w-16;fs--)"),
("#cmc{display:block;width:calc(100% - 24px);margin:0 12px 12px;height:132px","#cmc{display:block;width:calc(100% - 24px);margin:0 12px 12px;height:152px"),
("g.fillText(ct,10,h-6)}","g.fillText(ct,10,Math.min(h-8,30+4*cs+22))}"),
("const AXC=['#ff6b6b','#7dff8a','#6bb8ff','#c9a6ff']","const AXC=CK.ax"),
("COLS.cx=['#4fd8ff','#ff9a4a']","COLS.cx=[AXC[0],AXC[1]]"),
("c:ax?'#ff9a4a':'#4fd8ff'","c:ax?AXC[1]:AXC[0]"),
("S=[{n:pol?'F_r':'P',v:P,c:'#4fd8ff'},{n:pol?'F_θ':'Q',v:Q,c:'#ff9a4a'}","S=[{n:pol?'F_r':'P',v:P,c:AXC[0]},{n:pol?'F_θ':'Q',v:Q,c:AXC[1]}"),
("leg:[['#4fd8ff','x direction'],['#ff9a4a','y direction'],['#ffd166','gradient and flow'],['#ff6a5c','positive, maximum, outward'],['#62a6ff','negative, minimum, inward']]","leg:[[AXC[0],'x direction'],[AXC[1],'y direction'],['#ffd166','gradient and flow'],[CK.pos,'positive, maximum, outward'],[CK.neg,'negative, minimum, inward']]"),
("g.fillStyle=v>=0?'rgba(255,150,60,'+(.12+.88*a)+')':'rgba(70,150,255,'+(.12+.88*a)+')';","{const q=eqCm('div',clamp(v,-1,1),[0,0,0]);g.fillStyle='rgb('+(q[0]*255|0)+','+(q[1]*255|0)+','+(q[2]*255|0)+')'}"),
("const cxRGB=(t,o)=>eqCm(null,t,o||[0,0,0]),cxDiv=(t,o)=>eqCm('div',clamp(t,-1,1),o||[0,0,0]);","const cxRGB=(t,o)=>(CB.f|=1,eqCm(null,t,o||[0,0,0])),cxDiv=(t,o)=>(CB.f|=2,eqCm('div',clamp(t,-1,1),o||[0,0,0]));"),
("if(o.key===key&&o.cv.width===N&&o.cv.height===M){return o.cv}o.key=key;o.cv.width=N;o.cv.height=M;const x=o.cv.getContext('2d'),im=x.createImageData(N,M);fill(im.data,N,M);x.putImageData(im,0,0);return o.cv}","if(o.key===key&&o.cv.width===N&&o.cv.height===M){CB.cur|=o.cm||0;return o.cv}o.key=key;o.cv.width=N;o.cv.height=M;const x=o.cv.getContext('2d'),im=x.createImageData(N,M);CB.f=0;fill(im.data,N,M);o.cm=CB.f;CB.cur|=o.cm;x.putImageData(im,0,0);return o.cv}"),
("try{cxM().plane(g);if(cxPol()&&CXPOLV[st.cx.mode]){cxPolGrid(g,CXL.pg)}}","try{CB.cur=0;CB.r=null;CB.lb='';cxM().plane(g);if(cxPol()&&CXPOLV[st.cx.mode]){cxPolGrid(g,CXL.pg)}cbDraw(g,CXL.pg,WP,HP)}"),
("try{const md=st.cx.mode;if(cxSvv()==='cut'&&CXCUT[md]){CXCUT[md](g,w,h)}else{cxM().slice(g,w,h)}}","try{CB.cur=0;CB.r=null;CB.lb='';CB.g=null;const md=st.cx.mode;if(cxSvv()==='cut'&&CXCUT[md]){CXCUT[md](g,w,h)}else{cxM().slice(g,w,h)}cbDraw(g,CB.g||CXL.sg2,w,h)}"),
("function cxSurfHeat(S,N){const e=st.cx;","function cxSurfHeat(S,N){const e=st.cx;CB.r=e.cby==='h'?[S.lo,S.hi,'f(x, y)']:null;"),
("ix:px=>xa+(px-ox)/sc,iy:py=>yb-(py-oy)/sc,ox,oy,w:w*sc,h:h*sc});return G}","ix:px=>xa+(px-ox)/sc,iy:py=>yb-(py-oy)/sc,ox,oy,w:w*sc,h:h*sc});CB.g=G;return G}"),
("g.font='10px '+MONO;g.fillStyle='rgba(220,226,236,.55)';g.textAlign='center';for(const v of eqNice(G.xa,G.xb,4)){g.fillText(eqFmt(v),G.X(v),G.oy+G.h+11)}g.textAlign='right';for(const v of eqNice(G.ya,G.yb,4)){g.fillText(eqFmt(v),G.ox-3,G.Y(v)+3)}","g.font='11px '+UI;g.fillStyle='rgba(220,226,236,.6)';g.textAlign='center';{const A=eqNice(G.xa,G.xb,4),F=tkF(A);for(const v of A){g.fillText(F(v),G.X(v),G.oy+G.h+11)}}g.textAlign='right';{const A=eqNice(G.ya,G.yb,4),F=tkF(A);for(const v of A){g.fillText(F(v),G.ox-3,G.Y(v)+3)}}"),
("g.font='10px '+MONO;g.fillStyle='rgba(220,226,236,.55)';g.textAlign='center';const xt=F.dg[0]?[-180,-90,0,90,180].map(d=>[d*Math.PI/180,d+'°']):eqNice(G.xa,G.xb,4).map(v=>[v,eqFmt(v)]);","g.font='11px '+UI;g.fillStyle='rgba(220,226,236,.6)';g.textAlign='center';const xt=F.dg[0]?[-180,-90,0,90,180].map(d=>[d*Math.PI/180,(d<0?'−':'')+Math.abs(d)+'°']):(A=>A.map(v=>[v,tkF(A)(v)]))(eqNice(G.xa,G.xb,4));"),
("eqNice(G.ya,G.yb,4).map(v=>[v,eqFmt(v)]);for(const [v,t] of yt)","(A=>A.map(v=>[v,tkF(A)(v)]))(eqNice(G.ya,G.yb,4));for(const [v,t] of yt)"),
("g.lineTo(x,y0+h);g.stroke();const t=eqFmt(v),tw=g.measureText(t).width;","g.lineTo(x,y0+h);g.stroke();const t=tkF(eqNice(xr[0],xr[1],5))(v),tw=g.measureText(t).width;"),
("if(y>y0+5&&y<y0+h-5){g.fillText(eqFmt(v),x0-4,y","if(y>y0+5&&y<y0+h-5){g.fillText(tkF(eqNice(yr[0],yr[1],4))(v),x0-4,y"),
("d.textContent='The 3D view needs WebGL, which this browser did not start. The planes, telemetry, readouts and matrices below still work.'","d.textContent='The 3D view needs WebGL, which this browser did not start. Turn on hardware acceleration in the browser settings or try another browser. The planes, telemetry, readouts and matrices below still work.'"),
("fn colorFor(k:i32,f:F,e:f32)->vec3f{let m=U.v[L_COL].x;if(m==1.){return pcol(250.-250.*e,.55);}",'fn cm9(t0:f32,cv:bool)->vec3f{var a=array<vec3f,9>(vec3f(0.267,0.004,0.329),vec3f(0.278,0.176,0.482),vec3f(0.231,0.322,0.545),vec3f(0.173,0.447,0.557),vec3f(0.129,0.569,0.549),vec3f(0.157,0.682,0.502),vec3f(0.369,0.788,0.384),vec3f(0.678,0.863,0.188),vec3f(0.992,0.906,0.145));var b=array<vec3f,9>(vec3f(0,0.133,0.306),vec3f(0.122,0.227,0.431),vec3f(0.294,0.31,0.424),vec3f(0.42,0.42,0.439),vec3f(0.541,0.522,0.471),vec3f(0.675,0.635,0.467),vec3f(0.812,0.753,0.42),vec3f(0.941,0.871,0.361),vec3f(0.996,0.91,0.22));let x=clamp(t0,0.,1.)*8.;let i=min(7,i32(floor(x)));let f=x-f32(i);if(cv){return mix(b[i],b[i+1],f);}return mix(a[i],a[i+1],f);}\\n'+"fn colorFor(k:i32,f:F,e:f32)->vec3f{let m=U.v[L_COL].x;if(m>4.5){return cm9(e,m>5.5);}if(m==1.){return pcol(250.-250.*e,.55);}"),
("s(I.COL,cm,RT.bHue,pal?Math.min(8,pal.length):0,","s(I.COL,cm===1&&CMAP.k!=='classic'?(CMAP.k==='cividis'?6:5):cm,RT.bHue,pal?Math.min(8,pal.length):0,"),
("const L=[['x','#ff6b6b'],['y','#7dff8a'],['z','#6bb8ff'],['w','#c9a6ff']]","const L=[['x',CK.ax[0]],['y',CK.ax[1]],['z',CK.ax[2]],['w',CK.ax[3]]]"),
("g.lineWidth=1;g.font='10px '+MONO;g.fillStyle='rgba(220,226,236,.6)';const X=v=>x0+(v-xr[0])","g.lineWidth=1;g.font='11px '+UI;g.fillStyle='rgba(220,226,236,.6)';const X=v=>x0+(v-xr[0])"),
('style="--a:#ff6b6b"','style="--a:var(--dk-ax-x)"'),('style="--a:#7dff8a"','style="--a:var(--dk-ax-y)"'),('style="--a:#6bb8ff"','style="--a:var(--dk-ax-z)"'),('style="--a:#c9a6ff"','style="--a:var(--dk-ax-w)"'),
("g.lineWidth=1.8;for(const key in AB)","g.lineWidth=1.1;for(const key in AB)"),
("ex-Math.cos(a-.5)*4,ey+Math.sin(a-.5)*4,ex,ey,ex-Math.cos(a+.5)*4,ey+Math.sin(a+.5)*4","ex-Math.cos(a-.5)*3,ey+Math.sin(a-.5)*3,ex,ey,ex-Math.cos(a+.5)*3,ey+Math.sin(a+.5)*3"),
("g.moveTo(dots[i]+1.7,dots[i+1]);g.arc(dots[i],dots[i+1],1.7,0,7)","g.moveTo(dots[i]+1.2,dots[i+1]);g.arc(dots[i],dots[i+1],1.2,0,7)"),
("const x0=10+gi*(cs*4+14),y0=20;g.fillStyle='rgba(220,226,236,.8)';g.fillText(t,x0,13);","const x0=Math.max(10,(w-12*cs-28)/2)+gi*(cs*4+14),y0=30;g.fillStyle='rgba(220,226,236,.8)';g.fillText(t,x0,22);"),
("g.fillText(ct,10,Math.min(h-8,30+4*cs+22))}","g.textAlign='center';g.fillText(ct,w/2,Math.min(h-8,30+4*cs+22));g.textAlign='left'}"),
("placeholder='Settings text appears here; paste settings here to load them'","placeholder='Settings text appears here. Paste settings here to load them…'"),
("ph:'paste a share code or link here'","ph:'Paste a share code or link…'"),
("ph:'e.g. glimmeron'","ph:'e.g. glimmeron…'"),
("ph:'e.g. G̃'","ph:'e.g. G̃…'"),
("ex=cx+Math.cos(a)*L2,ey=cy-Math.sin(a)*L2","ex=cx+Math.cos(a)*L2*.675,ey=cy-Math.sin(a)*L2*.675"),
("(AB[key]=AB[key]||[]).push(cx-Math.cos(a)*L2*.35,cy+Math.sin(a)*L2*.35,","(AB[key]=AB[key]||[]).push(cx-Math.cos(a)*L2*.675,cy+Math.sin(a)*L2*.675,"),
('title="Download the data behind this chart as CSV">CSV</button>','title="Download the data behind this chart as CSV">Download CSV</button>'),
("h.style.color=c.col||'var(--fg)';","if(c.col){h.style.setProperty('--c',c.col);h.classList.add('dtx')}else{h.style.color='var(--fg)'}"),
("+'</div><div class=\"aprow\"><span>Quality</span>'","+'</div><div class=\"aprow\"><span>Colour maps</span>'+seg('cmap',[['viridis','viridis'],['cividis','cividis'],['classic','classic']])+'</div><div class=\"aprow\"><span>Quality</span>'")]
for x,y in P:
    assert s.count(x)>=1,x[:70]
    s=s.replace(x,y)
assert s.count("pal=PALK==='rainbow'?null:PALRGB[PALK];")==2
s=s.replace("pal=PALK==='rainbow'?null:PALRGB[PALK];","pal=PALK==='rainbow'?(CMAP.k==='classic'?null:CMS.cycRGB):PALRGB[PALK];")
m=list(re.finditer(r'<script>([\s\S]*?)</script>',s))
assert len(m)==1
js=m[0].group(1)
for lit in re.findall(r"'rgba\((?:220,226,236|255,255,255|232,236,242|214,222,236),(\.\d+|1|0\.\d+)\)'",js):
    pass
js=re.sub(r"'rgba\((?:220,226,236|255,255,255|232,236,242|214,222,236),((?:0?\.\d+)|1)\)'",lambda q:"CK.i("+q.group(1)+")",js)
js=js.replace("'#e8ecf2'","CK.fg").replace("'#cfd6e2'","CK.fg").replace("'#c8d0e0'","CK.fg").replace("'#7c86a0'","CK.faint").replace("'#070a10'","CK.bg").replace("'#04060a'","CK.bg")
js=re.sub(r"(\?|==='max'\?|>=0\?)'#ff6a5c':'#62a6ff'",lambda q:q.group(1)+"CK.pos:CK.neg",js)
js=js.replace("c[3]==='max'?'#ff6a5c':c[3]==='min'?'#62a6ff'","c[3]==='max'?CK.pos:c[3]==='min'?CK.neg")
js=re.sub(r"\['(∂f/∂[xyzw]|P|Q|R|S)',([^,']+?),'#(ff6b6b|7dff8a|6bb8ff|c9a6ff)'\]",lambda q:"['"+q.group(1)+"',"+q.group(2)+",AXC["+str(['ff6b6b','7dff8a','6bb8ff','c9a6ff'].index(q.group(3)))+"]]",js)
js=re.sub(r"c:'#(ff6b6b|7dff8a|6bb8ff|c9a6ff)'",lambda q:'c:AXC['+str(['ff6b6b','7dff8a','6bb8ff','c9a6ff'].index(q.group(1)))+']',js)
js=re.sub(r"(['\"])((?:\d00 |italic |bold )*)(9|9\.5|10|10\.5)px (['\"])",lambda q:q.group(1)+q.group(2)+"11px "+q.group(4),js)
s=s[:m[0].start(1)]+js+s[m[0].end(1):]
st=list(re.finditer(r'<style>([\s\S]*?)</style>',s))
big=max(st,key=lambda x:len(x.group(1)))
s=s[:big.start(1)]+ds.run(big.group(1),open('sys.css',encoding='utf8').read())+s[big.end(1):]
open('Field_Lab.html','w',encoding='utf8').write(s)

open('../dist/index.html','w',encoding='utf8').write(s)
