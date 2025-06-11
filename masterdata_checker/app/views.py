import datetime
import tempfile

from bam_masterdata.cli.cli import run_checker
from bam_masterdata.logger import log_storage, logger
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


def homepage(request):
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
                # Skip debug logs in the UI
                if log.get("level") == "debug":
                    continue

                log["timestamp"] = datetime.datetime.fromisoformat(
                    log["timestamp"].replace("Z", "+00:00")
                ).strftime("%H:%M:%S, %d.%m.%Y")

                context_log = {}
                for k, v in log.items():
                    if k in ["event", "timestamp", "level"]:
                        # bootstrap has a danger level instead of error
                        if k == "level" and v == "error":
                            v = "danger"
                        context_log[k] = v
                context_logs.append(context_log)
            # And store them in the context
            context["logs"] = context_logs
        except Exception as e:
            logger.exception("Error during checker execution")
            # Store raised errors in context for rendering
            context["error"] = str(e)

        request.session["checker_logs"] = context.get("logs", [])
        request.session["file"] = uploaded_file.name
        return redirect("homepage")

    # GET request (or after redirect)
    context["logs"] = request.session.pop("checker_logs", None)
    context["file"] = request.session.pop("file", None)
    return render(request, "homepage.html", context)


@require_POST
def clear_logs(request):
    request.session.pop("checker_logs", None)
    return redirect("homepage")
