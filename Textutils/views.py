# I have Created This File-ByME

from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Check checkbox value
    removepunch = request.POST.get('removepunch', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numbremove = request.POST.get('numbremove', 'off')
    # <-------Analyze the text------->
    # check which checkbox is on
    # Remove Punchtuation
    if removepunch == "on":
        punchtuation ='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punchtuation:
                analyzed = analyzed + char
        params ={'purpose' : 'Remove Punchtuations', 'analyzed_text' : analyzed}
        djtext = analyzed
    # UPPERCASE
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params ={'purpose' : 'UPPERCASE', 'analyzed_text' : analyzed}
        djtext = analyzed
    # New line Remover
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        print(analyzed)
        params ={'purpose' : 'Newline Remover', 'analyzed_text' : analyzed}
        djtext = analyzed
    # Extra Space Remover
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params ={'purpose' : 'Extra Space Remover', 'analyzed_text' : analyzed}
        djtext = analyzed
    # Number remover
    if numbremove == "on":
        analyzed = ""
        numbers = '0123456789'
        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    # Error Return 
    if removepunch != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and numbremove != "on":
        analyzed ="ERROR-no Operation Select"
        Message = "Please Select any Opertion And Try Again"
        params ={'purpose' : Message, 'analyzed_text' : analyzed}

    return render(request,"analyze.html", params)




def about(request):
    return render(request, 'about.html')

def aboutAnalyze(request):
    return render(request, 'aboutAnalyze.html')

def error(request):
    return render(request, 'error.html')