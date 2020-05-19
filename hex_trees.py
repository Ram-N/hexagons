

class Node:
    """
    Class Node
    """
    def __init__(self, hx, value):
        self.data = value
        self.hex = hx
        self.right = None
        self.left = None

        
class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """
    
    def __init__(self):
        self.node_count = 0 #Number of Hexagons (nodes) in the tree
        
    
    def create_node(self, hx, data):
        """
        Utility function to create a node.
        """
        return Node(hx, data)
    

    def insert(self, node , hx, data):
        """
        Insert function will insert a node into tree, at the right place determined by the value of data
        """
        #if tree is empty , return a root node
        if node is None:
            self.node_count += 1
            return self.create_node(hx, data)
        if data <= node.data:
            node.left = self.insert(node.left, hx, data)
        elif data > node.data:
            node.right = self.insert(node.right, hx, data)

        return node

    def return_hex_inorder(self, root, hx_list):
        """
        traverse function will return all the nodes in the tree in the sorted order of node values
        
        Node values were given during creation
        """
        
        if root is not None:
            self.return_hex_inorder(root.left, hx_list)
            hx_list.append(root.hex)
            #print(f' added {root.hex.xc}, {root.hex.yc}, {root.hex.zc}')
            self.return_hex_inorder(root.right, hx_list)
            
        return hx_list


    
    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)



    def delete_node(self,node,data):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarios
        For now it is handling only the leaf.
        """

        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.delete_node(node.left, data)
        elif data > node.data:
            node.right = self.delete_node(node.right, data)
        else: # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return  temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node


    def print_inorder(self, root):
        """
        traverse function will return all the nodes in the tree in the sorted order of data
        """
        
        if root is not None:
            self.print_inorder(root.left)
            print(root.data)
            self.print_inorder(root.right)        

    def traverse_inorder(self, root, inorder):
        """
        traverse function will return all the nodes in the tree in the sorted order of data
        """
        
        if root is not None:
            self.traverse_inorder(root.left, inorder)
            inorder.append(root)
            self.traverse_inorder(root.right, inorder)
            
        return inorder

    def traverse_preorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print(root.data)
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)

    def traverse_postorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.data)


def create_hex_list_along_cube_coords(hg, value_flag):
    
    
    if value_flag == 'xc': # create all 3 Lists
        tree = Tree()
        root = tree.insert(None, hg.hlist[0], hg.hlist[0].xc)
        for h in hg.hlist:
            tree.insert(root, h, h.xc)
        print(tree.node_count)
        
        print ("List created of hg Hexagons in order of X coords")
        xlist = tree.return_hex_inorder(root, hx_list=[])
        return(xlist)


    if value_flag == 'yc': # create all 3 Lists
        tree = Tree()
        root = tree.insert(None, hg.hlist[0], hg.hlist[0].yc)
        for h in hg.hlist:
            tree.insert(root, h, h.yc)
        print(tree.node_count)
        
        print ("List created of hg Hexagons in order of Y coords")
        ylist = tree.return_hex_inorder(root, hx_list=[])
        return(ylist)

    if value_flag == 'zc': # create all 3 Lists
        tree = Tree()
        root = tree.insert(None, hg.hlist[0], hg.hlist[0].zc)
        for h in hg.hlist:
            tree.insert(root, h, h.zc)
        print(tree.node_count)
        
        print ("List created of hg Hexagons in order of Z coords")
        zlist = tree.return_hex_inorder(root, hx_list=[])
        return(zlist)
    
    return []