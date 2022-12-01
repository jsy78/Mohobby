

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accepted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joindate', models.DateTimeField(auto_now=True)),
                ('joined', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('tags', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meeting_day', models.DateTimeField()),
                ('address_type', models.BooleanField(default=False)),
                ('address', models.CharField(default='온라인', max_length=100)),
                ('X', models.CharField(blank=True, max_length=30, null=True)),
                ('Y', models.CharField(blank=True, max_length=30, null=True)),
                ('entry_fee', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('hits', models.PositiveBigIntegerField(default=0)),
                ('recruit_type', models.BooleanField(default=False)),
                ('limit', models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(15)])),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hobby.categories')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hobby', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(through='hobby.Accepted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='accepted',
            name='hobby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hobby.hobby'),
        ),
        migrations.AddField(
            model_name='accepted',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
