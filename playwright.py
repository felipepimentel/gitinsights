def update_line(self, key, pattern):
    # Get the original value from the dictionary
    original_value = self.var_dict.get(key, '')
    if not isinstance(original_value, str):
        return original_value  # If it's not a string, return as is

    # Replace all variables in the value
    def replace(match):
        variable_name = match.group(1)
        # Get the variable value from the dictionary
        variable_value = self.var_dict.get(variable_name, '')
        if '$' in variable_value:
            # If the variable value contains a nested variable, don't replace it yet
            return match.group(0)
        return str(variable_value)
    
    updated_value = pattern.sub(replace, original_value)
    self.var_dict[key] = updated_value  # Update the dictionary with the new value
    return updated_value

def update_variables(self):
    # Compile the variable pattern
    pattern = re.compile(r'\$\((\w+)\)')

    # Keep track of whether we made any replacements
    replacements_made = True
    while replacements_made:
        replacements_made = False
        for key in self.var_dict:
            updated_value = self.update_line(key, pattern)
            # If the updated value is different from the original, we made a replacement
            if updated_value != self.var_dict[key]:
                replacements_made = True

    # Check if there are unresolved variables
    for key, value in self.var_dict.items():
        if isinstance(value, str) and pattern.search(value):
            raise ValueError(f"Unresolved variable in key '{key}': {value}")
