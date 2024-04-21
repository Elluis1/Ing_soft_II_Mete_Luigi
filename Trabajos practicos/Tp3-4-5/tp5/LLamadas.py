from clasesYfunciones import *
from observer import *
from IS2_taller_scanner import *
from IS2_taller_memory import *

# Punto 1 (LLamada)
# processor = NumberProcessor()
# processor.process_numbers()

# Punto 2
# word = "Hello"
# print("Straight traversal:")
# print("\n".join(word))
# print("")

# print("Reverse traversal:")
# print("\n".join(word[::-1]))
# print("\n")

# Punto 3
# if __name__ == "__main__":
#     # The client code.

#     subject = ConcreteSubject()

#     observer_ABCD = SpecificObserver("ABCD")
#     subject.attach(observer_ABCD)

#     observer_EFGH = SpecificObserver("EFGH")
#     subject.attach(observer_EFGH)

#     observer_WXYZ = SpecificObserver("WXYZ")
#     subject.attach(observer_WXYZ)

#     observer_1234 = SpecificObserver("1234")
#     subject.attach(observer_1234)

#     for _ in range(8):
#         generated_id = "".join(choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(4))
#         subject.notify(generated_id)

# Punto 4
# if __name__ == "__main__":
#     os.system("clear")
#     print("\nCrea un objeto radio y almacena las siguientes acciones")
#     radio = Radio()
#     actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
#     actions *= 2

#     # Memorizamos algunas estaciones
#     radio.memorize_station("1620")
#     radio.memorize_station("95.5")

#     # Recorremos las acciones ejecutando la acción, incluyendo la sintonización de estaciones memorizadas
#     print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
#     for action in actions:
#         action()

#     # Cambiamos a una estación memorizada
#     radio.switch_station(3)  # Cambia a la estación memorizada en la posición 3

# Punto 5
# os.system("clear")
# caretaker = FileWriterCaretaker()
# writer = FileWriterUtility("test.txt")
# # Escribimos algo y guardamos el estado
# writer.write("Hola, este es el estado inicial.\n")
# writer.save()
# # Escribimos algo más y guardamos el estado
# writer.write("Agregando más contenido.\n")
# writer.save()
# # Hacemos algunos undos para probar
# caretaker.undo(writer, 1)  # Deshacer el último cambio
# print("Contenido después de deshacer 1 cambio:")
# print(writer.content)
# caretaker.undo(writer, 2)  # Deshacer los últimos 2 cambios
# print("\nContenido después de deshacer 2 cambios:")
# print(writer.content)
# # Agregamos más contenido y guardamos un nuevo estado
# writer.write("Más contenido agregado.\n")
# writer.save()
# # Realizamos un undo para recuperar un estado anterior
# caretaker.undo(writer, 1)  # Deshacer el último cambio
# print("\nContenido después de deshacer 1 cambio:")
# print(writer.content)
