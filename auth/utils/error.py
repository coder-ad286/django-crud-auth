from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

def errorHandler(msg,statusCode):
    response = Response({
        "success" : False,
        "message" : msg,
    },status=statusCode)
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}
    response.render()
    return response