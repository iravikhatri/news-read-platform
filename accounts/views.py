from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm


def signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"You account has beed created! You are able to log in")
            return redirect('login')
    else:
        form = UserSignupForm()
        print(form)
    return render(request, 'accounts/signup.html', {'form': form, 'page_title': 'Sign Up'})
