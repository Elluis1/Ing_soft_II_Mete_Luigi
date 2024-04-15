# Trabajo practico n°3 Luigi Mete

from Clases_Y_Funciones import *

llamadoFunciones()

# punto 6
print('Punto 6')
print('')
espera2Seg()
if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)

    # Crear 20 anidamientos
    nested_components = []
    for _ in range(20):
        nested_component = copy.copy(component)
        nested_components.append(nested_component)

    # Procesar cada componente anidado
    for i, component in enumerate(nested_components):
        print(f"Procesando componente anidado {i + 1}:")
    component

