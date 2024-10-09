from django.shortcuts import render

def homepage(request):
    context = {}
    if request.method == "POST":
        if "upload" in request.POST:
            context["message"] = "Select File button pressed!"
        elif "check_instance" in request.POST:
            context["message"] = "Check Instance button pressed!"
    return render(request, 'homepage.html', context)