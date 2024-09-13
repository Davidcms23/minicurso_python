## 1° Defina uma função chamada calcular_preco_final() que receba os seguintes argumentos

def calcular_preco_final(valor_total, percentual_desconto, codigo_desconto=None):
  preco_com_desconto = valor_total - (valor_total*percentual_desconto/100)

  if codigo_desconto == "TOP10":
    preco_com_desconto -= (preco_com_desconto*10/100)

  return preco_com_desconto

## 2° Retorne o preço final da compra após aplicar o desconto. Se o código de desconto for informado, aplique um desconto adicional de 10% sobre o valor já com desconto.

calcular_preco_final(200, 10, "TOP10")
