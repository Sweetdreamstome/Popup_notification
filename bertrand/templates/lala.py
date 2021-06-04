
def agregar_popup(url, page, seconds):
    abrir_file=open(url,"r+")
    script="\n <script>\n setTimeout( \n function(){\n alert('"+str(page)+"');\n },\n "+str(seconds)+"*1000) // "+str(seconds)+" seconds\n </script>\n \n"
    #holi=open("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html","r+")
    texto_file=abrir_file.readlines()
    pos=texto_file.index('\n')
    if texto_file[pos+1]== ' <script>\n':
        pass
    else:
        texto_file[pos]=script
        
        new_text="".join(texto_file)
        abrir_file.close()
        #holii=open("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html","w")
        abrir_2file=open(url,"w")
        abrir_2file.write(new_text)
        abrir_2file.close()
    
lista=["Somos el equipo E2LabUP. Hemos notado el tiempo que te ha tomado en la seccion actual del experimento y queremos saber si tienes algun inconveniente, duda o consulta.","Somos el equipo E2LabUP. No te preocupes por el tiempo de espera. Es parte del experimento. En unos momentos, podras avanzar a la siguiente seccion."]
lista1=[6,3]
agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html",lista[0],lista1[0])
agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/MyWaitPage.html",lista[1],lista1[1])

text=open("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html","r+")
print(text.readlines())