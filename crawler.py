import urllib2
    


def buscador(web):
    fichero=urllib2.urlopen(web)
    lista=[]
    words=[]
    for line in fichero.readlines():
        for i in range(len(line)):
            if ord("a")<=ord(line[i])<=ord("z") or ord("A")<=ord(line[i])<=ord("Z"):
                lista.append(line[i])
            else:
                lista.append(" ")
        x="".join(str(i) for i in lista)
        x=x.split()
    for i in range(len(x)):
        n=x.count(x[i])
        if n>1:
            x[i]=""
        else:
            words.append(x[i])
    return words

def tratar(web):
    fichero=urllib2.urlopen(web).read()
    listadewebs=[]
    x=True
    porvisitar=[]
    while x:
        recopilar=fichero.find("href")
        if recopilar>0:
            longitud=len(fichero)
            fichero=fichero[recopilar:longitud]
            recopilar=fichero.find('"')
            longitud=len(fichero)
            fichero=fichero[recopilar+1:longitud]
            recopilar=fichero.find('"')
            pag=fichero[0:recopilar]
            if pag.startswith("http" or "www"):
                listadewebs.append(pag)
        else:
            x=False
    for i in range(len(listadewebs)-1):
        t=listadewebs.count(listadewebs[i])
        if t==1:
            porvisitar.append(listadewebs[i])
    return porvisitar

def main(web):
    z=tratar(web)
    search=raw_input("introduce una palabra: ")
    final=[]
    for k in range(len(z)-1):
        x=buscador(z[k])
        if (search in x)==True:
            final.append(z[k])
    return final
        


