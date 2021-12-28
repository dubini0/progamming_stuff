def num_hansu(n):
    if n < 100:
        return n
    else:
        result = 99
        for i in range(100, n+1):
            if (int(str(i)[2]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[0])):
                result += 1
        return result



if __name__ == "__main__":
    n = int(input())
    print(num_hansu(n))
