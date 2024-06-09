import django.shortcuts


def index(request):
    return django.shortcuts.render(request, 'app/index.html')
