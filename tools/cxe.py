import sys, asyncio, os
from playwright.async_api import async_playwright
async def main():
    scenes=sys.argv[1].split(',')
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl","--ignore-gpu-blocklist"])
        pg=await b.new_page(viewport={"width":int(os.environ.get("VW","1440")),"height":int(os.environ.get("VH","1000"))})
        errs=[]
        pg.on("pageerror",lambda e:errs.append('PE '+str(e)[:400]))
        pg.on("console",lambda m:errs.append('CE '+m.text[:400]) if m.type=='error' else None)
        await pg.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>false});try{localStorage.setItem('bitwistor-tour','1');if('"+os.environ.get('QL','')+"'){localStorage.setItem('bitwistor-app',JSON.stringify({perf:'"+os.environ.get('QL','')+"'}))}}catch(e){}/*QLV_ENV*/")
        await pg.goto("file://"+os.getcwd()+"/Field_Lab.html");await pg.wait_for_timeout(1500)
        await pg.evaluate("document.querySelector('#segTh button[data-th=cx]').click()");await pg.wait_for_timeout(800)
        for sc in scenes:
            n0=len(errs)
            await pg.select_option('#scene',sc);await pg.wait_for_timeout(1300)
            for sel in ['#views2','#cxMini','.sec']:
                await pg.evaluate(f"document.querySelector('{sel}').scrollIntoView()");await pg.wait_for_timeout(500)
            await pg.evaluate("window.scrollTo(0,0)");await pg.wait_for_timeout(400)
            print(sc, 'errors:',len(errs)-n0, await pg.evaluate("document.getElementById('pv').textContent"))
            for e in errs[n0:n0+3]: print('   ',e)
        await b.close()
asyncio.run(main())
