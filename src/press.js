{const PSEL='button,[role=button],[role=tab],[role=radio],[role=menuitem],.chip,.act,.icon,.mode,.tab,.ib,.erow,summary,h3.sph,.tpin,.pdh',PMIN=180;let pEl=null,pT=0;const pTm=new Map();
  const pFind=t=>t&&t.closest?t.closest(PSEL):null;
  const pRm=(el,w)=>{clearTimeout(pTm.get(el));pTm.set(el,setTimeout(()=>{el.classList.remove('prs','prs0');pTm.delete(el)},w))};
  const pOff=()=>{if(!pEl){return}const el=pEl;pEl=null;pRm(el,Math.max(0,PMIN-(performance.now()-pT)))};
  const pOn=el=>{if(pEl===el){return}if(pEl){pEl.classList.remove('prs','prs0')}clearTimeout(pTm.get(el));pEl=el;pT=performance.now();el.classList.add(el.disabled||el.getAttribute('aria-disabled')==='true'?'prs0':'prs')};
  const pDown=t=>{const el=pFind(t);if(el){pOn(el)}};
  document.addEventListener('pointerdown',e=>{if(e.button>0){return}pDown(e.target)},{passive:true,capture:true});
  document.addEventListener('touchstart',e=>{const t=e.touches&&e.touches[0];if(t){pDown(document.elementFromPoint(t.clientX,t.clientY)||e.target)}},{passive:true,capture:true});
  for(const t of ['pointerup','pointercancel','dragstart','touchend','touchcancel']){addEventListener(t,pOff,{passive:true,capture:true})}addEventListener('blur',e=>{if(e.target===window){pOff()}});
  document.addEventListener('click',e=>{const el=pFind(e.target);if(!el){return}if(pEl&&pEl!==el){pEl.classList.remove('prs','prs0');pEl=null}for(const o of document.querySelectorAll('.prs')){if(o!==el){o.classList.remove('prs')}}el.classList.add('prs');pRm(el,PMIN)},true);
  document.addEventListener('keydown',e=>{const a=document.activeElement;if((e.key==='Enter'||e.key===' ')&&a&&a.matches&&a.matches(PSEL)){pOn(a);pOff()}},true)}
