from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.utils import timezone
# Create your models here.
FUNCTION_CHOICES = (
    ("1","Harvest"),
    ("2","Pruning"),
    ("3","Scouting"),
    ("4","Other"),
)
class FieldWorker(models.Model):
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100,blank=False)
    function = models.CharField(max_length=1,choices = FUNCTION_CHOICES, default='4')
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['created_at']