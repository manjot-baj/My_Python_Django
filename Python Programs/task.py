import pandas as pd

li = []
New_Name = []
myDict = {}
val = ''
li_mob = []
write_dict = {}
New_Name_Cell = []


def Reverse(lst):
    return [ele for ele in reversed(lst)]


def write_csv():
    out_df = pd.read_csv("mob.csv", names=["Name", "Number"])
    mobile_no = out_df['Number'].values.tolist()
    for i in range(0, len(out_df['Name'])):
        if str(out_df['Name'][i]) == 'nan':
            New_Name_Cell.append(val)
            li_mob.append(mobile_no[i])
        else:
            val = out_df['Name'][i]

    write_dict = {'name': New_Name_Cell, 'mobile_no': li_mob}
    out_df = pd.DataFrame(write_dict)
    out_df.to_csv('file1.csv', index=False)


def print_output():
    out_df = pd.read_csv("mob.csv", names=["Name", "Number"])
    Name = Reverse(out_df["Name"].values.tolist())
    Number = out_df["Number"].values.tolist()
    count = 1
    for x in Name:
        if str(x) == 'nan':
            count += 1
        else:
            New_Name.append(x)
            li.append(count)
            count = 1
    count = 0
    count_c = 0
    num_list = []
    for x in li:
        for i in range(x):
            num_list.append(Number[count_c])
            count_c += 1
        new = []
        new.extend(num_list)
        myDict[New_Name[count]] = (new)
        count += 1
        num_list.clear()
    print(myDict)


if __name__ == '__main__':
    print_output()
    write_csv()
