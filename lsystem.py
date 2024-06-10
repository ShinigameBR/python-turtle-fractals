class LSystem:
    def __init__(self, axiom: str, rules: dict, angle: int):
        """
        Inicializa o LSystem com um axioma inicial, um conjunto de regras de substituição e um ângulo.
        
        :param axiom: A string inicial do LSystem.
        :param rules: Um dicionário onde as chaves são caracteres e os valores são as regras de substituição.
        :param angle: O ângulo de rotação usado na interpretação gráfica (não usado na geração da string).
        """
        self.axiom = axiom
        self.rules = rules
        self.angle = angle

    def apply_rules(self, axiom: str) -> str:
        """
        Aplica as regras de substituição ao axioma.
        
        :param axiom: A string à qual aplicar as regras.
        :return: A nova string resultante da aplicação das regras.
        """
        return ''.join([self.rules.get(char, char) for char in axiom])

    def generate(self, generation: int) -> str:
        """
        Gera a string resultante após um número especificado de gerações.
        
        :param generation: O número de gerações a serem aplicadas.
        :return: A string resultante após todas as gerações.
        """
        current_axiom = self.axiom
        for _ in range(generation):
            current_axiom = self.apply_rules(current_axiom)
        return current_axiom