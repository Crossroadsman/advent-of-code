class Solver():
    def solver(self, data: {str: [str]} ) -> str:
        if len(data) == 0:
            return "No items in list"

        if len(data) == 1:
            keys = data.keys()
            return next(iter(keys))
        
        # empty structures are falsy and structures with any contents are truthy hence `if v` to check if v is not empty
        data_elements_with_children = {k:v for (k, v) in data.items() if v}
        
        '''
        get a set (no duplicates) comprising all the children by:
        1. making a list by combining all the children lists from each data element;
        2. flatten the list of lists
        3. initialise a set from the list to eliminate duplicates
        This is equivalent to the following in Swift:
        `children = Set( data.flatMap {$0.1} )`
        '''
        
        children = [ v for (k, v) in data.items() ]
        '''
        The following line is equivalent to a nested for loop:
        ```
        for sublist in children:
             for item in sublist:
                 flat_children.append(item)
        ```
        '''
        flat_children = [ element for sublist in children for element in sublist ]
        children = set( flat_children )
        
        new_data = {k:v for (k, v) in data.items() if k not in children}
        
        return self.solver(data=new_data)
