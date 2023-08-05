
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from django.utils.translation import ugettext_lazy as _

from pure_pagination import Paginator

from reviews.models import Review
from reviews.forms import ReviewForm
from reviews.lib import send_new_review_notification


def index(request):

    reviews = Review.objects.filter(is_active=True)

    paginator = Paginator(reviews, per_page=10, request=request)

    context = {
        'reviews': paginator.page(request.GET.get('page', 1))
    }

    return render(request, 'reviews/index.html', context)


@require_GET
def get_new_review_modal(request):

    user = request.user

    if user.is_authenticated:
        initial = {
            'name': user.get_full_name(),
            'email': user.email,
        }
    else:
        initial = {}

    form = ReviewForm(initial=initial)

    context = {'form': form}

    return render(request, 'reviews/new_review_modal.html', context)


@require_POST
def add_review(request):

    form = ReviewForm(request.POST)

    if form.is_valid():

        review = form.save(commit=False)

        if request.user.is_authenticated:
            review.user = request.user

        review.save()

        send_new_review_notification(review)

        return HttpResponse(_('Review was successfully sent'))

    context = {'form': form}

    return render(request, 'reviews/new_review_form.html', context, status=400)
