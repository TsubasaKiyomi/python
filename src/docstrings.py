def example_func(param1, param2):
# 1行目にファンクションの中身がどういった意味か入れてある。
    """Exampl function with types documented in the docstring.
#Args(argument:引数）は param1/param2(パラメーター１・２)がどういった物なのか表す。
    Args: 
        param1 (int): The first parameter.
        param2 (str): The second parameter.
# このfunction（関数）が返すのは Returnsのbool型なのでTrueかFalseが返ってくる。
    Returns:
        bool: The return value. True for succes, False otherwise.
    
    """
    print(param1)
    print(param2)
    return True
# 「.」ドットを使うとメソッドが出る。　__doc__で書いたdocumentがprintされる
# print(example_func.__doc__)
# help関数でもdocumentがprintされる
help(example_func)