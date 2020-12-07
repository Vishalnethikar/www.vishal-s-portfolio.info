from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def aboutme(request):
    return render(request,'about.html')
def myworks(request):
    return render(request,'myworks.html')
def Contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact_num=request.POST.get('contact_num')
        country=request.POST.get('country')
        subject=request.POST.get('subject')
        contactme=Contact(name=name,email=email,contact_num=contact_num,country=country,subject=subject,)
        contactme.save()
    return render(request,'contactme.html')