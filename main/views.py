from django.http import request
from django.shortcuts import render, redirect

def cekfloat(x):
    boolean = True
    try:
        float(x)
    except:
        boolean = False
    
    return boolean

def home(request):

    if request.method == "POST":
        text = request.POST["detail"]
        
        scr = 0
        x = text.split('\n')
        detail = []
        eror = ''
        
        for i in x:
            a = i.split()
            if a != '':
                detail.append(a)
        print(detail)
        for i in detail:
            if len(i) == 0:
                detail.pop(detail.index(i))
        
        temp = []    
        precont = ''
        ctr = 0
        tmp1 = []

        for x in detail:
            
            for i in x:
                if ctr == 0:
                    precont += f'{i}'
                    ctr +=1
                else:
                    precont += f' {i}'
            ctr = 0
            temp.append(precont)
            precont = ''
        
        for i in detail:
            try:
                weight = i[-2][:-1]
                
            except:
                eror = 'yang bener inputnya:D'
            else:
                try:
                    float(weight)
                    scr += float(weight) / 100 * float(i[-1])
                except:
                    scr += 0

        print(scr)
        context = {
            'finals':[scr],
            'butir':temp,
            'eror':eror
        }
        
        return render(request, 'main/home.html', context)
    return render(request, 'main/home.html')
    
