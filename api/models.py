from django.db import models

class History(models.Model):
    job = models.CharField(max_length=60)
    server = models.CharField(max_length=60)
    server_user = models.CharField(max_length=60)
    script = models.CharField(max_length=60)
    terminal = models.CharField(max_length=5000)
    exectime = models.DateTimeField()
    terminal_error = models.CharField(max_length=5000)
    returncode = models.IntegerField()
    def __str__(self):
        return self.name

