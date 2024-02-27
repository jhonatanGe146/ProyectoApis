# Generated by Django 5.0.2 on 2024-02-27 15:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='estado_usuario',
            fields=[
                ('IDESTADO', models.AutoField(primary_key=True, serialize=False)),
                ('ESTADO', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_documento',
            fields=[
                ('IDTIPODOCUMENTO', models.AutoField(primary_key=True, serialize=False)),
                ('TIPO_DOCUMENTO', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_persona',
            fields=[
                ('IDTIPOPERSONA', models.AutoField(primary_key=True, serialize=False)),
                ('TIPO_PERSONA', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('NRODOCUMENTO', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=70)),
                ('APELLIDO', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=45)),
                ('TELEFONO', models.CharField(max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('ESTADO_USUARIO_IDESTADO', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.estado_usuario')),
                ('TIPO_DOCUMENTO_IDTIPODOCUMENTO', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.tipo_documento')),
                ('TIPO_PERSONA_IDTIPOPERSONA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.tipo_persona')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
