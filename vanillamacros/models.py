from django.db import models

class Ability(models.Model):
    abilityName = models.CharField(max_length=50, primary_key=True)
    warcraftClass = models.CharField(max_length=20)

    def __str__(self):
        return self.abilityName

class Macro(models.Model):
    isSuperMacro = models.BooleanField()
    code = models.CharField(max_length=500)
    abilityName = models.ForeignKey(Ability, on_delete=models.CASCADE)

    def __str__(self):
        return self.code        