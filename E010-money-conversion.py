# Convert Reais to Dollars

brl = float(input('How many Reais (R$) do you have? '))
usd = float(input('What is the dollar rate? '))
print('You can buy {:.2f} dollars with the Reais you have in your wallet.'.format(brl/usd))