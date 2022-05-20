from datetime import datetime
from distutils.dir_util import mkpath

from django.http import HttpResponse
from django.conf import settings

LOG_VOLUME_ROOT = '/log_data_volume'


def index(req):
    return HttpResponse(f"<h1>Hello from {settings.SERVER_NAME}</h1>")


def log(req):
    mkpath(LOG_VOLUME_ROOT)
    with open(f"{LOG_VOLUME_ROOT}/log.txt", "a+") as log_file:
        log_file.write(f"Received log request at {datetime.now().isoformat()}\n")
        log_file.seek(0)
        return HttpResponse("</br>".join(log_file.readlines()))
