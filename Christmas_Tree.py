# https://www.codewars.com/kata/52755006cc238fcae70000ed/train/python

def christmas_tree(height):
    tree = ''
    tree_list=[' '] * (2 * (height - 1) + 1)
    index_left, index_right = height - 1, height - 1
    for x in range(0, height):
        tree_list[index_left] = '*'
        tree_list[index_right] = '*'
        index_left -= 1
        index_right += 1
        tree += "".join(tree_list)
        if x < height - 1:
            tree += '\n'
    return tree


def christmas_tree_2(height: int) -> str:
    return '\n'.join(('*' * i).center(2 * height - 1) for i in range(1, height * 2, 2))

def christmas_tree_3(h):
    return '\n'.join(f'{"*" * i:^{2*h - 1}}' for i in range(1, 2*h, 2))

print(christmas_tree(0))#, '')
print(christmas_tree(1))#, '*')
print(christmas_tree(2))#, ' * \n***')
print(christmas_tree(3))#, '  *  \n *** \n*****')
print(christmas_tree(4))#, '   *   \n  ***  \n ***** \n*******')
print(christmas_tree(5))#, '    *    \n   ***   \n  *****  \n ******* \n*********')
print(christmas_tree(6))#, '     *     \n    ***    \n   *****   \n  *******  \n ********* \n***********')
print(christmas_tree(7))#, '      *      \n     ***     \n    *****    \n   *******   \n  *********  \n *********** \n*************')
print(christmas_tree(8))#, '       *       \n      ***      \n     *****     \n    *******    \n   *********   \n  ***********  \n ************* \n***************')
print(christmas_tree(9))#, '        *        \n       ***       \n      *****      \n     *******     \n    *********    \n   ***********   \n  *************  \n *************** \n*****************')
print(christmas_tree(10))#, '         *         \n        ***        \n       *****       \n      *******      \n     *********     \n    ***********    \n   *************   \n  ***************  \n ***************** \n*******************')