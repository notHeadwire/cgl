import tkinter as tk
import time
import random

row = 11
column = 11


# Matrix = [[1 for x in range(0, 12)] for x in range(0, 12)]
# for x in range(12):
#     Matrix[x][0] = 0
#     Matrix[0][x] = 0
#     Matrix[x][11] = 0
#     Matrix[11][x] = 0
# Matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#          [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
#          [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
#          [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
#          [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
#          [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
#          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
def createMatrix(userInputRow, userInputCol, userButton, canvas):
    userRow = int(userInputRow.get())
    userCol = int(userInputCol.get())
    userInputRow.delete(0, 'end')
    userInputCol.delete(0, 'end')
    userInputRow.pack_forget()
    userInputCol.pack_forget()
    userButton.pack_forget()

    Matrix = [[0 for x in range(userRow+2)] for y in range(userCol+2)]

    for x in range(1, userRow + 1):
        for y in range(1, userCol + 1):
            Matrix[userRow + 1][userCol + 1] = random.randint(0, 1)

    printer = PrintRect()
    printer.brrr(Matrix, canvas, userRow, userCol)
    return Matrix


Matrix = [[]]

Matrix2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


#root = tk.Tk()

#canvas = tk.Canvas(root, width=1280, height=720)
# canvas.pack()


class PrintRect:
    def brrr(self, Matrix, canvas, userRow, userCol):
        cellwidth = 10
        cellheight = 10
        creation = 0
        if creation == 0:
            for col in range(10):
                for ro in range(10):
                    x1 = col * cellwidth
                    y1 = ro * cellheight
                    x2 = x1 + cellwidth
                    y2 = y1 + cellheight
                    if Matrix[ro+1][col+1] == 1:
                        canvas.create_rectangle(
                            x1, y1, x2, y2, fill='black', width=0)
                    else:
                        canvas.create_rectangle(
                            x1, y1, x2, y2, fill='white', width=0)
            creation = 1
#rectangle(breitea, höhea, breiteb, höheb)
#canvas.create_rectangle(0, 0, 100, 100, fill='black', width=0)
#canvas.create_rectangle(100, 0, 200, 100, fill='black', width=0)


class CheckN:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def Check(self, Matrix):
        x = 0
        if Matrix[self.row - 1][self.column - 1] == 1:
            x += 1
        if Matrix[self.row - 1][self.column] == 1:
            x += 1
        if Matrix[self.row - 1][self.column + 1] == 1:
            x += 1
        if Matrix[self.row][self.column - 1] == 1:
            x += 1
        if Matrix[self.row][self.column + 1] == 1:
            x += 1
        if Matrix[self.row + 1][self.column - 1] == 1:
            x += 1
        if Matrix[self.row + 1][self.column] == 1:
            x += 1
        if Matrix[self.row + 1][self.column + 1] == 1:
            x += 1
        return x


class Run:

    def myFunc(self, Matrix):
        for i in range(1, row):
            for j in range(1, column):
                gol = CheckN(i, j)
                golSpeicher = gol.Check(Matrix)
                if Matrix[i][j] == 0:
                    if golSpeicher == 3:
                        Matrix2[i][j] = 1
                else:
                    if golSpeicher == 2:
                        Matrix2[i][j] = 1
                    elif golSpeicher == 3:
                        Matrix2[i][j] = 1
                    else:
                        Matrix2[i][j] = 0

        for k in range(row):
            for l in range(column):
                Matrix[k][l] = Matrix2[k][l]


#wait = 0
# while wait < 200000:
#    printer = PrintRect()
#    printer.brrr()
#    start = Run()
#    start.myFunc()
#    canvas.update()
#    wait += 1
#   # time.sleep(1)


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()

    userInputRow = tk.Entry(root)
    userInputRow.pack()

    userInputCol = tk.Entry(root)
    userInputCol.pack()

    #userRow = int(userInputRow.get())
    #userCol = int(userInputCol.get())
    userButton = tk.Button(root, text='create', command=lambda:
                           createMatrix(userInputRow, userInputCol, userButton, canvas))
    userButton.pack()

    printer = PrintRect()
    start = Run()
    wait = 0
    while wait < 200000:
        printer.brrr(Matrix, canvas, userInputRow, userInputCol)

        start.myFunc(Matrix)
        canvas.update()
        wait += 1

    root.mainloop()


if __name__ == '__main__':
    main()

# Matrix2 = [[1 for x in range(0, 12)] for x in range(0, 12)]
# for x in range(12):
#     Matrix2[x][0] = 0
#     Matrix2[0][x] = 0
#     Matrix2[x][11] = 0
#     Matrix2[11][x] = 0


# for x in range(12):
#     print(Matrix[x])
# print("_________________________")
# # for x in range(12):
# #     print(Matrix2[x])
# # print("_________________________")


# class CheckN:
#     def __init__(self, row, column):
#         self.row = row
#         self.column = column

#     def Check(self):
#         x = 0
#         if Matrix[self.row - 1][self.column - 1] == 1:
#             x += 1
#         if Matrix[self.row - 1][self.column] == 1:
#             x += 1
#         if Matrix[self.row - 1][self.column + 1] == 1:
#             x += 1
#         if Matrix[self.row][self.column - 1] == 1:
#             x += 1
#         if Matrix[self.row][self.column + 1] == 1:
#             x += 1
#         if Matrix[self.row + 1][self.column - 1] == 1:
#             x += 1
#         if Matrix[self.row + 1][self.column] == 1:
#             x += 1
#         if Matrix[self.row + 1][self.column + 1] == 1:
#             x += 1
#         return x


# class Run:

#     def myFunc(self):
#         for i in range(1, row):
#             for j in range(1, column):
#                 gol = CheckN(i, j)
#                 golSpeicher = gol.Check()
#                 if Matrix[i][j] == 0:
#                     if golSpeicher == 3:
#                         Matrix2[i][j] = 1
#                 else:
#                     if golSpeicher == 2:
#                         Matrix2[i][j] = 1
#                     elif golSpeicher == 3:
#                         Matrix2[i][j] = 1
#                     else:
#                         Matrix2[i][j] = 0

#         for k in range(row):
#             for l in range(column):
#                 Matrix[k][l] = Matrix2[k][l]


# aaaa = 0
# while aaaa < 20:
#     start = Run()
#     start.myFunc()
#     aaaa += 1
#     time.sleep(1)
#     for x in range(1, row):
#         print(Matrix[x])
#     print("_________________________")
# # for x in range(row):
# #     print(Matrix2[x])
