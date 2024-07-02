class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return

        result = [[]]
        sub_tree_index = 0
        
        def BFS(node):
            if not node:
                return
        
            if node.val in to_delete:
                if node.left:
                    sub_tree_index += 1
                    result.append([])
                    result[sub_tree_index].append(node.left)
                if node.right:
                    sub_tree_index +=1
                    result.append([])
                    result[sub_tree_index].append(node.right)

            else:
                result[sub_tree_index].append(node.val)

            BFS(node.left)
            BFS(node.right)

        BFS(root)
        
        return result