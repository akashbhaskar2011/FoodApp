from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid :
            username=form.cleaned_data.get('username')
            message=messages.success(request,f'The user {username} created suceefully')
            return redirect('food:index')
    else:
     form=UserCreationForm()
    return render(request,'users/registration.html',{'form':form})