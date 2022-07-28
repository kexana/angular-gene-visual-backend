from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json,os

with open('D:/Base/DEOto/Python/geneVisualBackend/resources/DIABLO.json') as file:
    diablo=json.load(file)

with open('D:/Base/DEOto/Python/geneVisualBackend/resources/PHEX.json') as file:
    phex=json.load(file)

data_dictionary={}

data_dictionary['diablo']=diablo
data_dictionary['phex']=phex

def getNames(request):
    return HttpResponse(json.dumps(list(data_dictionary.keys())))

def main(request,dataName):
    if(dataName in data_dictionary):
        return HttpResponse(json.dumps(data_dictionary[dataName]))
