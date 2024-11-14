import numpy as np
from time import sleep
from rtlsdr import RtlSdr  # If you decide to use an RTL-SDR as a source; otherwise, adapt for HackRF if using pyhackrf

# Threshold for detecting jamming (dB level)
JAMMING_THRESHOLD_DB = -50
# Frequency hop step in Hz
HOP_STEP_HZ = 5e6
# Sample rate in Hz
SAMPLE_RATE = 2.048e6  # Adjust as needed

# Initial frequency (in Hz, here set to WiFi frequency for example)
INITIAL_FREQ = 2.45e9  # Set this to the starting frequency

def detect_jamming(signal_data, threshold=JAMMING_THRESHOLD_DB):
    """
    Detect potential jamming in the given signal data.
    Returns True if jamming is detected, False otherwise.
    """
    # Convert signal data to dB
    signal_db = 10 * np.log10(np.abs(signal_data))
    if np.max(signal_db) > threshold:
        print("Jamming detected: Signal strength exceeds threshold.")
        return True
    return False

def hop_frequency(sdr, current_frequency, hop_step=HOP_STEP_HZ):
    """
    Hop to a new frequency to avoid jamming.
    """
    new_frequency = current_frequency + hop_step
    sdr.center_freq = new_frequency
    print(f"Hopped to new frequency: {new_frequency} Hz")
    return new_frequency

def main():
    # Initialize the SDR device (e.g., RTL-SDR or HackRF; adjust as necessary)
    sdr = RtlSdr()
    sdr.sample_rate = SAMPLE_RATE
    sdr.center_freq = INITIAL_FREQ
    sdr.gain = 'auto'

    current_frequency = INITIAL_FREQ

    try:
        while True:
            # Read samples from SDR
            samples = sdr.read_samples(1024)

            # Detect jamming
            if detect_jamming(samples):
                # Hop frequency if jamming is detected
                current_frequency = hop_frequency(sdr, current_frequency)

            # Delay between checks
            sleep(1)

    except KeyboardInterrupt:
        print("\nExiting program.")

    finally:
        sdr.close()

if __name__ == '__main__':
    main()

