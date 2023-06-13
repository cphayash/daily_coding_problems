from typing import Any, List, Optional, Type, Union
"""
This problem was asked by Google.

Given the sequence of keys visited by a postorder traversal of a binary search
tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the
following tree:

    5
   / \
  3   7
 / \   \
2   4   8
"""

class Node(object):
    def __init__(
            self,
            value: int,
            left: Optional[Union[int, "Node"]] = None,
            right: Optional[Union[int, "Node"]] = None,
    ) -> Any:
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __int__(self) -> int:
        return self.value
    
    def addChild(self, child: Union[int, "Node"]) -> None:
        if isinstance(child, int):
            child = Node(child)

        if int(child) >= int(self):
            if self.right:
                self.right.addChild(child)
            else:
                self.right = child
        elif int(child) < int(self):
            if self.left:
                self.left.addChild(child)
            else:
                self.left = child

    def printType(self: "Node") -> None:
        print(type(self))
            


def PrintTree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
    levels=[]

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.left,level+1,x-seg,'l'))
            q.append((node.right,level+1,x+seg,'r'))
    
    for i,l in enumerate(levels):
        pre=0
        preline=0
        linestr=''
        pstr=''
        seg= width//(pow(2,i+1))
        for n in l:
            valstr= str(n[0].value)
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
               linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
               preline = n[2] + seg + seg//2
            pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the position according to the number size
            pre = n[2]
        print(linestr)
        print(pstr)



def reconstructTree(array: List[int]) -> Node:
    array = array[::-1]
    head = None
    for value in array:
        node = Node(value)
        if head:
            head.addChild(node)
        else:
            head = node
    return head


testCases = [
    [2, 4, 3, 8, 7, 5],
]

for testCase in testCases:
    head = reconstructTree(testCase)
    PrintTree(head)