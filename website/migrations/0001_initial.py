# Django tạo file này tự động khi chạy lệnh makemigrations
# File này chứa các thông tin về migration của ứng dụng
# File này sẽ được chạy khi chạy lệnh migrate
# File này sẽ tạo ra bảng trong cơ sở dữ liệu

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                # gán "id" là khóa chính tự động tăng
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
            ],
        ),
    ]
