from django.urls import path
from .views import (
    index, index2, blog3columns, blogpost1, blog,
    portfolio2columns, portfolio4columns, portfolio5columns,
    portfolioproject1, portfolioproject2, portfolioproject3,
    portfolio, resume,contact
)

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('index-2', index2, name='index2'),
    path('blog-3-columns', blog3columns, name='blog3columns'),
    path('blog-post-1', blogpost1, name='blogpost1'),
    path('blog', blog, name='blog'),
    path('portfolio-2-columns', portfolio2columns, name='portfolio2columns'),
    path('portfolio-4-columns', portfolio4columns, name='portfolio4columns'),
    path('portfolio-5-columns', portfolio5columns, name='portfolio5columns'),
    path('portfolio-project-1', portfolioproject1, name='portfolioproject1'),
    path('portfolio-project-2', portfolioproject2, name='portfolioproject2'),
    path('portfolio-project-3', portfolioproject3, name='portfolioproject3'),
    path('portfolio', portfolio, name='portfolio'),
    path('resume', resume, name='resume'),
    path('contact', contact, name='contact'),
]