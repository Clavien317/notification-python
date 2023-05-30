from win10toast import ToastNotifier
import time


#si on l'affiche comme alarme 
while True:
    temps = time.strftime("%H:%M:%S")
    if(temps=="23:15:50"):
        print(temps)
        break
    else:
        pass


#notre message a affiche comme notification
hr= ToastNotifier()
hr.show_toast("Notification", "Vous devez dormir maintenant .... (tout de suite)  !",None,5)
