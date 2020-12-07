class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend, divider = float(input('введите делимое: ')), float(input('введите делитель: '))
    if divider == 0:
        raise ZeroDiv('деление на ноль')
    print(f'{dividend / divider:.3f}')
except (ValueError, ZeroDiv) as arr:
    print(arr)
