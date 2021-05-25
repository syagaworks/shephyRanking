import random
import json
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.db.models import Q
from .models import Record


def routing(request):
    if request.method == "POST":
        post = request.POST
        if ("userName" in post) and ("finishTime" in post):
            Record(userName=post["userName"],finishTime=post["finishTime"]).save()
            print("registered")
            order=Record.objects.filter(finishTime__lt=post["finishTime"]).count()
            response = JsonResponse({"text":"あなたの順位は"+str(order+1)+"位です。"})
        else:
            message = "Bad JSON request."
        # response['Access-Control-Allow-Origin'] = 'https://jwspgcr.github.io'
        # response['Access-Control-Allow-Credentials'] = 'true'
    elif request.method == "GET":
        records=list(Record.objects.order_by("finishTime")[:10].values())
        recordsFormatted = []
        for r in records :
            rFormatted={ **r, "reportedDate":r["reportedDate"].strftime("%Y/%m/%d %H:%M:%S")}
            print(rFormatted)
            recordsFormatted.append(rFormatted)
        response = JsonResponse(recordsFormatted,safe=False)
    elif request.method == "OPTIONS":
        response = HttpResponse()
        # response['Access-Control-Allow-Origin'] = 'https://jwspgcr.github.io'
        # response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Headers'] = "Content-Type, Accept, X-CSRFToken"
        response['Access-Control-Allow-Methods'] = "POST, OPTIONS"
    else:
        response = HttpResponse("POST only.")

    return response
