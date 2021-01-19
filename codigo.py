def calcular_media(notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  print('O aluno tirou', media)
  verificar_aprovacao(media)

def verificar_aprovacao(media):
    if media >= 6:
      print('Aluno Aprovado !')
    else:
      print('Aluno Reprovado !')

calcular_media = [9, 5, 8, 6]