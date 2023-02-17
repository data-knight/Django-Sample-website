from traceback import print_exception, print_tb
from django.shortcuts import( render, redirect, get_object_or_404,HttpResponseRedirect)
# from rest_framework.response import Response
from crudoperations.forms import StudentForm  
from django.http import HttpResponse, JsonResponse
from crudoperations.models import Students


# Create your views here.
# def api_response(request):
#     print("rest-ap")
#     context ={"header":"Welcome Knight"}
#     return render (request, "home.html", context)

# def json_response(request):
#     success = "API Hit Sucessfully"
#     return JsonResponse({"status":success})

# @csrf_exempt
# def add_data(request):
#     student = Students()
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     marks = request.POST.get('marks')
#     student.name = name
#     student.email = email
#     student.marks = marks
#     student.save()
#     return JsonResponse({"status":"success"})

def studs(request):  
    if request.method == "POST":  

        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    students = Students.objects.all()  
    return render(request,"show.html",{'students':students})  
def edit(request, id):  
    student = Students.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})  

# def update(request, id):  
#     student = Students.objects.all(id=id)  
#     form = StudentForm(request.POST, instance = student)  
#     if form.is_valid():  
#         form.save()  
#         return redirect("/show")  
#     return render(request, 'edit.html', {'student': student})   

def update(request, id): 
    if request.method=="POST":
        print("Function is working") 
        name = request.POST.get('name')
        email = request.POST.get('email')
        marks = request.POST.get('marks')

        students=Students(id=id,name=name,email=email,marks=marks)

        students.save()
        return redirect("/show")  



def delete(request,id):  
    student = Students.objects.get(id=id)  
    student.delete()  
    return redirect("/show")  