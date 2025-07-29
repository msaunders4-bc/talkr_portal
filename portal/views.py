from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def home_page_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"""
        <h1>Welcome to Talkr Portal, {request.user.username}!</h1>
        <p>You are logged in as a {'superuser' if request.user.is_superuser else 'regular user'}.</p>
        <a href="/login/logout/" style="background: #dc3545; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Logout</a>
        """)
    else:
        return redirect('/login/')
