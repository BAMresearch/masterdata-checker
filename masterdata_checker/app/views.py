import datetime
import logging
import tempfile
import uuid

from bam_masterdata.cli.cli import run_checker
from bam_masterdata.logger import log_storage, logger
from django.conf import settings
from django.contrib.auth import logout
from django.core.cache import cache
from django.shortcuts import redirect, render
from pybis import Openbis

from masterdata_checker.app.utils import encrypt_password, get_openbis_from_cache


def homepage(request):
    # Check if the user is logged in
    o = get_openbis_from_cache(request)
    if not o:
        logger.info("User not logged in, redirecting to login page.")
        return redirect("login")

    context = {}

    if request.method == "POST" and "upload" in request.POST:
        uploaded_file = request.FILES.get("file")
        context["file"] = uploaded_file.name
        if not uploaded_file:
            context["error"] = "No file uploaded."
            return render(request, "homepage.html", context)
        if not uploaded_file.name.endswith((".xls", ".xlsx")):
            context["error"] = (
                "Invalid file type. Only .xls and .xlsx files are allowed."
            )
            return render(request, "homepage.html", context)

        try:
            # Clear previous logs
            log_storage.clear()

            # Save file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
                for chunk in uploaded_file.chunks():
                    tmp.write(chunk)
                tmp_path = tmp.name

            # Run checker (with `incoming` mode)
            run_checker(file_path=tmp_path, mode="incoming")

            # Store logs in context for rendering
            log_storage.append(
                {
                    "event": f"Checked: {uploaded_file.name}",
                    "timestamp": datetime.datetime.now().isoformat(),
                    "level": "info",
                }
            )

            # Clean up for template rendering
            context_logs = []
            for log in log_storage:
                context_log = {}
                for k, v in log.items():
                    if k in ["event", "timestamp", "level"]:
                        # bootstrap has a danger level instead of error
                        if k == "level" and v == "error":
                            v = "danger"
                        elif k == "level" and v == "debug":
                            continue  # Skip debug logs in the UI
                        context_log[k] = v
                context_logs.append(context_log)
            # And store them in the context
            context["logs"] = context_logs
        except Exception as e:
            logger.exception("Error during checker execution")
            # Store raised errors in context for rendering
            context["error"] = str(e)

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

        except Exception as e:
            logger.error(f"Login failed for user '{username}': {e}", exc_info=True)
            error = "Invalid username or password."

    return render(request, "login.html", {"error": error})


def logout_view(request):
    request.session.flush()  # Clear all session data
    logout(request)
    return redirect("login")
