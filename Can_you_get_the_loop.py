import math

def loop_size(node):
    arr_loop = []
    while node and arr_loop.index(node) < 0:
        arr_loop.append(node)
        node = node.next

    index_first = math
    return len(arr_loop) - index_first


function
loop_size(node)
{
    var loopArr = [];
while (node & & loopArr.indexOf(node) < 0) {
loopArr.push(node);
node = node.next;
}
var
firstIndex = Math.max(0, loopArr.indexOf(node));
return loopArr.length - firstIndex;
}