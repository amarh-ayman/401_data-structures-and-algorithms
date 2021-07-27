# from hashmap_tree_intersection.BinarySearchTree import BinarySearchTree


def treeIntersection(tree1,tree2):
        def __interSection(nodeT2,treeArray=[]):
            if not nodeT2:
                return []
    
            tree1.contain(nodeT2.value) and treeArray.append(nodeT2.value)
           
            __interSection(nodeT2.left ,treeArray)
            __interSection(nodeT2.right,treeArray)
            return treeArray
        return __interSection(tree2.root,[])


# tree1 = BinarySearchTree()
# tree1.Add(23)
# tree1.Add(8)
# tree1.Add(42)
# tree1.Add(4)
# tree1.Add(16)
# tree1.Add(27)


# tree2 = BinarySearchTree()
# tree2.Add(100)
# tree2.Add(8)
# tree2.Add(42)
# tree2.Add(7)
# tree2.Add(16)
# tree2.Add(9)

# print(treeIntersection(tree1,tree2))
