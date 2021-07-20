from django import http
import django
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
     return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('remove_punc', 'off')
    spaceremove = request.POST.get('space_remover', 'off')
    fullcaps = request.POST.get('full_cap', 'off')
    newline_remove = request.POST.get('new_line_remover', 'off')
    char_count = request.POST.get('char_count', 'off')
    print(fullcaps)
    print(djtext)
    print(removepunc)
    analyzed = ""
    if removepunc != "on" and fullcaps != "on" and newline_remove != "on" and spaceremove != "on" and char_count != "on":
        return HttpResponse('Error')
    else:
        if removepunc == 'on':
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in djtext:

                if char not in punctuations:
                    analyzed = analyzed + char
            params = {
                'purpose': 'Remove Punctuations',
                'analyzed_text': analyzed,
            }
            djtext = analyzed
        if fullcaps == 'on':
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()

            params = {
                'purpose': 'Capitalize the whole text',
                'analyzed_text': analyzed,
            }
            djtext = analyzed
        if newline_remove == "on":
            analyzed = ""
            for char in djtext:
                if char != '\n' and char != '\r':
                    analyzed = analyzed + char
            params = {
                'purpose': 'Removing the New line',
                'analyzed_text': analyzed,
            }
            djtext = analyzed
        if spaceremove == 'on':
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char
                params = {
                    'purpose': 'Removing the extra spaces',
                    'analyzed_text': analyzed,
                }
            djtext = analyzed
        if char_count == 'on':
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char
                alen = len(analyzed)
                params = {
                    'purpose': 'Counting the Number of characters',
                    'charlen': alen,
                    'analyzed_text':analyzed

                }
            return render(request,'analyze.html',params)
        else:
            return render(request, 'analyze.html', params)


# def remove_punc(request):
#     djtext = request.GET .get('text','default')
#     print(djtext)

#     return HttpResponse('remove_punc')

# def cap_first(request):
#     return HttpResponse('capitalize first')

# def newline_remover(request):
#     return HttpResponse('new line has been removed')

# def space_remover(request):
#     return HttpResponse('extra spaces has been removed')

# def char_count(request):
#     return HttpResponse('character counting `')

