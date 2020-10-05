## Introdução

As duas maiores causas de morte no mundo são cardiopatia isquêmica e acidente vascular cerebral, no ano de 2016 foram responsáveis por 15,2 milhões de óbitos no mundo. Não muito longe encontra-se em **8º lugar mortes causadas por acidentes de trânsito** que no mesmo ano mataram cerca de 1,4 milhão de pessoas, dos quais cerca de três quartos (74%) foram homens e meninos. (1) 


**Os acidentes de trânsito são ainda a melhor forma de aborto para pós-nascidos, liderando como a principal causa de morte infantil. (2)**


Segundo o relatório ["GLOBAL STATUS REPORT ON ROAD SAFETY 2018"] da divisão de saúde da ONU, o número absoluto de mortes no trânsito cresce anualmente como pode ser visto na figura 1. 

![Figura1](https://raw.githubusercontent.com/lcscosta/BACEyeD/master/docs/images/fig1.png)<br />
Figura 1: Gráfico do número de mortes absoluto e relativo ao longo dos anos.

Nos EUA, de acordo com o departamento de transportes daquele país, estima-se que o gasto público com acidentes de carro causados por motoristas embriagados seja de aproximadamente US$ 44 bilhões (~10500 mortes).

Aqui no Brasil, segundo relatório da PRF, ao longo de 2019, o total de acidentes em BRs provocados por motoristas embriagados foi de 5.631, sendo 1.412 graves. Além disso, cerca de 18 mil motoristas foram notificados por serem flagrados dirigindo sob efeito de álcool.

Entre as medidas que servem como mitigadoras está a lei de regulamentação do consumo de álcool e dirigir, conhecida como Lei Seca, onde possui a seguinte distribuição de países que possuem legislação a respeito:

![Figura2](https://raw.githubusercontent.com/lcscosta/BACEyeD/master/docs/images/fig2.png)<br />
Figura 2: Mapa dos países que possuem leis de regulamentação do consumo de álcool e dirigir.

O parâmetro utilizado para definir o estado de embriaguez de um indivíduo é chamado de BAC (Blood Alcohol Concentration), dado na unidade de gramas por dl. A atual forma de se estimar este parâmetro está nos bafômetros ....



## Objetivos

Entre os objetivos do projeto são a criação de um bafômetro utilizando um arduíno e também utilizar dos dados coletados pelo bafômetro juntamente com fotos para treinar uma inteligência artificial capaz de detectar alterações fisiológicas que possam ser associadas à BAC, entre as alterações que esperamos observar está a dilatação da pupila que podemos identificar por meio da figura 3.

![Figura4](https://raw.githubusercontent.com/lcscosta/BACEyeD/master/docs/images/fig4.png)<br />
Figura 3: Labelling de uma imagem, delimitando íris e pupila.

## Materiais

Entre os materiais utilizados para a realização do projeto estão listados:

- 1 arduino uno
- 1 sensor de alcool MQ3
- 1 display
- Resistores
- Potenciometro

## Métodos

Primeiramente será construído o bafômetro utilizando os materiais acima listados, sendo que o circuito utilizado está descrito na figura abaixo:

![Figura3](https://raw.githubusercontent.com/lcscosta/BACEyeD/master/docs/images/fig3.jpeg)<br />
Figura 4: Imagem esquemática do circuito utilizado para fazer o bafômetro.

Para a identificação da dilatação da pupila utilizaremos uma rede neural focada em classificação, o modelo de inteligência artifical a ser utilizado é a MobileNet devido à sua alta portatibilidade.

![Figura3](https://raw.githubusercontent.com/lcscosta/BACEyeD/master/docs/images/fig5.png)<br />
Figura 5: Apresentação da MobileNet e suas várias aplicações.

Um exemplo de classificação que pode ser realizada é dada pela imagem abaixo:

![Figura3](https://raw.githubusercontent.com/lcscosta/BACEyeD/master/docs/images/fig6.png)<br />
Figura 6: Classificação de uma imagem em termos dos diferentes objetos pelo qual o modelo foi treinado a reconhecer.

As MobileNets são uma classe de convolução de redes neurais projetadas por pesquisadores do Google. 

![Figura3](https://miro.medium.com/max/1000/1*vkQ0hXDaQv57sALXAJquxA.jpeg)<br />
Figura 7: Funcionamento de uma Rede Neural Convolucional.


## Resultados 

...

### Autores

Lucas Murilo da Costa<br />
[lucasdacosta@usp.br](mailto:lucasdacosta@usp.br)

Marcelo Manduca<br />
[marcelo.manduca@usp.br](mailto:marcelo.manduca@usp.br)

Mateus Simões<br />
[mateusmrsimoes@usp.br](mailto:mateusmrsimoes@usp.br)
