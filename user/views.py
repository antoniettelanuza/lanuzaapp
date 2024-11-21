from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Handle user registration
def register(request):
    if request.method == 'POST':  # Check if the form is being submitted
        form = UserRegisterForm(request.POST)  # Create form instance with POST data
        if form.is_valid():  # Validate form
            form.save()  # Save new user to the database
            username = form.cleaned_data.get('username')  # Get the cleaned data
            messages.success(request, f'Account created successfully for {username}.')
            return redirect('login')  # Redirect to login after success
    else:
        form = UserRegisterForm()  # Create a blank form if the request is GET
    return render(request, 'user/register.html', {'form': form})

# Handle profile update for logged-in user
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)  # Bind form with the current user data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  # Bind form with the current profile data
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()  # Save the updated user information (username/email)
            p_form.save()  # Save the updated profile picture
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')  # Redirect back to the profile page after successful update
    else:
        u_form = UserUpdateForm(instance=request.user)  # Create form with the current user data
        p_form = ProfileUpdateForm(instance=request.user.profile)  # Create form with the current profile data

    context = {
        'u_form': u_form,  # Pass the user info form to the template
        'p_form': p_form   # Pass the profile image form to the template
    }

    return render(request, 'user/profile.html', context)

# Handle the email reset functionality
# Reset email view
@login_required
def reset_email(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email has been successfully updated!')
            return redirect('profile')  # Redirect back to the profile page
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'user/reset_email.html', {'form': form})