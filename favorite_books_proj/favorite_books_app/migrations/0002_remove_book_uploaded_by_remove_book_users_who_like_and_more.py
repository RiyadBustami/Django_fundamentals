# Generated by Django 4.1.1 on 2022-10-04 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("login_registration_app", "0002_rename_pw_user_password"),
        ("favorite_books_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="uploaded_by",
        ),
        migrations.RemoveField(
            model_name="book",
            name="users_who_like",
        ),
        migrations.AddField(
            model_name="book",
            name="uploaded_by",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books_uploaded",
                to="login_registration_app.user",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="users_who_like",
            field=models.ManyToManyField(
                related_name="liked_books", to="login_registration_app.user"
            ),
        ),
    ]
