def calcular_riesgo(promedio):
    if promedio < 10:
        return "BAJO"
    elif promedio < 25:
        return "MEDIO"
    else:
        return "ALTO"


def recomendaciones(riesgo):
    print("\nRECOMENDACIONES:")

    if riesgo == "BAJO":
        print("- Mantener limpios los espacios.")
        print("- Revisar recipientes con agua.")

    elif riesgo == "MEDIO":
        print("- Eliminar agua estancada.")
        print("- Utilizar repelente.")
        print("- Mantener puertas y ventanas protegidas.")

    else:
        print("- Riesgo elevado de propagación del dengue.")
        print("- Realizar campañas de limpieza.")
        print("- Reportar la situación a las autoridades.")
        print("- Usar repelente y mosquiteros.")


print("===================================")
print("MOSQUITO ALERT PERÚ")
print("Sistema Comunitario de Prevención del Dengue")
print("===================================")

comunidad = input("Ingrese el nombre de la comunidad: ")

num_reportes = int(input("¿Cuántos reportes desea registrar?: "))

total_mosquitos = 0

for i in range(num_reportes):
    print(f"\nReporte #{i + 1}")

    cantidad = int(input("Cantidad estimada de mosquitos observados: "))

    total_mosquitos += cantidad

promedio = total_mosquitos / num_reportes

riesgo = calcular_riesgo(promedio)

print("\n===================================")
print("RESULTADOS DEL ANÁLISIS")
print("===================================")
print("Comunidad:", comunidad)
print("Reportes registrados:", num_reportes)
print("Promedio de mosquitos:", round(promedio, 2))
print("Nivel de riesgo:", riesgo)

recomendaciones(riesgo)

print("\nGracias por utilizar Mosquito Alert Perú.")
