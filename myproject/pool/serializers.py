from rest_framework import serializers
from .models import Pool

from .connect_to_instance import *


class PoolSerializer(serializers.ModelSerializer):
    # Thông tin kết nối SSH
    ssh_client = connect_ssh(host, port, username, password)
    # Lấy danh sách database và user từ container PostgreSQL
    DATABASE_CHOICES = get_databases(ssh_client)
    # Lấy danh sách user từ container PostgreSQL
    USERNAME_CHOICES = get_users(ssh_client)
    # Danh sách mode
    MODE_CHOICES = [
        ('session', 'Session'),
        ('transaction', 'Transaction'),
        ('statement', 'Statement'),
    ]

    name = serializers.CharField(max_length=200)
    database = serializers.ChoiceField(choices=DATABASE_CHOICES)
    mode = serializers.ChoiceField(choices=MODE_CHOICES)
    size = serializers.IntegerField()
    username = serializers.ChoiceField(choices=USERNAME_CHOICES)



    class Meta:
        model = Pool
        fields = ['id', 'name', 'database', 'mode', 'size', 'username', 'pgbouncer_pid']
        read_only_fields = ['id', 'pgbouncer_pid']