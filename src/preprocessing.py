metadata.loc[metadata['brugada'] == 2, 'brugada'] = 1

metadata['brugada'].value_counts()

normal_ids = metadata[metadata['brugada']==0]['patient_id'].head(4).tolist()
brugada_ids = metadata[metadata['brugada']==1]['patient_id'].head(4).tolist()

print(normal_ids)
print(brugada_ids)

import numpy as np


### Membaca FIle ECG
def read_ecg(patient_id, folder="C:/Users/Ayuning Maretania Q/Documents/IDSC/brugada-huca/brugada-huca-12-lead-ecg-recordings-for-the-study-of-brugada-syndrome-1.0.0/files/"):
    
    path = f"{folder}{patient_id}/{patient_id}.dat"
    
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    
    ecg = np.fromfile(path, dtype=np.int16, count=1200*12)
    
    ecg_matrix = ecg.reshape(-1,12)
    
    leads = ["I","II","III","aVR","aVL","aVF",
             "V1","V2","V3","V4","V5","V6"]
    
    return pd.DataFrame(ecg_matrix, columns=leads)

ecg_normal_list = [read_ecg(pid) for pid in normal_ids]
ecg_brugada_list = [read_ecg(pid) for pid in brugada_ids]
ecg_all_list = [read_ecg(pid) for pid in metadata["patient_id"].values]

### Plot ECG Pasien Normal
fig, axes = plt.subplots(2,2, figsize=(10,6))

for i, ax in enumerate(axes.flatten()):
    ax.plot(ecg_normal_list[i]["V2"])
    ax.set_title(f"Normal Patient {normal_ids[i]}")
    ax.set_xlabel("Sample")
    ax.set_ylabel("Amplitude")

plt.tight_layout()
plt.show()

### Plot ECG PAsien Brugada
fig, axes = plt.subplots(2,2, figsize=(10,6))

for i, ax in enumerate(axes.flatten()):
    ax.plot(ecg_brugada_list[i]["V2"])
    ax.set_title(f"Brugada Patient {brugada_ids[i]}")
    ax.set_xlabel("Sample")
    ax.set_ylabel("Amplitude")

plt.tight_layout()
plt.show()
