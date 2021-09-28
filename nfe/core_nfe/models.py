from django.db import models


class Country(models.Model):
    id = models.BigAutoField(db_column='id_pais', null=False, primary_key=True)
    name = models.CharField(db_column='tx_nome', null=False, max_length=104)
    created_at = models.DateTimeField(db_column='dt_cadastro', auto_now_add=True)
    modified_at = models.DateTimeField(db_column='dt_ultima_alteracao', auto_now=True)

    class Meta:
        db_table = 'pais'
        managed = True

    def __str__(self):
        return self.name
