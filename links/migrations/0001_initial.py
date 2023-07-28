from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('shortened_url', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=timezone.now)),
            ],
        ),
    ]
