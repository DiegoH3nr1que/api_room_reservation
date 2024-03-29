from django.shortcuts import redirect, render
from bible_verse import main
from datetime import datetime
from django.views import View
from .models import ClassromEntity
from .repositories import ClassroomRepository
from .serializer import ClassroomSerializer
from .forms import ClassForm

# Create your views here.
class ClassView(View):
    def get(self, request):
        verse = main.get_bible_verse()
        repository = ClassroomRepository(collectionName='classrooms')
        classrooms = list(repository.getAll())
        serializer = ClassroomSerializer(data=classrooms, many=True)
        if (serializer.is_valid()):
            modelClassroom = serializer.save()
            print(serializer.data)
        else:
            print(serializer.errors)
        return render(request, "home.html", {"classrooms":modelClassroom, "verse":verse})

class ClassCreate(View):
    def get(self, request):
        classForm = ClassForm()

        return render(request, "form.html", {"form":classForm})
    
    def post(self, request):
        classroomForm = ClassForm(request.POST)
        if classroomForm.is_valid():
            serializer = ClassroomSerializer(data=classroomForm.data)
            if (serializer.is_valid()):
                repository = ClassroomRepository(collectionName='classrooms')
                repository.insert(serializer.data)
            else:
                print(serializer.errors)
        else:
            print(classroomForm.errors)

        return redirect('Class View')


