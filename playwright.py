import re

class YamlProcessor:
    def __init__(self, var_dict):
        self.variable_pattern = re.compile(r'\$\((\w+)\)')
        self.var_dict = var_dict

    def update_line(self, key):
        # Get the original value from the dictionary
        original_value = self.var_dict.get(key, "")
        # If it's not a string, return as is
        if not isinstance(original_value, str):
            return original_value
        
        # Replace all variables in the value
        def replace(match):
            variable_name = match.group(1)
            # Get the variable value from the dictionary
            variable_value = self.var_dict.get(variable_name, "")
            # If the variable value itself contains a nested variable, don't replace it yet
            if "$" in variable_value:
                return match.group(0)  # Return the original match
            return str(variable_value)

        updated_value = self.variable_pattern.sub(replace, original_value)
        # Update the dictionary with the new value
        self.var_dict[key] = updated_value
        return updated_value

    def update_variables(self):
        # Keep updating until there are no more variables to replace
        while True:
            replacements_made = False
            for key, value in self.var_dict.items():
                if isinstance(value, str) and self.variable_pattern.search(value):
                    updated_value = self.update_line(key)
                    if updated_value != value:
                        replacements_made = True

            if not replacements_made:
                break

        # Check if there are unresolved variables
        for key, value in self.var_dict.items():
            if isinstance(value, str) and self.variable_pattern.search(value):
                raise ValueError(f"Unresolved variable in key '{key}': '{value}'")

# Example usage
var_dict = {
    'var1': 'value1',
    'var2': 'value2',
    'var3': '$(var1) and $(var2)',
    'var4': '$(var3) are combined'
}

processor = YamlProcessor(var_dict)
processor.update_variables()
print(processor.var_dict)
