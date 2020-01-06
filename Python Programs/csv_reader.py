from csv import reader
with open("file.csv","r") as file_csv:
    with open("file1.csv","w") as w_csv:
        csv_reader = reader(file_csv)
        next(csv_reader)
        for k,v in dict(csv_reader).items():
            w_csv.write(f"{k} : {list(v)}\n")