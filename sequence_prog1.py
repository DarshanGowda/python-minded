import copy
import random

sample_list = [random.randrange(0, 100) for item in range(100)]

sample_list = sorted(sample_list)

seq_list = []
temp_dict = {}
cur_item = ''
next_item = ''

for index in range(len(sample_list)):
    if len(sample_list) > 1:  # to check if length of list is more than 1
        if index == 0:  # first item
            cur_item = sample_list[index]
            next_item = sample_list[index+1]
            if cur_item - next_item == -1:
                temp_dict[cur_item] = sample_list.count(cur_item)
                temp_dict[next_item] = sample_list.count(next_item)
            else:
                seq_list.append(cur_item)
        else:
            cur_item = next_item
            try:
                next_item = sample_list[index+1]
            except IndexError:  # last item in list
                if temp_dict:
                    seq_list.append(copy.deepcopy(temp_dict))
                    temp_dict.clear()
                else:
                    seq_list.append(cur_item)
                continue
            if cur_item - next_item == -1:
                temp_dict[cur_item] = sample_list.count(cur_item)
                temp_dict[next_item] = sample_list.count(next_item)
            else:
                if temp_dict:
                    seq_list.append(copy.deepcopy(temp_dict))
                    temp_dict.clear()
                else:
                    seq_list.append(cur_item)

for item in seq_list:
    if isinstance(item, dict):
        keys_list = item.keys()
        print str(keys_list[0])+'-'+str(keys_list[-1])+'('+str(sum(item.values()))+')'
    else:
        print str(item)
