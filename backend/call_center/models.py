from django.db import models


class Agent(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Летающий счастье'),
        ('sad', 'Мимолетная грусть'),
        ('excited', 'Буря эмоций'),
        ('calm', 'Спокойный океан'),
        ('angry', 'Ярость внутри'),
        ('confused', 'Загадочная путаница'),
        ('surprised', 'Неожиданный восторг'),
        ('content', 'Довольство моментом'),
        ('bored', 'Скучающая рутина'),
        ('grateful', 'Благодарность сердца'),
        ('hungry', 'Гастрономическое волнение'),
    ]

    name = models.CharField(
        max_length=255,
        verbose_name='Агент',
        help_text='Имя агента',
        unique=True,
        blank=False,
        null=False,
    )
    mood = models.CharField(
        max_length=50,
        choices=MOOD_CHOICES,
        default='hungry'
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
    agents = models.ManyToManyField(
        Agent,
        verbose_name='Агенты',
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

