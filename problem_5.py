class TrieNode:
    '''
    References: This code comes from References 1 & 2 from References.
    '''
    def __init__(self):
        '''
        This initializes the TrieNode.
        
        Init Variables:
            self.is_word = This is a boolean variable that signifies
                whether a string of characters is a word. The initial
                TrieNode in a Trie is not a word, because it does not
                consist of any characters.
            self.children = This is the suffix character dictionary of a
                TrieNode.
        '''
        self.is_word = False
        self.children = {}
    
    def insert_char(self, char):
        '''
        Funciton Purpose: This function inserts a child node for the node.
        
        Argument:
            Char = It must be a string character, and it must be exactly 
            one character.
                
        Returns: The function doesn't return anything.
        '''
        # An error is raised if char is not a string.
        assert type(char) == str, f'''Inserted character must be string!'''
        
        # An error is raised if a character 
        assert len(char) == 1, f'''
        The length of the character must be 1 exactly!
        '''
        
        # The character is lower cased, and then it is inserted into the
        # dictionary and given a node value.
        char = char.lower()
        self.children[char] = TrieNode()
    
    def has_children(self):
        '''
        This function determines whether the node has any character
        children. It returns True or False.
        '''
        return len(self.children) > 0
    
    def blank_set(self):
        '''
        This function creates and returns an empty set.
        '''
        empty_set = set()
        return empty_set
    
    def recurse_suffix_helper(self, node = None, suffix = "",
                              suffix_set = None, debug_mode = False):
        '''
        Helper Function Purpose: The purpose of this helper function is to 
            find all the suffixes below a given prefix that create a word.
            The function recursively calls itself in order to search 
            through all the nodes.
            
        Arguments: 
            Node = This is the node that's having it's suffix examined.
                It is initialized as "None", but is updated as the function
                is recursively called.
            Suffix = This is the character string being examined. It is 
                initialized as none, but is updated when the function is
                called recursively.
            Suffix_set = This is the set of suffixes that make a word for
                a particular prefix. This is initialized as None but is 
                updated when the funciton is called recursively.
            Debug_mode = This prints debugging text when it is set to true,
                but by default it is set to false.
        
        Returns: Output_collection = A set of all the suffixes in the Trie 
            that make a complete word for a particular prefix.
        '''
        # Debugging is initialized for the purpose of seeing bugs in
        # the function.
        debugging = debug_mode
        
        # This is a base case in which nothing follows a prefix.
        if node == None:
            if not self.has_children():
                return self.blank_set()
        
        # If we are not looking at the very first node, and the
        # current suffix is a word, then we add it to the suffix_set.
        if (node != None) and (node.is_word == True):
            
            # If debug mode is true, this prints the suffix if 
            # it can be formed into a word.
            if debug_mode:
                print(f'''
                The suffix ({suffix}) forms a word. Adding to set of
                suffixes!
                ''')
            
            # The suffix is added to the suffix set.
            suffix_set.add(suffix)
            
            # If debug mode is on, this prints the current suffix set.
            if debug_mode:
                print(f'''
                The set of suffixes is now: 
                ({suffix_set})
                ''')
        
        # If we are not looking at the initial node and the current node
        # does not have children. The suffix_set is returned.
        if (node != None) and (not node.has_children()):
            return suffix_set
    
        # This initiallizes the variables for the for loop that
        # calls the recurse_suffix_helper function to iterate through
        # all the suffixes to find the suffixes that make complete words
        # for a given prefix.
        output_collection = self.blank_set()
        if node == None:
            char_dict = self.children
        else:
            char_dict = node.children
            
        # This for loop iterates through the suffixes by calling upon
        # recurse_suffix_helper recursively.
        for char in char_dict:
            # This creates suffix_tracker to be put into
            # recurse_suffix_helper for the suffix_set argument.
            if node == None:
                suffix_tracker = self.blank_set()
            else:
                suffix_tracker = suffix_set
                
            # This creates new_suffix to be put into
            # recurse_suffix_helper for the suffix argument.
            new_suffix = suffix + char
            
            # This creates the node to be put into
            # recurse_suffix_helper for the node argument.
            if node is None:
                new_node = self.children[char]
            else:
                new_node = node.children[char]
            
            # The output is set to the recursive function.
            output = self.recurse_suffix_helper(new_node, new_suffix,
                                                suffix_tracker, debugging)
            
            # Once the output is actualized, the function is done
            # recursing, if there is anything in the output, it is appended
            # to the output_collection set.
            if len(output) >= 1:
                for i in output:
                    output_collection.add(i)
                    
        # Once the for loop is over, the output collection set is returned.
        return output_collection
        
    def suffixes(self):
        '''
        Function Purpose: The purpose of this function is to find all the 
            suffixes below a prefix that create a word.
            
        Arguments: No arguments.
        
        Returns: A sorted list of suffixes that create words for a given
        prefix.
        '''
        # This creates the output by calling the helper function
        # self.recurse_suffix_helper. The output is in a set()
        # format.
        output = self.recurse_suffix_helper()
        
        # This converts the set to a list format, and then sorts
        # the list.
        output = list(output)
        output.sort()
        
        # This returns the sorted list of suffixes.
        return output

## The Trie itself containing the root node and insert/find functions
class Trie:
    '''
    References: This code comes from References 1 & 2 from References.
    '''
    def __init__(self):
        '''
        This initializes the class, Trie.
        
        Init Variable:
            self.root = This is the root of the tree and a TrieNode.
        '''
        self.root = TrieNode()

    def insert_word(self, word):
        '''
        This adds a word to the Trie.
        
        Arguments:
            Word = This is word, in string fromat.
        
        Returns: This function doesn't return anything.
        '''
        # The current_node is set to self.root. This prepares for the
        # traversal through the root nodes children characters (if there 
        # are any) in the for loop.
        current_node = self.root
        
        # This lower cases all the characters in word.
        word = word.lower()
        
        # This for loop iterates through all the children dictionaries.
        for char in word:
            # If the character is not in the current node, this character
            # is put into the current node's children dictionary.
            if char not in current_node.children:
                current_node.insert_char(char)
            
            # The current node is then updated to be the child that has
            # the current character.
            current_node = current_node.children[char]
        
        # Once the for loop is finished and the last character has been
        # inserted from the word, the current node's init variable,
        # is_word, is set to true.
        current_node.is_word = True

    def find(self, prefix):
        '''
        Function Purpose: The purpose of this function is to return the
            node of a given prefix (the prefix argument). If the prefix
            doesn't exist within the Trie, this function returns None.
        
        Argument:
            Prefix = This is a string of characters. If this string
                is in the Trie, this function returns the current_node
                that contains the prefix. Otherwise, it returns None.
        
        Returns: Either the node containing the prefix or None.
        '''
        # The current node is set to self.root for the for loop.
        current_node = self.root
        
        # The prefix's characters are lower cased.
        prefix = prefix.lower()
        
        # The for loop traverses the characters. If the for loop
        # comes across a character not in the Trie, the loop breaks
        # and returns None. Otherwise, once the for loopis traversed, this 
        # function returns current_node, the node with all the prefix 
        # characters.
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        
        return current_node

# References: This comes from Reference 2 of References.
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert_word(word)

# References: This comes from Reference 2 of References.
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');

# REFERENCES
# 1. Udacity Data Structures & Algorithms Nanodegree; 3) Basic Algorithms; 
#        1) Basic Algorithms; 6) Tries
# 2. Udacity Data Structures & Algorithms Nanodegree; 3) Basic Algorithms; 
#        4) Problems Vs Algorithms; 6) Problem 5: Autocomplete with Tries