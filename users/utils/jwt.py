import jwt
import datetime
from rest_framework.response import Response


def sendToken(user):
    payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, "secret_key",algorithm="HS256").decode("utf-8")

    response = Response({
        "success": True,
        "message": "User Login Successfully...!",
        "token": token
    })

    expiry_time = 3 * 24 * 60 * 60
    response.set_cookie(key="token", secure=True, value=token, httponly=True, max_age=expiry_time)
    
    return response
