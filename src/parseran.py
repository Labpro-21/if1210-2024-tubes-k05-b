def read_csv(filename: str) -> list[list[any]]:
    """mengubah value dari satu csv file menjadi array-array yang terpisah"""
    values= []
    with open ("./data/" + filename, 'r') as file:
        for line in file:
            values.append(split(line))
    #mengembalikan list semua value
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

def matrix_to_csv(matrix):
    csv_string = ""
    for row in matrix:
        row_string = ";".join(str(element) for element in row)
        csv_string += row_string + "\n"
    return csv_string

def write_csv(filename, csv_data):
    with open(filename, 'w') as file:
        file.write(csv_data)

def convert_datas_to_string(data):
    # Mengubah data kembali menjadi string sesuai format agar dapat di-write ke dalam file csv
    # I.S. data terdefinisi
    # F.S. Dikembalikan string sesuai format
    
    # KAMUS LOKAL
    # data_string : string
    # arr_data : any of user or data_game or riwayat or kepemilikan
    # arr_data_all_string : array of string
    
    # ALGORITMA
    data_string = ""
    for arr_data in data:
        arr_data_all_string = [str(var) for var in arr_data]
        data_string += ";".join(arr_data_all_string)
        data_string += "\n"
    return data_string

def save_data(file:str,data:str):
    # Menulis data ke dalam csv
    # I.S. data terdefinisi
    # F.S. memperbarui file yang telah ada dan membuat file csv baru jika belum
    
    # KAMUS LOKAL
    # data : string
    # f : SEQFILES OF
    #       (*) array of string
    #       (1) mark : None
    
    # ALGORITMA
    data = convert_datas_to_string(data)
    f = open("./data/" + file, "w") 
    f.write(data)
    f.close()