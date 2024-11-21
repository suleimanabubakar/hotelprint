from django.apps import AppConfig
import logging
class PrintConfig(AppConfig):
    name = 'print'

    def ready(self):
        from .ipfetch import update_ip
        update_ip()
