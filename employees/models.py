from django.contrib.auth.models import User
from django.db import models


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, related_name="receiver")
    message = models.CharField(max_length=300, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)

