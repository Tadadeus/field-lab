import asyncio,os
from playwright.async_api import async_playwright
A="()=>{const a=document.activeElement;return (a.id||a.className||a.tagName)+'|'+(a.textContent||'').trim().slice(0,14)+' qPop.hidden='+(document.getElementById('qPop')||{hidden:true}).hidden+' appPop.hidden='+(document.getElementById('appPop')||{hidden:true}).hidden}"
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl"])
        pg=await b.new_page(viewport={"width":1440,"height":900})
        await pg.add_init_script("localStorage.setItem('bitwistor-tour','1')")
        await pg.goto("file://"+os.getcwd()+"/Field_Lab.html");await pg.wait_for_timeout(2500)
        for bid in ['qBtn','appSet']:
            await pg.focus('#'+bid);await pg.keyboard.press('Enter');await pg.wait_for_timeout(300)
            print(bid,'open ->',await pg.evaluate(A))
            await pg.keyboard.press('ArrowDown');await pg.keyboard.press('Tab');await pg.wait_for_timeout(200)
            print(bid,'tab ->',await pg.evaluate(A))
            await pg.keyboard.press('Escape');await pg.wait_for_timeout(300)
            print(bid,'esc ->',await pg.evaluate(A))
            await pg.focus('#'+bid);await pg.keyboard.press('Enter');await pg.wait_for_timeout(300)
            for i in range(30):
                await pg.keyboard.press('Tab')
                v=await pg.evaluate(A)
                if ('qPop.hidden=true' in v and bid=='qBtn') or ('appPop.hidden=true' in v and bid=='appSet'): break
            print(bid,'tab out after',i+1,'->',v)
        await pg.keyboard.press('Shift+Tab');await pg.focus('body')
        await pg.keyboard.press('Tab');print('first tab ->',await pg.evaluate(A))
        await b.close()
asyncio.run(m())
