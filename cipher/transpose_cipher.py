import numpy as np

def transpose_cipher(rows, cols, cipher_text):
    matrix = []
    message = ""
    for row in range(rows):
        row_msg = cipher_text[row*cols: (row+1)*cols]
        # print(row_msg)
        matrix.append(list(row_msg))
    t_matrix = np.array(matrix).T
    for t_row in range(cols):
        message += ("".join(t_matrix[t_row]))

    return message


cipher_text = "Mnpa rse Rreho rTipnst en  o tpai  aSo  nsihre u ccswwdcohltlAnAvmsgetesrtbtotwiiergighiEd iutecy tsomhr elnryrcomkS pdcrru.f o ierarl."
print(transpose_cipher(5, 27, cipher_text))