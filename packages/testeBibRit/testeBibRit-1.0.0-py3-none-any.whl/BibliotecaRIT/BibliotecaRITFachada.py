# Importe das APIs de Extração de Dados
# Import das Classes de Inserção dos Dados Extraídos
# dir_raiz_script_exe = os.path.split(os.path.split(sys.argv[0])[0])[1]
import numpy as np
from BibliotecaRIT.Sources.Requisicao import Requisicao
from BibliotecaRIT.Sources.controladoras.ControladoraCalculoRelevancia import ControladoraCalculoRelevancia
from BibliotecaRIT.Sources.controladoras.ControladoraExportacaoDados import ControladoraExportacaoDados
from BibliotecaRIT.Sources.controladoras.ControladoraExtracaoDados import ControladoraExtracaoDados
from BibliotecaRIT.Sources.estrategias.exportacao.VisaoRelevanciaTematicaPorData import VisaoRelevanciaTematicaPorData
from BibliotecaRIT.Sources.estrategias.extracao.FiltroExtracaoIssuesAbertasFechadas import FiltroExtracaoIssuesAbertasFechadas
from BibliotecaRIT.Sources.estrategias.extracao.FiltroExtracaoIssuesFechadas import FiltroExtracaoIssuesFechadas


class BibliotecaRITFachada:
    def __init__(self, tokens=[]):
        print(tokens)
        Requisicao.init_tokens(tokens=tokens)

    @classmethod
    def calcularRelevanciaTematicaGitHub(cls,usuario, repositorio, visao, arg=""):
        tipoIssue = visao if visao < 4 else 3
        print('-- Processando Dados das Issues do Repositório --')
        projeto = cls.__processarDadosGitHub(usuario,repositorio,tipoIssue)
        print()
        print("Quantidade de tópicos: ", len(projeto.topicos))
        print('-- Processando o Cálculo da Relevância Temática dos Comentários de Cada Issue --')
        cls.__calcularRelevanciaTematicaComentariosGitHub(projeto)
        print()

        print('-- Gerando o .csv com os Resultados Obtidos --')
        cls.__gerarCSVGitHub(projeto, visao, arg)
        print()

    @staticmethod
    def __processarDadosGitHub(usuario, repositorio, tipoIssue):
        controladoraExtracao = ControladoraExtracaoDados
        if tipoIssue == 2:
            controladoraExtracao.setFiltroExtracaoStrategy(filtroExtracaoStrategy=FiltroExtracaoIssuesFechadas)
        elif tipoIssue == 3:
            controladoraExtracao.setFiltroExtracaoStrategy(filtroExtracaoStrategy=FiltroExtracaoIssuesAbertasFechadas)
    
        return controladoraExtracao.requisicaoIssues(usuario,repositorio)
    
    @staticmethod
    def __calcularRelevanciaTematicaComentariosGitHub(projeto):
        comentariosAnteriores = ''
        contador = 0
        for topico in projeto.topicos:
            print()
            print("Processando tópico número: ", topico.number)
            contador+= len(topico.listaComentarios)
            # print("Quantidade de comentários: ",len(topico.listaComentarios))
            for comentario in topico.listaComentarios:
                relevancia = ControladoraCalculoRelevancia.relevanciaTematica(comentario.mensagem, comentariosAnteriores, (str(topico.titulo) + str(topico.descricao)))
                comentariosAnteriores += comentario.mensagem
                comentario.inserirRelevanciaTematica(relevancia)
            print(f"Tópico número {topico.number} finalizado")
            print()
        print("Quantidade total comentários: ",contador)
    
    @staticmethod
    def __gerarCSVGitHub (projeto, visao,arg=""):
        controladoraExportacao = ControladoraExportacaoDados
        if(visao == 4):
            controladoraExportacao.setVisaoStrategy(visao=VisaoRelevanciaTematicaPorData)
        elif(visao == 5):
            controladoraExportacao.setVisaoStrategy(visao=VisaoRelevanciaTematicaPorData)
        controladoraExportacao.gerarCSV(projeto,arg)
    
    
