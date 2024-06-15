from django.views.generic import DetailView

from logmail.models import LogMail


class LogMailDetailView(DetailView):

    model = LogMail
