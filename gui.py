import threading
import tkinter as tk
import socket

from time import sleep

TCP_HOST = "172.17.0.1"
TCP_PORT = 9933

def get_logs():
    print("Log thread started")
    while True:
        sleep(5)
        recvd = ""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((TCP_HOST, TCP_PORT))
            sleep(5)
            sock.sendall(b"PING")
            data = sock.recv(1024)
            while not data.decode("UTF-8").endswith("~~"):
                recvd += data.decode("UTF-8")
                data = sock.recv(1024)
        text_box.configure(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)  # Clear previous text
        text_box.insert(tk.END, recvd)
        text_box.configure(state=tk.DISABLED)

def send_slice(mode):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((TCP_HOST, TCP_PORT))
        if mode == "WORK":
            sock.sendto("SLICE_0".encode("UTF-8"), (TCP_HOST, TCP_PORT))
        elif mode == "CONFERENCE":
            sock.sendto("SLICE_1".encode("UTF-8"), (TCP_HOST, TCP_PORT))
        elif mode == "EMERGENCY":
            sock.sendto("SLICE_2".encode("UTF-8"), (TCP_HOST, TCP_PORT))

root = tk.Tk()
root.geometry("400x300")
root.title("SDN Slicing Controller")

text_box = tk.Text(root, wrap="word")
text_box.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
text_box.configure(state=tk.DISABLED)

style = {"pady": (0, 10)}
work_button = tk.Button(root, text="WORK", bg="green", command=lambda: send_slice("WORK"))
work_button.grid(row=1, column=0, sticky="w", padx=(10, 0), **style)

conference_button = tk.Button(root, text="CONFERENCE", bg="blue", command=lambda: send_slice("CONFERENCE"))
conference_button.grid(row=1, column=0, sticky="w", padx=(110, 0), pady=(0, 10))

emergency_button = tk.Button(root, text="EMERGENCY", bg="red", command=lambda: send_slice("EMERGENCY"))
emergency_button.grid(row=1, column=0, sticky="w", padx=(260, 0), **style)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

x = threading.Thread(target=get_logs)
x.start()

root.mainloop()
