from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "eat no meat for january",
    "febuary": "eat no meat for febuary",
    "march": "eat no meat for march",
    "april": "eat no meat for april",
    "may": "eat no meat for may",
    "june": "eat no meat for june",
    "july": "eat no meat for july",
    "august": "eat no meat for august",
    "september": "eat no meat for september",
    "october": "eat no meat for october",
    "november": "eat no meat for november",
    "december": "eat no meat for december",

}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        cap_mont = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{cap_mont}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(f"<h1>{month} is not supported!</h1>")
