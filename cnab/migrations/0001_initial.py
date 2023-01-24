# Generated by Django 4.1.3 on 2023-01-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Documentation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.IntegerField(
                        choices=[
                            (1, "Debito"),
                            (2, "Boleto"),
                            (3, "Financiamento"),
                            (4, "Credito"),
                            (5, "Emprestimo"),
                            (6, "Vendas"),
                            (7, "Ted"),
                            (8, "Doc"),
                            (9, "Aluguel"),
                        ]
                    ),
                ),
                ("date", models.DateField()),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=12)),
                ("hour", models.TimeField()),
                ("store_owner", models.CharField(max_length=15)),
                ("store_name", models.CharField(max_length=20)),
            ],
        ),
    ]