### Challenge 05
### Translate DNA sequences to proteins


### Import libraries
import json



### Load utilities to translate

# Load list of aminoacids
def load_aminoacids():

    # Initialize list of aminoacids
    ls_aminoacids = []

    # Fill list of aminoacids
    with open('input_aminoacids.dat') as file_aminoacids:
        for line in file_aminoacids:
            # Whitespaces are deleted, characters to uppercase, and splitting information into columns
            aminoacid_info = line.replace(" ", "").replace("\n", "").upper().split("-")
            # Append extracted aminoacid information
            ls_aminoacids.append(aminoacid_info)

    return ls_aminoacids


# Load dictionary of codons (3-nucleotids-in-a-row) to aminoacids
def load_codons(ls_aminoacids):
    
    # Opening database of codons
    file_codons = open('input_codon_to_aminoacids.json')
    # Convert JSON object to a dictionary
    dc_codons = json.load(file_codons)
    # List of aminoacids - names of 3 characters
    ls_aminoacids_abbrv_3char = [aminoacid[1] for aminoacid in ls_aminoacids]+['STOP']

    # Assign new values to dictionary, 1 character per aminoacid instead of 3 characters
    for key, value in dc_codons.items():
        # Convert the value to uppercase
        value_aux = value.upper()
        # Special case for stop codons
        if value_aux == "STOP":
            dc_codons[key] = "_"
        # Normal cases
        else:
            # Index of the aminoacid
            index_aux = ls_aminoacids_abbrv_3char.index(value_aux)
            # Equivalent name of 1 character
            aminoacid_1char = ls_aminoacids[index_aux][2]
            # New value in the dictionary for the codon
            dc_codons[key] = aminoacid_1char
        
    return dc_codons



### Generate translation 

# Load input (DNA sequence)
def load_input():
    with open('input_dna_sequence.dat') as file_dna_sequence:
        # The entire text processing is wrapped in one line
        dna_chain = "".join([line.replace("\n", "").replace(" ", "").upper() for line in file_dna_sequence])
    return dna_chain


# RNA transcription
def rna_chain(dna_chain):
    # Just replacing nucleotide "T" by "U"
    dna_chain = dna_chain.upper().replace("T", "U")
    return dna_chain


# Find start and end of the RNA sequence
def crop_rna_sequence(rna):

    # Look for the 3-characters sequence "AUG" as they set the beginning of a protein
    while rna[0:3] != "AUG":
        rna = rna[1:]

    # Look for the 3-characters sequences that set the end of a protein
    # Initial guess
    final_index = 3
    possible_end = rna[final_index:final_index+3]
    # Iterative search from the starting aminoacid "AUG"
    while (possible_end != "UAA") and (possible_end != "UAG") and (possible_end != "UGA"):
        final_index += 3
        possible_end = rna[final_index:final_index+3]
    rna = rna[0:final_index]

    return rna


# Convert RNA into aminoacids
# Complete translation for a single protein
def rna2protein(rna, dc_codons):
    
    # Lenght of the RNA chain
    lrna = len(rna)

    # Empty string where sequence of aminoacids will be saved
    sequence_aminoacids = ""
    
    # Translation of RNA into aminoacids
    for ii in range(int(lrna/3)):
        # Extract codon
        codon = rna[3*ii:3*(ii+1)]
        # Add aminoacid to the sequence
        aminoacid_1char = dc_codons[codon]
        sequence_aminoacids = sequence_aminoacids + aminoacid_1char

    return sequence_aminoacids


# Verify result
def validation(real_res):
    # Load expected result
    with open('output_protein_sequence.dat') as file_protein_sequence:
        exp_res = "".join([line.replace("\n", "").replace(" ", "").upper() for line in file_protein_sequence])
    # Verification
    check_val = real_res == exp_res
    return check_val



### Full sequence of aminoacids for a single protein (main function)
def main():

    # Load list of 20 fundamental aminoacids
    ls_aminoacids = load_aminoacids()

    # Load dictionary of codons
    # Each combination between nucleotides "U", "C", "A", and "G" represent an aminoacid 
    dc_codons = load_codons(ls_aminoacids)

    # Load DNA sequence
    dna_chain = load_input()

    # Transcription of DNA sequence into RNA
    rna = rna_chain(dna_chain)

    # Crop RNA from the starting to end aminoacids
    rna = crop_rna_sequence(rna)

    # RNA translated into sequence of aminoacids
    sequence_aminoacids = rna2protein(rna, dc_codons)

    # Perform result validation
    check_val = validation(sequence_aminoacids)

    return dna_chain, sequence_aminoacids, check_val



### Translate a DNA sequence into an aminoacid sequence for a given protein (execute the main function)

# Call the main function
if __name__ == '__main__':
    dna_chain, sequence_aminoacids, check_val = main()
    print("--------------------- Result is the same as expected? ---------------------")
    print(check_val)
    print("--------------------- DNA sequence ---------------------")
    print(dna_chain)
    print("--------------------- Translated sequence of aminoacids ---------------------")
    print(sequence_aminoacids)
