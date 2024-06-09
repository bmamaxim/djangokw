import datetime

from django.core.mail import send_mail

from config import settings
from logmail.models import LogMail
from mailing.models import MailingLetters


def _send_mail(message_settings, message_client):
    result = send_mail(
        subject=message_settings.messege.subject,
        message=message_settings.messege.messege,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[message_client.email],
        fail_silently=False
    )

    LogMail.objects.create(
        status=LogMail.STATUS_SUCCESS if result else LogMail.STATUS_FAILED,
        settings=message_settings,
        client_id=message_client.pk
    )


def send_mails():
    datetime_now = datetime.datetime.now(datetime.timezone.utc)
    for mailing_letters in MailingLetters.objects.filter(status=MailingLetters.STATUS_STARTED):
        if (datetime_now > mailing_letters.start) and (datetime_now < mailing_letters.end):
            for mailing_client in mailing_letters.clients.all:
                mailing_log = LogMail.objects.filter(client=mailing_client.pk,
                                                     settings=mailing_letters)
                if mailing_log.exists():
                    last_try_date = mailing_log.order_by('-last_try').first().last_try

                    if mailing_letters.period == MailingLetters.PERIOD_DAILY:
                        if (datetime_now - last_try_date).days >= 1:
                            _send_mail(mailing_letters, mailing_client)
                    elif mailing_letters.period == MailingLetters.PERIOD_WEEKLY:
                        if (datetime_now - last_try_date).days >= 7:
                            _send_mail(mailing_letters, mailing_client)
                    elif mailing_letters.period == MailingLetters.PERIOD_MONTHLY:
                        if (datetime_now - last_try_date).days >= 28:
                            _send_mail(mailing_letters, mailing_client)
                else:
                    _send_mail(mailing_letters, mailing_client)
