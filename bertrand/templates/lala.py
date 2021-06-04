import os
def agregar_popup(directorio,url, page, seconds):
    #directorio: string que contiene el directorio de los templates de la aplicación
    #url: string del nombre de los templates respectivos
    #page: string que contiene el anuncio a escribir dentro del popup
    #seconds: int de los segundos a esperar para que aparezca el popup
    os.chdir(directorio)
    abrir_file=open(url,"r+")
    script="\n <script>\n setTimeout( \n function(){\n alert('"+str(page)+"');\n },\n "+str(seconds)+"*1000) // "+str(seconds)+" seconds\n </script>\n \n"
    texto_file=abrir_file.readlines()
    pos=texto_file.index('\n')
    if texto_file[pos+1]== ' <script>\n':
        pass
    else:
        texto_file[pos]=script
        
        new_text="".join(texto_file)
        abrir_file.close()
        abrir_2file=open(url,"w")
        abrir_2file.write(new_text)
        abrir_2file.close()
    
lista=["Somos el equipo E2LabUP. Hemos notado el tiempo que te ha tomado en la seccion actual del experimento y queremos saber si tienes algun inconveniente, duda o consulta.","Somos el equipo E2LabUP. No te preocupes por el tiempo de espera. Es parte del experimento. En unos momentos, podras avanzar a la siguiente seccion."]
lista1=[6,3]
#agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html",lista[0],lista1[0])
#agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/MyWaitPage.html",lista[1],lista1[1])

#Ahora voy a tratar de leer directorios en un archivo...
dir="C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand"
with os.scandir(dir) as ficheros:
    for fichero in ficheros:
        print(fichero.name)

#creo que ya esta hecho, crearé una lista con esos nombres...
url=[]
for fichero in os.scandir(dir):
    url.append(fichero.name)

#ahora intentare usar este url en la funcion agregar_popup
#url=['Decide.html', 'instructions.html', 'Introduction.html', 'MyWaitPage.html', 'Results.html', 'TestMobile.html']
agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand",url[0],lista[0],lista1[0])
agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand",url[3],lista[1],lista1[1])

#y salió