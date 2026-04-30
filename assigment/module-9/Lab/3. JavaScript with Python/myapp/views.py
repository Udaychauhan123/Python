from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')

        # You can store in DB later
        return redirect('success')
    
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')