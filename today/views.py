from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response

from today.serialization import TodayQuerySchema
from today.service import get_today


def get_today_celebrate(request):
    main_template = loader.get_template('main.html')
    date = TodayQuerySchema().load(request.GET).data.date
    return HttpResponse(main_template.render(
        context={
            'today': get_today(date),
            'current_date': date.strftime("%d.%m.%Y"),
        },
        request=request,
    ))


@api_view(['GET'])
def get_raw_today_celebrate(request):
    date = TodayQuerySchema().load(request.GET).data.date
    return Response(get_today(date))
