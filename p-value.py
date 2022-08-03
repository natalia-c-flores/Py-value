import csv

geneset = set()
genearray = []

# opening the CSV file
with open('pathfindR_cAMNxControle.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    with open('new_pathfindR_cAMNxControle.csv', 'w', newline='') as newfile:
        newCsvFile = csv.writer(newfile)
        for row in csvFile:
            [n, gene, p_val] = row
            if gene in geneset:
                pass
            else:
                # genearray.append(row)
                newCsvFile.writerow([gene,p_val])
                geneset.add(gene)
