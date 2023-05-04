import smtplib
from email.message import EmailMessage


async def send_password_reset_email(email: str, token: str):
    email_address = "notate.sender@gmail.com"  # ваш адрес электронной почты
    email_password = "alwraoqkfuzwmfgk"  # пароль вашего аккаунта

    # создание письма
    msg = EmailMessage()
    msg["Subject"] = "Password reset"
    msg["From"] = email_address
    msg["To"] = email

    # здесь необходимо добавить ссылку на ваш сайт, где будет размещена страница сброса пароля
    reset_link = f"https://todo.kolotech.space/user/password-reset/{token}"

    msg.set_content(
        f"""
        Hi,

        We received a request to reset your password. Please follow the link below to reset your password:

        {reset_link}

        If you did not request a password reset, please ignore this email.

        Best regards,
        Your App Name
        """
    )

    # отправка письма
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
