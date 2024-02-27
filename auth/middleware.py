import jwt
from  users.models import User
from auth.utils.error import errorHandler


class IsAuthenticatedUser:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, req):
        path = req.path
        print(path)
        if not path == "/api/login/":
            token = req.COOKIES.get("token")
            if token is None:
                print("called 0")
                return errorHandler("Login to View..!", 403)
            try:
                payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
            except:
                print("called 1")
                return errorHandler("Login to Continue..!", 403)
            user = User.objects.filter(id=payload["id"]).first()
            req.user = user
            response = self.get_response(req)
            return response
        return self.get_response(req)

