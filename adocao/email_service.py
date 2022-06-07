from django.core.mail import send_mail


def send_confirmation_email(adocao):
    content1 = f"Parabéns pela adoção do pet {adocao.pet.name}.\n"
    content2 = f"Adoção no valor mensal de R$ {adocao.donation}.\n"

    subject = "A sua adoção foi realizada com sucesso!"
    message = content1 + content2
    from_email = "adote.um.p3t@gmail.com"
    recipient_list = [adocao.email]

    send_mail(subject, message, from_email, recipient_list)
