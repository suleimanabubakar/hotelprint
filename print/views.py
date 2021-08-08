from print.print import printPdf
from django.shortcuts import render
import pdfkit
from django.http import JsonResponse
import config
from print import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def checkavailability(request):
    return Response(status=status.HTTP_200_OK,data={"msg":"available"})



def getLinkType(type):
    if type == 'main':
        urlL = 'mainorderprintauto'
    else:
        urlL = 'orderprintauto'
    return urlL

def getPdfName(type,order):
    return type+str(order)+'.pdf'

@api_view(['GET'])
def mainprint(request,order):
    makepdf(order,"main")
    return JsonResponse({'state':'200'})

def orderprint(request,order):
    makepdf(order,"waiter")
    return JsonResponse({'state':'200'})


def makepdf(order,type):

    options = {
    'margin-top': '0',
    'margin-left': '0',
        }    
    try:
        orderUrl = config.url+getLinkType(type)+'/'+str(order)
        file = config.loc+'/'+ getPdfName(type,order)
        pdfkit.from_url(orderUrl,file , options=options)
        printPdf(file,type)
    except:
        return "made"