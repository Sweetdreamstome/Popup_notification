from bs4 import BeautifulSoup
lol=open("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html","r")
filee=lol.read()

def agregar_html(page):
    f1le=open(page,"r+")
    text=f1le.read()
    tet=""" 
    
    <script>
        setTimeout(
    function () {
        alert("Hemos notado el tiempo que te ha tomado en la sección actual del experimento y queremos saber si tienes algún inconveniente, duda o consulta. No olvide que su compañer@ esta esperando a que termine esta sección para avanzar. ");
    },
    6*1000) // 6 seconds
    </script>
    """
    find=text.find(" ")
    


    
    #f1le=open(page,"r+")
    #for line in f1le:
    #    if line==" ":
    #        f1le.write(tet)
    
    

agregar=agregar_html("C:/Users/fredi/Desktop/python/e2labup/bertrandd/bertrand/templates/bertrand/Decide.html")
