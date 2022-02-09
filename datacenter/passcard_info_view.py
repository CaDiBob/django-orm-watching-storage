from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long


def passcard_info_view(request, passcode):
    this_passcard_visits = list()
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard__passcode=passcard.passcode)
    for visit in visits:
        one_visit = {
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(visit, minutes=60),
            }
        this_passcard_visits.append(one_visit)
    context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
