from django.db import models
import time


class BaseFiled(models.Model) :
    create_at = models.TextField(default=time.time())

    class Meta :
        abstract = True