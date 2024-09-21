from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')
def index2(request):
    return render(request, 'pages/index-2.html')
def blog3columns(request):
    return render(request, 'pages/blog-3-columns.html')
def blogpost1(request):
    return render(request, 'pages/blog-post-1.html')
def blog(request):
    return render(request, 'pages/blog.html')
def portfolio2columns(request):
    return render(request, 'pages/portfolio-2-columns.html')
def portfolio4columns(request):
    return render(request, 'pages/portfolio-4-columns.html')
def portfolio5columns(request):
    return render(request, 'pages/portfolio-5-columns.html')
def portfolioproject1(request):
    return render(request, 'pages/portfolio-project-1.html')
def portfolioproject2(request):
    return render(request, 'pages/portfolio-project-2.html')
def portfolioproject3(request):
    return render(request, 'pages/portfolio-project-3.html')
def portfolio(request):
    return render(request, 'pages/portfolio.html')
def resume(request):
    return render(request, 'pages/resume.html')
def contact(request):
    return render(request, 'pages/contact.html')
