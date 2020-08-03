from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #if it get a post request, it shud instatiate UserRegisterForm with the
        #POST request, else empty UserRegisterForm will be instatiated
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #form is saved in cleaned_data
            messages.success(request, f'Your Account has been created! You can now login') # f means flash
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
 #{'form': form} is to access the form content within the templates
 
 
@login_required #it means user must loggedin b4 accessing profile 
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) #instance=request.user will populate the form with the 
        p_form = ProfileUpdateForm(request.POST,                     #current user infor as placeholder
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)