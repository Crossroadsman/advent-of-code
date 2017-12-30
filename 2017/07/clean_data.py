import re

class CleanData():

    def get_filename(self) -> str:
        return input("Enter filename > ")

    def clean_data(self, filename: str) -> [{str : [str]}]:
        file_object = open(filename, 'r')
        
        cleaned_data = []
        
        """
        (?P<element>\w+) : capture group `element` comprising one or more word characters
        [ \t]+ : one or more of either space or tab
        \( : open paren
        \d+ : one or more digit characters
        \) : close paren
        [ \t]+ : one or more of either space or tab
        -
        >
        [ \t]+ : one or more of either space or tab
        (?P<children>[\w, ]+) : capture group `children` comprising one or more of either word character, comma or space
        """
        has_children_pattern = r'(?P<element>\w+)[ \t]+\(\d+\)[ \t]+->[ \t]+(?P<children>[\w, ]+)'
        no_children_pattern = r'(?P<element>\w+)[ \t]+\(\d+\)$'
        
        for line in file_object:
            element = None
            children = None
            
            # note that if we wanted to find the match somewhere in the string but not necessarily at the beginning, we would use re.search
            has_children_match_object = re.match(has_children_pattern, line)
            if has_children_match_object: # a match was found
                element = has_children_match_object.groupdict()['element']
                children = has_children_match_object.groupdict()['children'].split(', ')
                cleaned_data.append( { element : children } )
            
            else: # no match for has_children_pattern
                no_children_match_object = re.match(no_children_pattern, line)
                if no_children_match_object: # a match was found
                    element = no_children_match_object.groupdict()['element']
                    children = []
                    cleaned_data.append( { element : children } )
                    
                else: # no match for no_children_pattern
                    print("Unable to match data. Was input file valid?")
        
        file_object.close()
        return cleaned_data
