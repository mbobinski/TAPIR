from django.db import models

class News(models.Model):
    title = models.CharField('Tytul', max_length=255)
    publicator = models.CharField('Wystawione', max_length=255, default="a")
    text = models.TextField(verbose_name='Tresc')
    posted_date = models.DateTimeField('Data dodania', auto_now_add=True)

    class Meta:
        verbose_name = "Wiadomosc"
        verbose_name_plural = "Wiadomosci"

    def __unicode__(self):
        return self.title