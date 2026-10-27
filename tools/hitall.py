import asyncio,os,json
from playwright.async_api import async_playwright
H="""async()=>{let n=0,f=0,sk=0,ex={};const els=[...document.querySelectorAll('.icon,.chip,.act,.mode,.tab,.ib,.tpin,.seg button,.apseg button,#qBtn,#full,#segTh button')].filter(e=>e.offsetParent);for(const el of els){el.scrollIntoView({block:'center',inline:'center'});await new Promise(r=>requestAnimationFrame(r));const r=el.getBoundingClientRect();const cx=r.left+r.width/2,cy=r.top+r.height/2;if(cx<0||cx>innerWidth||cy<0||cy>innerHeight){sk++;continue}n++;let ok=true;for(const dy of [-20,20]){if(cy+dy<0||cy+dy>innerHeight){continue}const t=document.elementFromPoint(cx,cy+dy);if(!(t&&(t===el||el.contains(t)||(t.closest&&t.closest('button,[role=tab],[role=radio],a,select,input')&&t.closest('button,[role=tab],[role=radio],a,select,input')!==el&&false)))){const tc=t&&t.closest&&t.closest('button,[role=tab],[role=radio],a[href],select,input,summary,label');if(tc&&tc!==el){continue}ok=false}}if(!ok){f++;{const k=(el.id||el.className||el.textContent).toString().slice(0,22)+' h'+Math.round(r.height);ex[k]=(ex[k]||0)+1}}}return {n,f,sk,ex}}"""
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl"])
        ctx=await b.new_context(viewport={"width":390,"height":844},device_scale_factor=2,is_mobile=True,has_touch=True)
        pg=await ctx.new_page()
        await pg.add_init_script("localStorage.setItem('bitwistor-tour','1')")
        await pg.goto("file://"+os.getcwd()+"/Field_Lab.html");await pg.wait_for_timeout(2500)
        for th in os.environ.get('LABS','tw,cx,un').split(','):
            await pg.evaluate("document.querySelector('[data-th=%s]').click()"%th);await pg.wait_for_timeout(1200)
            print(th,json.dumps(await pg.evaluate(H)))
        await b.close()
asyncio.run(m())
