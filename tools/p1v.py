import asyncio,os,json,re,sys
from playwright.async_api import async_playwright
SRC=os.getcwd()+"/"+(sys.argv[1] if len(sys.argv)>1 else "Field_Lab.html")
CON="""(th)=>{const L=(()=>{const cv=document.createElement('canvas');cv.width=cv.height=1;const x=cv.getContext('2d',{willReadFrequently:true});const M={};return c=>{if(!c)return null;if(M[c])return M[c];x.clearRect(0,0,1,1);x.fillStyle='rgba(0,0,0,0)';x.fillStyle=c;x.fillRect(0,0,1,1);const d=x.getImageData(0,0,1,1).data;return M[c]={r:d[0],g:d[1],b:d[2],a:d[3]/255}}})();const lum=o=>{const f=v=>{v/=255;return v<=.04045?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(o.r)+.7152*f(o.g)+.0722*f(o.b)};
const bgOf=el=>{let e=el,stack=[];while(e&&e.nodeType===1){const c=L(getComputedStyle(e).backgroundColor);if(c&&c.a>0){stack.push(c);if(c.a>=.99)break}e=e.parentElement}let base={r:0,g:0,b:0};if(!e){base=L(getComputedStyle(document.body).backgroundColor)||base}for(let i=stack.length-1;i>=0;i--){const c=stack[i];base={r:c.r*c.a+base.r*(1-c.a),g:c.g*c.a+base.g*(1-c.a),b:c.b*c.a+base.b*(1-c.a)}}return base};
const out=[];const seen=new Set();for(const el of document.querySelectorAll('body *')){if(!el.offsetParent&&getComputedStyle(el).position!=='fixed')continue;if(el.closest('#gl,canvas,svg,.mgrid figure canvas'))continue;let own='';for(const n of el.childNodes){if(n.nodeType===3)own+=n.textContent}own=own.trim();if(!own)continue;const cs=getComputedStyle(el);if(cs.visibility==='hidden'||parseFloat(cs.opacity)<.5)continue;const r=el.getBoundingClientRect();if(r.width<2||r.height<2)continue;const fg=L(cs.color);if(!fg)continue;const bg=bgOf(el);const f2={r:fg.r*fg.a+bg.r*(1-fg.a),g:fg.g*fg.a+bg.g*(1-fg.a),b:fg.b*fg.a+bg.b*(1-fg.a)};const a=lum(f2),b=lum(bg);const cr=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);const fs=parseFloat(cs.fontSize),bold=parseInt(cs.fontWeight)>=600;const large=fs>=24||(fs>=18.66&&bold);const need=large?3:4.5;if(cr<need){const k=(el.id||el.className||el.tagName)+'|'+cs.color;if(seen.has(k))continue;seen.add(k);out.push({el:(el.tagName+'#'+el.id+'.'+String(el.className).slice(0,30)),txt:own.slice(0,30),cr:+cr.toFixed(2),fs})}}return out}"""
TGT="""()=>{const o={tot:0,lt24:[],hit44fail:0};for(const el of document.querySelectorAll('button,select,input,[role=tab],[role=radio],a[href],summary')){if(!el.offsetParent)continue;const r=el.getBoundingClientRect();if(r.width<1||r.height<1)continue;if(el.closest('#gl.full'))continue;o.tot++;if(Math.min(r.width,r.height)<23.5){o.lt24.push((el.id||String(el.className)||el.tagName).slice(0,20)+' '+Math.round(r.width)+'x'+Math.round(r.height))}}return o}"""
HIT="""()=>{let n=0,f=0,ex=[];for(const el of document.querySelectorAll('.icon,.chip,.act,.mode,.tab,.ib,.tpin,.seg button,.apseg button,#qBtn,#full')){if(!el.offsetParent)continue;const r=el.getBoundingClientRect();if(r.top<60||r.bottom>innerHeight-30)continue;const cx=r.left+r.width/2;n++;let ok=true;for(const dy of [-20,20]){const y=r.top+r.height/2+dy;const t=document.elementFromPoint(cx,y);if(!(t&&(t===el||el.contains(t)))){ok=false}}if(!ok){f++;if(ex.length<6)ex.push((el.id||el.className).slice(0,18)+' h'+Math.round(r.height))}}return {n,f,ex}}"""
async def run(b,w,h,dpr,mobile,theme):
    ctx=await b.new_context(viewport={"width":w,"height":h},device_scale_factor=dpr,is_mobile=mobile,has_touch=mobile)
    pg=await ctx.new_page();errs=[];pg.on("pageerror",lambda x:errs.append(str(x)[:150]))
    await pg.add_init_script("localStorage.setItem('bitwistor-tour','1');localStorage.setItem('bitwistor-app',JSON.stringify({theme:'%s'}))"%theme)
    await pg.goto("file://"+SRC);await pg.wait_for_timeout(2500)
    res={}
    for th in (os.environ.get('LABS') or 'tw,cx,eq').split(','):
        await pg.evaluate("document.querySelector('[data-th=%s]').click()"%th);await pg.wait_for_timeout(1500)
        c=await pg.evaluate(CON,theme);t=await pg.evaluate(TGT)
        res[th]={'contrast_fail':c[:8],'n_cf':len(c),'targets':t['tot'],'lt24':t['lt24'][:6],'n_lt24':len(t['lt24']),'hs':await pg.evaluate("document.documentElement.scrollWidth>innerWidth")}
        if mobile: res[th]['hit']=await pg.evaluate(HIT)
    res['errs']=errs[:3]
    await ctx.close();return res
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl"])
        for (w,h,dpr,mob) in [(390,844,2,True),(1440,900,1,False)]:
            for theme in ['dark','light']:
                r=await run(b,w,h,dpr,mob,theme)
                print(w,theme,json.dumps(r,ensure_ascii=False))
        await b.close()
asyncio.run(main())
