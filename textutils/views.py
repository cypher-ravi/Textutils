from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
      return render(request, 'index.html')
  



def analyze(request):
    # get the text
    djtext = request.POST.get('text','default')
    # Check checkbox values
    remove_punc = request.POST.get('removepunc','off')
    full_caps = request.POST.get('fullcap','off')
    New_line_remover = request.POST.get('newlineremover','off')
    char_count = request.POST.get('charcounter','off')

    #check which checkbox is on and for removing punctuation
    if remove_punc == "on":
        punctations = '''!"#$%&'()*+,-./:;<=>?@\][^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        
    # For capitalization full text   
    if (full_caps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
       

    if (New_line_remover == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
            params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
            djtext = analyzed
            

    if (char_count == "on"):
            count = len(djtext)
            print(count)
            params = {'purpose': 'Charcter counted','counter':count}
   

    if (remove_punc != "on" and full_caps != "on" and New_line_remover != "on" and char_count != "on" ):
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)
 

