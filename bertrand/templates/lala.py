def agregar_popup(page):
    abrir_file=open(page,"r+")
    script="""
    <script>
        setTimeout(
    function () {
        alert("Hemos notado el tiempo que te ha tomado en la seccion actual del experimento y queremos saber si tienes algun inconveniente, duda o consulta. No olvide que su compañer@ esta esperando a que termine esta seccion para avanzar. ");
    },
    6*1000) // 6 seconds
    </script>

    """
    #holi=open("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html","r+")
    texto_file=abrir_file.readlines()
    pos=texto_file.index('\n')
    if texto_file[pos+1]== '    <script>\n':
        pass
    else:
        texto_file[pos]=script
        
        new_text="".join(texto_file)
        abrir_file.close()
        #holii=open("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html","w")
        abrir_2file=open(page,"w")
        abrir_2file.write(new_text)
        abrir_2file.close()
    
    
agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html")
agregar_popup("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/MyWaitPage.html")