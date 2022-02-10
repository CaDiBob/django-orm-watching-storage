from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import get_duration, format_duration


def storage_information_view(request):
    non_closed_visits = list()
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        one_visit = {
                'who_entered': visit.passcard,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(get_duration(visit)),
            }
        non_closed_visits.append(one_visit)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
