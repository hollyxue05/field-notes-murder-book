import itertools

def get_full_length_permutations(input_string):
    """
    Generates all possible permutations of letters from an input string
    that are the same length as the input string.

    Args:
        input_string (str): A string of letters.

    Returns:
        list: A list of tuples, where each tuple is a permutation of letters.
    """
    
    letters = list(input_string)
    print(f"\n--- Generating full-length permutations for: '{input_string}' ---")
    
    # Use itertools.permutations
    # By default, without an 'r' argument, it generates permutations 
    # of the full length of the input iterable.
    perms = list(itertools.permutations(letters))
    
    return perms

def print_sequences_nicely(sequence_list, sequence_type="sequences"):
    """
    Prints the list of sequences (combinations or permutations)
    in a user-friendly format, automatically removing duplicates.

    Args:
        sequence_list (list): The list of tuples to print.
        sequence_type (str, optional): The name of the sequence type for printing.
    """
    
    unique_sequences = []
    # Use a set to keep track of items we've already seen
    # This preserves the order of first appearance
    seen = set()
    for seq in sequence_list:
        if seq not in seen:
            unique_sequences.append(seq)
            seen.add(seq)
    
    print(f"\nFound {len(unique_sequences)} total unique {sequence_type} (duplicates removed):")
    
    # We join the tuple of characters (e.g., ('a', 'b')) 
    # into a string (e.g., "ab") for cleaner printing.
    for seq in unique_sequences:
        print("".join(seq))

# word1 = "abbc"
# all_perms = get_full_length_permutations(word1)

capital_letters = "TTHHSISSISDIEDERCOUNHTYMESS"
all_perms = get_full_length_permutations(capital_letters)

print_sequences_nicely(all_perms, "permutations")