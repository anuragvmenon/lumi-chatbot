from django.db import models

class Mood(models.Model):
    user_id = models.CharField(max_length=255)
    emotion = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_id} - {self.emotion} at {self.timestamp}'
