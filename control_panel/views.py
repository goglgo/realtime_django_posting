from django.shortcuts import render

# Create your views here.
def index_page(request):
    template_name = "index_page.html"

    context = {

    }
    return render(request, template_name, context)