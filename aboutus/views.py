from django.shortcuts import render

def about_us(request):
    return render(request, 'aboutus/about_us.html')

def service_policy(request):
    return render(request, 'aboutus/service_policy.html')

def privacy_policy(request):
    return render(request, 'aboutus/privacy_policy.html')