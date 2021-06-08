import os
"""
Si quieres modificar tu template, elimina el texto que se agrega en el template con la funcion de agregar_popup.
Después que modifiques tu template, asegura que exista un espacio en blanco para que el texto del
pop up pueda ser escrito y no suceda un error. Luego puedes usar la funcion de agregar_popup 
(solo se agregará el script en aquel template que lo necesite)
"""
def agregar_popup(directorio1,directorio2):
    """
    Input:
    directorio1: string que contiene el directorio de los templates de la aplicacion,
    directorio2: string que contiene el archivo txt que tiene el cuerpo del pop up.
    Output:
    Funcion de html en cada template.
    """
    os.chdir(directorio2) #abres el directorio del texto en python
    abrir_file_texto=open("texto.html","r+")
    file_texto=abrir_file_texto.readlines()
    lista1=[]
    #lista1="Somos el equipo E2LabUP. Hemos notado el tiempo que te ha tomado en la seccion actual del experimento y queremos saber si tienes algun inconveniente, duda o consulta.","Somos el equipo E2LabUP. No te preocupes por el tiempo de espera. Es parte del experimento. En unos momentos, podras avanzar a la siguiente seccion."]
    lista2=[6,3]
    #creas lista 1 con el siguiente for, además eliminas los espacios en blancos dentro del archivo texto.html
    for lista in file_texto:
        tag="\n"
        for word in range(len(tag)):
            lista=lista.replace(tag[word],"")
        lista1.append(lista)
        
        
        
    os.chdir(directorio1) #abres el directorio de los templates en python
    #Lista con todos los templates:
    lista=[]
    for fichero in os.scandir(directorio1):
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

#lista=["Somos el equipo E2LabUP. Hemos notado el tiempo que te ha tomado en la seccion actual del experimento y queremos saber si tienes algun inconveniente, duda o consulta.","Somos el equipo E2LabUP. No te preocupes por el tiempo de espera. Es parte del experimento. En unos momentos, podras avanzar a la siguiente seccion."]
#lista1=[6,3]


agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/popup/templates/popup","C:/Users/fredi/Desktop/python/e2labup/bertrandd")

