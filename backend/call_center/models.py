from django.db import models


class Agent(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Агент',
        help_text='Имя агента',
        unique=True,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return self.name


class Queue(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Очередь',
        help_text='Название очереди',
        unique=True,
        blank=False,
        null=False,
    )
    skill = models.CharField(
        max_length=255,
        verbose_name='Умение',
        help_text='Название Умения',
        blank=False,
        null=False,
    )
    agent = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE,
        verbose_name='Агент',
        blank=False,
        null=False,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'agent'],
                name='unique_agent'
            )
        ]

    def __str__(self) -> str:
        return self.name

