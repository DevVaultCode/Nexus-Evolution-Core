import os
import random

def calculate_iq(history_len):
    """
    Har naye creature (history_len) ke saath IQ badhta jayega.
    Yeh system ki 'Growth' ko darshata hai.
    """
    base_iq = 100
    growth_factor = 5
    return base_iq + (history_len * growth_factor)

def mutate_dna():
    """
    Yeh system ka 'Evolution' trigger hai.
    Har 30 nodes (din) ke baad, yeh code mein nayi 'skills' add karega.
    """
    mutation_file = "core/neural_logic.py"
    if os.path.exists(mutation_file):
        with open(mutation_file, "a") as f:
            f.write(f"\n# MUTATION_EVENT_{random.randint(1000, 9999)}: System evolved to higher logic.\n")
            f.write("def advanced_cognition():\n")
            f.write("    return 'System is now self-optimizing and learning patterns.'\n")
        print("DNA Mutation complete: System upgraded.")

def get_logic_pattern():
    """
    Har creature ko uska specific 'DNA pattern' deta hai.
    """
    patterns = [
        "Analyzing global data streams...",
        "Simulating quantum crypto-nodes...",
        "Optimizing neural pathways...",
        "Human-like pattern recognition active..."
    ]
    return random.choice(patterns)
  
