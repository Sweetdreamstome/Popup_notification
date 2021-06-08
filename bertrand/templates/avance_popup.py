import os
def agregar_popup(directorio):
    #directorio: string que contiene el directorio de los templates de la aplicación

    os.chdir(directorio) #abres el directorio en python
    
    #Diccionario con los textos y minutos:
    lista1=["Somos el equipo E2LabUP. Hemos notado el tiempo que te ha tomado en la seccion actual del experimento y queremos saber si tienes algun inconveniente, duda o consulta.","Somos el equipo E2LabUP. No te preocupes por el tiempo de espera. Es parte del experimento. En unos momentos, podras avanzar a la siguiente seccion."]
    lista2=[6,3]
    #Lista con todos los templates:
    lista=[]
    for fichero in os.scandir(directorio):
        lista.append(fichero.name)

    #abrir el file y realizar el procedimiento para cada template dentro del directorio:
    for template in lista: 
        if template=="MyWaitPage.html":
            abrir_file=open(template,"r+")
            script="\n <script>\n setTimeout( \n function(){\n alert('"+str(lista1[1])+"');\n },\n "+str(lista2[1])+"*1000) // "+str(lista2[1])+" minutos\n </script>\n \n"
            texto_file=abrir_file.readlines()
            pos=texto_file.index('\n')
            if texto_file[pos+1]== ' <script>\n': #si ya ha sido escrito antes, la función no debería hacer nada 
                pass
            else:
                #se va a sobreescribir el texto en el html, por eso se usa el método write.
                texto_file[pos]=script
                new_text="".join(texto_file)
                abrir_file.close()
                abrir_2file=open(template,"w")
                abrir_2file.write(new_text)
                abrir_2file.close()
        else:
            abrir_file=open(template,"r+")
            script="\n <script>\n setTimeout( \n function(){\n alert('"+str(lista1[0])+"');\n },\n "+str(lista2[0])+"*1000) // "+str(lista2[0])+" minutos\n </script>\n \n"
            texto_file=abrir_file.readlines()
            pos=texto_file.index('\n')
            if texto_file[pos+1]== ' <script>\n': #si ya ha sido escrito antes, la función no debería hacer nada 
                pass
            else:
                #se va a sobreescribir el texto en el html, por eso se usa el método write.
                texto_file[pos]=script
                new_text="".join(texto_file)
                abrir_file.close()
                abrir_2file=open(template,"w")
                abrir_2file.write(new_text)
                abrir_2file.close()

lista=["Somos el equipo E2LabUP. Hemos notado el tiempo que te ha tomado en la seccion actual del experimento y queremos saber si tienes algun inconveniente, duda o consulta.","Somos el equipo E2LabUP. No te preocupes por el tiempo de espera. Es parte del experimento. En unos momentos, podras avanzar a la siguiente seccion."]
lista1=[6,3]
#agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html",lista[0],lista1[0])
#agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/MyWaitPage.html",lista[1],lista1[1])

#Ahora voy a tratar de leer directorios en un archivo...
#dir="C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand"
#with os.scandir(dir) as ficheros:
#    for fichero in ficheros:
#        print(fichero.name)

# crearé una lista con esos nombres...
#url=[]
#for fichero in os.scandir(dir):
#    url.append(fichero.name)

#ahora intentare usar este url en la funcion agregar_popup
#url=['Decide.html', 'instructions.html', 'Introduction.html', 'MyWaitPage.html', 'Results.html', 'TestMobile.html']
#agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand",url[0],lista[0],lista1[0])
#agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand",url[3],lista[1],lista1[1])

#y salió


#si quieres modificar tu template, elimina el script que se agrega con la funcion de agregar_popup
#después que modifiques tu template, asegura que exista un espacio en blanco para que el html pueda ser 
#escrito y no suceda un errror. Luego puedes usar la funcion de agregar_popup

agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand")