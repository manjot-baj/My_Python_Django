from csv import reader

with open("mob.csv", "r") as f:
    with open("mob_new.csv", "w") as csv_write:
        dic = {}
        csv_reader = reader(f)
        next(csv_reader)
        for row in csv_reader:
            if row[0]:
                Key = row[0]
                temp = []
                temp.append(row[1])
            else:
                csv_write.write(f"{Key},{row[1]}\n")
                temp.append(row[1])
            dic.update({Key: temp})
        print(dic)
