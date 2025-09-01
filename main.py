from fastapi import FastAPI
app = FastAPI()


receitas = [
    {
        'nome' : 'Brownie',
        'ingredientes' : ['5 colheres de manteiga', '3 xicara de achocolatado', '12 colheres de farinha de trigo', '3 ovos', '6 colheres de açucar'],
        'utensílios' : ['Bowl', 'Forma', 'Prato de sobremesa', 'Espatula', 'Fouet'],
        'modo de preparo' : '1- Derreta a manteiga e reserve; 2- Enquanto derrete a manteiga, misture os 3 ovos e a açúcar e misture bem; 3- Acrescente a manteiga derretida no ovo e o açúcar; 4- Agora é so misturar o achocolatado e o trigo; 5- Unte uma forma com manteiga e achocolatado; 6- Leve ao forno a 180° C por 30 minutos'
    },
    {
        'nome' : 'Salada Caesar',
        'ingredientes' : ['1 pacote de frango em tiras', '1 gema de ovo', '1 colher de sopa de mostarda Dijon', 'Suco de ½ limão', '1 pitada de pimenta', '½ xícara de óleo de girassol', '½ xícara de parmesão de boa qualidade ralado', '1 maço de alface americana ou romana lavado', '1 xícara de croutons'],
        'utensílios' : ['Bowl', 'Faca', 'Tábua de corte', 'Pegador multiuso'],
        'modo de preparo' : '1- Grelhe o frango; 2- Para fazer o molho, misture a gema de ovo, com a mostarda, o limão e a pimenta. Acrescente devagar o óleo batendo bem com um batedor de arame emulsionando essa mistura. Vai ficar um molho cremoso; 3- Acrescente metade do parmesão ralado e acerte o sal; 4- Misture a alface com esse molho, com o frango e os croutons e finalize com o restante do parmesão. Sirva.'

    },
    {
'nome' : 'Tonkatsu',
'ingredientes' : ['1 bisteca de porco', '2 colheres (sopa) de farinha de trigo', 'sal e pimenta-do-reino a gosto', 'molho para tonkatsu a gosto', '1 ovo levemente batido', '4 colheres (sopa) de farinha panko ou farinha de rosca', 'óleo para fritar'],
'utensílios' : ['Frigideira', 'Tigela'],
'modo de preparo' : '1- Tempere a bisteca de porco com sal e pimenta-do-reino; 2- Passe a bisteca no ovo levemente batido; 3- Em seguida, passe-a na farinha de trigo; 4- Passe a bisteca no ovo novamente e finalize passando na farinha de rosca ou farinha panko; 5- Aqueça uma frigideira com óleo em temperatura média; 6- Frite a bisteca até ficar dourada dos dois lados; 7- Corte-a em fatias de mais ou menos 1 dedo de largura; 8- Sirva com molho tonkatsu.'

    },
    {
        'nome' : 'Pipoca doce',
        'ingredientes' : ['5 colheres (sopa) de óleo', '5 colheres (sopa) de açúcar', '1 colher (sopa) de chocolate em pó', '5 colheres (sopa) de milho para pipoca', '3 colheres (sopa) de água'],
        'utensílios' : ['Panela', 'Bowl', 'espátula de silicone', 'Pipoqueira'],
        'modo de preparo' : '1- Em uma panela, adicione todos os ingredientes e misture delicadamente; 2- Desligue o fogo quando o intervalo de tempo entre os estouros da pipoca diminuir; 3- Está pronta para comer.'

    },
    {

    }
]