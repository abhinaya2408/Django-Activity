from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, "home.html")

def colleges(request):
    college_list = ["SVEW", "VIT", "BVRICE"]
    return render(request, "colleges.html", {
        "colleges": college_list
    })

def students(request):
    student_list = [
        {"sno": 1, "name": "Anu", "branch": "CSE", "age": 17},
        {"sno": 2, "name": "Ravi", "branch": "ECE", "age": 19},
        {"sno": 3, "name": "Sita", "branch": "IT", "age": 18},
    ]
    return render(request, "students.html", {
        "students": student_list
    })

def address(request):
    return render(request, "address.html")

def contact(request):

    department_emails = {
        "cse": "abhinayasridaggula058@gmail.com",
        "ece": "dangudubiyyampavani@gmail.com",
        "it": "dpavani5555@gmail.com",
    }

    if request.method == "POST":
        department = request.POST.get("department")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        print("Selected Dept:", department)

        receiver_email = department_emails.get(department)
        print("Receiver Email:", receiver_email)

        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [receiver_email],
                fail_silently=False,
            )
            print("EMAIL SENT SUCCESSFULLY")
        except Exception as e:
            print("EMAIL ERROR:", e)

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")