# hop_frequency.py
def hop_frequency(sdr, current_frequency, hop_step=5e6):
    """
    Hop to a new frequency to avoid jamming.
    """
    new_frequency = current_frequency + hop_step
    sdr.set_center_freq(new_frequency)
    print(f"Hopped to new frequency: {new_frequency} Hz")
    return new_frequency
