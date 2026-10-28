{const PSEL='button,[role=button],[role=tab],[role=radio],[role=menuitem],.chip,.act,.icon,.mode,.tab,.ib,.erow,summary,h3.sph,.tpin,.pdh',PMIN=180;let pEl=null,pT=0,pTm=0;
  const pOff=()=>{if(!pEl){return}const el=pEl;pEl=null;clearTimeout(pTm);pTm=setTimeout(()=>el.classList.remove('prs'),Math.max(0,PMIN-(performance.now()-pT)))};
  const pOn=el=>{if(pEl&&pEl!==el){pEl.classList.remove('prs')}clearTimeout(pTm);pEl=el;pT=performance.now();el.classList.add('prs')};
  document.addEventListener('pointerdown',e=>{if(e.button>0){return}const el=e.target&&e.target.closest?e.target.closest(PSEL):null;if(!el||el.disabled||el.getAttribute('aria-disabled')==='true'){return}pOn(el)},{passive:true,capture:true});
  for(const t of ['pointerup','pointercancel','dragstart']){addEventListener(t,pOff,{passive:true,capture:true})}addEventListener('blur',e=>{if(e.target===window){pOff()}})
  document.addEventListener('keydown',e=>{const a=document.activeElement;if((e.key==='Enter'||e.key===' ')&&a&&a.matches&&a.matches(PSEL)){pOn(a);pOff()}},true);
  document.addEventListener('touchstart',()=>{},{passive:true})}
