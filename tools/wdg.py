import asyncio,os,json,re,sys
from playwright.async_api import async_playwright
F=sys.argv[1] if len(sys.argv)>1 else 'Field_Lab.html'
J="""()=>{const o={};const vis=e=>e.offsetParent||getComputedStyle(e).position==='fixed';
o.iconNoLabel=[...document.querySelectorAll('button')].filter(b=>vis(b)&&!b.textContent.trim()&&!b.getAttribute('aria-label')&&!b.getAttribute('aria-labelledby')).map(b=>b.id||b.className).slice(0,8);
o.inputNoLabel=[...document.querySelectorAll('input,select,textarea')].filter(e=>vis(e)&&e.type!=='hidden'&&!e.labels?.length&&!e.getAttribute('aria-label')&&!e.getAttribute('aria-labelledby')&&!e.title).map(e=>e.id||e.className||e.type).slice(0,8);
o.imgNoDim=[...document.querySelectorAll('img')].filter(i=>!i.getAttribute('width')||!i.getAttribute('height')).length;
o.imgNoAlt=[...document.querySelectorAll('img:not([alt])')].length;
o.dots=[...document.querySelectorAll('body *')].filter(e=>vis(e)&&[...e.childNodes].some(n=>n.nodeType===3&&/\\.\\.\\./.test(n.textContent))).map(e=>e.textContent.trim().slice(0,40)).slice(0,6);
o.placeholders=[...document.querySelectorAll('[placeholder]')].map(e=>e.placeholder).filter(p=>p&&!/…$/.test(p)).slice(0,6);
o.textInputsNoAC=[...document.querySelectorAll('input[type=text],input[type=search],input:not([type])')].filter(e=>vis(e)&&!e.getAttribute('autocomplete')).map(e=>e.id||e.className).slice(0,6);
o.vp=document.querySelector('meta[name=viewport]')?.content;
o.cs=getComputedStyle(document.documentElement).colorScheme;o.tc=document.querySelector('meta[name=theme-color]')?.content;o.bg=getComputedStyle(document.body).backgroundColor;
o.live=[...document.querySelectorAll('[aria-live],[role=status],[role=alert]')].map(e=>e.id||e.className).slice(0,10);
o.toast=[...document.querySelectorAll('.toast')].map(t=>t.getAttribute('aria-live')||t.getAttribute('role')||'none');
const H=[...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(vis).map(h=>+h.tagName[1]);let skip=0;for(let i=1;i<H.length;i++){if(H[i]>H[i-1]+1){skip++}}o.headings={n:H.length,h1:H.filter(x=>x===1).length,skips:skip};
o.selectBg=[...document.querySelectorAll('select')].filter(vis).slice(0,1).map(s=>getComputedStyle(s).backgroundColor+' / '+getComputedStyle(s).color);
o.clickDivs=[...document.querySelectorAll('div[onclick],span[onclick]')].length;
o.tapHl=getComputedStyle(document.documentElement).webkitTapHighlightColor;
o.touchAction=[...document.querySelectorAll('button')].filter(vis).slice(0,1).map(b=>getComputedStyle(b).touchAction);
o.skip=!!document.getElementById('skipC');o.main=!!document.querySelector('main,[role=main]');o.lang=document.documentElement.lang;
return o}"""
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl"])
        pg=await b.new_page(viewport={"width":390,"height":844})
        await pg.add_init_script("localStorage.setItem('bitwistor-tour','1')")
        await pg.goto("file://"+os.getcwd()+"/"+F);await pg.wait_for_timeout(2500)
        R={}
        for th in ['tw','cx','eq','fl','un']:
            await pg.evaluate("document.querySelector('[data-th=%s]').click()"%th);await pg.wait_for_timeout(1200)
            R[th]=await pg.evaluate(J)
        print(json.dumps(R,ensure_ascii=False,indent=0)[:6000])
        await b.close()
asyncio.run(m())
