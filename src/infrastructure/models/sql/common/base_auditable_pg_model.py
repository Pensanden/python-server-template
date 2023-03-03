from django.db import models

from pg_user_model import PgUserModel as UserModel


class AuditablePgModel(models.Model):
    created_by_user = models.ForeignKey(to=UserModel, on_delete=models.PROTECT, related_name='+')
    last_update_by_user = models.ForeignKey(to=UserModel, on_delete=models.PROTECT, related_name='+')

    class Meta:
        abstract = True
