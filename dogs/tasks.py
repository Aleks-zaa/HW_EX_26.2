from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_information_about_like(email):
    send_mail('Тема', 'Тело письма', EMAIL_HOST_USER, [email])


@shared_task
def print_any():
    print('Hello, world!')
