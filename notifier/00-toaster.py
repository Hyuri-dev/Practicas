from win10toast import ToastNotifier
import time

notifitacion = ToastNotifier()
ToastNotifier().show_toast("Hi", " i am message of example",icon_path="C:\\Users\\Jefferson\\Documents\\Desarrollo\\Python\\notifier\\assets\\noti-ico.ico", duration= 5, threaded=True)

while notifitacion.notification_active():
    time.sleep(0.1)