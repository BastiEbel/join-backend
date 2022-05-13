from datetime import date
from django.conf import settings
from django.db import models

# Create your models here.
Todo = "Todo"
DoToday = "Do_Today"
Progress = "Progress"
Done = "Done"

CATEGORY_CHOICES = (
(Todo, "Todo"),
(DoToday, "DoToday"),
(Progress, "Progress"),
(Done, "Done"),
)

class Task(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="Todo")