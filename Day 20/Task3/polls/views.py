from django.http import HttpResponse    
from .models import user
from django.template import loader
from django.shortcuts import redirect
from .models import FormModel
from .models import LoginModel
from .models import SignupModel
from .models import ContactModel
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.conf import settings

def main(request):
    return render(request, "polls/index.html")

def index(request):
    my_users = user.objects.all().values()
    template = loader.get_template('polls/user_list.html')
    context = {
        'my_users': my_users,        
    }
    return HttpResponse(template.render(context, request))

from django.shortcuts import render
from .forms import InputForm
def home_view(request):
    context={}
    context['form']=InputForm()
    return render(request, "polls/home.html", context)

def form_view(request):
    if request.method=="POST":
        print(request.POST)#Prints the posted data as a queryDict
        title=request.POST.get("title")
        description=request.POST.get("description")
        x=FormModel(title=title, description=description)
        x.save()
    
    return render(request, "polls/forms.html")

   
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = LoginModel.objects.get(username=username, is_active=True)
        except LoginModel.DoesNotExist:
            messages.error(request, "Invalid username or password")
        else:
            # 🔥 password check (IMPORTANT)
            if check_password(password, user.password):
                # 🔥 session set
                request.session["user_id"] = user.id
                request.session["username"] = user.username

                messages.success(request, f"Welcome {username}!")
                return redirect("main")
            else:
                messages.error(request, "Invalid username or password")
    
    return render(request, "polls/login.html")

def signup_view(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if LoginModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        LoginModel.objects.create(
            username=username,
            password=make_password(password)
        )

        messages.success(request, "Signup successful. Please login.")
        return render(request, "polls/login.html")
    
       
    return render(request, "polls/signup.html")

def logout_view(request):
    request.session.flush()
    return redirect("main")

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save in database
        ContactModel.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send thank you email
        send_mail(
            subject="Thank You For Contacting Us",
            message=f"Hi {name},\n\nThank you for reaching out to us.\nWe received your message:\n\n{message}\n\nWe will contact you soon.\n\n- Aayush",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("main")

    return render(request, "polls/contact.html")
