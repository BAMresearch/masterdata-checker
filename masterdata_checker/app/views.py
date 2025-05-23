import uuid

from django.conf import settings
from django.contrib.auth import logout
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect, render
from pybis import Openbis

from app.utils import encrypt_password, get_openbis_from_cache


def homepage(request):
    # Check if the user is logged in
    o = get_openbis_from_cache(request)
    if not o:
        return redirect("login")

    context = {}
    return render(request, "homepage.html", context)


def login(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            o = Openbis(settings.OPENBIS_URL)
            o.login(username, password, save_token=True)

            encrypted_password = encrypt_password(password)
            session_id = str(uuid.uuid4())

            request.session["openbis_username"] = username
            request.session["openbis_password"] = encrypted_password
            request.session["openbis_session_id"] = session_id

            cache.set(session_id, o, timeout=60 * 60)  # Cache for 1 hour (adjustable)

            return redirect("homepage")

        except Exception:
            error = "Invalid username or password."

    return render(request, "login.html", {"error": error})


def logout_view(request):
    request.session.flush()  # Clear all session data
    logout(request)
    return redirect("login")
