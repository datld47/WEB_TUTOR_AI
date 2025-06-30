from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.conf import settings 

# Create your views here.

def store_file(file):
    with open(settings.TEMP_DIR / "image.jpg","wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        #print(request.FILES['image'])
        store_file(request.FILES['image'])
        return HttpResponseRedirect("/profiles")