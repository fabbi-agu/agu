def primo (num):
    if num<2:
        return False
    for q in range(2,total):
        if total % q == 0 :
            return False
    return True
palabra =input('ingrese una palabra')
total=0
lis1=[]
conj=set()
for i in range(len(palabra)):
    total=0
    letra=palabra[i]
    if not letra in conj:
        conj.add(letra)
        for h in range(len(palabra)):
            if(letra==palabra[h]):
                total=total+1
        booleano=primo(total)
        if booleano :
            lis1.append(letra)
        print('la letra: ',letra,' se repite ',total)
lis_imprimir=''
for i in lis1 :
    lis_imprimir=lis_imprimir+' '+i
print('las lletras ',lis_imprimir,' aparecen un numero primo de veces ')
