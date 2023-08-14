### Challenge 04
### Repeated DNA Sequences


### Function for identifying DNA sequences (main function)
def main(s):

    # Define lenght of the DNA chain and dictionary where DNA sequences are going to be saved
    l = len(s)
    dc_sequences = dict()

    # Handling sequences
    for ii in range(0,l-9):

        # Extract sequence
        substr = s[ii:ii+10]
        ls_keys = list(dc_sequences.keys())

        # Saved number of occurrences of the extracted sequence
        if substr not in ls_keys:
            dc_sequences[substr] = 1
        else:
            dc_sequences[substr] = dc_sequences[substr]+1

    # Retrieve sequences that appeared more than once in the DNA chain
    result = []
    for key, value in dc_sequences.items():
        if value >= 2:
            result.append([key, value])
    
    return result


### Identification of the DNA sequences (execute the main function)

# Initialize chain of DNA
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# s = "AAAAAAAAAAAAA"

# Call the main function
if __name__ == '__main__':
    print("------- Repeated sequences -------")
    print(main(s))
