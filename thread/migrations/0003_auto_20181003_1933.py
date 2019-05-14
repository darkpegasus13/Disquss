# Generated by Django 2.0.7 on 2018-10-03 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0002_post_reply_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_reply_comments',
            name='reply_comments',
        ),
        migrations.RemoveField(
            model_name='post_reply_comments',
            name='user',
        ),
        migrations.AddField(
            model_name='post_reply',
            name='Post_reply_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nested_comments', to='thread.Post_reply'),
        ),
        migrations.DeleteModel(
            name='Post_reply_comments',
        ),
    ]
