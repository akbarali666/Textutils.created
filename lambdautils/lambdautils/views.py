# i have created file in lambdautils
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Home')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    if removepunc == "on":
        # analyzed=djtext
        Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
       
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

        # analize the text
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        
    if (removepunc !="on" and newlineremover !="on" and extraspaceremover !="on" and fullcaps!="on"):
        return HttpResponse("Does't responce")

    return render(request, 'analyze.html', params)


# def capatilizefirst(request):
#     return HttpResponse('capatilize first')

# def newlineremove(request):
#     return HttpResponse('new line remove')

# def spaceremove(request):
#     return HttpResponse("space remove <a href='/'>back</a>")

# def charcount(request):
#     return HttpResponse('charcount')
