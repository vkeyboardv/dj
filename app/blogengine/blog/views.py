from django.shortcuts import render

# Create your views here.
def posts_list(request):
    n = ['Vladik', 'Oladik']
    return render(request, 'blog/index.html', context={'names': n})
