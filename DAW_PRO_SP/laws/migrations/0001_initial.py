# Generated by Django 2.2.4 on 2019-08-10 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asableista',
            fields=[
                ('id_asambleista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('partido', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id_comentario', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=35)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ley',
            fields=[
                ('id_ley', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_oficial', models.CharField(max_length=35)),
                ('nombre_publico', models.CharField(max_length=35)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('contrasena', models.CharField(max_length=10)),
                ('nombreUsuario', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voto', models.CharField(max_length=35)),
                ('id_asambleista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laws.Asableista')),
                ('id_ley', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laws.Ley')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('correo', models.CharField(max_length=35)),
                ('ruta_imagen', models.CharField(max_length=35)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laws.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ComentarioLey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laws.Comentario')),
                ('id_ley', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laws.Ley')),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laws.Usuario'),
        ),
    ]