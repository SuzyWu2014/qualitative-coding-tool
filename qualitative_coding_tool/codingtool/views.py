from django.shortcuts import render


def add_code(request):
    return render(request, "codingtool/add_code.html", {})
