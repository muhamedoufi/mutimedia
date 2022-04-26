from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class PatientConfig(AppConfig):
    name = 'patient'

class SuiteConfig(DjangoSuitConfig):
    # layout = "horizontal" 
    # vous pouvez utiliser 
    layout = "vertical"
