from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.

def ContactView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # if 'name' in request.POST and 'email' in request.POST and'phone_no' in request.POST and 'Message' in request.POST:
            print("Form is Valid ")
            name = request.POST['name']
            email = request.POST['email']
            phone_no = request.POST['phone_no']
            Message = request.POST['Message']
            print(f"Thanks for contacting us {name} + {email} + {phone_no} + {Message}")

            # sending contact us message to CC grouop
            send_mail(
                'Hello! You got a mail from ' + str(email),
                "Name : " + str(name) + '\n'
                                        f"Email : {str(email)} \n"
                                        f"Phone number : {str(phone_no)} \n"
                                        f"Meassage : {str(Message)} \n",
                settings.EMAIL_HOST_USER,  # 'from@example.com',
                ['krishnadeveloper309@gmail.com'],  # ['to@example.com'],
                fail_silently=False
            )

            # sending confirmation message to Contacted person
            from django.core.mail import EmailMessage
            try:
                response_email = EmailMessage(
                    f'Hello {name.upper()}', #subect
                    f"""Greetings from Logitha Currency Exchange.
                    About Us : 
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                    
                     We have received your Information.
                     We will contact you soon.
                     Your Message is {Message}""", #Body
                settings.EMAIL_HOST_USER, #from mail
                [email], #to mail
                # ['bcc@example.com'],
                reply_to = ['gopi01996@gmail.com'],
                # headers={'Message-ID': 'foo'},
                )
                response_email.send(fail_silently=False)
            except:
                pass
            # if User mail is valid then only we will save the contacted information
            form.save()
            messages.success(request, f"Thanks for contacting us '{name}' we will contact you soon to ur mail '{email}'")
            return redirect('home')
        else:
            messages.success(request, "Invalid Form")
            print("Form is not valid")
            return redirect("/contact/")
    return HttpResponseRedirect("/")
