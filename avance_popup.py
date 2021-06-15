import os
"""
Si quieres modificar tu template, elimina el texto que se agrega en el template con la funcion de agregar_popup.
Después que modifiques tu template, asegura que exista un espacio en blanco para que el texto del
pop up pueda ser escrito y no suceda un error. Luego puedes usar la funcion de agregar_popup 
(solo se agregará el script en aquel template que lo necesite)
"""
def agregar_popup(directorio1,directorio2,directorio_del_texto,instructions_template,waitpage_template):
    """
    Lo que hace la función es agregar un texto en cada template de un proyecto en otree que permita
    el uso de popups en cada página de los experimentos.
    Input:
    directorio de los templates de la aplicacion (string), el archivo txt que tiene el cuerpo del pop up (string), directorio del archivo con los mensajes del popup (string), nombre del template que contiene las instrucciones (string), nombre del template que es un waitpage(string)
    Output:
    None
    """
    os.chdir(directorio2) #abres el directorio del texto en python
    abrir_file_texto=open(directorio_del_texto,"r+") #texto.html contiene el texto de c/ popup
    file_texto=abrir_file_texto.readlines()
    lista_texto_popup=[]
    lista_minutos=[6,3]
    #creas lista que contiene el texto de cada popup, además eliminas los espacios en blanco dentro del archivo texto.html
    for lista in file_texto:
        tag="\n"
        for word in range(len(tag)):
            lista=lista.replace(tag[word],"")
        lista_texto_popup.append(lista)


    os.chdir(directorio1) #abres el directorio de los templates en python
    #Lista con todos los templates:
    lista_templates=[]
    for fichero in os.scandir(directorio1):
        lista_templates.append(fichero.name)

    #abrir el file y realizar el procedimiento para cada template dentro del directorio:
    for template in lista_templates: 
   
        if template==waitpage_template:
            abrir_file=open(template,"r+")
            script="\n{ % block content % }\n <script>\n setTimeout( \n function(){\n alert('"+str(lista_texto_popup[1])+"');\n },\n "+str(lista_minutos[1])+"*1000) // "+str(lista_minutos[1])+" segundos\n </script>\n{ % endblock % }\n \n"
            script2="\n <script>\n setTimeout( \n function(){\n alert('"+str(lista_texto_popup[1])+"');\n },\n "+str(lista_minutos[1])+"*1000) // "+str(lista_minutos[1])+" segundos\n </script>\n \n"
            texto_file=abrir_file.readlines()

            if " alert('"+str(lista_texto_popup[1])+"');\n" in texto_file:
                pass
            else:
                if '{% block content %}\n' in texto_file:
                    pos=texto_file.index('{% block content %}\n')#posición del {%block content%}
                    #se va a sobreescribir el texto en el html, por eso se usa el método write.
                    texto_file[pos+1]=script2
                    new_text="".join(texto_file)
                    abrir_file.close()
                    abrir_2file=open(template,"w")
                    abrir_2file.write(new_text)
                    abrir_2file.close()
           
                else:
                    pos=texto_file.index('\n')#posición del primer espacio en blanco del template
                    #se va a sobreescribir el texto en el html, por eso se usa el método write.
                    texto_file[pos+1]=script
                    new_text="".join(texto_file)
                    abrir_file.close()
                    abrir_2file=open(template,"w")
                    abrir_2file.write(new_text)
                    abrir_2file.close()
        
        elif template==instructions_template:
            pass
        
        else:
            abrir_file=open(template,"r+")
            script="\n{ % block content % }\n <script>\n setTimeout( \n function(){\n alert('"+str(lista_texto_popup[0])+"');\n },\n "+str(lista_minutos[0])+"*1000) // "+str(lista_minutos[0])+" segundos\n </script>\n{ % endblock % }\n \n"
            script2="\n <script>\n setTimeout( \n function(){\n alert('"+str(lista_texto_popup[0])+"');\n },\n "+str(lista_minutos[0])+"*1000) // "+str(lista_minutos[0])+" segundos\n </script>\n \n"
            texto_file=abrir_file.readlines()

            if " alert('"+str(lista_texto_popup[0])+"');\n" in texto_file:
                pass
            else:
                if '{% block content %}\n' in texto_file:
                    pos=texto_file.index('{% block content %}\n')
                    #se va a sobreescribir el texto en el html, por eso se usa el método write.
                    texto_file[pos+1]=script2
                    new_text="".join(texto_file)
                    abrir_file.close()
                    abrir_2file=open(template,"w")
                    abrir_2file.write(new_text)
                    abrir_2file.close()
           
                else:
                    pos=texto_file.index('\n')#posición del primer espacio en blanco del template
                    #se va a sobreescribir el texto en el html, por eso se usa el método write.
                    texto_file[pos+1]=script
                    new_text="".join(texto_file)
                    abrir_file.close()
                    abrir_2file=open(template,"w")
                    abrir_2file.write(new_text)
                    abrir_2file.close()

agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/popup/templates/popup","C:/Users/fredi/Desktop/python/e2labup/bertrandd","C:/Users/fredi/Desktop/python/e2labup/bertrandd/texto.html","instructions.html","MyWaitPage.html")

#l=open("C:/Users/fredi/Desktop/python/e2labup/bertrandd/popup/templates/popup/TestMobile.html","r+")
#print(l.readlines())