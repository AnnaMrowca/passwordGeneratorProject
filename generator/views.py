from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'generator/home.html')#użytkownik wchodzi na stronę

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    how_long = int(request.POST.get("length"))  # użytkownik wysłał formularz i przetwarzamy go
    lower_letters = string.ascii_lowercase
    numbers = string.digits
    special_chars = string.punctuation
    upper_letters = string.ascii_uppercase

    password = ''
    for i in range(how_long):
        if request.POST.get("uppercase"):
            password += random.choice(upper_letters)
        if request.POST.get("specialchars"):
            password += random.choice(special_chars)
        if request.POST.get("numbers"):
            password += random.choice(numbers)
    finalPassword = ''.join(random.choice(password + lower_letters) for i in range(how_long))

    # views zawsze muszą coś zwaracać, zawsze musi być return !!!!
    return render(request, 'generator/password.html', {'password': finalPassword})
