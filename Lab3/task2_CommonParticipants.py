# TODO Напишите функцию find_common_participants
def find_common_participants(group_one, group_two, space=','):
	seperated_group_one = set(group_one.split(space))
	seperated_group_two = set(group_two.split(space))
	common_participants = seperated_group_one & seperated_group_two
	return sorted(common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
