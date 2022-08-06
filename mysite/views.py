from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def page_not_found_view(request: HttpRequest, exception) -> HttpResponse:
    return render(request, 'no_page.html', {"exception": exception})