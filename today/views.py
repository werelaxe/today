from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response

from today.service import get_today


def get_today_celebrate(request):
    main_template = loader.get_template('main.html')
    return HttpResponse(main_template.render(
        context={
            'today': get_today()
        },
        request=request,
    ))


@api_view(['GET'])
def get_raw_today_celebrate(request):
    return Response(get_today())
