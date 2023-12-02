input = open('inputDay2.txt', 'r').read().split('\n')
limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def createDataStructure(data):
  structure = []

  for item in data:

    color_list = []
    scores = item.strip().split(';')

    for score in scores:

      score = score.split(',')

      for groups in score:
        parts = groups.split()
        color = parts[-1]
        number = int(parts[-2])
        color_list.append([color, number])

    structure.append(color_list)
  return structure


def sumId(list):
  idList = []

  for id, items in enumerate(list):
    
    if cubeLimit(items):
      idList.append((id + 1))

  return print('the sum is', sum(idList))


def cubeLimit(list):

  for item in list:
    if item[1] > limits[item[0]]:
      return False
    
  return True


sumId(createDataStructure(input))
