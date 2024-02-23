# You are given a list of lists where each group represents a friendship
# for example, given the list:
# [[1,2], [2,4], [2,3]]
# 1 is friends with 2, 2 is friends with 4 and 3.
# Write a function to find how many friends each person have
#


def find_friends(ls):
    # very naive solution, use double for loops and check if each element is present in other list or not
    # there are issues with following code:
    # 1. it doesn't look back e.g. [1,3], [3,2], friends of 3 will be counted as 1 only
    # 2. multiple for loops, there is definitely a better solution
    # 3. A new data structure will probably help in resolving multiple for loops
    result = []
    for i, l in enumerate(ls):
        for j in l:
            counter = 0
            for n in ls[i + 1 :]:
                if j in n:
                    counter += 1
            result.append((j, counter))
    return result


if __name__ == "__main__":
    exampl1 = [[1, 3], [2, 3], [3, 5], [4]]
    exampl2 = [[1], [2], [3], [4]]

    examples = [exampl2, exampl1]
    for ex in examples:
        print(find_friends(ex))
