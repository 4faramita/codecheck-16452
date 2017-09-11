def main(argv):
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.

  for i, v in enumerate(argv):
    # print("argv[{0}]: {1}".format(i, v))
    if v <= 1:
      print(1)
    else:
      current_index = 1
      current_str = '1'

      while current_index < v:
        current_str = look_and_say(current_str)
        current_index += 1

      print(current_str)


def look_and_say(last_str: str) -> str:
  '''return the way to say last_str'''

  num_sets = []

  current_element = last_str[0]
  last_index = 0
  current_index = 1

  while current_index < len(last_str):
    if last_str[current_index] == current_element:
      current_index += 1
    else:
      num_set = last_str[last_index:current_index]
      num_sets.append(num_set)
      current_element = last_str[current_index]
      last_index = current_index

  num_set = last_str[last_index:current_index]
  num_sets.append(num_set)

  result = ''

  for num_set in num_sets:
    result += str(len(num_set))
    result += str(num_set[0])

  return result
