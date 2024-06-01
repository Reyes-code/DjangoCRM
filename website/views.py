from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import SignUpForm
from .models import Order

def home(request):
    orders = Order.objects.all()
    #check if the user is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f"Bienvenido {username}")
            
            return redirect('home')
        else:
            messages.success(request,"Error al iniciar sesión, verifica tus credenciales o comunicate con soporte al 3203468540")
            return redirect('home')
    else:

        return render(request, 'home.html',{'orders':orders},)

def logout_user(request):
    logout(request)
    messages.success(request, "Gracias por usar el sitio, has cerrado tu sesión")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
             #Auth and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"You have been registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{"form":form})
    return render(request,'register.html',{"form":form})

'''def order_record(request,pk):
    if request.user.is_authenticated():
        order_record = Order.objects.get(id=pk)
        return render(request, 'order.hmtl' 
        '''