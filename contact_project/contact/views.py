from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactManualForm, ContactModelForm

def contact_manual(request):
    if request.method == "POST":
        form = ContactManualForm(request.POST)
        if form.is_valid():
            # save manually
            from .models import Contact
            Contact.objects.create(**form.cleaned_data)
            messages.success(request, "Message sent successfully (Manual)!")
            return redirect("contact_manual")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ContactManualForm()
    return render(request, "contact/manual_form.html", {"form": form})


def contact_modelform(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully (ModelForm)!")
            return redirect("contact_modelform")
        else:
            messages.error(request, "Please correct the errors.")
    else:
        form = ContactModelForm()
    return render(request, "contact/model_form.html", {"form": form})
