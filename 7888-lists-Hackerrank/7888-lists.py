if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        # Read the command string and split it into components
        parts = input().split()
        command = parts[0]
        
        if command == "insert":
            my_list.insert(int(parts[1]), int(parts[2]))
        elif command == "print":
            print(my_list)
        elif command == "remove":
            my_list.remove(int(parts[1]))
        elif command == "append":
            my_list.append(int(parts[1]))
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna