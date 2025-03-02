from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        # Debugging to check the csrf token, you can remove it later
        print(request.COOKIES.get('csrftoken'))
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # Check if the form is valid
            # Save the new user
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}, your account was created successfully!')

            # Authenticate the user (use email if it's the primary identifier)
            new_user = authenticate(
                request,
                username=form.cleaned_data['email'],  # Use email as the username
                password=form.cleaned_data.get('password1')
            )
            
            # Log the user in if authentication is successful
            if new_user is not None:
                login(request, new_user)
                return redirect('core:index')  # Redirect to the homepage or appropriate page
                
            # If authentication failed, show an error (optional)
            messages.error(request, 'Login failed. Please try again.')
            return redirect('userauths:sign-up')  # Stay on the registration page if there's an issue

    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'userauths/sign-up.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:index', 'partials:base')
    
    if request.method == 'POST':
        email = request.POST.get('email')