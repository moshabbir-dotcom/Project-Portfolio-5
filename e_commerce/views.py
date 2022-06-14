from django.shortcuts import render


def page_404_view(request, exception):
    return render(request, 'page_404.html', status=404)