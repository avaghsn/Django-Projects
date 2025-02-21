from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review

# Create your views here.


def review(request):
    """
    method gives access to the method that was used for submitting the data
    .POST gives access to the data itself
    POST is a dict where keys are the names sat on the inputs in the form,
    and values are the entered values
    post req is meant to submit data to the server, 
    instead of returning a rendered template we redirect to a different url with get req
    and that url will render a template

    if request.method == "POST":
        entered_username = request.POST["username"] .POST gives us access to the key

        if entered_username == "" and len(entered_username) >= 100:
            return render(request, "reviews/review.html", {
                "has_error": True
            })

        return HttpResponseRedirect("/thank-you")

    return render(request, "reviews/review.html", {
        "has_error": False
    })

    """
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            """
        form.is_valid() is defines in Form class and does 3 things:
        1- validating the input(checking if it is not empty)
        2- returns true if form is valid
        3- if data is valid, it'll populate another field with that valid data
        """
            review = Review(
                user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating'])
            review.save()  # field that contains cleaned data
            return HttpResponseRedirect("/thank-you")
    else:
        """else it is a GET request: """
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
