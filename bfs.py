
#! Функция обхода графа в ширину
def bfs(v):
    visited[v] = True
    stack = list_of_adjacency[v]

    # Пока что-то есть в стеке
    while stack:
        s = stack.pop(0)  # Извлекаем вершину
        if not visited[s]:
            print(s)
            visited[s] = True

            # Добавляем непосещенные вершины
            for w in list_of_adjacency[s]:
                if not visited[w]:
                    stack.append(w)

choice = 'y'
while choice.lower() == 'y':
    try:
        #! Определяем кол-во вершин графа
        print('Введите кол-во вершин:')
        number = int(input())
        list_of_adjacency = list()

        #! Определяем смежность вершин графа
        for n in range(number):
            print('Введите через "," список смежности для вершины', n)
            string = input()
            list_from_string = string.split(',')
            
            # Преобразуем список для вершины n в тип int с обработкой исключений
            for m in range(len(list_from_string)):
                try:
                    list_from_string[m] = int(list_from_string[m].strip())
                except:
                    list_from_string[m] = 0
            list_of_adjacency.append(list_from_string)

        visited = [False for i in range(len(list_of_adjacency))]

        #! Вызываем целевую функцию
        print('Обход графа в глубину:')
        for c in range(len(list_of_adjacency)):
            if not visited[c]:
                print(c)
                bfs(c)
        print('Попробуем ещё раз? (введите "y" для согласия)')
        choice = input()

    except:
        print('Что-то пошло не так, попробуем ещё раз? (введите "y" для согласия)')
        choice = input()
