from django.db import models


class Show(models.Model):
    name = models.CharField(max_length=50)
    character = models.ForeignKey(
        'Character',
        on_delete = models.CASCADE,
    )


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.character} is on the show {self.name}'