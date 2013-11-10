from django.db import models

class Rank(models.Model):
    name = models.CharField(('Name'), max_length=30, blank=True)
    participated = models.CharField('Rozegrane', max_length=30)
    win = models.CharField('Wygrane', max_length=30)
    defeat = models.CharField('Przegrane', max_length=30)
    survive = models.CharField('Przetrwane', max_length=30)
    destroyed = models.CharField('Zniszczone', max_length=30)
    spoted = models.CharField('Wykryte', max_length=30)
    shootPercent = models.CharField('PTrafien', max_length=30)
    dmg = models.CharField('Obrazenia', max_length=30)
    ocupated = models.CharField('PktPrzejecia', max_length=30)
    defense = models.CharField('PktObrony', max_length=30)
    exp = models.CharField('Doswiadczenie', max_length=30)
    severalExp = models.CharField('SrDoswiadczenie', max_length=30)
    maxExp = models.CharField('MaxDoswiadczenie', max_length=30)
    date = models.DateTimeField('Date', auto_now_add=True)

    class Meta:
        verbose_name = "Ranking"
        verbose_name_plural = "Rankingi"

    def __unicode__(self):
        return self.name

class RankLive(models.Model):
    name = models.CharField(('Name'), max_length=30, blank=True)
    participated = models.CharField('Rozegrane', max_length=30)
    win = models.CharField('Wygrane', max_length=30)
    defeat = models.CharField('Przegrane', max_length=30)
    survive = models.CharField('Przetrwane', max_length=30)
    destroyed = models.CharField('Zniszczone', max_length=30)
    spoted = models.CharField('Wykryte', max_length=30)
    shootPercent = models.CharField('PTrafien', max_length=30)
    dmg = models.CharField('Obrazenia', max_length=30)
    ocupated = models.CharField('PktPrzejecia', max_length=30)
    defense = models.CharField('PktObrony', max_length=30)
    exp = models.CharField('Doswiadczenie', max_length=30)
    severalExp = models.CharField('SrDoswiadczenie', max_length=30)
    maxExp = models.CharField('MaxDoswiadczenie', max_length=30)
    date = models.DateTimeField('Date', auto_now_add=True)

    class Meta:
        verbose_name = "RankingLive"
        verbose_name_plural = "RankingiLive"

    def __unicode__(self):
        return self.name