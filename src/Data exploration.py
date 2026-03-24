import pandas as pd

metadata_path = "C:/Users/Ayuning Maretania Q/Documents/IDSC/brugada-huca/brugada-huca-12-lead-ecg-recordings-for-the-study-of-brugada-syndrome-1.0.0/metadata.csv"

metadata = pd.read_csv(metadata_path)

metadata.head()

summary = metadata.agg(
    total=('brugada','count'),
    brugada_cases=('brugada', lambda x: (x==1).sum()),
    normal_cases=('brugada', lambda x: (x==0).sum())
)

print(summary)

### Distribusi Basal Pattern
metadata['basal_pattern'].value_counts()

### Distribusi Sudden Death
metadata['sudden_death'].value_counts()

import matplotlib.pyplot as plt

metadata['brugada'].value_counts().sort_index().plot(kind='bar')

plt.xlabel("Diagnosis Brugada (0 = Normal, 1 = Brugada)")
plt.ylabel("Jumlah pasien")
plt.title("Distribusi Diagnosis Brugada pada Metadata")

plt.show()
