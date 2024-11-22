from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import Personal
from django.shortcuts import get_object_or_404, redirect
def home(request):
    personal_list = Personal.objects.all()
    return render(request, 'index.html', {'Personal': personal_list})

def getinfo(request):
    if request.method == 'POST':
        print("HI")
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_num = request.POST.get('phone_num')
        address = request.POST.get('address')
        image = request.FILES.get('image')
       
        print(f"Name: {name}, Email: {email}, Phone: {phone_num}, Address: {address}")

        if image:
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
        
        personal = Personal(
            name=name,
            email=email,
            phone_num=phone_num,
            address=address,
            image=image  
        )
        personal.save()

        return HttpResponseRedirect('/')

    return HttpResponse("Invalid request method. Please submit the form.")

def delete_info(request,id):
    queryset = get_object_or_404(Personal, id=id)
    queryset.delete()
    print(id)
    return HttpResponseRedirect('/')

def about(request):
    return HttpResponse("<h1> This is about page </h1>")

def update_info(request, id):
   
    personal = get_object_or_404(Personal, id=id)

    if request.method == "POST":
       
        personal.name = request.POST.get('name')
        personal.email = request.POST.get('email')
        personal.phone_num = request.POST.get('phone_num')
        personal.address = request.POST.get('address')
        
        # If there's an image, update it as well
        if request.FILES.get('image'):
            personal.image = request.FILES.get('image')
        
        personal.save()

        # Redirect to the home page or a success page
        return redirect('/')

    return render(request, 'update.html', {'personal': personal})

 