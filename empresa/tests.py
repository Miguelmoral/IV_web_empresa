from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Datos

class TestIntroduccionValores(TestCase):

    def test_formulario(self):
        e = Datos(nombre_empresa = "Empresatest", persona = "Personaprueba", pub_date = timezone.now(), puntuacion = "5")
        e.save()
        self.assertEqual(e.nombre_empresa, "Empresatest")
