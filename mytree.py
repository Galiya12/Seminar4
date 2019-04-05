 class BSTMap :
     # ...
      # Removes the map entry associated with the given key.
      def remove( self, key ):
        assert key in self, "Invalid map key."
        self._root = self._bstRemove( self._root, key )
        self._size -= 1

        # Helper method that removes an existing item recursively.
        def _bstRemove( self, subtree, target ):
            # Search for the item in the tree.
            if subtree is None :
                return subtree
            elif target < subtree.key :
                subtree.left = self._bstRemove( subtree.left, target )
                return subtree
            elif target > subtree.key :
                subtree.right = self._bstRemove( subtree.right, target )
                return subtree
            # We found the node containing the item.
            else :
                if subtree.left is None and subtree.right is None :
                    return None
                elif subtree.left is None or subtree.right is None :
                    if subtree.left is not None :
                        return subtree.left
                    else :
                        return subtree.right
                    else
                    successor = self._bstMinimum( subtree.right )
                    subtree.key = successor.key
                    subtree.value = successor.value
                    subtree.right = self._bstRemove( subtree.right, successor.key )
                    return subtree
