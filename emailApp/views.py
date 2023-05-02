from .forms import EmailForm
from django.shortcuts import render
from django.core.mail import EmailMessage


def send(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        subject = request.POST.get('subjectubject')
        receiver_email = request.POST.get('receiver_email')
        message = request.POST.get('message')
        email = EmailMessage(subject, message, to=[receiver_email])
        email.send()
    else:
        form = EmailForm()
    return render(request, 'email_form.html', {'form': form})
