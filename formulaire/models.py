from django.db import models


class Utilisateur(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.email




