import json
import jsonsfunciones

#Funcion para ingresar campers

def registroCampers():
    ListaCampers=jsonsfunciones.CargarDatos("campers.json")
    print("--------------------------------")
    print("-------Registro de Camper-------")
    print("--------------------------------") 
    while True:
        try:
            nombre=input("Escribe solo tus nombres\n")
            apellidos=input("Escribe tus apellidos\n")
            documento=int(input("Por favor escribe tu documento de identidad\n"))
            direccion=input("Escribe tu dirección de residencia\n") 
            Acudiente=input("Escribe el nombre de tu acudiente\n")
            Telefono=int(input("Escribe tu numero de celular\n")) 
            Estado="En proceso de ingreso"
            Riesgo=""
            Salon=""
            DatosSalon=""
            Notas={
                'Fundamentos de Programacion':None,
                'Programacion Web':None,
                'Programacion Formal':None,
                'SGBD':None,
                'Backend':None
            }
            ListaCampers.append({'nombre': nombre, 'apellidos': apellidos, 'documento':documento,'direccion': direccion, 'Acudiente': Acudiente, 'Telefono': Telefono, 'Estado':Estado, 'Riesgo':Riesgo,'Salon':Salon,'datosSalon':DatosSalon,'Notas':Notas})
            jsonsfunciones.guardarcambios(ListaCampers,"campers.json")
            print("Usuario creado con exito")
            break
        except ValueError:
            print("Por favor ingrese los valores indicados correctamente\n")    

def campersInscritos():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    print("----------------------------------------")
    print("-------Lista de Campers Inscritos-------")
    print("----------------------------------------") 
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Estado'] == "En proceso de ingreso" or camper['Estado'] == "Inscrito" :
            print(f"{index+1}-{nombre}{apellido}")
            
def campersAprobados():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    print("----------------------------------------")
    print("-------Lista de Campers Aprobados-------")
    print("----------------------------------------") 
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Estado'] == "Aprobado" or camper['Estado'] == "Cursando" :
            print(f"{index+1}-{nombre}{apellido}")

def trainersInCampus():
    listaSalones = jsonsfunciones.CargarDatos("salones.json")
    listaprofes = set()
    print("----------------------------------------------------")
    print("-------Lista de Trainers Trabajando en Campus-------")
    print("----------------------------------------------------") 
    for salon in listaSalones.values():
        profeasignado = salon.get('Trainer','Sin Trainer')
        if profeasignado != "":
            if profeasignado not in listaprofes:
                listaprofes.add(profeasignado)
    cont = 0
    for x in listaprofes:
        cont += 1
        print(f"{cont}--> {x}")

def campersRendimientoBajo():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    print("---------------------------------------------------")
    print("-------Lista de Campers Con Rendimiento BAJO-------")
    print("---------------------------------------------------") 
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Riesgo'] == "Alto" :
            print(f"{index+1}-{nombre}{apellido}")

def campersYtrainersEnUnaRuta():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    listaRutas=jsonsfunciones.CargarDatos('rutasaprendizaje.json')
    listaSalones=jsonsfunciones.CargarDatos('salones.json')
    listaprofes=set()
    print("---------------------------------------------------")
    print("-------Lista de Campers y Trainers la Ruta --------")
    print("---------------------------------------------------") 
    
    
    while True:
        #Definir cual ruta vamos a revisar
        print("\nLas Rutas disponibles son:\n")
        for index,ruta in enumerate(listaRutas):
            nombre=ruta.get('Nombre','No hay nombre')
            if nombre!="":
                print(f"{index+1}-{nombre}")
        try:
            rutaseleccionada=int(input("\nLa ruta que deseas revisar es:  "))
            if rutaseleccionada<0 or rutaseleccionada>index+1:
                print("Este valor no corresponde a las opciones")
            else:
                while True:
                    hacer=int(input("¿Que deseas revisar?\n1. Campers\n2. Trainers\n0. Volver al menú anterior\nOpción:   "))
                    nombreruta=listaRutas[rutaseleccionada-1]['Nombre']
                    if hacer==1:
                        #Entontrar el nombre de la ruta seleccionada
                        print("--------------------------------------------------------")
                        print(f"Para la {nombreruta} los ESTUDIANTES asignados son")
                        print("--------------------------------------------------------")
                        for index,camper in enumerate(listaEstudiantes):
                            nombre=camper.get('nombre','No hay nombre')
                            apellido=camper.get('apellidos','No hay apellidos')
                            if camper['datosSalon']['ruta']== nombreruta :
                                print(f"{index+1}-{nombre} {apellido}")
                    elif hacer==2:        
                         # Encontrar los trainers asignados a la ruta seleccionada
                        print("--------------------------------------------------------")
                        print(f"Para la {nombreruta} los TRAINERS asignados son")
                        print("--------------------------------------------------------")
                        for salon in listaSalones:
                            datosSalon = listaSalones[salon]
                            if datosSalon.get('ruta') == nombreruta:
                                profeRuta = datosSalon.get('Trainer')
                                if profeRuta not in listaprofes:
                                    listaprofes.add(profeRuta)                         
                        cont = 0
                        for x in listaprofes:
                            cont += 1
                            print(f"{cont}--> {x}")
                        print("\n")
                    elif hacer == 0:
                        print("....Saliendo....")
                        break
                    else: 
                        print("La opción no es valida, intentalo de nuevo")
        except Exception:
            print("\nVuelve a intentarlo\n")            
    
    
def camperspormodulo():
    listaEstudiantes = jsonsfunciones.CargarDatos("campers.json")
    listaSalones = jsonsfunciones.CargarDatos("salones.json")
    aprobados=0
    reprobados=0
    while True:
        try:
            print("\nPor favor elije el módulo que deseas revisar:")
            print("1. Fundamentos de Programación")
            print("2. Programación Web")
            print("3. Programación Formal")
            print("4. SGBD")
            print("5. Backend")
            print("0. Salir al menú anterior")
            
            opcion = int(input("Opción: "))
            if opcion==0:
                break
            
            for x in listaEstudiantes:
                notas=x.get('Notas',{}) 
                if notas and opcion in notas:     
                    resultado=notas[opcion]
                    if resultado[1]=="Aprobado":
                        aprobados+=1
                    elif resultado[1]=="Reprobado":
                        reprobados+=1
            print(f"\nMódulo seleccionado: {opcion}")
            print(f"Campers que aprobaron: {aprobados}")
            print(f"Campers que perdieron: {reprobados}")
                                
                           
                #for index,camper in enumerate(listaEstudiantes):
                #    nombre=camper.get('nombre','No hay nombre')
                #    apellido=camper.get('apellidos','No hay apellidos')
                #    
                #    print(f"{index+1}-{nombre}")
        except Exception:
            print("Los datos ingresados no corresponden\nIntentalo de nuevo ")        
        
camperspormodulo()