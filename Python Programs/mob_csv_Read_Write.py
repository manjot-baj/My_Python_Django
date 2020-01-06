# Expected output:
# {'test':[123456, 8965332], 'test2':[45, 5656, 5652632], 'test3':[9625,2131321]}

# code for above output
from csv import reader

with open("mob.csv", "r") as f:
    with open("mob_new.csv", "w") as csv_write:
        dic = {}
        csv_reader = reader(f)
        next(csv_reader)
        for row in csv_reader:
            value = row[1]
            if row[0]:
                Key = row[0]
                temp = []
            if value.isdigit():
                try:
                    temp.append(int(row[1]))
                    dic.update({Key: temp})
                    # else:
                    #     temp.append(int(row[1]))
                    #     dic.update({Key:temp})
                except:
                    pass
            else:
                csv_write.write(f"{Key},{row[1]}\n")
        print(dic)
