def backtracking(list_origin,apontador, row_element, column_element, quant_linhas, quant_colunas, visitados):
        padrao = ["A","L","L","I","Z","Z","W","E","L","L"]
        result = False
        if apontador == len(padrao) -1 :
                return True
        else:
                for x in range(-1,2):
                        for y in range(-1,2):
                                if not (x==0 and y==0):
                                        if(validar(quant_linhas,quant_colunas, row_element+x, column_element+y)):
                                                if((list_origin[row_element+x][column_element+y] == padrao[apontador+1]) and  visitados[row_element+x][column_element+y]==0):
                                                        visitados[row_element+x][column_element+y] = 1
                                                        result = backtracking(list_origin, apontador+1, row_element+x, column_element+y, quant_linhas, quant_colunas,visitados)
                                                        if result:
                                                                return result
        visitados[row_element][column_element] = 0;
        return result


def validar(quant_linhas, quant_colunas, index_row, index_column):
        if (index_row>=0 and index_row < quant_linhas and index_column >= 0 and index_column < quant_colunas):
                return True
        return False

def main():
        entrada = int(raw_input())
        for i in range(entrada):
                linha, coluna = map(int, raw_input().split(" "))
                lista = []
                result = 'no'
                visitados = linha*[coluna*[0]]

                for j in range(linha):
                        lista.append(raw_input())

                for l in range(0, linha):
                        for c in range (0, coluna):
                                if(lista[l][c] == 'A' and backtracking(lista, 0, l, c, linha, coluna, visitados )):
                                        result = 'yes'
                                        break
                        if (result == 'yes'):
                                break
                print result
if __name__ == '__main__':
        main()