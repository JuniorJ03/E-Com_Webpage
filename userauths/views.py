from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')   # if you want to you can swap the form.cleaned_data.get('xyz') with just form.cleaned_data['xyz']
            messages.success(request, f'Hey {username}, your account was created succesfully')
            new_user = authenticate(username=form.cleaned_data['email'],   # see line 12
                                    password=form.cleaned_data.get('password1')
            )
            login(request, new_user)
            return redirect('core:index')
   
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form,
    }
    print("register_view is being accessed!")
    return render(request, 'userauths/sign-up.html', context)

