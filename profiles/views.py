from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import UserProfile
from .forms import UserProfileForm

@login_required
def display_profile(request):
    """Display the user's profile."""
    profile = request.user.userprofile
    return render(request, 'profile/display_profile.html', {'profile': profile})
