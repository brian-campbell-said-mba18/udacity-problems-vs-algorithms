# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    '''
    REFERENCES: This comes from References 1 & 2 of References at
    the bottom of the python file.
    '''
    def __init__(self, handler = None, current_pathparcel = '/'):
        '''
        Class Purpose: The purpose of this class is to provide the node
            structure for the RouteTrie class.
            
        Init Variables:
            self.handler = This is the hanlder for an HTTP route. It is
                None by default.
            self.current_path_parcel = This is the current part of path. A
                full path is something like "/home/about". The 
                current_path_parcel is one of the following places in
                the full path: "/", "home", or "about".
            self.children = This is a dictionary repository of all the
                children nodes of this node.
        '''
        self.handler = handler
        self.children = {}
        self.current_pathparcel = current_pathparcel
    
    def get_handler(self):
        '''This returns the handler of the node.'''
        return self.handler
    
    def set_handler(self, handler):
        '''This sets the handler for the node'''
        self.handler = handler
    
    def get_current_pathparcel(self):
        '''This gets the current_pathparcel for the node.'''
        return self.current_pathparcel
    
    def set_current_pathparcel(self, current_path_section):
        '''This sets the current_pathparcel for the node.'''
        self.current_pathparcel = current_path_section
        
    def has_children(self):
        '''
        This determines whether a node has children.
        
        Returns: True/False
        '''
        return len(self.children) > 0
    
    def get_child_node(self, path_parcel):
        '''
        If there is a child node, this function returns it,
        otherwise it returns none.
        '''
        if self.children.get(path_parcel) != None:
            return self.children[path_parcel]
        
        return None
        
    def insert_new_child_node(self, path_parcel):
        '''
        Function Purpose: This function inserts a new child node.
        
        Arguments:
            path_parcel = A parcel of the entire http full path, this is
                in string format.
        
        Returns: It doesn't return anything.
        '''
        # This creates a new node.
        new_node = RouteTrieNode()
        
        # This sets the new_nodes current_pathparcel to path_parcel.
        new_node.set_current_pathparcel(path_parcel)
        
        # This creates a new entry in the node's repostiory dictionary
        # and sets that entry to the new_node, effectively inserting it.
        self.children[path_parcel] = new_node
    
    def __repr__(self):
        '''
        Function Purpose: This is the formatted string that is returned when
            print(RouteTrieNode) is called.
        
        Arguments: None
        
        Returns: The formatted string that prints when print(RouteTrieNode) is
            called.
        '''
        return f'''
        Node Path Parcel: ({self.get_current_pathparcel()})
            Node Handler: ({self.get_handler()})
        '''
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    '''
    REFERENCES: This comes from References 1 & 2 of References at
    the bottom of the python file.
    '''
    def __init__(self, handler = None):
        '''
        Class Purpose: This is the data structure for the class Router, a 
        RouteTrie.
        
        Init Variables:
            self.root = This is the root node of the RouteTrie, and it is
                a RouteTrieNode object. By default, the handler is set to
                None.
        '''
        self.root = RouteTrieNode(handler)
        
    def get_root(self):
        '''This function returns the root of the RouteTrie.'''
        return self.root
    
    def insert_fullpath(self, fullpath):
        '''
        Function Purpose: This creates an HTTP path.
        
        Arguments:
            fullpath = This is list of path parcels that is used to create
                nodes at each path parcel.
        
        Returns: The end node in the fullpath, AKA, the node at the very
            last path parcel.
        '''
        
        # This creates the current_node for the for loop.
        current_node = self.root
        
        # If the root node is querried, the root node is retuned.
        if (fullpath == '/') and (current_node.get_current_pathparcel() == '/'):
            return current_node
        
        # The for loop inserts a node at each path parcel point in the
        # full path.
        for path_part in fullpath:
            if current_node.get_child_node(path_part) == None:
                current_node.insert_new_child_node(path_part)
            current_node = current_node.get_child_node(path_part)
        
        # Once the for loop has traversed through full path, the last node
        # in the full path is returned.
        return current_node
    
    def find_node(self, fullpath):
        '''
        Function Purpose: This returns the node given the full path.
        
        Arguments:
            fullpath: This is a list of path parcels that is followed to find
                a node.
            
        Returns: If the for loop traverses every path parcel, this returns
            the node given the full path. If the full path doesn't exist,
            this function returns None.
        '''
        # The current_node is set to self.root for the for loop.
        current_node = self.root
        
        # If the root node is querried, the root node is returned.
        if (fullpath == '/') and (current_node.get_current_pathparcel() == '/'):
            return current_node
        
        # The for loop traverses the full path. If a path_part does not 
        # exist, then the loop breaks and None is returned.
        for path_part in fullpath:
            if current_node.children.get(path_part) == None:
                return None
            current_node = current_node.get_child_node(path_part)
        
        # If all path_parts exist and the for loop does not break, this
        # returns the current_node at the end of fullpath.
        return current_node
    
            
    def find_handler(self, fullpath):
        '''
        Function Purpose: This returns the handler of a node at the end of
            the full path.
        
        Arguments: 
            fullpath = This is a list of path parcels that is folled to find
            a node and its handler.
        
        Returns: If the full path exists, the handler for the node is
            returned. However, some nodes do not have handlers, and
            a null_handler is returned. Also, if the fullpath and node
            do not exist, the null_handler is returned.
        '''
        # This sets the current_node to self.root for the for loop.
        current_node = self.root
        
        # In the event that there is no node, or there is a node but there
        # is not handler, the null_handler will be returned.
        null_handler = "not found handler"
        
        # This conditional is for when the root node is querried.
        if (fullpath == '/') and (current_node.get_current_pathparcel() == '/'):
            # If there is no handler, the null_handler is returned.
            if current_node.get_handler() == None:
                return null_handler
            # If there is a handler, the handler is returned.
            return current_node.get_handler()
        
        # This is for all other other handler queries other than the root node
        # query. This for loop breaks if path_part in the full path does not
        # exist.
        for path_part in fullpath:
            if current_node.get_child_node(path_part) == None:
                return null_handler
            current_node = current_node.get_child_node(path_part)
        
        # If the full path exists, but the node at the end of the full path
        # does not have a handler, the null_handler is returned.
        if current_node.get_handler() == None:
            return null_handler
        
        # If the full path exists and the node at the end of the full path
        # has a handler, the handler is returned.
        return current_node.get_handler()

# The Router class will wrap the Trie and handle 
class Router:
    '''
    REFERENCES: This comes from References 1 & 2 of References at
    the bottom of the python file.
    '''
    def __init__(self, handler = None):
        '''
        Class Purpose: This is a router. It's used to traverse a RouteTrie
        and ammend it.
        
        Arguments: 
            handler = This sets the handler for the root node of the
                RouteTrie. By default, the handler is None.
        
        Init Variables:
            self.the_router = This creates a RouteTrie. It accepts the
                argument, handler, to set the root node of the RouteTrie.
                By default, the handler is None.
        
        '''
        self.the_router = RouteTrie(handler)
        
    def add_handler(self, the_fullpath, the_handler):
        '''
        Function Purpose: This adds a handler to a full path.
        
        Arguments:
            the_fullpath = This is the full path.
            the_handler = This is the handler that is added to the node
                at the end of the full path.
                
        Returns: Nothing.
        '''
        # This formats the full path so that it can add the handler.
        lookup_path = self.split_path(the_fullpath)
        
        # This is an edge case. When the full_path is an empty string,
        # this prints a message saying that a path must be entered.
        if len(lookup_path) < 1:
            return "A path must be entered to add a handler"
        
        # This creates the full path and the node at the end of the
        # full path.
        node = self.the_router.insert_fullpath(lookup_path)
        
        # This sets the end node's handler to the_handler.
        node.set_handler(the_handler)
    
    def is_string(self, the_string):
        return type(the_string) == str
    
    def lookup(self, the_fullpath):
        '''
        Function Purpose: This looks up a handler for a given full path.
        
        Argument:
            the_fullpath = This is the full path.
        
        Returns: This returns a handler if there is one, and a null_handler
            if there is no handler to return.
        '''
        # This puts the_fullpath in a format that can be used to look up
        # the handler.
        lookup_path = self.split_path(the_fullpath)
        
        # In the edge case in which an empty string was input as
        # the_fullpath, this returns a message saying that a path
        # msut be entered.
        if len(lookup_path) < 1:
            return "A path must be entered to return a handler"
        
        # This either returns the handler or the null_handler.
        return self.the_router.find_handler(lookup_path)

    def split_path(self, string_fullpath):
        '''
        Function purpose: This takes a string and separates it into a list
            of path parcels.
        
        Arguments:
            string_fullpath: This takes the string version of the full path
                and breaks it up into a list of path parcels. 
                
        Returns:
            This usually returns a list of path parcels. There are two
            exceptions when string_fullpath is '/' or ''.
        '''
        # This makes the string lower case.
        string_fullpath = string_fullpath.lower()
        
        # If the string is "/" we simply return "/" for a root node query.
        if string_fullpath == '/':
            return string_fullpath
        
        # If the string is '', 
        if string_fullpath == '':
            return string_fullpath
        
        # For normal full paths, the '/' at the beginning of the full
        # path is deleted.
        if string_fullpath[0] == '/':
            string_fullpath = string_fullpath[1:]
        
        # There are edge cases in which the query ends with "/", this
        # deletes the '/' at the end to handle the edge cases.
        if string_fullpath[-1] == '/':
            string_fullpath = string_fullpath[:-1]
        
        # This creates the list of path parcels from the full path.
        full_path_list = string_fullpath.split('/')
        
        # This returns the list of path parcels from the full path.
        return full_path_list

# Here are some test cases and expected outputs you can use to test your implementation
# The below test cases come from Reference 2 from References at the bottom of this
# python file.

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
# These are four boilerplate examples from Udacity.
print("FOUR NORMAL TEST CASES:")
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print("__________________________________________________", "\n")

print("TWO EDGE CASES:")
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup('')) # This should print "A path must be entered to return a handler"

# REFERENCES
# 1. Udacity Data Structures & Algorithms Nanodegree; 3) Basic Algorithms; 
#        1) Basic Algorithms; 6) Tries
# 2. Udacity Data Structures & Algorithms Nanodegree; 3) Basic Algorithms; 
#        4) Problems Vs Algorithms; 8) Problem 7: Request Routing in a Web
#        Server with a Trie