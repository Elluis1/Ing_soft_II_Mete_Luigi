import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):

		self.file = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):

		self.file = file
		self.content = ""
		self.history = []

	def write(self, string):
		self.content += string


	def save(self):
		# Guarda solo los últimos 4 estados
		if len(self.history) >= 4:
			self.history.pop(0)
		self.history.append(Memento(self.file, self.content))

	def undo(self, steps_back=0):
		if steps_back >= len(self.history):
			steps_back = len(self.history) - 1
		memento = self.history[-1 - steps_back]
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:
	def __init__(self):
		self.history_index = -1

	def save(self, writer):
		writer.save()

	def undo(self, writer, steps_back=0):
		writer.undo(steps_back)


if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar");
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional II")
	writer.write("Material adicional de la clase de patrones II\n")
	print(writer.content + "\n\n")


	print("se invoca al <undo>")
	caretaker.undo(writer)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	print("se invoca al <undo>")
	caretaker.undo(writer)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

