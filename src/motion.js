{const R=document.documentElement,SEL='.seg:not(#segTh),#modes,#svPlane,#axRow,.apseg';
 const on=b=>b.getAttribute('aria-checked')==='true'||b.getAttribute('aria-selected')==='true'||b.getAttribute('aria-pressed')==='true';
 const att=box=>{if(box.__sind){return}const i=document.createElement('span');i.className='sind';i.setAttribute('aria-hidden','true');box.classList.add('hassind');box.__sind=i;
  let q=0;const up=()=>{q=0;if(i.parentNode!==box){box.appendChild(i);if(i.__t){i.style.transform=i.__t}getComputedStyle(i).transform}
   const bs=[...box.querySelectorAll(':scope>button')].filter(on),b=bs.length===1?bs[0]:null;
   if(!b||!b.offsetParent||!box.offsetParent){i.style.opacity='0';return}
   const t='translate('+b.offsetLeft+'px,'+(b.offsetTop+b.offsetHeight-2)+'px) scaleX('+(b.offsetWidth/100)+')';
   if(!i.__t){i.classList.add('nt');i.style.transform=t;getComputedStyle(i).transform;i.classList.remove('nt')}else if(t!==i.style.transform){i.style.transform=t}
   i.__t=t;i.style.opacity='1'};
  const k=()=>{if(!q){q=requestAnimationFrame(up)}};
  new MutationObserver(k).observe(box,{subtree:true,childList:true,attributes:true,attributeFilter:['aria-checked','aria-selected','aria-pressed','hidden']});if(window.ResizeObserver){new ResizeObserver(k).observe(box)}addEventListener('resize',k);if(document.fonts&&document.fonts.ready){document.fonts.ready.then(k)}k()};
 const scan=()=>{for(const b of document.querySelectorAll(SEL)){att(b)}};scan();setInterval(scan,800);document.addEventListener('click',()=>setTimeout(scan,30),true)}
