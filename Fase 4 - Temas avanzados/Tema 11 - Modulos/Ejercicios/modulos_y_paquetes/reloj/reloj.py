import datetime, time, os

while True:
    dt = datetime.datetime.now()
    # Formateo de hora
    dt = dt.strftime(" %H:%M:%S ")
    print(dt)
    time.sleep(1)
    os.system('clear')