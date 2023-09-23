from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import UserProfile
from .forms import UserProfileForm

@login_required
def profile(request):
    """Display the user's profile."""
    profile = request.user.userprofile
    return render(request, 'profile/display_profile.html', {'profile': profile})

@login_required
def update_profile(request):
    """Update the user's profile."""
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile/update_profile.html', {'form': form})
