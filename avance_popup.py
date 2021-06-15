import os
"""
Si quieres modificar tu template, elimina el texto que se agrega en el template con la funcion de agregar_popup.
Después que modifiques tu template, asegura que exista un espacio en blanco en una línea específicamente,
para que el texto del pop up pueda ser escrito y no suceda un error. 
Luego puedes usar la funcion de agregar_popup 
(solo se agregará el script en aquel template que lo necesite)
"""
def agregar_popup(directorio1,directorio2,nombre_texto,instructions_template,waitpage_template,minutos_pagenormal,minutos_waitpage):
    """
    Lo que hace la función es agregar un texto en cada template de un proyecto en otree que permita
    el uso de popups en cada página de los experimentos. Sin embargo, para el caso de los template de
    instrucciones no se agregará el popup, puesto que usualmente el template de las instrucciones está 
    en todos los templates. Waitpage tiene otro texto de popup, es por esa razón que se debe crear un
    waitpage costumizable para poder correr la función.
    Input:
    directorio de los templates de la aplicacion (string), 
    el archivo txt que tiene el cuerpo del pop up (string), 
    nombre del archivo con los mensajes del popup (string), 
    nombre del template que contiene las instrucciones (string), 
    nombre del template que es un waitpage(string),
    minutos antes de que aparezca el popup en un template normal (int),
    minutos antes de que aparezca el popup en un waipage (int)
    Output:
    None
    """
    os.chdir(directorio2) #abres el directorio del texto que contiene los popup en python
    abrir_file_texto=open(nombre_texto,"r+") 
    file_texto=abrir_file_texto.readlines()
    lista_texto_popup=[] #lista que contiene los textos a leer en el popup
    lista_minutos=[minutos_pagenormal*60,minutos_waitpage*60] #lista que contiene los minutos de espera antes de que aparezca el popup
   
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
   
        if template==waitpage_template: #si el template es el waitpage....
            abrir_file=open(template,"r+")
            """
            diferencia entre script y script2:
            script es para aquellos templates que no contengan {% block content %}
            script2 es para aquellos templates que sí contienen un {% block content %}
            """
            script="\n{% block content %}\n \n <script>\n setTimeout( \n function(){\n alert('"+str(lista_texto_popup[1])+"');\n },\n "+str(lista_minutos[1])+"*1000) // "+str(lista_minutos[1])+" segundos\n </script>\n \n{% endblock %}\n \n"
            script2="\n{% block content %}\n \n <script>\n setTimeout( \n function(){\n alert('"+str(lista_texto_popup[1])+"');\n },\n "+str(lista_minutos[1])+"*1000) // "+str(lista_minutos[1])+" segundos\n </script>\n \n"
            texto_file=abrir_file.readlines() #lista con cada línea del html en cada elemento.

            if " alert('"+str(lista_texto_popup[1])+"');\n" in texto_file: #si ya se escribió la función alert previamente, no se hará nada
                pass
            else:
                if '{% block content %}\n' in texto_file:
                    """
                    Se agrega el script2 en la lista que tiene como elementos las líneas del template, 
                    posteriormente se junta esta lista, creando un texto llamado 'new text'. 
                    Luego, se abre de nuevo el template, pero solo con el método "w". 
                    Finalmente, se transcribe el template con 'new_text', que contiene todo el texto del template incluido 
                    el script2.
                    """
                    pos=texto_file.index('{% block content %}\n')#posición del {%block content%}
                    texto_file[pos]=script2 #en la línea donde está el {%block content%} se escribirá un nuevo texto que contiene el texto del script2
                    new_text="".join(texto_file) #juntas la lista en un texto
                    abrir_file.close() 
                    abrir_segundo_file=open(template,"w") #abres por segunda vez el archivo, pero solo con el método write
                    abrir_segundo_file.write(new_text) #transcribes 
                    abrir_segundo_file.close()
           
                else:
                    """
                    Se agrega el script en la lista que tiene como elementos las líneas del template, 
                    posteriormente se junta esta lista, creando un texto llamado 'new text'. 
                    Luego, se abre de nuevo el template, pero solo con el método "w". 
                    Finalmente, se transcribe el template con 'new_text', que contiene todo el texto del template incluido 
                    el script.
                    """
                    pos=texto_file.index('\n')#posición del primer espacio en blanco del template
                    texto_file[pos]=script
                    new_text="".join(texto_file)
                    abrir_file.close()
                    abrir_2file=open(template,"w")
                    abrir_2file.write(new_text)
                    abrir_2file.close()
        
        elif template==instructions_template: #no escribir el 'script' o 'script2' en el template de instrucciones
            pass
        
        else:
            abrir_file=open(template,"r+")
            script="\n{% block content %}\n \n <script>\n setTimeout( \n function(){\n alert('"+str(lista_texto_popup[0])+"');\n },\n "+str(lista_minutos[0])+"*1000) // "+str(lista_minutos[0])+" segundos\n </script>\n \n{% endblock %}\n \n"
            script2="\n{% block content %}\n \n <script>\n setTimeout( \n function(){\n alert('"+str(lista_texto_popup[0])+"');\n },\n "+str(lista_minutos[0])+"*1000) // "+str(lista_minutos[0])+" segundos\n </script>\n \n"
            texto_file=abrir_file.readlines()

            if " alert('"+str(lista_texto_popup[0])+"');\n" in texto_file: #si ya se escribió la función alert previamente, no se hará nada
                pass
            else:
                if '{% block content %}\n' in texto_file:
                    """
                    Se agrega el script2 en la lista que tiene como elementos las líneas del template, 
                    posteriormente se junta esta lista, creando un texto llamado 'new text'. 
                    Luego, se abre de nuevo el template, pero solo con el método "w". 
                    Finalmente, se transcribe el template con 'new_text', que contiene todo el texto del template incluido 
                    el script2.
                    """
                    pos=texto_file.index('{% block content %}\n')
                    #se va a sobreescribir el texto en el html, por eso se usa el método write.
                    texto_file[pos]=script2
                    new_text="".join(texto_file)
                    abrir_file.close()
                    abrir_2file=open(template,"w")
                    abrir_2file.write(new_text)
                    abrir_2file.close()
           
                else:
                    """
                    Se agrega el script en la lista que tiene como elementos las líneas del template, 
                    posteriormente se junta esta lista, creando un texto llamado 'new text'. 
                    Luego, se abre de nuevo el template, pero solo con el método "w". 
                    Finalmente, se transcribe el template con 'new_text', que contiene todo el texto del template incluido 
                    el script.
                    """
                    pos=texto_file.index('\n')#posición del primer espacio en blanco del template
                    #se va a sobreescribir el texto en el html, por eso se usa el método write.
                    texto_file[pos]=script
                    new_text="".join(texto_file)
                    abrir_file.close()
                    abrir_2file=open(template,"w")
                    abrir_2file.write(new_text)
                    abrir_2file.close()

agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/popup/templates/popup","C:/Users/fredi/Desktop/python/e2labup/bertrandd","C:/Users/fredi/Desktop/python/e2labup/bertrandd/texto.html","instructions.html","MyWaitPage.html")

#l=open("C:/Users/fredi/Desktop/python/e2labup/bertrandd/popup/templates/popup/MyWaitPage.html","r+")
#print(l.readlines())