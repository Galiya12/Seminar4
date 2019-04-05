class Tree23Map :
    # ...
    def _23Insert( self, key, newitem ):
        # If the tree is empty, a node has to be created for the first key.
        if self._root is None :
            self._root = _23TreeNode( key, newitem )

        # Otherwise, find the correct leaf and insert the key.
        else :
            (pKey, pData, pRef) = _23Insert( self._root, key, newitem )

        # See if the node was split.
            if pKey is not None :
                newRoot = _23TreeNode( pKey, pData )
                newRoot.left = self._root
                newRoot.middle = pRef
                self._root = newRoot

        # Recursive function to insert a new key into the tree.
    def _23RecInsert( subtree, key, newitem ):
        # Make sure the key is not already in the tree.
        if subtree.hasKey( key ) :
            return (None, None, None)
        # Is this a leaf node?
        elif subtree.isALeaf() :
            return _23AddToNode( subtree, key, newitem, None )

        # Otherwise, it's an interior node.
        else :
        # Which branch do we take?
        branch = subtree.getBranch( key )
        (pKey, pData, pRef) = _23Insert( branch, key, newitem )
        # If the child was split, the promoted key and reference have to be
        # added to the interior node.
        if pKey is None :
            return (None, None, None)
        else :
            return _23AddToNode( subtree, pKey, pData, pRef )
