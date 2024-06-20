import time 
from datetime import datetime
from playsound import playsound 


def set_alarme(alarm_time):
    print(f"Alarme definido para {alarm_time}")

    while True:
        # pega o horario atual do sistema 
        #formata o horario
        now = datetime.now().strftime("%H:%M")

        # compara o horario atual com o horario do sitema, para ver quanto tempo falta 
        if now == alarm_time:
            print(" Hora de ACORDA VADIO! ")
            playsound('sound.mp3')
            break 

# espera 1 minutin antes de tocar de volta 
        time.sleep(60)
if __name__ == "__main__":
    alarm_time = input("Digite o horario para o alarme (HH:MM): ")
    set_alarme(alarm_time)