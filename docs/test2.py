from tfidf import TfIdf
import unittest
from operator import itemgetter


table = TfIdf()
table.add_document("oqueE", ["Business","Model","Generation","ou","simplesmente","Canvas","É","uma","metodologia","criada","em","meados","dos","anos","2000","pelo","Suíço","Alex","Osterwalder","durante","sua","Tese","de","Doutorado","na","prestigiada","HEC","Lausanne",",e","Yves","Pigneur.","O","Canvas","é","um","esquema","visual","que","possibilita","as","pessoas","cocriarem","modelos","de","negócios","analisando","9","elementos","que","toda","empresa","ou","organização","possuem:","proposta","de","valor","parcerias","chaves",",atividades","chaves",",recursos","chaves",",relacionamento","com","clientes",",segmentos","de","clientes",",canais","de","distribuição",",estrutura","de","custos","e","fluxo","de","receitas","(HSM",",2017","organização","do","empreendedor","de", "seus","concorrentes","ou","qual","quer","outra","empresa","Conforme","Osterwalder","e","Pigneur","o","conceito","Canvas","já","foi","aplicado","e","testado","em","todo","o","mundo","e","já","é","utilizado","por","grandes","organizações","como","IBM","Ericsson","Deloitte","Public","Works","o","governo","do","Canadá","entre","outras"]) 

table.add_document("ondeUsar", ["O","canvas","pode","ser","usado","em","companhia","firma","casa","negócio","sociedade","entidade","estabelecimento","instituição","organização","empregador","parceria","corporação","cometimento","desígnio","empreendimento","feito","intento","tentativa","projeto","realização","acometimento","elaboração","feitura","produção","trabalho","campanha","expedição","jornada."])
       
table.add_document("criadorCanvas", [ "Por","muitos","anos","o","termo","modelo","de","negócios","foi","usado","sem","um","consenso","na","sua","definição",".","Muitos","autores","o","mencionavam","sem","explicitar","do","que","exatamente","falavam","E","foi","exatamente","pensando","nisso","que","o","consultor","suíço","Alexander","Osterwalder", "começou","a","desenvolver","sua","tese","de","doutorado","que","daria","origem","ao","Business","Model","Canvas.","Alexander","percebeu","que","definir","o","termo","não","seria","suficiente.","Era","necessário","criar","algo","que","incentivasse","a","inovação,","a","prototipação","e","co-criação","(criação","colaborativa).","Utilizando-se,","assim,","de","conceitos","de","design","thinking","Alexander","começou","com","um","simples","gráfico","feito","em","powerpoint","que","anos","mais","tarde","se","tornaria","uma","bela","tela","(canvas)","separada","em","nove","blocos."])
ordena = table.similarities(["o", "que", "é", "canvas"])   
dicio = dict(ordena)
print sorted(dicio.items(), key=itemgetter(1),reverse=True)

#tableOrdenada = []tableCopia = ordena[:]
#while len(tableOrdenada) < len(ordena):
    #maior = tableCopia[0]
    #for a in tableCopia:
        #if a[1] > maior[1]:
            #maior = a
    #tableOrdenada.append(maior)
    #tableCopia.remove(maior)
#print(tableOrdenada)


