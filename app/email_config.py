from fastapi_mail import FastMail, ConnectionConfig
from pydantic import BaseModel
import os

class EmailConfig(BaseModel):
    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int = 587
    mail_server: str = "smtp.gmail.com"
    mail_starttls: bool = True
    mail_ssl_tls: bool = False

# Global email configuration
email_config = EmailConfig(
    mail_username=os.getenv("MAIL_USERNAME", ""),
    mail_password=os.getenv("MAIL_PASSWORD", ""),
    mail_from=os.getenv("MAIL_FROM", "test@example.com"),  # Default fallback
    mail_port=int(os.getenv("MAIL_PORT", 587)),
    mail_server=os.getenv("MAIL_SERVER", "smtp.gmail.com"),
    mail_starttls=bool(os.getenv("MAIL_TLS", True)),
    mail_ssl_tls=bool(os.getenv("MAIL_SSL", False)),
)

def get_mail_config() -> ConnectionConfig:
    return ConnectionConfig(
        MAIL_USERNAME=email_config.mail_username,
        MAIL_PASSWORD=email_config.mail_password,
        MAIL_FROM=email_config.mail_from,
        MAIL_PORT=email_config.mail_port,
        MAIL_SERVER=email_config.mail_server,
        MAIL_STARTTLS=email_config.mail_starttls,
        MAIL_SSL_TLS=email_config.mail_ssl_tls,
    )

# Global FastMail instance - only create if email is configured
fm = None
if email_config.mail_username and email_config.mail_password:
    fm = FastMail(get_mail_config())