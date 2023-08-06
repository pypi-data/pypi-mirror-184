from django.apps import AppConfig
from django.core.checks import register
from django.utils.translation import gettext_lazy as _

from ob_dj_otp.core.otp import settings_validation


class OTPConfig(AppConfig):
    name = "ob_dj_otp.core.otp"
    verbose_name = _("OTPs")

    def ready(self):
        register(settings_validation.required_installed_apps)
        register(settings_validation.otp_settings_validation)
