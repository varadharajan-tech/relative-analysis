import yfinance

companies = ['AAPL', 'MSFT', 'NVDA', 'AMZN',  'GOOGL', 'META', 'TSLA', 'AVGO', 'ORCL', 'AMD']
industrial_pe_ratio = 37.17

for symbol in companies:
 company = yfinance.Ticker(symbol)
 pe_ratio = company.info['trailingPE']
 if pe_ratio < industrial_pe_ratio:
  print(f'{company.info['longName']}: is recommended for investing')
 else:
  print(f'{company.info['longName']} is not recommended for investing')