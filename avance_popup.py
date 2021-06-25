import os
def agregar_texto_html(texto_a_buscar,texto_file,script,template):   
    """
    Se agrega el script2 en la lista que tiene como elementos las líneas del template, posteriormente se junta esta lista, creando un texto llamado 'new text'. 
    Luego, se abre de nuevo el template con el método "w". Finalmente, se transcribe el template con 'new_text'.
    """
    pos=texto_file.index(texto_a_buscar)
    texto_file[pos]=script
    new_text="".join(texto_file)       
    abrir_2file=open(template,"w")
    abrir_2file.write(new_text)
    abrir_2file.close()

def agregar_popup():
    """
    Lo que hace la función es agregar un texto en cada template de un proyecto en otree que permita
    el uso de popups en cada página de los experimentos. 
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

    directorio1=input("Por favor, escriba el directorio de los template de la aplicación: ")
    directorio2=input("Por favor, escriba el directorio del .html que contiene el texto del popup: ")
    nombre_texto=input("Por favor, escriba el nombre del texto .html: ")
    instructions_template=input("Si tu template de instrucciones no se repite en otras páginas a parte del de introducción, pon 'No'; caso contrario, escriba el nombre de su template de instrucciones, por favor: ")
    waitpage_template=input("Por favor, escriba el nombre del template de su waitpage: ")
    minutos_pagenormal=input("Por favor, escriba los minutos que una persona puede mantenerse respondiendo una pregunta o leyendo en cualquier página: ")
    minutos_waitpage=input("Por favor, erscriba los minutos que una persona puede esperar en un WaitPage: ")


    os.chdir(directorio2) 
    abrir_file_texto=open(nombre_texto,"r+") 
    file_texto=abrir_file_texto.readlines()
    lista_texto_popup=[]
    #lista_minutos=[minutos_pagenormal*60,minutos_waitpage*60] 
    lista_minutos=[minutos_pagenormal,minutos_waitpage]
    #Creas lista que contiene el texto de cada popup, además eliminas los espacios en blanco dentro del archivo texto.html
    for lista in file_texto:
        tag="\n"
        for word in range(len(tag)):
            lista=lista.replace(tag[word],"")
        lista_texto_popup.append(lista)


    os.chdir(directorio1) 

    #Lista con todos los templates:
    lista_templates=[]
    for fichero in os.scandir(directorio1):
        lista_templates.append(fichero.name)

    #abrir el file y realizar el procedimiento para cada template dentro del directorio:
    for template in lista_templates: 
   
        if template==waitpage_template: 
            abrir_file=open(template,"r+")
            script="\n{% block content %}\n \n <script>\n setTimeout( \n function(){\n alert('"+str(lista_texto_popup[1])+"');\n },\n "+str(lista_minutos[1])+"*1000) // "+str(lista_minutos[1])+" segundos\n </script>\n \n{% endblock %}\n \n"
            script2="\n{% block content %}\n \n <script>\n setTimeout( \n function(){\n alert('"+str(lista_texto_popup[1])+"');\n },\n "+str(lista_minutos[1])+"*1000) // "+str(lista_minutos[1])+" segundos\n </script>\n \n"
            texto_file=abrir_file.readlines()

            if " alert('"+str(lista_texto_popup[1])+"');\n" in texto_file: 
                pass
            else:
                if '{% block content %}\n' in texto_file:
                    
                    agregar_texto_html('{% block content %}\n',texto_file,script2,template)
           
                else:
                    agregar_texto_html('\n',texto_file,script,template)
                    
    
        elif instructions_template!='No':#no escribir el 'script' o 'script2' en el template de instrucciones
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
                    agregar_texto_html('{% block content %}\n',texto_file,script2,template)
                    
                else:
                    agregar_texto_html('\n',texto_file,script,template)
                

#agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/popup/templates/popup","C:/Users/fredi/Desktop/python/e2labup/bertrandd","C:/Users/fredi/Desktop/python/e2labup/bertrandd/texto.html","instructions.html","MyWaitPage.html",6,3)

agregar_popup()
