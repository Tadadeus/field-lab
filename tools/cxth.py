import asyncio, os
from playwright.async_api import async_playwright
INIT="Object.defineProperty(navigator,'webdriver',{get:()=>false});try{localStorage.setItem('bitwistor-tour','1');if('"+os.environ.get('QL','')+"'){localStorage.setItem('bitwistor-app',JSON.stringify({perf:'"+os.environ.get('QL','')+"'}))}}catch(e){}/*QLV_ENV*/"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl","--ignore-gpu-blocklist"])
        m=await b.new_page(viewport={"width":390,"height":844})
        errs=[];m.on("pageerror",lambda e:errs.append('PE '+str(e)[:250]));m.on("console",lambda x:errs.append('CE '+x.text[:250]) if x.type=='error' else None)
        await m.add_init_script(INIT)
        await m.goto("file://"+os.getcwd()+"/Field_Lab.html");await m.wait_for_timeout(2000)
        ths=await m.evaluate("[...document.querySelectorAll('#segTh button')].map(b=>b.dataset.th)")
        for t in ths:
            n0=len(errs)
            await m.evaluate(f"document.querySelector('#segTh button[data-th={t}]').click()");await m.wait_for_timeout(1500)
            sts=await m.evaluate("[...document.getElementById('state').options].map(o=>o.value)")
            for sv in sts[:6]:
                await m.select_option('#state',sv);await m.wait_for_timeout(700)
            await m.evaluate("document.getElementById('views2').scrollIntoView()");await m.wait_for_timeout(500)
            await m.evaluate("window.scrollTo(0,0)")
            print(t,len(sts),'errors',len(errs)-n0)
            for x in errs[n0:n0+3]:print('   ',x)
        await b.close()
asyncio.run(main())
