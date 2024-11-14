# NoJam4U

## Overview
**NoJam4U** utilizes HackRF One and GNU Radio to dynamically counter WiFi jamming by detecting interference and initiating frequency hops, ensuring continued network stability and security.

## Installation
### Prerequisites
- HackRF One
- GNU Radio
- Python with NumPy library

### Setup
```bash
sudo apt install gnuradio gnuradio-dev gr-osmosdr
pip install numpy

## Running NoJam4U in Python

To detect WiFi jamming and automatically hop frequencies to avoid interference, run the `nojam4u.py` script:

```bash
python nojam4u.py

## Explanation of the Script
detect_jamming: This function takes a sample data array and checks if any signal strength exceeds a specified threshold (JAMMING_THRESHOLD_DB), indicating potential jamming.
hop_frequency: This function increments the current frequency by a specified step (HOP_STEP_HZ) to avoid jamming.
main: This function initializes the SDR, starts reading samples, and checks for jamming. If jamming is detected, it hops to a new frequency.

This consolidated approach keeps your project straightforward and easy to use without needing `.grc` files or multiple scripts. Let me know if you have any further questions!
