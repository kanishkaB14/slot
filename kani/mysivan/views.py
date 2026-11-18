from django.shortcuts import render

def calculate_Churn(request):
    result = None
    initial = ""
    present = ""
    if request.method == "POST":
        initial = request.POST.get("initial_Customer")
        present = request.POST.get("present_Customer")
        if initial and present and int(initial) != 0:
            result = round(((int(initial) - int(present)) / int(initial)) * 100, 2)
    return render(request, "mylove/gogul.html", {
        "result": result,
        "initial": initial,
        "present": present
    })