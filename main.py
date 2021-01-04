# importo il modulo subprocess per interagire con il terminale
import subprocess

# Consiste nel lanciare i seguenti comandi tramite python
#netsh wlan show profile
#netsh wlan show profile PROFILE-NAME key=clear

# lanciamo il primo comando con the subprocess.check_output e salviamo nella variabile users la lista delle wifi memorizzate
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
users = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for user in users:
    # lanciamo il secondo comando per controllare le password
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', user,
                        'key=clear']).decode('utf-8').split('\n')
    # salviamo le password e le convertiamo in una lista
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    # stampiamo il nome del profilo con la password
    try:
        print("{:<30}|  {:<}".format(user, results[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(user, ""))