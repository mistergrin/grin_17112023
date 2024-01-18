with open("airport-codes_csv.csv", mode='r',  encoding='utf-8') as file:
    file_content = file.read().strip()
    file_splited = file_content.split('\n')
    for line in file_splited:
        if line.split(';')[5] == 'UA':
            print(line.split(';')[2])
