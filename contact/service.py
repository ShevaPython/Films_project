from django.core.mail import send_mail

def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем присылать вам письма',
        'sheva199220@ukr.net',
        [user_email],
        fail_silently=False,
    )