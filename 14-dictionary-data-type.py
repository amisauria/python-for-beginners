#ejercicio sets
 

def dias_a_minutos(num_de_dias, unidad_conversion):
    if unidad_conversion == "minutos":
        return f"{num_de_dias} dias son {num_de_dias * 1440} minutos"
    elif unidad_conversion == "horas":
        return f"{num_de_dias} dias son {num_de_dias * 24} horas"
    else:
        return "unidad no valida" 
def validar_y_ejecutar():
    try:
        user_input_number = int(dias_y_unidad_dictionary["dias"])
        if user_input_number > 0:
            valor_calculado = dias_a_minutos(user_input_number, dias_y_unidad_dictionary["unidad"])#asi el usuario entrega la informacion para que la variable lo calcule
            print(valor_calculado)
        elif user_input_number == 0:
            print("entregaste un 0, porfavor digita un numero positivo")
        else:
            print("lo ingresado no es un numero valido. fuck off bitch")
    except ValueError:
        print("lo que ingresaste no es un numero valido, no te voy a convertir nah")

user_input =""
while user_input != "salir":
    user_input=input("hola usuario, dame el numero de dias y la unidad de conversion\n")
    dias_y_unidad = user_input.split(":")
    print(dias_y_unidad)
    dias_y_unidad_dictionary = {"dias":dias_y_unidad[0], "unidad": dias_y_unidad[1]} 
    print(dias_y_unidad_dictionary)
    validar_y_ejecutar()