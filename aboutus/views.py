from django.shortcuts import render

def about_us(request):
    """
    Render the about_us template
    """
    return render(request, 'aboutus/about_us.html')

def service_policy(request):
    """
    Render the service_policy template
    """
    return render(request, 'aboutus/service_policy.html')

def privacy_policy(request):
    """
    Render the privacy_policy template
    """
    return render(request, 'aboutus/privacy_policy.html')