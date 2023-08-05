
from django.core.mail import mail_managers
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.contrib.sites.models import Site


def send_new_review_notification(review):

    subject = _('New review #{}').format(review.id)

    current_site = Site.objects.get_current()

    context = {'review': review, 'site': current_site}

    template_name = 'reviews/new_review_notification.html'

    html = render_to_string(template_name, context)

    mail_managers(subject=subject, message='', html_message=html)
