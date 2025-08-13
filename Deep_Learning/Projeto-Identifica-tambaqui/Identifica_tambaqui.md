# 1 Objetivo do Projeto CITHA - IFAM

O projeto CITHA surge com o objetivo de fortalecer a economia da Amazônia por meio
do incentivo ao empreendedorismo local e do desenvolvimento sustentável. Sua proposta é
capacitar profissionais e impulsionar a criação de startups voltadas para a bioeconomia, além
de apoiar cooperativas locais na melhoria de seus processos produtivos. A implementação de
tecnologias inovadoras é uma das estratégias centrais do projeto, visando oferecer soluções
eficientes que atendam às necessidades regionais, como a otimização dos recursos naturais e
a melhoria da infraestrutura local.

Ao longo de sua execução, o projeto se compromete a integrar os diversos stakeholders,
como governos, empresas, ONGs e comunidades, por meio da capacitação da mão de obra
local. O objetivo é formar um capital intelectual qualificado, capaz de apoiar uma governança
eficiente, promover a inovação e assegurar a sustentabilidade. O CITHA dedica-se à criação
de processos internos que incentivem o desenvolvimento de novos métodos e tecnologias,
adaptáveis às particularidades do território amazônico.

Em síntese, o projeto CITHA visa criar um ciclo de desenvolvimento que não só incentive
o empreendedorismo, mas também promova a modernização das estruturas locais, elevando
a qualidade de vida das populações da Amazônia. Focado em áreas como bioeconomia, inovação e transferência de tecnologia, o projeto busca estabelecer um ecossistema mais forte e autossustentável, capaz de responder eficientemente às demandas do mercado e da sociedade.

# 2 Projeto final (Identifica Tambaqui) - Redes Neurais

O projeto final que identifica 4 especies de peixes, não só o tambaqui, mas também piranha, pirarucu e tucunare utilizando de Redes Neurais Densas, Redes Convolucionais (CNN), Redes Recorrentes (RNN) com a linguagem de programação python e suas bibliotecas. Trabalho totalmente centrado em equipe de 8 pessoas, cada um com seu papel no projeto, sendo eles: Scrum Master, Desenvolvedores, Testadores, Documentaristas, com prazo de entrega de 7 dias e apresentação da IA Treinada.

## 2.1 Aprendizado da IA 

A IA teve como Treinamento um Dataset Pequeno de imagens que se localiza na pasta(train) e (test), pois ela precisa treina e testa o que acabou de aprender e verificar se errou, e aprender com esses erros, as imagens utilizadas são dos seguintes peixes tambaqui, piranha, pirarucu e tucunare, que são redemencionadas para o tamanho adequado para melhor tratamento de dados, utilizando o modelo senquencial e cada camada densa e ativada com ativação Relu e por ultimo a softmax para à categotização, uma vez que possuimos 4 classes de peixes e rotulamos elas de acordo com cada pasta e na mesma ordem, por fim mostrado o valor da acurácia - (Taxa de acerto, no caso dessa IA) 

## 2.2 Definição das Classes 

Para Classifição de fato dos Peixes, Foi feito uma função para Definir as Classes de cada peixe, primeiramente a imagem vira um array de numeros, por sengundo ela faz um predict com base nesse array de numeros (O predict ela tenta prever de fato a classe da imagem com base em uma sequencia de numeros do array) em seguida traz o posição desse numero, com base na posição desse numero e que criamos a limiar de confiança, que é a probabilidade de ser aquele peixe, por fim ela faz a defição da classe com quase certeza, com base nessa limiar de confiança, caso ela não encontre caracteristicas unicas para define a especie do peixe, ela diz INDETERMINADO, pois a limiar de confiança e baixa.



## 2.3 Definição Visual das Classes 

A IA pede pelo o CMD (Prompt de Comando) um caminho de uma imagem para fazer a previsão com base no que ela aprendeu durante o treinamento, e mostrado sua imagem e a decisão que ela tomou do que pode ser aquele peixe. 

# INFORMAÇÕES ADICIONAIS DO PROJETO - (Identifica Tambaqui)

No projeto (Identifica Tambaqui) além das pastas de treino e teste, colocamos algumas imagens da internet de diversos peixes e inclusive os que queremos identificar, em algumas dessas imagens possui poluições Exemplo(Pessoas, Casas, Vegetação, objetos..etc), mas tudo com um proposito de testa o real aprendizado da IA.

O arquivo de Treinamento do Modelo de IA *Treinamento_modelo.py*, toda vez que é feita execução dele, no final ele pergunta se você quer salva aquele modelo que você treinou, para sempre que você fizer alguma alteração, a IA sempre pega o melhor treino já feito.

Deixamos um arquivo python de que foi feito o treinamento do modelo, e outro que ja usar o modelo salvo treinado *Modelo_treinado.py* e o treino com a melhor acuracia de 89% *modelo_salvo_peixe.h5* 


# DECLARAÇÕES FINAIS

Essa documentação foi pensada por ***Wilken silva***, para pessoas leigas ou entusiastas possam entender o que esta acontecedo, tentar utilizar de alguma forma para as suas vidas....

### Bons estudos :)