# Generated by Django 5.1.4 on 2024-12-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Augment_Image",
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
                    "img_path",
                    models.CharField(max_length=128, verbose_name="增强结果路径"),
                ),
                (
                    "create_time",
                    models.DateField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Remote_Sensing_Image",
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
                ("img_path", models.CharField(max_length=128, verbose_name="图像路径")),
                (
                    "create_time",
                    models.DateField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Segmentation_Image",
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
                    "img_path",
                    models.CharField(max_length=128, verbose_name="分割结果路径"),
                ),
                (
                    "create_time",
                    models.DateField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Site_Data",
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
                    "total_views",
                    models.BigIntegerField(default=0, verbose_name="总浏览量"),
                ),
                ("total_datas", models.IntegerField(verbose_name="总数据量")),
                ("total_used", models.IntegerField(verbose_name="总使用量")),
                (
                    "create_time",
                    models.DateField(auto_now=True, verbose_name="创建时间"),
                ),
            ],
        ),
    ]
