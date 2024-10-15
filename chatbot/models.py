from django.db import models

class UserMessage(models.Model):
    message = models.TextField()
    recipient = models.CharField(max_length=255)
    is_forwarded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message to {self.recipient}: {self.message}"

