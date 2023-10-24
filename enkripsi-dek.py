import tkinter as tk

# Fungsi untuk enkripsi teks
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            char_code = ord(char)
            shifted_code = char_code + shift
            if char.isupper():
                if shifted_code > ord('Z'):
                    shifted_code -= 26
                elif shifted_code < ord('A'):
                    shifted_code += 26
            elif char.islower():
                if shifted_code > ord('z'):
                    shifted_code -= 26
                elif shifted_code < ord('a'):
                    shifted_code += 26
            result += chr(shifted_code)
        else:
            result += char
    return result

# Fungsi untuk dekripsi teks
def decrypt(text, shift):
    return encrypt(text, -shift)

# Fungsi yang dipanggil saat tombol Enkripsi ditekan
def encrypt_button_clicked():
    plaintext = input_text.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    encrypted_text = encrypt(plaintext, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

# Fungsi yang dipanggil saat tombol Dekripsi ditekan
def decrypt_button_clicked():
    ciphertext = input_text.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    decrypted_text = decrypt(ciphertext, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)

# Membuat jendela GUI
window = tk.Tk()
window.title("Chiper Caesar Kelompok RANGAJUKAR")

# Membuat dan mengatur elemen-elemen GUI
input_label = tk.Label(window, text="Teks:")
input_label.pack()

input_text = tk.Text(window, height=5, width=30)
input_text.pack()

shift_label = tk.Label(window, text="Pergeseran :")
shift_label.pack()

shift_entry = tk.Entry(window)
shift_entry.pack()

encrypt_button = tk.Button(window, text="Enkripsi", command=encrypt_button_clicked)
encrypt_button.pack()

decrypt_button = tk.Button(window, text="Dekripsi", command=decrypt_button_clicked)
decrypt_button.pack()

output_label = tk.Label(window, text="Hasil:")
output_label.pack()

output_text = tk.Text(window, height=5, width=30)
output_text.pack()

# Menampilkan GUI
window.mainloop()
