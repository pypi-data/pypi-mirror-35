class Test():
  def __init__(self, zahl1, zahl2):
    print('Die Zahlen {} und {} wurden eingegeben.'.format(zahl1, zahl2))
    if zahl1 < zahl2:
      print('Eine Subtraktion ergibt ein negatives Ergebnis.')
    if zahl2 == 0:
      print('Eine Division kann nicht durchgeführt werden.')
      
  def Subtraktion(zahl1, zahl2):
    print('{} - {} = {}'.format(zahl1, zahl2, zahl1-zahl2))