from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if 'title' not in postData or len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters."
        if 'network' not in postData or len(postData['network']) < 2:
            errors["network"] = "Network should be at least 2 characters."
        if 'description' not in postData or len(postData['description']) < 5:
            errors["description"] = "Description should be at least 5 characters"
        return errors
        
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()