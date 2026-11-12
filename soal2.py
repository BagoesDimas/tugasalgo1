BERAT_DASAR = 2
BIAYA_DASAR = 10000
BIAYA_PER_KG = 4000
BATAS_JARAK = 20
BIAYA_JARAK = 5000
DISKON_ANGGOTA = 0.10


def hitung_biaya_berat(berat):
    """hitung biaya berat paket"""
    if berat <= BERAT_DASAR:
        return BIAYA_DASAR
    kelebihan = berat - BERAT_DASAR
    return BIAYA_DASAR + kelebihan * BIAYA_PER_KG


def hitung_biaya_jarak(jarak):
    """menghitung biaya tambahan berdasarkan jarak kirim"""
    if jarak > BATAS_JARAK:
        return BIAYA_JARAK
    return 0


def hitung_potongan(subtotal, anggota):
    """hitung diskon untuk pelanggan anggota"""
    if anggota == "ya":
        return round(subtotal * DISKON_ANGGOTA)
    return 0


def buat_rincian(pesanan):
    """rincian biaya tiap pesanan"""
    rincian = []
    for nama, berat, jarak, anggota in pesanan:
        biaya_berat = hitung_biaya_berat(berat)
        biaya_jarak = hitung_biaya_jarak(jarak)
        subtotal = biaya_berat + biaya_jarak
        potongan = hitung_potongan(subtotal, anggota)
        ongkir_akhir = subtotal - potongan
        rincian.append((nama, biaya_berat, biaya_jarak, potongan, ongkir_akhir))
    return rincian


def hitung_total_pendapatan(rincian):
    """jumlahin ongkir akhir semua pesanan"""
    total = 0
    for data in rincian:
        total += data[4]
    return total


def cetak_struk(rincian):
    """untuk cetak struk tiap pelanggan."""
    for nama, biaya_berat, biaya_jarak, potongan, ongkir_akhir in rincian:
        print("Pelanggan    :", nama)
        print("Biaya berat  : Rp", biaya_berat)
        print("Biaya jarak  : Rp", biaya_jarak)
        print("Potongan     : Rp", potongan)
        print("Ongkir akhir : Rp", ongkir_akhir)
        print("-" * 30)


def cetak_total(total):
    """untuk cetak total pendapatan ongkir hari ini"""
    print("Total pendapatan hari ini : Rp", total)


def main():
    """alur utama program"""
    pesanan = [
        ("Rina", 1, 10, "bukan"),
        ("Sari", 5, 25, "bukan"),
        ("Tono", 5, 25, "ya"),
        ("Umar", 2, 30, "ya"),
        ("Vina", 8, 15, "bukan"),
    ]
    rincian = buat_rincian(pesanan)
    cetak_struk(rincian)
    total = hitung_total_pendapatan(rincian)
    cetak_total(total)


if __name__ == "__main__":
    main()