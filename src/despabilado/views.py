from django.shortcuts import render
from .forms import SignUpForm, ContactForm
# Create your views here.
def home(request):
    title = "Welcome"
    form = SignUpForm(request.POST or None)


    context = {
        "title": title,
        "form": form

    }

    # On form submit and valid
    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")


        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name

        # if not instance.full_name:
        #     instance.full_name = "Bruh"
        instance.save()

        context = {
            "title": "Thank you!"
        }


    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        for key, value in form.cleaned_data.iteritems():
            print key, value

        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        full_name = form.cleaned_data.get("full_name")

    return render(request, "forms.html", context)



