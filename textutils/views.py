from email.policy import default
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    p = {'name': 'prasanna', 'place': 'sindhanoor'}
    return render(request, 'index1.html', p)


def analyze(request):
    # get the text
    djtext = request.POST.get('text', default)

    # Check checkboxes value
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    characount = request.POST.get('characount', 'off')

    # check which checkbox is on
    if removepunc == "on":
        punctuation = '''!()-[]{};:|'"\,<>./?@#$%^&*_~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if capfirst == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Newline remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index] == "    "):
                analyzed = analyzed + char
        params = {'purpose': 'Extraspaceremover', 'analyzed_text': analyzed}
        djtext = analyzed

    if characount == "on":
        analyzed = ""
        i = 0
        for char in djtext:
            i += 1
        params = {'purpose': 'Character counter', 'analyzed_text': i}
        djtext = i

    if(removepunc != "on" and capfirst != "on" and newlineremover != "on" and extraspaceremover != "on" and characount != "on"):
        return HttpResponse("<h1>please select any option try again</h1>")

    return render(request, 'analyze.html', params)
