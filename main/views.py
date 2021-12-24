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
        print(text)
    
    

    scr = 0
    x = text.split('\n')
    detail = []
    
    for i in x:
        a = i.split()
        detail.append(a)
    print(detail)
    temp = []    
    precont = ''
    ctr = 0
    tmp1 = []

    for x in detail:
        print(x)
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
        weight = i[-2][:-1]
        try:
            float(weight)
            scr += float(weight) / 100 * float(i[-1])
        except:
            scr += 0

    print(scr)
    context = {
        'finals':[scr],
        'butir':temp
    }
    
    
    return render(request, 'main/home.html', context)

