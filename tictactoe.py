turn = 0
win = False
row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]
pos = 0
while win == False:

                if turn == 0:
                    print("x")
                if turn == 1:
                    print("o")
                pos = int(input("geef positie"))

                if pos > 0 & pos < 10:
                    if pos < 4:
                        if turn == 0:
                            if row1[pos - 1] == "":
                                row1[pos - 1] = "X"
                                turn = 1

                            else:
                                print("kies een nieuwe positie")
                                turn = 0
                        else:
                            if row1[pos - 1] == "":
                                row1[pos - 1] = "O"
                                turn = 0

                            else:
                                print("kies een nieuwe positie")
                                turn = 1

                    elif pos < 7:
                        if turn == 0:
                            if row2[pos - 4] == "":
                                row2[pos - 4] = "X"
                                turn = 1

                            else:
                                print("kies een nieuwe positie")
                                turn = 0
                        else:
                            if row2[pos - 4] == "":
                                row2[pos - 4] = "O"
                                turn = 0

                            else:
                                print("kies een nieuwe positie")
                                turn = 1
                    else:
                        if turn == 0:
                            if row3[pos - 7] == "":
                                row3[pos - 7] = "X"
                                turn = 1

                            else:
                                print("kies een nieuwe positie")
                                turn = 0
                        else:
                            if row3[pos - 7] == "":
                                row3[pos - 7] = "O"
                                turn = 0

                            else:
                                print("kies een nieuwe positie")
                                turn = 1
                print(row1)
                print(row2)
                print(row3)
                if(row1[1]== "X" and row2[2]=="X" and row3[2]=="X"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[1] == "O" and row2[2] == "O" and row3[2] == "0"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[0] == "X" and row2[0] == "X" and row3[0] == "X"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[0] == "O" and row2[0] == "O" and row3[0] == "0"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[1] == "X" and row2[1] == "X" and row3[1] == "X"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[0] == "O" and row2[0] == "O" and row3[1] == "0"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[0] == "X" and row1[1] == "X" and row1[2] == "X"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[0] == "O" and row1[1] == "O" and row1[2] == "0"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[0] == "X" and row1[1] == "X" and row1[2] == "X"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row2[0] == "O" and row2[1] == "O" and row2[2] == "0"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[0] == "X" and row1[1] == "X" and row1[2] == "X"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row3[0] == "O" and row3[1] == "O" and row3[2] == "0"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[0] == "X" and row2[1] == "X" and row3[2] == "X"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break
                if (row1[0] == "O" and row2[1] == "O" and row3[2] == "0"):
                    if turn == 1:
                        print("X wint")
                    else:
                        print("O wint")
                    break



