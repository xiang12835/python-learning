# coding=utf-8
import os
import requests
import random
import json
import logging
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse


MIMEANY = '*/*'
MIMEJSON = 'application/json'
MIMETEXT = 'text/plain'


def save_tmp_file(f, path):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(memfile, url="http://123.206.180.82/file/upload/", data=None, _headers=None):
    if not _headers:
        _headers = {"Content-Type": "multipart/form-data"}

    ff = memfile.name.split(".")

    r1 = random.randint(1,10000)
    r2 = random.randint(1,10000)

    tmp_path = './tmp_%s_%s.%s' % (r1,r2,ff[-1])

    save_tmp_file(memfile, tmp_path)
    files = {"files": open(tmp_path, 'rb')}

    r = requests.post(url, files=files)
    r_json = r.json()
    logging.info(r_json)
    remote_path = r_json.get("result", {}).get("filePath", None)

    if remote_path:
        os.remove(tmp_path)

    return remote_path


def img_upload(request):
    if request.method == 'POST':
        file_obj = request.FILES[u'files[]']
        screenshot_type = request.POST.get("type")

        if False and screenshot_type:
            screenshot_size = "480x270" if screenshot_type == "0" else "270x480"

        remote_url = upload_file(file_obj)

        if not remote_url:
            response_data = {
                "e": {
                    "code": -1
                }
            }
        else:
            response_data = {
                "files": [
                    {
                        "name": file_obj.name,
                        "type": file_obj.content_type,
                        "size": file_obj.size,
                        "url": remote_url,
                    }
                ]
            }

        response = JSONResponse(response_data, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response
    else:
        return HttpResponse('OK')


class JSONResponse(HttpResponse):
    """JSONResponse -- Extends HTTPResponse to handle JSON format response.

    This response can be used in any view that should return a json stream of
    data.

    Usage:

        def a_iew(request):
            content = {'key': 'value'}
            return JSONResponse(content, mimetype=response_mimetype(request))

    """

    def __init__(self, obj='', json_opts=None, mimetype=MIMEJSON, *args, **kwargs):
        json_opts = json_opts if isinstance(json_opts, dict) else {}
        content = json.dumps(obj, **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)


def response_mimetype(request):
    """response_mimetype -- Return a proper response mimetype, accordingly to
    what the client accepts, as available in the `HTTP_ACCEPT` header.

    request -- a HttpRequest instance.

    """
    can_json = MIMEJSON in request.META['HTTP_ACCEPT']
    can_json |= MIMEANY in request.META['HTTP_ACCEPT']
    return MIMEJSON if can_json else MIMETEXT