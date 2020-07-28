def test(*args):
    table_arg = []
    for arg in args:
        table_arg += [arg]
    return table_arg

if __name__ == '__main__':
    table = test('slowo','jest','w','tabeli')
    print(table)