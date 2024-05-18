import os
def read_csv_folder(file,folder_path) -> list[list[any]]:
    values=[]
    with open(os.path.join(folder_path,file)) as f:
        for line in f:
            values.append(split(line))
    return values
def split(line: str) -> list[any]:
    """
    split memisahkan nilai-nilai dalam satu baris CSV dan mengembalikan sebagai list.
    """
    out = []
    tmp = ''
    for c in line:
        if c == ';':
            out.append(tmp)
            tmp = ''
        else:
            if c != '\n':
                tmp += c
    out.append(tmp)
    return out

def manual_join(separator: str, items: list) -> str:
    result = ""
    for i in range(len(items)):
        if i > 0:
            result += separator
        result += items[i]
    return result

def write_csv_to_folder(foldername: str, csv: str, matrix: list):
    with open(f'./data/{foldername}/{csv}.csv', 'w', encoding='utf-8') as file:
        for row in matrix:
            row_type_str = [str(var) for var in row]
            row_str = manual_join(';', row_type_str)
            if not(row==matrix[len(matrix)-1]):
                file.write(row_str + '\n')
            else:
                file.write(row_str)

def copy(array:list)->list:
    arr_copy = ['' for _ in range(len(array))]
    for i in range(len(array)):
        arr_copy[i] = array[i]
    return arr_copy