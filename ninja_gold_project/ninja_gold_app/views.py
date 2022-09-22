from django.shortcuts import render,redirect
from  random import randint, random
from time import strftime

# Create your views here.
def go_to_gold(request):
    request.session['gold']=0
    request.session['message']=[]
    return redirect("Gold/")

def gold(request):
    return render(request,"index.html")

def process_money(request):
    if request.POST['field']=='quest':
        random_inc=randint(-50,50)
        request.session['gold']+=random_inc
        if random_inc==0:
            request.session['message'].insert(0,['You entered '+ request.POST['field'] 
                            +' and earned '+str(random_inc)+' gold.'
                            +' ('+strftime("%m/%d/%Y, %H:%M:%S")+')','danger'])
        elif random_inc>0:
            request.session['message'].insert(0,['You entered '+ request.POST['field'] 
                            +' and earned '+str(random_inc)+' gold.'+' ('
                            +strftime("%m/%d/%Y, %H:%M:%S")+')','success'])
        elif random_inc<0:
            request.session['message'].insert(0,['You failed a '+ request.POST['field'] 
                            +' and lost '+str(random_inc)+' gold.'+'Ouch.'
                            +' ('+strftime("%m/%d/%Y, %H:%M:%S")+')','danger'])

    else:
        random_inc=randint(10,20)
        request.session['gold']+=random_inc
        request.session['message'].insert(0,['You entered '+ request.POST['field'] 
                        +' and earned '+str(random_inc)+' gold.'
                        +' ('+strftime("%m/%d/%Y, %H:%M:%S")+')','success'])
        

    
    
    print(random_inc)



    return redirect('/Gold')
