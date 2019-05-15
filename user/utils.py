import jwt
from functools import wraps

def login_decorator(f):
    @wraps(f)
    def decorated_fuction(*args, **kwargs):
        access_token = request.headers.get('AUthorization')
        if access_token is not None:
            try:
                payload = jwt.decode(access_token, wtw_secret, 'HS256')
            except jwt.InvalidTokenError:
                payload = None

            if payload is not None: return HttpResponse(status=401)
            return f(*args, **kwargs)
        else:
            return HttpResponse(status=401)

        return f(*args, **kwargs)
    return decorated_fuction
    
