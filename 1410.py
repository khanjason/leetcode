class Solution:
    def entityParser(self, text: str) -> str:
        d={}
        d['&quot;']='"'
        d['&apos;']="'"
        d['&amp;']='&'
        d['&gt;']='>'
        d['&lt;']='<'
        d['&frasl;']='/'
        t=text
        for k in d.keys():
            if k in text:
                t=t.replace(k,d[k])
        return(t)
