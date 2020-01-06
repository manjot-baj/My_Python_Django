# modify
from csv import DictReader,DictWriter
with open("file.csv","r") as file_csv:
    with open("file3.csv","w") as w_csv:
        csv_reader = DictReader(file_csv)
        # for i in csv_DictReader:
        #     print(i)
        csv_writer = DictWriter(w_csv,fieldnames=["name","phone1","phone2"])
        # csv_writer.writeheader()
        for row in csv_reader:
            Name,Phone,Phone2 = row["name"],row["phone1"],row["phone2"]
            csv_writer.writerow({
                "name" :f"{Name} : ",
                "phone1" :list(Phone),
                "phone2" :list(Phone2)
            })
        