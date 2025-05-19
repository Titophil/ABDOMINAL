# ABDOMINAL

Features
Reads EDF signal files using mne library

Extracts basic statistical features (mean, std, max, min) from segmented ECG signals

Trains a Gaussian Naive Bayes classifier using scikit-learn

Evaluates classification performance with a detailed classification report

Requirements
Python 3.8+

Libraries:

wfdb

mne

numpy

scikit-learn

matplotlib

Installation
Clone the repo:

bash
Copy
Edit
git clone <git@github.com:Titophil/ABDOMINAL.git>
cd <ABDOMINAL>
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Place your EDF files (e.g., r01.edf) in the abdominal directory.

Run the script to train and evaluate the model:

bash
Copy
Edit
python index.py
Script Details
Loads abdominal ECG signal from EDF file using mne

Segments the signal into fixed-length windows

Extracts features for each segment

Labels segments based on a simple threshold on the mean signal value

Trains a Gaussian Naive Bayes model to classify segments

Prints classification performance metrics

Notes
The current labeling is synthetic for demonstration and should be replaced with domain-specific labels for real-world use.

Visualization can be enabled if running in an environment with a GUI or by saving plots to disk.

Contact
For questions or support, contact [kipronotitus254@gmail.com].