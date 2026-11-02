class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def tampilkan_info(self):
        return f"NIM: {self.nim}, Nama: {self.nama}"
