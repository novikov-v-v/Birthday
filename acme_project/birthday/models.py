from django.db import models

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения', validators=(real_age,))

    class Meta:
        verbose_name = 'день рождения'
        verbose_name_plural = 'Дни рождения'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
