import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from Tests.KeyGenerator import generate
from Modes.ECBencrypt import ecb_encrypt
from Modes.ECBdecrypt import ecb_decrypt
from Modes.CBCencrypt import cbc_encrypt
from Modes.CBCdecrypt import cbc_decrypt
from Modes.CTRencrypt import ctr_encrypt
from Modes.CTRdecrypt import ctr_decrypt

root = tk.Tk()
root.title("AES GUI")
mode_var = tk.StringVar(value="ECB")  # выбранный режим


def set_key():
    size = int(key_size_var.get())
    key_hex = generate(size)
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key_hex)


def encrypt_text():
    key_hex = key_entry.get()
    plaintext = input_text.get("1.0", tk.END).strip()
    if not key_hex or not plaintext:
        messagebox.showwarning("Warning", "Enter key and plaintext")
        return

    key_bytes = bytes.fromhex(key_hex)
    plaintext_bytes = plaintext.encode("utf-8")
    mode = mode_var.get()

    if mode == "ECB":
        ciphertext = ecb_encrypt(key_bytes, plaintext_bytes)
    elif mode == "CBC":
        ciphertext = cbc_encrypt(key_bytes, plaintext_bytes)
    elif mode == "CTR":
        ciphertext = ctr_encrypt(key_bytes, plaintext_bytes)
    else:
        messagebox.showerror("Error", "Unknown mode")
        return

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, ciphertext.hex())


def decrypt_text():
    key_hex = key_entry.get()
    ciphertext_hex = input_text.get("1.0", tk.END).strip()
    if not key_hex or not ciphertext_hex:
        messagebox.showwarning("Warning", "Enter key and ciphertext")
        return

    key_bytes = bytes.fromhex(key_hex)
    try:
        ciphertext_bytes = bytes.fromhex(ciphertext_hex)
    except ValueError:
        messagebox.showerror("Error", "Ciphertext must be in hex format")
        return

    mode = mode_var.get()

    if mode == "ECB":
        plaintext_bytes = ecb_decrypt(key_bytes, ciphertext_bytes)
    elif mode == "CBC":
        plaintext_bytes = cbc_decrypt(key_bytes, ciphertext_bytes)
    elif mode == "CTR":
        plaintext_bytes = ctr_decrypt(key_bytes, ciphertext_bytes)
    else:
        messagebox.showerror("Error", "Unknown mode")
        return

    try:
        plaintext = plaintext_bytes.decode("utf-8")
    except UnicodeDecodeError:
        plaintext = str(plaintext_bytes)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, plaintext)


# файламы
def encrypt_file():
    file_path = filedialog.askopenfilename(title="Select file to encrypt")
    if not file_path:
        return

    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, data)
    encrypt_text()

    save_path = filedialog.asksaveasfilename(title="Save encrypted file", defaultextension=".txt")
    if save_path:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(output_text.get("1.0", tk.END).strip())
        messagebox.showinfo("Success", f"Encrypted file saved to {save_path}")


def decrypt_file():
    file_path = filedialog.askopenfilename(title="Select file to decrypt")
    if not file_path:
        return

    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, data)
    decrypt_text()

    save_path = filedialog.asksaveasfilename(title="Save decrypted file", defaultextension=".txt")
    if save_path:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(output_text.get("1.0", tk.END).strip())
        messagebox.showinfo("Success", f"Decrypted file saved to {save_path}")



# Ключеки
tk.Label(root, text="Key (hex)").grid(row=0, column=0, sticky="w")
key_entry = tk.Entry(root, width=50)
key_entry.grid(row=0, column=1)

tk.Label(root, text="Generate key size:").grid(row=0, column=2, sticky="w")
key_size_var = tk.StringVar(value="128")
tk.OptionMenu(root, key_size_var, "128", "192", "256").grid(row=0, column=3)
tk.Button(root, text="Generate Key", command=set_key).grid(row=0, column=4)

# Моды
tk.Label(root, text="Mode").grid(row=1, column=0, sticky="w")
tk.OptionMenu(root, mode_var, "ECB", "CBC", "CTR").grid(row=1, column=1, sticky="w")

# Ввод
tk.Label(root, text="Input").grid(row=2, column=0, sticky="nw")
input_text = scrolledtext.ScrolledText(root, width=60, height=10)
input_text.grid(row=2, column=1, columnspan=4)

# Вывод
tk.Label(root, text="Output").grid(row=3, column=0, sticky="nw")
output_text = scrolledtext.ScrolledText(root, width=60, height=10)
output_text.grid(row=3, column=1, columnspan=4)

# Кнопки
tk.Button(root, text="Encrypt Text", command=encrypt_text).grid(row=4, column=1)
tk.Button(root, text="Decrypt Text", command=decrypt_text).grid(row=4, column=2)
tk.Button(root, text="Encrypt File", command=encrypt_file).grid(row=5, column=1)
tk.Button(root, text="Decrypt File", command=decrypt_file).grid(row=5, column=2)

# --- Запуск GUI ---
root.mainloop()
