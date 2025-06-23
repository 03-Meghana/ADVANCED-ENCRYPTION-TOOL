import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Style
from PIL import Image, ImageTk
from encryption_tool import encrypt_file, decrypt_file

# ========== Functions ==========
def select_file():
    path = filedialog.askopenfilename()
    if path:
        file_path.set(path)
        update_status("📁 File selected!", "#00ffff")

def encrypt_action():
    if not file_path.get() or not password.get():
        update_status("⚠️ Select file and password!", "#ffae42")
        return

    try:
        progress.start()
        output = encrypt_file(file_path.get(), password.get())
        update_status("✅ Encrypted Successfully!", "#00ff88")
        messagebox.showinfo("Success", f"Encrypted as:\n{output}")
    except Exception as e:
        update_status("❌ Encryption Failed!", "red")
        messagebox.showerror("Error", str(e))
    finally:
        progress.stop()

def decrypt_action():
    if not file_path.get() or not password.get():
        update_status("⚠️ Select file and password!", "#ffae42")
        return

    try:
        progress.start()
        output = decrypt_file(file_path.get(), password.get())
        update_status("✅ Decrypted Successfully!", "#00cfff")
        messagebox.showinfo("Success", f"Decrypted as:\n{output}")
    except Exception as e:
        update_status("❌ Decryption Failed!", "red")
        messagebox.showerror("Error", str(e))
    finally:
        progress.stop()

def toggle_password():
    entry_password.config(show="" if show_pass.get() else "*")

def update_status(msg, color):
    status_label.config(text=msg, fg=color)

def show_about():
    messagebox.showinfo("About", "🔐 AES-256 Encryption Tool\nColorful Edition by Alla R.")

# ========== GUI ==========
root = tk.Tk()
root.title("🔐 AES-256 Encryption Tool")
root.geometry("620x500")
root.config(bg="#1f1f2e")

# ========== Banner ==========
try:
    banner_img = Image.open("banner.png")
    banner_img = banner_img.resize((600, 100))
    banner = ImageTk.PhotoImage(banner_img)
    tk.Label(root, image=banner, bg="#1f1f2e").pack(pady=10)
except Exception:
    tk.Label(root, text="🔐 AES-256 Encryption Tool", font=("Segoe UI", 20, "bold"), fg="cyan", bg="#1f1f2e").pack(pady=10)

# ========== Variables ==========
file_path = tk.StringVar()
password = tk.StringVar()
show_pass = tk.BooleanVar()

# ========== File Selection ==========
frame = tk.Frame(root, bg="#1f1f2e")
frame.pack(pady=10)

tk.Label(frame, text="📁 Select File", font=("Segoe UI", 11), fg="white", bg="#1f1f2e").grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=file_path, width=50, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5)
tk.Button(frame, text="Browse", command=select_file, bg="#00bfff", fg="white", width=10).grid(row=1, column=1)

# ========== Password ==========
tk.Label(root, text="🔑 Enter Password", font=("Segoe UI", 11), fg="white", bg="#1f1f2e").pack()
entry_password = tk.Entry(root, textvariable=password, show="*", width=30, bg="#f0f0f0", font=("Segoe UI", 11))
entry_password.pack(pady=5)
tk.Checkbutton(root, text="Show Password", variable=show_pass, command=toggle_password, bg="#1f1f2e", fg="white").pack()

# ========== Buttons ==========
tk.Button(root, text="🔐 Encrypt File", command=encrypt_action, bg="#28a745", fg="white", font=("Segoe UI", 11), width=25).pack(pady=10)
tk.Button(root, text="🔓 Decrypt File", command=decrypt_action, bg="#007bff", fg="white", font=("Segoe UI", 11), width=25).pack(pady=5)

# ========== Progress & Status ==========
progress = Progressbar(root, orient=tk.HORIZONTAL, length=500, mode='indeterminate')
progress.pack(pady=10)

status_label = tk.Label(root, text="", font=("Segoe UI", 10, "bold"), bg="#1f1f2e")
status_label.pack(pady=10)

# ========== Menu ==========
menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu)

root.mainloop()

