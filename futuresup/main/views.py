from django.shortcuts import render

def main(request):
    return render(request, 'main/main_page.html')

def chat(request):
    return render(request, 'main/chat_page.html')

def about(request):
    return render(request, 'main/about_page.html')

def profile(request):
    return render(request, 'main/profile_page.html')