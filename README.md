<img width="2882" height="1434" alt="2752B777-0D04-4D80-B6E8-53BA337C0F49" src="https://github.com/user-attachments/assets/73120603-ae85-40af-b612-2f231ae194e1" />
<img width="2882" height="1434" alt="2B7486DC-963F-4DCD-B2C3-DA770A9F8244" src="https://github.com/user-attachments/assets/11a4a33b-ead9-4600-a09a-586b37f85fa6" />
<img width="2882" height="1434" alt="A9B93621-8E6A-49E7-BA33-CEF6083BD638" src="https://github.com/user-attachments/assets/eec00339-6266-4c17-8fdc-bffeb5b63b3b" />
# AI-DRIVEN PHISHING DETECTION:

**A Machine Learning Prototype for Cybersecurity matrix Analysis**
*Developed as a Portfolio Project for cyberscurity Application (2026)*

## PROJECT OVERVIEW:
This project is an automated **AI-Driven Phishing Detection** designed to combat social engineering and cyber threats. Built using Python, if features a high
accuracy machine learning backend trained on **over 50,000 global phishing and legitimate URL records**, integrated with a functional real-time web
portal dashboard.

## KEY DELIVERABLES:
**High-Accuracy Brain:** uses a tuned **Random Forest Classifier** achieving a **96.01% empirical accuracy rating**.
**Automated Feature Parser:** extracts critical structural indicators from raw URLs(length, dot-counts, script injections, protocol verification, numerical ratios) automatically.
**Interactive Portal:** built using the **streamlit** micro-framework for swift end-use processing.

## CORE DATASETATTRIBUTES (SIMA ANJALI FRAMWORK):
The analytical processing engine monitors 12 structural variables derived from network telemetry data, including:
**NumDots / URLlength:** structural manipulation tracking:
**Atsymbol / Numdash / Numpercent:** redirect formating anomalies.
**IpAddress / httpsInhostname:** cryptographic & host machine verification layers.

## MODEL EVALUTION &  PERFORMANCE:
the system yield standard benchmarks evaluated via scikit-learn:
* **Global Test Accuracy:** '96.01%'
* **Confusion Matrix Insights:** minimal false negatives (FN) to ensure mission-critical safety in threat containment.
* **Evaluation Output:** saved natively as 'accuracy_graph.png' inside the repository workspace.
* **Confusion Matrix Insights:** minimal false negatives (FN) to ensure mission-critical safety in threat containment.

## TECNOLOGY STACK:
**Language:** python 3.x
**Core ML Engineering:** scikit-learn, pandas, numpy
**Visual Analytics:** seaborn, matplotlib
**Web UI Engine:** streamlit framework

##EXECUTION INSTRUCTIONS:

## 1. REPOSITORY SETUP & INSTALLATIONS
Clone this Repository Workspace and trigger component dependencies installations:
'''bash
pip install pandas numpy scikit-learn streamlit seaborn matplotlib
'''

## 2. MACHINE LEARNING BRAIN GENERATION:
train the random foreset architecture and export serialized vector serialization payloads:
'''bash
python train_model.py
'''
*Expected Terminal OutPut:* verfication print of **96.01% accuracy** along with generation of 'cyber_phishing_model.pkl' and 'accuracy_graph.png'.

## 3. DEPLOY LOCAL AUTOMATED UI ENGINE
launch thr client-side streaming user interface dashboard:
'''bash
streamlit run app-dashboard.py
'''

## FUTURE SCALABILITY ARCHITECTURE (ROADMAP)
**Natural Language Parsing:** integration the 'urlextract' tokenization module to analyze complete text documents and raw enterprise email payloads.
**Advanced Deep Learning Transition:** porting core algorithoms to TensorFlow/keras sequential lstm nets to calculate structural anomalies in real-time streaming connections.

