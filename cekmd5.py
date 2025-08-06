#!/usr/bin/python
# -*- coding: utf-8 -*-import

import hashlib
import sys

# Fungsi untuk membuat hash MD5 dari file
def buat_md5(file_path):
    try:
        with open(file_path, 'rb') as f:
            hash_md5 = hashlib.md5()
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
            return hash_md5.hexdigest()
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
        sys.exit(1)

# Fungsi untuk memverifikasi hash MD5
def verifikasi_md5(file_path, hash_asli):
    hash_file = buat_md5(file_path)
    if hash_file == hash_asli:
        print(f"File {file_path} valid. MD5 cocok.")
    else:
        print(f"File {file_path} tidak valid. MD5 tidak cocok.")

# Main program
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Penggunaan: python md5check.py <path_to_file> <expected_md5_hash>")
        sys.exit(1)

    file_path = sys.argv[1]
    expected_md5 = sys.argv[2]
    #md5_hash = buat_md5(file_path)

    verifikasi_md5(file_path, expected_md5)
    #print(f"berhasil dibuat hash MD5: {md5_hash} untuk file {file_path}")
