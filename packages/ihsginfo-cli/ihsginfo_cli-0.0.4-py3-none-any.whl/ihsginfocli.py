import click
import yfinance as yf

FIELDS = {
  'longName': 'Company',
  'currentPrice': 'Current Price',
  'bookValue': 'Book Value',
  'returnOnEquity': 'ROE (annualized)',
  'priceToBook': 'PBV',
  'trailingPE': 'PER (ttm)'
}

@click.group()
def cli():
  '''
  IHSG Key Stats
  '''
  pass

@click.group(name='get')
def get_group():
  '''
  Group of commands to get something
  '''
  pass

@click.command(name='price')
@click.argument('stock')
def get_stock_price(stock):
  '''
  Get the stock price
  '''
  tick = yf.Ticker(stock.upper() + '.JK')
  if not tick.info: return
  click.secho(stock.upper(), bold=True, bg='yellow')
  click.echo(FIELDS['currentPrice'] + ': ', nl=False)
  click.secho(tick.info['currentPrice'], fg='green')

@click.command(name='info')
@click.option('--resource', '-r', help="Resource data (default is 'yahoo')", default='yahoo')
@click.argument('stock')
def get_stock_info(stock, resource):
  '''
  Get the stock info
  '''
  if resource == 'yahoo':
    tick = yf.Ticker(stock.upper() + '.JK')
    if not tick.info: return
  elif resource == 'manual':
    click.echo('Data is not found!')
    return
  else:
    click.echo('Wrong resource parameters')
    return

  result = {}
  for fk in (FIELDS.keys()):
    if fk == 'returnOnEquity':
      result[fk] = f'{str(round(tick.info[fk]*100, 2))}%'
    elif fk == 'priceToBook':
      result[fk] = f'{str(round(tick.info[fk], 2))}x'
    else:
      result[fk] = tick.info[fk] if type(tick.info[fk]) is str else round(tick.info[fk], 2)

  click.secho(stock.upper(), bold=True)
  for i in result.keys():
    click.echo(FIELDS[i] + ': ', nl=False)
    click.secho(f'{result[i]}', fg='green')

# @click.command()


get_group.add_command(get_stock_price)
get_group.add_command(get_stock_info)

cli.add_command(get_group)

if __name__ == '__main__':
  cli()