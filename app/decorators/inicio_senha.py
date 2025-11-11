from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, create_access_token
from flask_jwt_extended import  set_access_cookies, set_refresh_cookies, create_refresh_token
from flask import make_response, flash, redirect, url_for
from datetime import timedelta
from functools import wraps

def jwt_refresh(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception:
            try:
                verify_jwt_in_request(refresh=True)
                identity = get_jwt_identity()
                new_access_token = create_access_token(
                    identity=identity,
                    expires_delta=timedelta(minutes=5)
                )
                new_refresh_token = create_refresh_token(
                    identity=identity,
                    expires_delta=timedelta(minutes=15)
                )
                response = make_response(func(*args, **kwargs))
                set_access_cookies(response, new_access_token)
                set_refresh_cookies(response, new_refresh_token)
                return response
            except Exception as e:
                flash(f"Sessão expirada. Faça login novamente.", "error")
                return redirect(url_for("login"))
        return func(*args, **kwargs)
    return wrapper