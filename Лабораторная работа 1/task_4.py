users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

logs = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

logs['Общее количество'] = len(users)
logs['Уникальные посещения'] = len(set(users))

print(logs)
