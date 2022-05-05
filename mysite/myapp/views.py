from django.shortcuts import redirect, render
from .models import Consume, food

# Create your views here.
def index(request):

    if request.method=="POST":
        food_consumed=request.POST['food_consumed'] 
        consume=food.objects.get(name=food_consumed)
        user=request.user    #request.user is current logged-in user if user logged in. Else it's AnonymousUser 
        consume=Consume(user=user, food_consumed=consume)
        consume.save()
        foods=food.objects.all()


    else:
        foods=food.objects.all()   #fetching data from database
        
    consumed_food=Consume.objects.filter(user=request.user)
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})    




def delete_consume(request,id):
    consumed_food=Consume.objects.get(id=id)
    if request.method=='POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')     
