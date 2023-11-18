import paramiko

# Thông tin kết nối SSH
host = "192.168.122.67"
port = 22
username = "vinh"
password = "1"


def connect_ssh(host, port, username, password):
    # Tạo một đối tượng SSHClient
    ssh_client = paramiko.SSHClient()

    try:
        # Automatically add the server's SSH key (without checking)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Kết nối tới máy chủ SSH
        ssh_client.connect(host, port, username, password)

        return ssh_client
    except paramiko.AuthenticationException:
        print("Failed to authenticate with the server.")
        return None
    except paramiko.SSHException as sshException:
        print(f"Unable to establish SSH connection: {sshException}")
        return None
    except Exception as e:
        print(f"Operation error: {e}")
        return None


def get_users(ssh_client):
    # Thực thi lệnh để lấy danh sách người dùng từ container PostgreSQL
    command = """docker exec psql psql -U postgres -c "SELECT usename FROM pg_user WHERE usename != 'postgres';" """
    stdin, stdout, stderr = ssh_client.exec_command(command)

    lines = stdout.read().decode().splitlines()
    users = [(line.strip(), line.strip()) for line in lines[2:-2]]

    return users


def get_databases(ssh_client):
    # Thực thi lệnh để lấy danh sách database từ container PostgreSQL
    command = """docker exec psql psql -U postgres -c "SELECT datname FROM pg_database WHERE datname NOT IN ('postgres', 'template1', 'template0');" """
    stdin, stdout, stderr = ssh_client.exec_command(command)

    lines = stdout.read().decode().splitlines()
    databases = [(line.strip(), line.strip()) for line in lines[2:-2]]

    return databases

