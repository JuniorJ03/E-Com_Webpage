from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
       # print("POST request received!")  # Debugging
       # print(request.POST)  # Check if data is being sent
        print(request.COOKIES.get('csrftoken'))
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}, your account was created successfully!')

            new_user = authenticate(
                request,
                username=form.cleaned_data['username'],  # If 'email' doesn't work, change to 'username'
                password=form.cleaned_data.get('password1')
            )
            login(request, new_user)
            return redirect('core:index', 'partials:base')  # Change this if necessary
    else:
        form = UserRegisterForm()

    context = {'form': form}

    return render(request, 'userauths/sign-up.html', context)
