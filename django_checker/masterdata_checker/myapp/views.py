from django.shortcuts import render
from pybis import Openbis
from myapp.utils import name_checker, content_checker, entity_checker
import logging

# Get an instance of the logger for the app (replace 'myapp' with your app name)
logger = logging.getLogger('myapp')

def homepage(request):
    context = {}
    if request.method == "POST":
        if "upload" in request.POST and request.FILES.get("file"):
            uploaded_file = request.FILES["file"]
            # Check file extension
            if uploaded_file.name.endswith(('.xls', '.xlsx')):
                try:
                    
                    url = f"https://devel.datastore.bam.de/"
                    o = Openbis(url)
                    o.login("cmadaria", "Berlin.2024", save_token=True)
                    
                    file_name = uploaded_file.name

                    result_name, code, name_ok = name_checker(file_name)
                    result_content = str(content_checker(uploaded_file, name_ok))
                    result_entity = str(entity_checker(uploaded_file, o))
                    logger.info(f"Type {type(file_name)} of file {file_name}")
                    result_format = "CHECKED NAME:" + "\n----------------------------\n" + result_name + "\n" + "\nCHECKED CONTENT:" + "\n----------------------------\n" + result_content + "\n" + "\nCHECKED ENTITY" + "\n----------------------------\n" + result_entity


                    context["result"] = result_format
                    context["file_name"] = file_name
                    context["code"] = code

                except Exception as e:
                    context["error"] = f"Error processing file: {str(e)}"
            else:
                context["error"] = "Invalid file type. Only .xls and .xlsx files are allowed."

    return render(request, 'homepage.html', context)

def masterdata_visualizer(request):
    return render(request, 'homepage.html', {'page': 'visualizer'})