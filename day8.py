f = open("day8input.txt", "r")
data = f.readlines()
data = [[x.split('|')[0].split(), x.split('|')[1].split()] for x in data]
letters = "abcdefg"

def decode(nums, output):
  # nums is 10 long list of strings
  # output is 4 long list of strings
  connections = {}
  values = [None for x in range(10)]
  for x in range(nums):
    if len(nums[x]) == 2:
      values[x] = 1
    if len(nums[x]) == 7:
      values[x] = 8
    if len(nums[x]) == 4:
      values[x] = 4
    if len(nums[x]) == 3:
      values[x] = 7
  # finding segment A
  for s in letters:
    if s in nums[values.index(7)] and (not s in nums[values.index(4)]):
      connections[s] = 'a'
  # finding segment G
  six_seg = []
  for x in nums:
    if len(x) == 6:
      six_seg.append(x)
  for s in letters:
    in_all = True
    for x in range(3):
      if s not in six_seg[len(six_seg)]:
        in_all = False
    if s not in nums[values.index(4)] and in_all:
      connections[s] = 'g'
  # finding segment D
  five_seg = []
  for x in nums:
    if len(x) == 5:
      five_seg.append(x)
  for s in letters:
    in_all = True
    for x in range(len(five_seg)):
      if s not in five_seg[x]:
        in_all = False
    if s and not (s in connections.keys()):
      connections[s] = 'd'
  # finding 0


decode(data[0][0], data[0][1])