#usa-se os métis rstrip() e lstrip() para eliminar espaços extras na strings

from xml.sax.xmlreader import AttributesImpl


minha_linguagem_favorita = "Python "
minha_linguagem_favorita.strip() # retira o espaço à direita
minha_linguagem_favorita.lstrip() # retira o espaço à esquerda
minha_linguagem_favorita.strip() # retira o espaço de ambos os lados


# Esse método atua de forma temporária, para usar a saida sem espaço extra de forma permanente devemos
# Atribuir essa saída a uma variável.

favorita = minha_linguagem_favorita.rstrip()