from django.db import models
import uuid
from copy import copy


class BasePgModel(models.Model):
    __domain_class__ = None

    id = models.UUIDField(primary_key=True, default=uuid.uuid3, editable=False)
    creation_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

    def to_domain(self):
        inst = copy(self.__dict__)
        del inst['_state']
        return self.__domain_class__(
            **inst
        )
