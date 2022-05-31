import tkinter as tk
import time
import random
global creation
global Matrix
global MatrixSave
global userRow
global userCol
creation = 0

def createMatrix(userInputRow, userInputCol, userButton, canvas):
    # if userInputRow.get() != '':
    global userRow
    global userCol
    userRow = int(userInputRow.get())
    userCol = int(userInputCol.get())
    userInputRow.delete(0, 'end')
    userInputCol.delete(0, 'end')
    userInputRow.pack_forget()
    userInputCol.pack_forget()
    userButton.pack_forget()

#    Matrix = [[0]*(userCol+2) for i in range(userRow+2)]
    Matrix = [[0 for x in range(userRow+2)] for y in range(userCol+2)]

#    for x in range(userRow+2):
#        for y in range(userCol+2):
#            print(Matrix[x][y])
#    print('______________________________________________')
    brrr(Matrix, canvas, userRow, userCol)


def brrr(Matrix, canvas, userRow, userCol):
    cellwidth = 10
    cellheight = 10
    global creation
    global MatrixSave
#    creation = 0
    timer = 0
    while timer < 10000:
        if creation == 0:
            for ro in range(userCol):
                for col in range(userRow):
                    x1 = col * cellwidth
                    y1 = ro * cellheight
                    x2 = x1 + cellwidth
                    y2 = y1 + cellheight

                    Matrix[ro+1][col+1] = random.randint(0, 1)

                    if Matrix[ro+1][col+1] == 1:
                      #  Matrix[ro+1][col+1] = canvas.create_rectangle(
                        canvas.create_rectangle(
                            x1, y1, x2, y2, fill='black', width=1)

                    else:
                       # Matrix[ro+1][col+1] = canvas.create_rectangle(
                        canvas.create_rectangle(
                            x1, y1, x2, y2, fill='white', width=1)

                    MatrixSave = Matrix
                    
                    creation = 1
            canvas.update()

        else:
            start = Run()
            start.myFunc(Matrix)
            # Hier die Prüfung auf Nachbarn -> Spielbeginn
            for ro in range(userCol):
                for col in range(userRow):
                    x1 = col * cellwidth
                    y1 = ro * cellheight
                    x2 = x1 + cellwidth
                    y2 = y1 + cellheight

                        

                    # jedes canvas rectangle hat eine id, diese wird hier den einzelnen elementen der matrix hinzugefügt
                    if Matrix[ro+1][col+1] == 1:
                        
                        canvas.create_rectangle(
                            x1, y1, x2, y2, fill='black', width=1)
                    else:
                        canvas.create_rectangle(
                            x1, y1, x2, y2, fill='white', width=1)
            canvas.update()
            timer += 1

#                print(Matrix[ro+1][col+1])

        

#    for x in range(userRow+2):
#        print(Matrix[x])
#    print('______________________________________________')
#    print(canvas.find_all())




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
        
        for i in range(1, userRow):
            for j in range(1, userCol):
                gol = CheckN(i, j)
                golSpeicher = gol.Check(Matrix)
                if Matrix[i][j] == 0:
                    if golSpeicher == 3:
                        MatrixSave[i][j] = 1
                else:
                    if golSpeicher == 2:
                        MatrixSave[i][j] = 1
                    elif golSpeicher == 3:
                        MatrixSave[i][j] = 1
                    else:
                        MatrixSave[i][j] = 0

        for k in range(userRow):
            for l in range(userCol):
                Matrix[k][l] = MatrixSave[k][l]


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()

    userInputRow = tk.Entry(root)
    userInputRow.pack()

    userInputCol = tk.Entry(root)
    userInputCol.pack()
    userButton = tk.Button(root, text='create', command=lambda: createMatrix(
        userInputRow, userInputCol, userButton, canvas))
    userButton.pack()
    #print(canvas.find_all())

    #labelRow = tk.Label(root, text='rows')
    #labelCol = tk.Label(root, text='columns')

    # Matrix[1][1] = canvas.create_rectangle(0, 0, 101, 101, fill='black', width=0)

    # canvas.itemconfig(Matrix[1][1], fill='white')

    root.mainloop()


if __name__ == '__main__':
    main()
