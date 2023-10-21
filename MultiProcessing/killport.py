import socket
import multiprocessing

def close_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        print(f"پورت {port} بر روی {host} بسته شد.")
    except Exception as e:
        print(f"خطا در بستن پورت: {str(e)}")

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5432

    # ایجاد یک پروسه جدید برای بستن پورت
    process = multiprocessing.Process(target=close_port, args=(host, port))
    process.start()
    process.join()
