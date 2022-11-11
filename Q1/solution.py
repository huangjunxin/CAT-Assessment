def fun():
    number_t_shirts_in_shop = int(input())
    representation_t_shirts_in_shop = input().split(' ')
    number_requests = int(input())
    representation_requests = input().split(' ')

    if number_requests > number_t_shirts_in_shop:
        return 'No'

    # Generate a size dict
    size_dict = {
        'M': 0
    }
    # for XXXX...XXXS
    for i in range(1001):
        size_dict['X' * i + 'S'] = -i - 1
    # for XXXX...XXXL
    for i in range(1001):
        size_dict['X' * i + 'L'] = i + 1

    sized_t_shirts_in_shop = []
    for req_i in range(len(representation_t_shirts_in_shop)):
        sized_t_shirts_in_shop.append(size_dict[representation_t_shirts_in_shop[req_i]])
    sized_t_shirts_in_shop.sort()
    # print(sized_t_shirts_in_shop)
    sized_requests = []
    for req_i in range(len(representation_requests)):
        sized_requests.append(size_dict[representation_requests[req_i]])
    sized_requests.sort()
    # print(sized_requests)
    for solution_i in range(0, number_t_shirts_in_shop - number_requests + 1):
        check_list = sized_t_shirts_in_shop[solution_i : number_requests + solution_i]
        # print('check_list', check_list)
        count_correct = 0
        for size_i in range(len(check_list)):
            if check_list[size_i] >= sized_requests[size_i]:
                # print(check_list[size_i], '>=', sized_requests[size_i])
                count_correct += 1
            else:
                # print(check_list[size_i], '<', sized_requests[size_i])
                # print('Current check_list: No')
                break
        if count_correct == number_requests:
            return 'Yes'
    return 'No'


print(fun())
