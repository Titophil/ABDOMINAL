
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import mne
import matplotlib.pyplot as plt


#load record and annotations

file_path = '/home/user/MACHINE LEARNING/abdominal/r01.edf'
raw = mne.io.read_raw_edf(file_path, preload=True)
data = raw.get_data()

signal = data[0]

segment_length= 1000
segments = []
labels = []

for i in range(0, len(signal) - segment_length,segment_length):
    segment = signal[i:i + segment_length]
    features = [np.mean(segment), np.std(segment), np.max(segment), np.min(segment)]
    segments.append(features)
  
    label = 1 if np.mean(segment)>0 else 0
    labels.append(label)

X= np.array(segments)
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

clf = GaussianNB()
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

plt.savefig("ecg_plot.png")
