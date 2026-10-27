import re,difflib,sys
B=open('/mnt/user-data/attachments/47fd48c3-e8a0-599b-9f2d-c17d40f53247/15346740-Field_Lab__1_.html',encoding='utf8').read()
N=open('Field_Lab.html',encoding='utf8').read()
def js(s):
    return '\n'.join(re.findall(r'<script>([\s\S]*?)</script>',s))
def toks(s):
    return [t for t in re.split(r'(?<=[;{}])',s) if t.strip()]
a,b=toks(js(B)),toks(js(N))
sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
out=[];ch=0
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op=='equal':continue
    ch+=1
    out.append('@@ %s base[%d:%d] new[%d:%d]\n- %s\n+ %s\n'%(op,i1,i2,j1,j2,''.join(a[i1:i2])[:600],''.join(b[j1:j2])[:600]))
open('p1/mathdiff.txt','w').write(''.join(out))
print('base stmts',len(a),'new stmts',len(b),'changed hunks',ch,'equal ratio',round(sm.ratio(),4))
def norm(s):
    s=re.sub(r"'rgba\((?:220,226,236|255,255,255|232,236,242|214,222,236),(?:(?:0?\.\d+)|1)\)'","COL",s)
    s=re.sub(r"CK\.i\((?:(?:0?\.\d+)|1)\)","COL",s)
    s=re.sub(r"'#(?:e8ecf2|cfd6e2|c8d0e0|7c86a0|070a10|04060a)'|CK\.(?:fg|faint|bg|dim)\b","COL",s)
    s=re.sub(r"(\d00 |italic |bold )*(9|9\.5|10|10\.5|11)px ","FPX ",s)
    return s
rest=[];cls={'presentation-literal':0}
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op=='equal':continue
    x,y=''.join(a[i1:i2]),''.join(b[j1:j2])
    if norm(x)==norm(y):
        cls['presentation-literal']+=1;continue
    rest.append((x,y))
print(cls,'remaining',len(rest))
with open('p1/mathdiff_rest.txt','w') as f:
    for x,y in rest:
        f.write('-----\n- '+x[:1500]+'\n+ '+y[:3000]+'\n')
