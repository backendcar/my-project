from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days = {
    'saturday': 'this is satureday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': None
}


def dynamic_days(reqeust, day):
    day_data = days.get(day)

    context = {
        "data": day_data,
        "day": f'selected DAY is {day}'
    }

    return render(reqeust, 'challenges/challenge.html', context)


def days_list(request):

    days_list = list(days.keys())
    context = {
        'days': days_list
    }

    return render(request, "challenges/index.html", context)


def dynamic_days_by_number(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('day does not exists')
    redirect_day = days_names[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day])
    return HttpResponseRedirect(redirect_url)
    # return HttpResponse(day)
