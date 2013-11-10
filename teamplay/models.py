from django.db import models

class Team(models.Model):

    CHOICES=[('7 vs 7', '7 vs 7'),
             ('Kompania VIII tieru', 'Kompania VIII tieru'),
             ('Kompania VI tieru', 'Kompania VI tieru'),
             ('Kompania IV tieru', 'Kompania IV tieru')]

    title = models.CharField('Tytul', max_length=40, choices=CHOICES)
    leader = models.CharField('Prowadzacy', max_length=60, blank=True)
    persons = models.TextField(verbose_name='Osoby', blank=True)
    win = models.CharField('Zwyciestwa', max_length=3, blank=True)
    draw = models.CharField('Remisy', max_length=3, blank=True)
    defeat = models.CharField('Przegrane', max_length=3, blank=True)

    date = models.DateTimeField('Data Kompanii')

    class Meta:
        verbose_name = "Kompania"
        verbose_name_plural = "Kompanie"

    def __unicode__(self):
        return self.title