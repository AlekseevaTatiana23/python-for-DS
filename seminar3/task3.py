#Напишите программу для печати всех уникальных
#значений в словаре.
#Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
#":" S007 "}]
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
          {" VIII": "S007"}]

set_1 = set()

for element in list_1:
    for i in element:
        set_1.add(element[i])
print(set_1)

