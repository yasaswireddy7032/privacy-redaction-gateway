import re,json
PATTERNS={
 'EMAIL':re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
 'SSN':re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
 'PHONE':re.compile(r'(?<!\w)(?:\+1[- .]?)?\(?\d{3}\)?[- .]\d{3}[- .]\d{4}(?!\w)'),
 'CARD':re.compile(r'(?<!\d)(?:\d[ -]?){12,18}\d(?!\d)')}

def luhn(value):
    digits=[int(c) for c in value if c.isdigit()]
    if not 13<=len(digits)<=19 or len(set(digits))==1:return False
    total=0
    for i,n in enumerate(reversed(digits)):
        if i%2:n=n*2-9 if n*2>9 else n*2
        total+=n
    return total%10==0

def redact(text):
    if not isinstance(text,str):raise TypeError('Text required')
    matches=[]
    for kind,pattern in PATTERNS.items():
        for m in pattern.finditer(text):
            if kind=='CARD' and not luhn(m.group()):continue
            matches.append((m.start(),m.end(),kind,m.group()))
    matches.sort(key=lambda m:(m[0],-(m[1]-m[0])))
    end=0;parts=[];counts={};mapping={}
    for start,stop,kind,value in matches:
        if start<end:continue
        key=(kind,value)
        if key not in mapping:mapping[key]=f'[{kind}_{1+sum(k[0]==kind for k in mapping)}]'
        parts.extend([text[end:start],mapping[key]]);end=stop;counts[kind]=counts.get(kind,0)+1
    parts.append(text[end:])
    # Never include original values or reversible mappings in the returned audit.
    return {'text':''.join(parts),'redactions':counts,'total':sum(counts.values())}
if __name__=='__main__':print(json.dumps(redact('Demo only: alex@example.test, 202-555-0123, card 4111 1111 1111 1111.'),indent=2))
