print('     *\n')
print('    ***\n')
print('   *****\n')
print('  *******\n')
print(' *********\n')

treeLevel = '*'
spaceString = '     '
levelLength = 0
print(spaceString+treeLevel)
while levelLength <= 10:
    spaceString = spaceString[:-1]
    treeLevel+='**'
    print(spaceString+treeLevel)
    levelLength = len(treeLevel)+len(spaceString)