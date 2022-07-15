# Signal-Processing-Features

All the presented codes are really simple algorithms that can helps in extracting features from signals, useful when talking about signal processing.

## The project

The features presented was calculated to build up a dataset that has been employed for classification purposes in NILM ( non-intrusive load monitoring ).
To extract and collecting data the used software was Python. In particular all the signals analyzed come from the COOLL dataset, therefore in the code snippets will be always used power, current or voltage signals (but actually codes can be implemented over any kind of signal).

If your intentions are to use this repository, please cite and refer to:
G.Braglia, A.E. Lazzaretti, "An Embedded System for NILM using Machine Learning", XV Brazilian Congress on Computational Intelligence, 2021.

Full-text available on ResearchGate at
https://www.researchgate.net/publication/356092329_An_Embedded_System_for_NILM_Using_Machine_Learning

## Important Resources

Here I leave attached the materials that helped me in get all that I needed for this project.

- COOLL dataset : https://coolldataset.github.io/
- Classification algorithms : https://github.com/rasbt/python-machine-learning-book-3rd-edition
- VI trajectories features : https://github.com/brunamulinari/V-I_trajectory
- A. L. Wang, B. X. Chen, C. G. Wang, and D. D. Hua, "Non-intrusive load monitoring algorithm based on features of V–I trajectory" Electric Power Systems Research, 2018.
- MULINARI, B. M., CAMPOS, D. P., COSTA, C. H., ANCELMO, H. C., LAZZARETTI, A. E., OROSKI, E., LIMA, C. R. E., RENAUX, D. P. B., POTTKER, F., LINHARES, R. R. "A New Set of Steady-State and Transient Features for Power Signature Analysis Based on V-I Trajectory". Accepted in: IEEE PES Innovative Smart Grid Technology Latin America, 2019. 

## Folders

- **Features/_Common Features_** : most common and used features that can be extrapolated from a signal (power signals will be used here) ;
- **Features/_VI trajectories_** : few features relative to VI trajectory analysis ;
- **Features/_Power Features_** : algorithms relative to the computation of active, reactive and apparent power .

## Questions & Suggestions
For any doubt, question or suggestion, please feel free to email at:
giovanni.braglia@unimore.it



