TUGAS = 0.30
UTS = 0.30
UAS = 0.40


def hitung_nilai_akhir(tugas, uts, uas):
    """hitung nilai akhir dri tugas,uts,uas"""
    return tugas * TUGAS + uts * UTS + uas * UAS


def tentukan_huruf(nilai_akhir):
    """nilai akhir di ubah menjadi huruf"""
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 55:
        return "C"
    elif nilai_akhir >= 40:
        return "D"
    else:
        return "E"


def cek_lulus(huruf):
    """untuk mengecek apakah mahasiswa lulus"""
    return huruf in ("A", "B", "C")


def buat_rekap(data_mahasiswa):
    """membuat rekap tiap mahasiswa."""
    rekap = []
    for nama, tugas, uts, uas in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        huruf = tentukan_huruf(nilai_akhir)
        lulus = cek_lulus(huruf)
        rekap.append((nama, nilai_akhir, huruf, lulus))
    return rekap


def hitung_rata_rata(rekap):
    """untuk hitung rata" nilai akhir"""
    total = 0
    for data in rekap:
        total += data[1]
    return total / len(rekap)


def hitung_jumlah_lulus(rekap):
    """jumlah mahasiswa yg lulus"""
    jumlah = 0
    for data in rekap:
        if data[3]:
            jumlah += 1
    return jumlah


def tampilkan_tabel(rekap):
    """menampilkan keterangan tiap mahasiswa"""
    for nama, nilai_akhir, huruf, lulus in rekap:
        keterangan = "lulus" if lulus else "tidak lulus"
        print(nama, "nilainya =", round(nilai_akhir, 1), "predikatnya =", huruf, keterangan)


def tampilkan_ringkasan(rekap):
    """menampilkan rata" semua mahsaiswa dan jumlah yg lulus"""
    print("rata rata nilai mahasiswa adalah =", round(hitung_rata_rata(rekap), 2))
    print("jumlah yg lulus =", hitung_jumlah_lulus(rekap))


def main():
    """alur utama program"""
    data_mahasiswa = [
        ("Andi", 80, 70, 90),
        ("Bunga", 90, 85, 88),
        ("Citra", 60, 45, 50),
        ("Dimas", 75, 80, 65),
        ("Eka", 30, 40, 35),
    ]
    rekap = buat_rekap(data_mahasiswa)
    tampilkan_tabel(rekap)
    tampilkan_ringkasan(rekap)


if __name__ == "__main__":
    main()