def tpl_sort(*tpl):
    if not all(isinstance(num, int) for num in tpl):
        return tpl

    return tuple(sorted(tpl))


print(tpl_sort(6, 3, -1, 8, 4, 10, -5))
