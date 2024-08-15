def are_we_in_trouble(j_angry, s_angry):
    if (j_angry and s_angry) or (not j_angry and not s_angry):
        return True
    else:
        return False

# Example usage:
print(are_we_in_trouble(True, True))   # Output: True
print(are_we_in_trouble(False, False)) # Output: True
print(are_we_in_trouble(True, False))  # Output: False
print(are_we_in_trouble(False, True))  # Output: False

