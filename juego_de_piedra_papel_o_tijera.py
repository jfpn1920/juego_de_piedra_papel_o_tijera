import random
opciones = ["piedra", "papel", "tijera"]
print("#-------------------------------------#")
print("#--|juego de piedra, papel o tijera|--#")
print("#-------------------------------------#")
while True:
    print("\nopciones: piedra, papel, tijera")
    print("escriba 'salir' para finalizar el juego.")
    eleccion_usuario = input("ingrese su elección: ").lower()
    if eleccion_usuario == "salir":
        print("¡gracias por jugar! fin del juego.")
        break
    if eleccion_usuario not in opciones:
        print("opcion invalida, intente nuevamente.")
        continue
    eleccion_sistema = random.choice(opciones)
    print(f"sistema eligio: {eleccion_sistema}")
    if eleccion_usuario == eleccion_sistema:
        print("¡empate!")
    elif (eleccion_usuario == "piedra" and eleccion_sistema == "tijera") or \
        (eleccion_usuario == "papel" and eleccion_sistema == "piedra") or \
        (eleccion_usuario == "tijera" and eleccion_sistema == "papel"):
        print("¡ganaste!")
    else:
        print("¡perdiste!")