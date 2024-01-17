from flask import Flask,send_file
import socket

aplikasi = Flask(__name__)

# Route untuk halaman default
@aplikasi.route("/")
def home():
    # menampilkan pesan masuk server mana
    return f'<center><h3>Anda memasuki Server dengan container ID {socket.gethostname()}</h3></center>'

if __name__ == '__main__':
    aplikasi.run('0.0.0.0')