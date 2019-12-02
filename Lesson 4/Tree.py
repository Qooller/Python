

myTree = ['a', #root
          ['b', #left subree
           ['d', [], []],
           ['e', [], []] ],
          ['c', #right subree
           ['f', [], []],
           []]
          ]
print(myTree)
print('left subtree = ', myTree[1])
print('root = ', myTree[0])
print('right subtree = ', myTree[2])
print(myTree[1][2][0])

