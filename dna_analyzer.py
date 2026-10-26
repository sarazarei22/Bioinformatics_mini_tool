"""
DNA Sequence Analyzer & GC Content Calculator
Description: A clean utility to process raw DNA sequences, clean them, 
             and compute the GC content percentage.
"""

def clean_sequence(raw_seq: str) -> str:
    """Removes whitespaces, numbers, and converts the sequence to uppercase."""
    # Using list comprehension and string methods learned in Python basics
    cleaned = "".join([char.upper() for char in raw_seq if char.isalpha()])
    return cleaned


def calculate_gc_content(sequence: str) -> float:
    """Calculates the percentage of G and C bases in a DNA sequence."""
    if not sequence:
        return 0.0
    
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    
    gc_percentage = ((g_count + c_count) / len(sequence)) * 100
    return round(gc_percentage, 2)


def main():
    # Sample raw DNA sequence with noise (simulating messy lab data)
    raw_dna = "  atg cgt acg tag cgc gcg tat acg tcg 123 "
    
    print("=" * 40)
    print("      DNA SEQUENCE ANALYSIS REPORT      ")
    print("=" * 40)
    print(f"Raw Input Sequence: {raw_dna.strip()}")
    
    # Process data
    cleaned_seq = clean_sequence(raw_dna)
    gc_result = calculate_gc_content(cleaned_seq)
    
    # Display results
    print(f"Cleaned Sequence:   {cleaned_seq}")
    print(f"Sequence Length:    {len(cleaned_seq)} bp")
    print(f"GC Content:         {gc_result}%")
    print("=" * 40)


if __name__ == "__main__":
    main()
