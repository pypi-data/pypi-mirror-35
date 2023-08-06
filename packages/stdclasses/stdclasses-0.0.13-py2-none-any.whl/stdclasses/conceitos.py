class IAList:

    @classmethod
    def reconhecimento_padroes(cls):
        return "reconhecimento_padroes"

    @classmethod
    def etapas_reconhecimento_padroes(cls):
        return """
           etapas_reconhecimento_padroes
        """

    @classmethod
    def modalidades_machine_learn(cls):
        return """
           modalidades_machine_learn
        """,

    @classmethod
    def classificação_linear_nao_linear(cls):
        return """
           classificação_linear_nao_linear
        """,

    @classmethod
    def machine_learning(cls):
        return """"
        machine_learning
        """

    @classmethod
    def all(cls):
        return {
            "1. Reconhecimento de padrões?": cls.reconhecimento_padroes(),
            "2. Etapas reconhecimento de padrões": (
                cls.etapas_reconhecimento_padroes()
            ),
            "3. Modalidades de aprendizagem em machine learning": (
                cls.modalidades_machine_learn()
            ),
            """
                4. Classificadores lineares e nao-lineares? Pesquise e
                de um exemplo de cada. O kNN encontra-se em que categoria?
            """: cls.classificação_linear_nao_linear(),
            "Machine Learning": cls.machine_learning()
        }