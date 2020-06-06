from django.shortcuts import render
import string
import requests
import datetime
from .forms import DateForm
import arrow
import calendar
# Create your views here.


def calendarHomeView(request):
    if request.method == "POST":
        weekdays = {
            1: "MONDAY",
            2: "TUESDAY",
            3: "WEDNESDAY",
            4: "THURSDAY",
            5: "FRIDAY",
            6: "SATURDAY",
            7: "SUNDAY",
        }
        print(request.POST)
        form = DateForm(request.POST)
        if form.is_valid():

            date = form.cleaned_data['date']
            new_year = date.replace(month=1, day=1)
            next_year = date.replace(day=1, month=1, year=date.year+1)

            # ISO day, week, year
            isoday = weekdays[date.isoweekday()]
            isoweek = date.isocalendar()[1]
            isoyear = date.isocalendar()[0]

            # check if leap year
            isleap = calendar.isleap(date.year)

            # nth day since 1/1/1
            ordinal = date.toordinal()

            # Added 1 since it counts from 0
            days_since_new_year = (date-new_year) + datetime.timedelta(days=1)
            nthday = days_since_new_year.days

            # Time to new year
            # Subtracted 1 since it counts from 0
            days_to_next_year = (next_year-date) - datetime.timedelta(days=1)
            days_remaining = days_to_next_year.days
            weeks_remaining = days_to_next_year.days//7

            # HTML Calendar
            hc = calendar.HTMLCalendar(calendar.SUNDAY)
            html_cal = hc.formatmonth(date.year, date.month)

            # Historical Events
            events = requests.get(
                f"http://history.muffinlabs.com/date/{date.month}/{date.day}").json()

            events = events['data']['Events']
            hist_events = list()

            for e in events:
                hist_events.append(e['html'])
                hist_events = hist_events[::-1]
            context = {
                "context": {
                    "date_form": form.as_p(),
                    "date": date,
                    "new_year": new_year,
                    "isoday": isoday,
                    "isoweek": isoweek,
                    "isoyear": isoyear,
                    "isleap": isleap,
                    "ordinal": ordinal,
                    "nthday": nthday,
                    "days_remaining": days_remaining,
                    "weeks_remaining": weeks_remaining,
                    "html_cal": html_cal,
                    "hist_events": hist_events,

                }
            }

    else:
        form = DateForm()
        context = {
            "date_form": form
        }
    return render(request, 'calendar_home.html', context)
