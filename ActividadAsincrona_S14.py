
# Mensaje de bienvenida del programa
print("BIENVENIDOS AL PROGRAMA DE INFORMACIÓN SOBRE LOS DEPARTAMENTOS DE EL SALVADOR")
#Preguntar al usuario si desea ejecutar el programa
while True:
        respuesta = input("¿Desea ejecutar el programa? (si/no): ")
        if respuesta.lower() == "si":
            print("INICIO DEL PROGRAMA")
            #Mostrar el menú de departamentos 
            print("Seleccione un integrante del grupo: ")
            lisT = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
            departamentos = ["Chalatenango", "Auachapán","Santa Ana","Sonsonate","La Libertad" , "San Salvador","Cuscatlán" , "Cabañas", "La Paz",
                           "San Vicente", "Usulután" ,"San Miguel", "Morazán" , "La Unión"]
            for l1, l2 in zip(lisT,departamentos):
                print(l1,l2)   
                    #Pedir al usuario que ingrese el nombre del departamento
                  #ARRAYS DE TODOS LOS DEPARTAMENTOS         
            intentos = 5
            while intentos > 0:
                depart = input("INGRESE EL NOMBRE DEL DEPARTAMENTO: ").upper()
                #DEP 1
                if depart == "Chalatenango".upper():
                      print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {depart} ---")
                      
                      print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON :")
                      lista1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,28,29,30,31,32,33]
                      muni1=["Agua Caliente" , "Arcatao" , "Azacualpa" , "Cancasque" ,"Chalatenango" , "Citalá" , "Comalapa"  , "Concepción" , "Quezaltepeque"
                            , "Dulce Nombre de María" ,  "El Carrizal" , "El Paraíso" , "La Laguna" , "La Palma" , "La Reina" , "Las Flores" , "Las Vueltas" , "Nombre de Jesús",
                            "Nueva Concepción" , "Nueva Trinidad" ,"Ojos de Agua" , "Potonico" , "San Antonio de la Cruz" , "San Antonio Los Ranchos", "San Fernando" ,
                            "San Francisco Lempa" ,"San Francisco Morazán", "San Ignacio" , "San Isidro Labrador"	"San Luis del Carmen" , "San Miguel de Mercedes" , "San Rafael",
                            "Santa Rita" , "Tejutla"""]
                      for l1 , l2 in zip(lista1,muni1):
                           print(l1,l2)       
                                       #DEP 2
                elif depart == "Ahuachapán".upper():
                      print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {depart} ---")
                      
                      print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON :")    
                      lista2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
                      muni2=["Ahuachapán" , "Apaneca" , "Atiquizaya" , "Concepción de Ataco" , "El Refugio" , "Guaymango" , "Jujutla" ,
                           "San Francisco Menéndez" , "San Lorenzo" , "San Pedro" ,"Puxtla" , "Tacuba" , "Turín"]
                      for l1 , l2 in zip(lista2,muni2):
                       print(l1,l2)
                      # DEP 3
                elif depart == "Santa Ana".upper():
                    print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {depart} ---")
        
                    print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON :")  
                    lista3=[1,2,3,4,5,6,7,8,9,10,11,12,13]
                    muni3=["Candelaria de la Frontera" , "Chalchuapa" , "Coatepeque" , "El Congo" 
                           ,"El Porvenir" , "Masahuat" , "Metapán" , "San Antonio Pajonal" , "San Sebastián Salitrillo"
                           ,"Santa Ana" , "Santa Rosa Guachipilín" ,"Santiago de la Frontera", "Texistepeque"]
                    for l1,l2 in zip(lista3,muni3):
                        print(l1,l2)
                   # DEP 4
                elif depart == "Sonsonate".upper():
                     print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {depart} ---")
        
                     print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON :")  
                     lista4=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
                     muni4=["Acajutla" , "Armenia" ,  "Caluco", "Cuisnahuat", "Izalco", "Juayúa", 
                     "Nahuizalco" , "Nahulingo" , "Salcoatitán", "San Antonio del Monte" , "San Julián",
                     "Santa Catarina", "Masahuat", "Santa Isabel" , "Ishuatán" , "Santo Domingo de Guzmán" , 
                     "Sonsonate" , "Sonzacate"]
                     for l1,l2 in zip(lista4,muni4):
                         print(l1,l2)
                      #DEP 5
                elif depart == "La Libertad".upper():
                    print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {depart} ---")
        
                    print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON :")  
                    lista5=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
                    muni5=["Antiguo Cuscatlan", "chilitupán", "Ciudad Arce", "Colón",
                          "Comasagua", "Huizúcar", "Jayaque", "Jicalapa", "La Libertad", "Santa Tecla",
                         "Nuevo Cuscatlan", "San Juan Opico", "Quezaltepeque", "Sacacoyo", " San José Villanueva"
                         "San Matias", "San Pablo Tacachico", "Talnique", "Teotepeque","Tepecoyo", "Zaragoza"]
                    for l1,l2 in zip(lista5,muni5):
                        print(l1,l2)

                     #DEP 6
                elif depart == "San Salvador".upper():
                     print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {depart} ---")
        
                     print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON :")  
                     lista6=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21]
                     muni6=["Aguilares","Apopa","Ayutuxtepeque","Cuscatancingo","Ciudad delgado","El Paisnal", "Guazapa"
                            ,"Ilopango","Mexicanos","Nejapa","Panchimalco", "Rosario de Mora","San Marcos","San Martín","San Salvador"
                            ,"Santiago","Texacuango","Santo Tomás","Soyapango","Tonacatepeque"]
                     for l1,l2 in zip(lista6,muni6 ):
                         print(l1,l2)  
    
                     #DEP 7
                elif depart == "Cuscatlán".upper():
                    
                     print(f"--- INFORMACION DEL DEPARTAMENTO DE {depart} ---")
    
                     print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON:")
                     lista7=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17]          
                     muni7=["Candelaria" , "Cojutepeque" , "El Carmen" , "El Rosario" , "Monte San Juan" , 
                           "Oratorio de Concepción" , "San Bartolomé Perulapía" , "San Cristóbal" ," San José Guayabal" ,
                           "San Pedro Perulapán" , "San Rafael Cedros" , "San Ramón"
                           , "Santa Cruz Analquito" , "Santa Cruz Michapa", "Suchitoto" , "Tenancingo"]
                     for l1,l2 in zip(lista7,muni7):
                           print(l1,l2)
                    
                    #DEP 8
                elif depart == "Cabañas".upper():
                     print(f"--- INFORMACION DEL DEPARTAMENTO DE {depart} ---")
    
                     print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON:")
                     lista8=[1,2,3,4,5,6,7,8,9]   
                            
                     muni8=["Cinquera" , "Dolores" , "Guacotecti" , "Ilobasco " , "Jutiapa " , "San Isidro " , "Sensuntepeque " , "Tejutepeque " , "Victoria"]
                     for l1,l2 in zip(lista8,muni8):
                      print(l1,l2)
                
                    #DEP 9
                elif depart == "La Paz".upper():
                    
                  print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {depart} ---")
        
                  print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON :") 
                  lista9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14,15,16,17,18,19,20,21,22]
                  muni9 = ["Zacatecoluca", "Cuyultitán", "El Rosario", "Jerusalén", 
                              "Mercedes La Ceiba", "Olocuilta", "Paraíso de Osorio", 
                             "San Antonio Masahuat", "San Emigdio", "San Francisco Chinameca", 
                             "San Pedro Masahuat", "San Juan Nonualco","San Juan Talpa","San Juan Tepezontes","San Luis La Herradura"
                             ,"San Luis Talpa","San Miguel Tepezonte","San Pedro Nonualco","San Rafael Obrajuelo","San María Ostuma","Santiago Nonualco",
                             "Tapalhuaca"]
                  for l1,l2 in zip (lista9,muni9):
                        print(l1, l2)
                      
                           #DEP 10
                elif depart == "San Vicente".upper():
                    
                    print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {depart} ---")
        
                    print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON :") 
                    
                    lista10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13]
                    muni10 = ["Apastepeque", "Guadalupe", "San Cayetano Istepeque", 
                             "San Esteban Catarina", "San Ildefonso", "San Lorenzo", 
                             "San Sebastián", "San Vicente", "Santa Clara", "Santo Domingo", 
                             "Tecoluca", "Tepetitán", "Verapaz"]
                    for l1,l2 in zip (lista10,muni10):
                        print(l1, l2)
                
                      #DEP 11
                elif depart == "Usulután".upper():
                  print(f"---INFORMACIÓN DEL DEPARTAMENTO DE: {depart}---")
     
                  print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON:")
                  lista11=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
                  muni11=["Alegría", "Berlín", "California", "Concepción Batres", "El Triunfo", "Ereguayquín", "Estanzuelas", 
                                "Jiquilisco", "Jucuapa", "Jucuarán", "Mercedes Umaña", "Nueva Granada", "Ozatlán", "Puerto El Triunfo", 
                                 "San Agustín", "San Buenaventura", "San Dionisio", "San Francisco Javier", "Santa Elena", 
                                "Santa María", "Santiago de María", "Tecapán", "Usulután"]
                  for l1,l2 in zip(lista11,muni11):
                      print(l1,l2)
                    
                       #DEP 12
                elif depart == "San Miguel".upper():
                    
                     print(f"---INFORMACIÓN DEL DEPARTAMENTO DE: {depart}---")
        
                     print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON:")
                     lista12=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
                     
                     muni12=["Carolina", "Chapeltique", "Chinameca", "Chirilagua", "Ciudad Barrios", "Comacarán",
                              "El Tránsito", "Lolotique", "Moncagua", "Nueva Guadalupe", "Nuevo Edén de San Juan", "Quelepa", "San Antonio del Mosco",   
                             "San Gerardo", "San Jorge", "San Luis de la Reina", "San Miguel", "San Rafael Oriente", "Sesori", "Uluazapa",]
                     for l1,l2 in zip(lista12,muni12):
                         print(l1,l2)
                    
                    #DEP 13
                elif depart == "Morazán".upper():
                    print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {depart} ---")
        
                    print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {depart} SON :")
                
                    lista13=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
                    muni13=["Arambla", "Cacaopera", "Chilanga", "Corinto", "Delicias de concepción", 
                            "El Divisadero", "El Rosario", "Gualocoti", "Guatajiagua", "Joateca",
                             "Jocoatique", "Jocoro", "Lolotiquillo", "Osicala", "Perquin",
                            "San Carlos", "San Fernando", "San Francisco Gotera", "San Isidro", "Sam Simón",
                            "Sensembra", "Sociedad", "Torola", "Yamabla", "Yoloaiquin"]
                    for l1,l2 in zip(lista13,muni13):
                        print(l1,l2)
             
                   #DEP 14
                elif depart == "La Unión".upper():
                    
                    print(f"---INFORMACIÓN DEL DEPARTAMENTO DE {depart} ---")
    
                    print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE LA UNIÓN DE {depart} SON :")
                    lista14=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
                    muni14=["Anamorós", "Bolívar", "Concepción de Oriente", "Conchagua", "El Carmen", "El Sauce", "Intipucá", "La Unión", "Lislique", 
                        	"Meanguera del Golfo", "Nueva Esparta", "Pasaquina", "Polorós", "San Alejo", "San José", "Santa Rosa de Lima", "Yayantique", "Yucuaiquín"]
                    for l1,l2 in zip (lista14,muni14):
                        print(l1, l2)
                          
                else:
#ADVERTENCIA DE QUE EL DATO QUE EL USUARIO INGRESÓ NO FUE ENCONTRADO
                  intentos -= 1
                  if intentos > 0:
                        print(f"DEPARTAMENTO NO ENCONTRADO INGRESE UN NOMBRE VÁLIDO. LE QUEDAN  {intentos} INTENTOS.")
                        continue
                  else:
                        print("Número máximo de intentos finalizado.")
                            
                            #Preguntar si desea consultar otro dato
                
                respuesta = input("¿DESEA CONSULTAR INFORMACIÓN DE OTRO DEPARTAMENTO ? (si/no): ")
                if respuesta.lower() == "si":
                    continue
                elif respuesta.lower() == "no":
                    print("Programa finalizado.")
                    break
                else:
                     intentos -= 1
                     if intentos > 0:
                        print(f"DEPARTAMENTO NO ENCONTRADO INGRESE UN NOMBRE VÁLIDO. LE QUEDAN  {intentos} INTENTOS.")
                        continue
                  
                print("Fin del programa")
                break   
        else:            
            print("Fin del programa")
        break