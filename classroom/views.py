from django.shortcuts import render
from datetime import datetime
from django.views import View

# Create your views here.
class ClassView(View):
    def get(self, request):
        return render(request,'Home.html')
    
# class ClassDelete(View):
#     def delete(self, request):
#         return render(request, "Home.html")
