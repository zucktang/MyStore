from django.db import models

from ..core.abstracts import BaseModel


class AbstractProduct(BaseModel):
    name = models.CharField(
        
    )