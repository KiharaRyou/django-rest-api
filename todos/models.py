from django.db import models

class Todo(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-is_active', 'created']
