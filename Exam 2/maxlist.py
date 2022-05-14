def main():
    list = [23,54,12,34,65] #Should return 65
    print(maximum(list))
def maximum(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], maximum(list[1:]))
main()