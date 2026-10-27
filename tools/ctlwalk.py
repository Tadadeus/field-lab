import asyncio,os,sys,json
from playwright.async_api import async_playwright
F=sys.argv[1];LABS=(os.environ.get('LABS') or 'tw,ca,cl,cx,eq,fl,la,oc,qb,se,su,un').split(',')
WALK="""async(th)=>{const sleep=t=>new Promise(r=>setTimeout(r,t));const skip=b=>b.closest('#appbar,#segTh,.kov,.tour')||/download|csv|offline|record|rec\\b|snapshot|camera|full|tour|glossary|share|copy|paste|load|reset all|clear/i.test((b.id||'')+' '+(b.getAttribute('aria-label')||'')+' '+(b.title||'')+' '+b.textContent)||['rec','snap','full','hsLive','apTour','dlb'].includes(b.id)||b.classList.contains('dlb');
let n=0,sel=0;const seen=new Set();for(let pass=0;pass<2;pass++){const bs=[...document.querySelectorAll('.wrap button,.wrap [role=tab],.wrap [role=radio],.wrap .chip')].filter(b=>b.offsetParent&&!b.disabled&&!skip(b));for(const b of bs){const k=(b.id||'')+'|'+b.textContent.trim().slice(0,20)+'|'+(b.dataset?JSON.stringify(b.dataset):'');if(seen.has(k)){continue}seen.add(k);try{b.click();n++}catch(e){}await sleep(25)}}
for(const s of [...document.querySelectorAll('.wrap select')].filter(s=>s.offsetParent&&!s.disabled&&s.id!=='scene'&&s.id!=='state')){const v0=s.value;for(const o of [...s.options].slice(0,8)){s.value=o.value;s.dispatchEvent(new Event('change',{bubbles:true}));sel++;await sleep(40)}s.value=v0;s.dispatchEvent(new Event('change',{bubbles:true}))}
let r=0;for(const i of [...document.querySelectorAll('.wrap input[type=range]')].filter(i=>i.offsetParent&&!i.disabled).slice(0,60)){const v0=i.value;for(const v of [i.min,i.max,v0]){i.value=v;i.dispatchEvent(new Event('input',{bubbles:true}))}r++;await sleep(10)}
return [n,sel,r]}"""
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl"])
        out={}
        for th in LABS:
            ctx=await b.new_context(viewport={"width":1440,"height":900},accept_downloads=True)
            pg=await ctx.new_page();e=[];pg.on("pageerror",lambda x:e.append('PE '+str(x)[:160]));pg.on("console",lambda x:e.append('CE '+x.text[:160]) if x.type=='error' else None)
            pg.on("dialog",lambda d:asyncio.ensure_future(d.dismiss()))
            await pg.add_init_script("localStorage.setItem('bitwistor-tour','1')")
            await pg.goto("file://"+os.getcwd()+"/"+F);await pg.wait_for_timeout(2000)
            await pg.evaluate("document.querySelector('[data-th=%s]').click()"%th);await pg.wait_for_timeout(1500)
            try:
                c=await asyncio.wait_for(pg.evaluate(WALK,th),timeout=240)
            except Exception as x:
                c=['timeout',str(x)[:80]]
            await pg.wait_for_timeout(1500)
            alive=await pg.evaluate("(()=>{const t=document.querySelector('.pv')?.textContent||'';return t.slice(0,30)})()")
            out[th]={'counts':c,'errs':sorted(set(x for x in e if 'GroupMarker' not in x and 'GL Driver' not in x and 'swiftshader' not in x.lower()))[:6],'pv':alive}
            print(th,json.dumps(out[th],ensure_ascii=False),flush=True)
            await ctx.close()
        await b.close()
asyncio.run(m())
