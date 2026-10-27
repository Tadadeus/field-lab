import asyncio,os,json
from playwright.async_api import async_playwright
F="""()=>new Promise(r=>{const t=[];let l=performance.now();const f=n=>{t.push(n-l);l=n;if(t.length<240){requestAnimationFrame(f)}else{t.sort((a,b)=>a-b);r({med:+t[120].toFixed(2),p95:+t[228].toFixed(2),mean:+(t.reduce((a,b)=>a+b)/t.length).toFixed(2)})}};requestAnimationFrame(f)})"""
async def run(b,file):
    out={}
    pg=await b.new_page(viewport={"width":390,"height":844})
    await pg.add_init_script("localStorage.setItem('bitwistor-tour','1');localStorage.setItem('bitwistor-app',JSON.stringify({perf:'potato'}))")
    await pg.goto("file://"+os.getcwd()+"/"+file);await pg.wait_for_timeout(3000)
    for th in ['tw','cx','fl','la']:
        await pg.evaluate("document.querySelector('[data-th=%s]').click()"%th);await pg.wait_for_timeout(2500)
        out[th]=await pg.evaluate(F)
    await pg.close();return out
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl","--ignore-gpu-blocklist"])
        for rep in range(3):
            for f in ['base_v17.html','Field_Lab.html']:
                print(rep,f,json.dumps(await run(b,f)))
        await b.close()
asyncio.run(main())
