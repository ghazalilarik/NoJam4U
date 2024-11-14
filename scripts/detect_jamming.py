# detect_jamming.py
import numpy as np

def detect_jamming(signal_data, threshold=-50):
    """
    Detect potential jamming in the given signal data.
    Returns True if jamming is detected, False otherwise.
    """
    signal_db = 10 * np.log10(signal_data)
    if np.max(signal_db) > threshold:
        print("Jamming detected: Signal strength exceeds threshold.")
        return True
    return False
