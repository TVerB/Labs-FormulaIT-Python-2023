def find_common_participants(group_1, group_2, sep=','):
    common_participants = list(set(group_1.split(sep)).intersection(group_2.split(sep)))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
