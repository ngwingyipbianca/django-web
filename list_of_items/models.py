from django.db import models

class List_of_items(models.Model):
  line_item = models.TextField()
  line_item_description = models.TextField()