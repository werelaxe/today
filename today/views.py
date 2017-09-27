from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response

from today.serialization import TodayQuerySchema
from today.service import get_today
from logging import getLogger, FileHandler, INFO, Formatter

logger = getLogger(__name__)
logger.setLevel(INFO)
local_handler = FileHandler("log")
local_handler.setFormatter(Formatter("%(asctime)s  %(message)s"))
logger.addHandler(local_handler)


def log_request(request):
    path = request.path
    host = request.get_host()
    user_agent = str(request.environ.get("HTTP_USER_AGENT", None))
    logger.info(" ".join([path, user_agent, host]))


def get_today_celebrate(request):
    log_request(request)
    main_template = loader.get_template("main.html")
    date = TodayQuerySchema().load(request.GET).data.date
    return HttpResponse(main_template.render(
        context={
            "today": get_today(date),
            "current_date": date.strftime("%d.%m.%Y"),
        },
        request=request,
    ))


@api_view(["GET"])
def get_raw_today_celebrate(request):
    log_request(request)
    date = TodayQuerySchema().load(request.GET).data.date
    return Response(get_today(date))
