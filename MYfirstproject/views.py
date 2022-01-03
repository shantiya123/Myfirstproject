from django.http import HttpResponse
from django.shortcuts import render
import operator

def Hi(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items() , key=operator.itemgetter(1), reverse=False)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':sortedwords})
def Enter(request):
    return render(request,'Enter.html')
def Show(request):
    firstname=request.GET['firstname']
    lastname=request.GET['lastname']
    age=request.GET['age']
    ag=int(age)
    birthyear=2022-ag
    str(birthyear)
    return render(request,'Show.html',{'firstname':firstname,'lastname':lastname,'age':age,'birthyear':birthyear})
