# Generated by Django 4.2.7 on 2024-02-26 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mod_user', '0001_initial'),
        ('mod_guest', '0001_initial'),
        ('mod_room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='estado_reserva',
            fields=[
                ('IDESTADORESERVA', models.AutoField(primary_key=True, serialize=False)),
                ('ESTADO_RESERVA', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('IDRESERVA', models.AutoField(primary_key=True, serialize=False)),
                ('FECHA_RESERVACION', models.DateField()),
                ('FECHA_ENTRADA', models.DateField()),
                ('HORA_ENTRADA', models.TimeField(null=True)),
                ('FECHA_SALIDA', models.DateField()),
                ('HORA_SALIDA', models.TimeField(null=True)),
                ('PRECIO_CALCULADO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CANTIDAD_ADULTOS', models.IntegerField()),
                ('CANTIDAD_NINOS', models.IntegerField()),
                ('ESTADO_RESERVA', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mod_reservation.estado_reserva')),
                ('PERSONA_NRODOCUMENTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_user.persona')),
            ],
        ),
        migrations.CreateModel(
            name='huesped_reserva',
            fields=[
                ('ID_HUESPED_RESERVA', models.AutoField(primary_key=True, serialize=False)),
                ('HUESPED_IDHUESPED', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_guest.huesped')),
                ('RESERVA_IDRESERVA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_reservation.reserva')),
            ],
        ),
        migrations.CreateModel(
            name='habitacion_reserva',
            fields=[
                ('ID_HABITACION_RESERVA', models.AutoField(primary_key=True, serialize=False)),
                ('HABITACION_NROHABITACION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_room.habitacion')),
                ('RESERVA_IDRESERVA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_reservation.reserva')),
            ],
        ),
    ]
