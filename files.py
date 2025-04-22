
import os

with open('input.txt', 'r') as input:
    content = input.read()

    words=content.split()
    print()
    print(f'this file has ', len(words)," words")
    print()
    
    content_upper =content.upper()

    #print(content_upper)

    with open('output.txt', 'w') as output:
        output.write(content_upper)

    if os.path.exists('output.txt'):
        print('The file \'output.txt\' was created successfully')
        print()
