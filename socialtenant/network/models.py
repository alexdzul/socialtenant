from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Post(models.Model):
    content = models.TextField(verbose_name=_("Contenido"))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Creado por"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Publicación")
        verbose_name_plural = _("Publicaciones")

