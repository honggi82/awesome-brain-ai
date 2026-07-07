[Figure 1]

# Radi´omica utilizando representaciones frecuenciales, casos de estudio: Caracterizacio´n de trastorno del espectro autista y c´ancer de pro´stata utilizando MRI

### Nicol´as Mu´nera Garzo´n Director: Eduardo Romero Castro. MD. Ph.D.

Universidad Nacional de Colombia Departamento de Ingenierı´a de sistemas y computaci´n Bogot´, Colombia 2021

# Radiomics using frequency representations, cases of study: Autism spectrum disorder and prostate cancer characterization through MRI

### Nicol´as Mu´nera Garzo´n

Thesis presented as partial requirement for the degree of: Master in Systems Engineering

Advisor: Eduardo Romero Castro. MD. Ph.D.

Research Area: Radiomics, Magnetic Resonance Imaging, Deep Learning Cim@Lab Research Group

Universidad Nacional de Colombia Faculty of Medicine Bogot´, Colombia 2021

To my family whose support and love have carried me to this point, thank you for everything.

who can say where the road goes, where the day ﬂows, only time... Only time - Enya

## Acknowledgments

As one of the wildest roller coasters I’ve ever ridden I got the chance to work with incredible people throughout the process. The ﬁrst one is Professor Eduardo Romero, whose vision, persistence, knowledge and will of one day transforming this country kept us persistent in every challenge, I’m really grateful of having the chance to work with him.

With my heart I must thank Charlems Alvarez, she was originally assigned as a Ph.D advisor for all this journey. However, this turned into true team work becoming one of my mentors. Her persistence, commitment to excellence and passion are a true inspiration. Apart from profesional and/or academic advice there were moments in which I had the chance to learn from her as a person. We pushed ahead in situations where we were drowning. After this ride I can only thank her for all and wish her the best of the careers, she truly deserves it.

To professor Fabio Gonz´alez who collaborated in two chapters of this thesis work. His advice, expertise and knowledge were key to approach these challenges.

To professor Marcela Iregui, she supported me throughout all this joruney and was always there pushing this work forward even from the shadows.

To my family with their constant support, patience and advice, I love them all and this work represents how grateful I am with everything I’ve received from them.

To Cim@Lab research group with their hard questions, constant feedback, support and friendships. I’ll keep with me every special moment we lived during this time: Jennifer, Charlems, Andres, Jorge, Diego, Miguel, Jose, Angela, Tatiana, Jully.

To my boyfriend - partner Andres Celis, whose unconditional help, support and love have been key to keep me going and to get to this point.

ix

## Abstract

Radiomics is a research ﬁeld in which features from radiological images are extracted to provide non-invasive but reliable quantiﬁcation with potential usage in personalized medicine. One of its applications is the extraction of sub-visual patterns, which are not commonly analyzed but have high correlation with pathology and require a speciﬁc representation to appear. As so, the state of the art has demonstrated the use of higher order transforms a.k.a the frequency domain to obtain such patterns. For this thesis work two use cases that beneﬁted from the use of the frequency domain for radiomic analysis are presented, these are, characterization of prostate cancer and autism spectrum disorder (ASD) from prostate and brain MRI respectively. In both cases gold standard diagnosis protocols do not involve the use of MRI but could beneﬁt from it, as in the case of Prostate Cancer an eﬀective characterization could help to triage prior to a biopsy procedure with tasks like tumor segmentation, classiﬁcation of normal vs cancerous tissue or automatic tumor staging. Additionally, for ASD an eﬀective characterization from MRI could help to contribute in the study of different manifestations of the spectrum. As a result three contributions in this matter were done: The ﬁrst one is an adaptive frequency saliency model (AFSM) that sparsely learns a bank of ﬁlters in the frequency domain and was used as a preprocessing strategy prior to a transfer learning scheme which classiﬁes cancerous vs healthy tissue in prostate MRI, this method obtains an accuracy of 0,792 ± 0,016 which yields better performance than a baseline experiment without preprocessing that scores 0,776 ± 0,036. The second one is a preliminary study that uses Fourier transform’s phase space to study the spatial support of prostate cancerous versus non cancerous tissue. This strategy consisted in a random selection of one subject per class, then, the dataset is preprocessed by replacing the phase of each image by the one of the random selected subject obtaining diﬀerent preprocessed datasets, and, ﬁnally transfer learning models are obtained. Results from this study suggested how spatial support is important for model training. Additionally, a classiﬁcation improvement was observed when a healthy subject was used for preprocessing obtaining sensitivity and speciﬁcity of 0,77 and 0,80 respectively, against a baseline that obtains 0,69 and 0,80 for both metrics. As a third contribution of this thesis, two characterization strategies to diﬀerentiate between ASD and control subjects are proposed, these are: Zernike moments and Curvelet Transform under a region-wise analysis. Anatomical brain regions were repersented by a 2D multi slice mapping to analyze ﬁrst and second order relationships. Both characterization strategies were evaluated under a 10 fold cross validation scheme with children cohorts from the heterogeneous datasets ABIDE I and II. Top performance regions for area under the reciever-operating curve (AUC) were: Left supramarginal gyrus (0,77), Right occipital fusiform cortex (0,76), Right supramarginal gyrus - anterior division (0,75) and Left superior temporal gyrus anterior division (0,77). Additionally the Curvelet approach presented generalizability as a hold out experiment was able to yield an AUC of 0,69 for the Right parahippocampal gyrus - posterior division. This representation also showed no correlation

x

with other state of the art techniques representing a contribution to ASD characterization with structural MRI.

Keywords: Radiomics, Prostate Cancer, Convolutional neural networks, Frequency Domain, Autism Spectrum Disorder, Magnetic Resonance Imaging, Deep Learning, Curvelet Transform, Zenike Moments, Fourier Transform.

xi

## Resumen

Radio´mica es un a´rea de investigacio´n en la que se extraen patrones de im´agenes radiol´ogicas con el objetivo de lograr una cuantiﬁcacio´n no invasiva y conﬁable con usos potenciales en medicina personalizada. Una aplicacio´n comu´n es la extracci´on de patrones sub-visuales; ´estos, no son f´aciles de apreciar o analizar en campo y requieren de un cambio de dominio para poderlos apreciar. El estado del arte en el ´area ha demostrado c´omo el uso de transformaciones de alto orden tambi´en nombradas en la literatura como representaciones frecuenciales son aptas para obtener patrones sub-visuales, de manera que ´este trabajo de tesis se enfoco´ en la aplicaci´on de radi´omica utilizando el dominio de la frecuencia para dos casos de estudio: caracterizacio´n de cancer de pro´stata y trastorno del espectro autista (TEA) a partir de ima´genes de resonancia magn´etica estructural de pr´ostata y cerebro. El protocolo esta´ndar de diagno´stico para ambos casos no incluye la toma de resonancia magn´etica, sin embargo una caracterizacio´n adecuada de esta fuente de informacio´n no invasiva puede traer ventajas sustanciales como por ejemplo en el caso de cancer de pr´ostata, servir de triage antes de un procedimiento de biopsia transrectal realizando tareas como segmentaci´on de tumores, clasiﬁcacio´n de tejido sano vs c´ancer o deteccio´n de la agresividad del ca´ncer en tejido. Mientras que en el caso del TEA esta caracterizaci´on contribuye al estudio de diferentes manifestaciones del espectro autista. Como resultado tres contribuciones se realizaron: La primera es un m´etodo adaptativo de saliencia en el dominio de la frecuencia (AFSM) que de manera sparse aprende un banco de ﬁltros en el dominio de la frecuencia y se utilizo´ como estrategia de preprocesamiento previo a la clasiﬁcacio´n via transfer learning entre tejido sano y cancer. Este m´etodo obtiene un accuracy de 0,792 ± 0,016 superando una l´ınea de base que obtiene 0,776 ± 0,036. La segunda contribuci´on es un estudio preliminar que utiliza el espacio de fase de la transformada de Fourier para para estudiar el soporte espacial de tejido canceroso y no canceroso en resonancia de pr´ostata. Esta estrategia consiste en la seleccio´n de un sujeto aleatorio por clase, luego, la base de datos se preprocesa reemplazando la fase de todos los sujetos por la de cada sujeto escogido de manera aleatoria, obteniendo versiones modiﬁcadas de la base de datos que son sometidas a un esquema de clasiﬁcaci´on utilizando transfer learning. Los resultados de este trabajo sugieren co´mo el soporte espacial es importante en el entranamiento de cualquier modelo. Adicionalmente, se observ´o una mejora en clasiﬁcacio´n cuando se utilizo´ tejido sano en el preprocesamiento, es decir, mejora de una lı´nea de base con sensibilidad y especiﬁcidad de 0,69 y 0,80 respectivamente, a 0,77 0,80 en las im´agenes preprocesadas. Como u´ltima contribucio´n, se propusieron dos estrategias de caracterizacio´n para diferencias entre sujetos con TEA y control en imagen de resonancia, estas fueron: momentos de Zernike y transformada Curvelet. Ambas estrategias se realizaron bajo una representaci´on 2D de cada regio´n cerebral y fueron evaluadas utilizando validaci´on cruzada 10 fold en dos cohortes infantiles de las bases de datos ABIDE I y II. Las regiones con mejor rendimiento en la m´etrica Area´ bajo la curva ROC (AUC) fueron: giro supramarginal izquierdo (0,77), corteza fusiforme occipital derecha (0,76), giro supramarginal derecho

xii

- - divisi´on anterior (0,75) y giro temporal superior izquierdo - diviso´n anterior (0,77). Adicional a esto, el enfoque con la transformada Curvelet presento´ generalizacio´n obteniendo un AUC de 0,69 para un experimento hold out en la regi´on: giro parahipocampal derecho
- - divisi´on posterior. Adema´s, esta repesentaci´on no mostr´o ning´un tipo de correlacio´n con otras t´ecnicas del estado del arte, representando una contribucio´n al estado del arte en el a´rea.

Palabras clave: Radio´mica, Ca´ncer de Pro´stata, Redes Neuronales Convolucionales, Dominio de la frecuencia, Trastorno del espectro Autista, Resonancia Magn´etica, Deep Learning, Transformada Curvelet, Momentos de Zenike, Transformada de Fourier.

Esta tesis de maestría se sustentó el 27 de septiembre de 2021 a las 08:00 AM, y fue evaluada por los siguientes jurados:

John William Branch Bedoya (Ph.D.) Universidad Nacional de Colombia sede Medellín

Jairo Jose Espinosa Oviedo (Ph.D.) Universidad Nacional de Colombia sede Medellín

# Contents

Acknowledgments VII Abstract IX

- 1. Introduction 1

- 1.1. Radiomics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
- 1.2. Prostate Cancer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 1.3. Autism Spectrum Disorder . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 1.4. Contribution and Academic products . . . . . . . . . . . . . . . . . . . . . . 8
- 1.5. Thesis outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

- 2. Adaptive frequency saliency model based on CNN 11

- 2.1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 2.2. Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

- 2.2.1. Feature extraction: Adaptive Frequency Saliency Model . . . . . . . . 13
- 2.2.2. Transfer Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

2.3. Evaluation and Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

- 2.3.1. Case of study: Prostate Cancer Data . . . . . . . . . . . . . . . . . . 15

- 2.4. Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

- 2.3.2. Data Augmentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
- 2.3.3. Experimental setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
- 2.3.4. Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

- 3. Uncovering patterns in PCa MRI by Using FT Phase Space 20

- 3.1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
- 3.2. Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

- 3.2.1. Phase Estimator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- 3.2.2. Transfer Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

3.3. Evaluation and Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

- 3.3.1. Case of study: Prostate Cancer Data . . . . . . . . . . . . . . . . . . 24

- 3.3.2. Data Augmentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 3.3.3. Experimental setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
- 3.3.4. Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

xiv Contents

- 3.4. Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

- 4. ASD Characterization by Decomposing MRI Brain Regions with ZM 29

4.1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

- 4.2. Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

- 4.2.1. Pre-processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
- 4.2.2. Registration and segmentation . . . . . . . . . . . . . . . . . . . . . . 32
- 4.2.3. Anatomic Region representation and Collage . . . . . . . . . . . . . . 32
- 4.2.4. Region-based characterization: Zernike Moments . . . . . . . . . . . . 33
- 4.2.5. Classiﬁer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

- 4.3. Experiments and results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

- 4.3.1. Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
- 4.3.2. Registration and segmentation . . . . . . . . . . . . . . . . . . . . . . 35
- 4.3.3. Region-based characterization: Zernike Moments . . . . . . . . . . . . 36
- 4.3.4. Classiﬁer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

- 4.4. Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
- 4.5. Conclusions and future work . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

- 5. ASD characterization in children by capturing local-regional changes 40

- 5.1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
- 5.2. Materials and Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

- 5.2.1. Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
- 5.2.2. Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
- 5.2.3. Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47

- 5.3. Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

- 5.3.1. Experiment 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
- 5.3.2. Experiment 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
- 5.3.3. Experiment 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
- 5.3.4. Experiment 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
- 5.3.5. Computational performance . . . . . . . . . . . . . . . . . . . . . . . 55

- 5.4. Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
- 5.5. Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

6. Conclusions and perspectives 61

- 6.1. Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61 6.2. Future work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62

A. Appendix: Diﬀerentiating Cancerous and Non-cancerous Prostate Tissue Using Multi-scale Texture Analysis on MRI 63

- A.1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
- A.2. Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

Contents xv

- A.3. Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

- A.3.1. Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
- A.3.2. Experimental setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

- A.4. Results and Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
- A.5. Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70 Bibliografı´a 71

# List of Figures

- 1-1. Radiomics pipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
- 2-1. Adaptive frequency saliency model (AFSM) pipeline . . . . . . . . . . . . . . 13

- 2-2. Transfer learning: Inception V3 Architecture . . . . . . . . . . . . . . . . . . 14
- 2-3. Experimental setup for testing AFSM using transfer learning . . . . . . . . . 17
- 2-4. Qualitative results using AFSM . . . . . . . . . . . . . . . . . . . . . . . . . 17
- 2-5. Quantitative results of transfer learning tests with and without using AFSM 18

- 3-1. Pipeline for selecting representative subjects . . . . . . . . . . . . . . . . . . 22

- 3-2. Pipeline for phase preprocessing using representative subjects . . . . . . . . 22
- 3-3. Transfer learning pipeline and Inception V3 architecture . . . . . . . . . . . 23
- 3-4. Pipeline of statistic analysis of phase per class . . . . . . . . . . . . . . . . . 26
- 3-5. Qualitative results of preprocessing with the proposed phase strategy . . . . 26
- 3-6. Results of statistic analysis of phase per class . . . . . . . . . . . . . . . . . 27

- 4-1. Zernike characterization pipeline . . . . . . . . . . . . . . . . . . . . . . . . . 32

- 4-2. Example of proposed 2D multislice construction of a brain region . . . . . . 33
- 4-3. Polar plot of zernike space characterization for a control and an ASD subject in the Right Frontal Orbital Cortex . . . . . . . . . . . . . . . . . . . . . . . 37
- 4-4. Area under the curve of top performing regions in the classiﬁcation task . . . 39

- 5-1. Curvelet-based pipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

- 5-2. Brain region description given the 2D multislice image representation . . . . 45
- 5-3. Classiﬁcation results when the model is trained with ABIDE II sample and tested using ABIDE I sample . . . . . . . . . . . . . . . . . . . . . . . . . . 49
- 5-4. Discriminant regions when evaluating the proposed multiscale descriptor with the ABIDE I sample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
- 5-5. Discriminant regions when evaluating the proposed approach with the ABIDE II sample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
- 5-6. Visualization of the highlighted diﬀerences between ASD and control subjects 52
- 5-7. Curvelet-based feature analysis . . . . . . . . . . . . . . . . . . . . . . . . . 54
- 5-8. Relationship between Curvelet-based sub-bands and classical measures . . . 56

List of Figures xvii

- A-1. Characterization pipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
- A-2. Feature reduction results in the Curvelet space . . . . . . . . . . . . . . . . . 67

# List of Tables

1-1. Prostate classiﬁcation, state of the art techniques and performance . . . . . . 5

- 3-1. Classiﬁcation performance comparison between baseline and the proposed phase preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
- 4-1. ABIDE I cohort description . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

- 4-2. ABIDE II cohort description . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
- 4-3. Overlap analysis of elastic registration for ABIDE I cohort subjects . . . . . 36
- 4-4. Overlap analysis of elastic registration for ABIDE II cohort subjects . . . . . 36
- 4-5. Classiﬁcation results with the proposed Zernike characterization strategy . . 38

- 5-1. Data description: ABIDE I and II samples . . . . . . . . . . . . . . . . . . . 43

- 5-2. Classiﬁcation performance comparison: Voxel based morphometry against the proposed approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
- 5-3. Classiﬁcation performance comparison: State of the art against the proposed approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

- A-1. Classiﬁcation results for the proposed Curvelet characterization . . . . . . . 68
- A-2. Classiﬁcation results when using other state of the art features: radiomics and convolutional neural networks . . . . . . . . . . . . . . . . . . . . . . . . . . 69

# 1. Introduction

### 1.1. Radiomics

Currently, research on medical imaging aims to use computational methods and extensive mathematical tools to calculate descriptors for a given image (e.g. Computed Tomography - CT, Magnetic Resonance Imaging - MRI or Positron Emission Tomography - PET), and correlate them with medical ﬁndings or patient outcomes. As a result, models generated using such descriptors are able to perform tasks like prognosis, diagnosis or prediction on speciﬁc medical conditions. This whole process is what is known as radiomics, a research ﬁeld in which patterns from radiological images are extracted to provide non-invasive but reliable quantiﬁcation with potential usage in personalized medicine1,59,167.

As illustrated in Figure 1-1, for extracting radiomic descriptors, a common pipeline consists in four main steps: 1) image acquisition, 2) ROI extraction, 3) feature engineering that includes feature extraction and reduction, and 4) modelling.

|1. Image Acquisition| |
|---|---|
| | |

|2. ROI Extraction| |
|---|---|
| | |

|3. Feature Engineering| |
|---|---|
| | |

|4. Modelling|
|---|

|3A. Feature Extraction|
|---|

|3B. Feature Reduction|
|---|

|4A. Feature Analysis|
|---|

|Supervised Methods|
|---|

|Intensity Based Features|
|---|

|Shape Features|
|---|

|Unsupervised Methods|
|---|

|Texture Features|
|---|

|Higher Order<br><br>Features|
|---|

|Deep Learning|
|---|

Figure 1-1.: Radiomics pipeline, and state of the art methods for feature extraction and

feature reduction.

In the ﬁrst step, radiological images are captured and inspected by expert radiologists to provide qualitative description of medical ﬁndings. Then, regions of interest (ROI’s) are annotated by experts and extracted for further analysis. After that, radiomic descriptors are extracted, and often selected for reducing dimensionality, to correlate them with medical ﬁndings. The most common descriptors are intensity level features31,94,168, shape-based features35,81,81,130,130,143, texture features16,65,122,162, high-order features29,78,115, and deep learning strategies1,10,26,166. Finally in the modelling step, machine learning models are trained or statistical analyses are performed for evaluating how useful these descriptors are at predicting clinical ﬁndings, i.e., diagnosis or prognosis in speciﬁc cases of study.

Speciﬁcally, regarding feature engineering, a detailed description of each feature type is hereafter presented. Regarding intensity level features, they provide a probability estimation of gray level intensities of a given image or ROI. Examples of this feature type include histograms and calculations from those histograms such as statistical moments. For instance, Corino et. al31 aimed to distinguish intermediate from high level soft tissue sarcoma in DWI images by computing statistical moments upon gray level histograms. Zhang et. al168 directly used the gray level histogram of ROIs in brain MRI, speciﬁcally T1-weighted, T2-weighted and ADC modalities, to provide statistically signiﬁcant diﬀerences between diﬀerent grades of gliomas. In addition, current applications such as characterization of hepatocellular carcinoma (HCC) have also used these features by relating histograms of parameters in functional multi-parametric MRI, including DWI, blood oxygenation level-dependent (BOLD), tissue oxygenation level-dependent (TOLD), and dynamic contrast-enhanced (DCE)-MRI, to ﬁnd out that those measures correlate with molecular characteristics of HCC68,94.

Shape-based features describe a given region of interest to quantify its geometry and have been used for instance to compare tumors in brain or prostate cancers, providing a descriptor able to identify malignant versus healthy tissue or to stage tumor severity. Such features could be extracted in 2D or 3D spaces as well, and the most common ones are volume, thickness, compactness, diameter, and eccentricity1. For instance, Cuocolo et. al35 used these features to characterize prostate cancer, quantifying diﬀerences between clinically signiﬁcant and nonsigniﬁcant lesions by measuring the surface area. Similarly, shape features have also been used to study complex neuro-developmental conditions such as Autism Spectrum Disorder (ASD) through MRI analysis. In such case, voxel based morphometry has been widely used to compute measures such as cortical thickness, volume or surface area81,130,143, which are studied to ﬁnd diﬀerences in brain regions across ASD and control individuals.

Texture features are able to describe local-regional spatial relationships between pixels. For instance, the co-occurrence matrix estimates the joint probability of a voxel I(x,y) to change its intensity to I(x + ∆,y + ∆) with distance ∆ on an angle θ. In particular, Haralick features use co-occurrence matrices to compute moments such as contrast, entropy, heterogeneity and correlation66. These features have been used for instance on brain, prostate

1.1 Radiomics 3

and lung applications. Han et al.65 demonstrated the potential of using Haralick features, from gray level co-ocurrence matrices (GLCM) and gray level run length features (GLRLM), to distinguish brain inﬂammation from grade II glioma in population without contrast enhancement. Similarly, Nketiah et al.122 and Wibmer et al.162 demonstrated the correlation of Haralick features with prostate cancer aggressiveness. Finally, Beig et a.l16 used Gabor ﬁlters to diﬀerentiate granuloma from adenocarcinoma in lung CT images.

Higher-order features involve computing transformations or changing signals domain to obtain relevant information by analyzing a given image in the transformed target space. Such transforms are able to decompose the signal into a set of coeﬃcients that when analyzed independently are able to describe diﬀerent order features at once, i.e., texture, shape and local relationships. Common strategies of this kind of descriptors are the Fourier, Wavelet and Curvelet transforms. The Curvelet transform has been used to provide a feature space able to detect brain tumors in MRI with high accuracy78. In the case of the Wavelet transform, it has been used to characterize colorectal cancer in MRI, for instance, Chaddad et. al27 found out how features based on this representation correlated with cancer progression. In addition, Meselhy et. al115 compared features extracted using the Wavelet and Curvelet transforms under the task of diﬀerentiating benign tumors, malignant toumors and normal tissue in mammographies, showing improved classiﬁcation accuracy when using Curveletbased features.

In the case of deep learning, a common approach is to let a model train from scratch or by means of transfer learning, depending on dataset size. Then, features are extracted from their responsible layer for further analyses. An advantage of this approach is that network training might be able to provide a rich feature space that can relate to a mix of diﬀerent order radiomic features. However, a solid interpretation of the resultant space is still an open problem in which class activation maps (CAM) or grad-CAM algorithms appear as possible solutions126,157,166. Nevertheless, implementations of such algorithms are still not standard, i.e., some grad-CAM implementations set probabilities to convolutional layers whereas other ones just use the last convolutional layer to provide such interpretation in the image space166. For instance, Ye et al.166 analyzed and classiﬁed chest X-rays (from the public dataset Chexnet-14) in 14 diﬀerent radiologic conditions. This work also proposed an interpretation algorithm based on class activation maps with a probabilistic approach to guide better lesion localization and interpretation of the network at inference. Similarly, in prostate cancer detection from MRI, neural networks have also been used10,26 to detect clinically signiﬁcant versus non-signiﬁcant cancer, speciﬁcally from scratch training or transfer learning.

As the second main part of feature engineering, since in some cases radiomic features are in a high dimensional and redundant space, a feature selection process is used to reduce a given feature space and preserve only the most descriptive ones. The state of the art deﬁnes three criteria to perform such reduction: i) reproducibility, ii) informativeness, and iii)

redundancy1. Reproducibility describes radiomic features as stable i.e., invariant to diﬀerent image captures or noise sources. The second one, informativeness, is described as selecting features that are related with a target variable such as a particular class or outcome. Finally, redundancy is related with high correlation of informative features. Radiomic feature sets are therefore not intended to have highly redundant features.

Supervised and unsupervised methods are used to achieve these three conditions for feature spaces. In the case of supervised methods, ﬁltering methods are able to test, one feature at once, its relationship with a target variable. Examples of these methods are ﬁsher score (FSCR), Wilcoxon rank sum test, Gini index (GINI), mutual information feature selection (MIFS), maximum relevance minimum redundancy (MRMR), and Student t-test. Even though ﬁltering methods are able to reduce feature spaces to get the most informative features, they are commonly limited to leave some redundancy, so, to overcome this problem wrapper methods like greedy forward selection or greedy forward elimination appeared. In these methods, a new set is created and each feature is tested for informativeness, the most informative one is added to the new set, then the same test is performed and a correlation test is carried out between the candidate feature and the one that is about to be added to the new space to avoid high redundancy in the resultant set. In the case of unsupervised methods, their core objective is to reduce redundant features rather than obtaining informativeness as target variables are not available. For this case methods can be linear or non-linear, in that sense, common linear methods include principal component analysis (PCA), multidimensional scaling (MDS), and non-linear methods include isometric mapping and locally linear embedding (LLE)1,88,113.

### 1.2. Prostate Cancer

Prostate cancer (PCa) is the most commonly diagnosed cancer type in men and the second with the highest morbidity in males118. Its diagnosis starts with a suspicion due to higher levels of prostate-speciﬁc antigens (PSA) in routine rectal exams. Secondly, a digital rectum examination is performed, and ﬁnally a transrectal ultrasound guided biopsy is taken and analyzed to stage aggressiveness and to provide treatment. Although biopsy, the gold standard test, tends to be sensitive to tumor detection, it is prone to false negative results142 as during this procedure the needle could miss the most aggressive part of a cancer or detect a non-signiﬁcant part of aﬀected tissue. In this sense, non-invasive methods like magnetic resonance imaging (MRI) are explored to guide this procedure or to triage a patient prior to biopsy procedure.

1.2 Prostate Cancer 5

The role of such non-invasive methods has been discussed so far. For instance, Haﬀner et al.64 studied the diﬀerence between a common biopsy procedure and capturing a MRI image before biopsy on 555 patients. These experiments ended in statistically signiﬁcant diﬀerences (p−value ≤ 0,001) with an improvement up to 16% in detecting prostate cancers with Gleason 4-5. As a consequence, automatic image processing methods have been tried for diﬀerent tasks such as segmentation, classiﬁcation of cancerous vs healthy tissue, or to stage between clinically signiﬁcant vs non-signiﬁcant cancers. In the case of diﬀerentiating signiﬁcant versus non-signiﬁcant cancer, Castillo et al.26 performed a systematic literature review using more than 1000 articles. After selection criteria, only 27 were used and found to resolve the problem. The preferred image modalities were ADC map (93%), T2W (81%), DCE (52%). These studies used a variety of machine learning techniques, as presented in Table 1.2.

|Technique|AUC|
|---|---|
|Radiomic features + SVM|0.91|
|Radiomic features + Linear mixed model|0.89|
|Radiomic features + k-nearest neighbour<br><br>|0.87|
|Radiomic features + Neural networks<br><br>|0.81|
|Convolutional Neural Network (CNN)<br><br>|0.80|
|Radiomic features + Random forest|0.80|
|Radiomic features + Logistic regression|0.79|
|Radiomic features + LDA|0.74|

Table 1-1.: State of the art techniques and results in classiﬁcation of signiﬁcant versus non

signiﬁcant cancer in prostate MRI

Other works have tried to classify between multiple Gleason scores. For instance, Wibmer et al.162 performed an analysis using 147 T2W images and their respective ADC maps. From these images, prostate cancer lesions were segmented and characterized using Haralick descriptors like entropy, energy, correlation, homogeneity and inertia. Classiﬁcation task between Gleason 3+3, 3+4 and greater than 7 was performed, providing results of statistically signiﬁcant diﬀerence for energy and correlation features of ADC maps. Similarly, Nketiah et al.122 performed the analysis using 26 multi-parametric scans in which a region of interest was segmented by an expert, and Haralick features were computed for T2W, KTrans and ADC modalities, to identify diﬀerences between Gleason 3+4 and 4+3.

Access to data used in these studies is pretty diﬃcult, due to data being captured by the same research group or corresponded to allied private data sources. However, in 2017, the ProstateX challenge was launched and with it the public dataset ProstateX101. Main aim of this challenge was to perform two tasks, i) classifying between clinically signiﬁcant vs

non-signiﬁcant cancer, and ii) classifying between cancer aggressiveness in scale (1 − 5). Challenge submissions provided results of AUC ranging between 0,45-0,87 for the ﬁrst task, and between 0,24-0,27 for the second one10, being Convolutional Neural Networks the most used approach to solve these tasks. This leaves some open problems like how to improve classiﬁcation methods and how to eﬀectively characterize prostate cancer via MRI.

### 1.3. Autism Spectrum Disorder

Autism spectrum disorder (ASD) is a neuro-developmental condition that commonly aﬀects 1 per 54 children85. Any person with ASD may experience one or more of these characteristic signs: i) social interaction diﬃculties, ii) stereotyped behaviours, and iii) language skills problems. ASD is commonly diagnosed by following the Diagnostic and Statistical Manual of Mental Disorders (DSM-V)116 protocol which includes the autism diagnostic observation schedule (ADOs)108 and the autism diagnostic interview – revised (ADI-R)135

- as gold-standard assessment package. This evaluation is composed by a battery of neuropsychological tests able to stage the most characteristics signs of ASD and a protocol of interviews, which provide a ﬁnal decision. Although this process may be able to identify ASD signs, it is subjective and may lead to late diagnoses in some cases2,12. In that sense, other sings of the disease are being studied speciﬁcally using brain Magnetic Resonance Imaging, as it is a non-invasive method which may provide useful information that might lead to better understanding of the disease and therefore, faster diagnosis times due to quantitative methods to support it81.

Brain patterns in ASD have been studied in post-mortem subjects and functional resonance imaging, suggesting anatomical diﬀerences in regions like hippocampus, amygdala, entorhinal cortex, frontal and temporal cortices7,14,33. This has allowed researchers to seek for patterns in structural magnetic resonance imaging that may correlate with such ﬁndings138. Those studies have mainly used voxel based morphometry and texture characterizations to ﬁnd patterns in brain regions to establish diﬀerences between control and ASD subjects. In addition, a combination of morphometric features and neural networks have also been tried to contribute to this research ﬁeld.

Regarding voxel based morphometry, Katuwal et al.81 presented an approach using voxel based morphometry and diﬀerent classiﬁcation models (SVM, Boosting and Random Forest), obtaining accuracy ranging (75%−90%) for a single center, and 60% on a multi-center study (on the heterogeneous public ABIDE I dataset). Important changes were observed in regions such as frontal, parietal/temporal lobes and cerebellum. Similarly, Retico et al.130 used voxel based morphometry features to classify on a small dataset captured at their study center, obtaining an AUC of 0,74 and 0,68 for male and female populations respectively, and after

1.3 Autism Spectrum Disorder 7

a subject selection using the NVIQ ≥ 0,70, results boosts up to 0,81 − 0,72. Regions that exhibited best classiﬁcation score were: medial orbifrontal cortex, middle temporal gyrus pars triangularis, posterior cingulate cortex, transverse temporal gyrus, medial orbifrontal cortex and insula pars opecularis. A more recent work is the one from Shen et al.143 that used a homogeneously captured dataset from UC Davis MIND Institute Autism Phenome Project. This study characterizes each subject with measures such as cerebral volume, intracranial volume and extra-axial CSF, which are normalized per subject and corrected using age and sex. A RUS-Boost algorithm was trained, obtaining 0,83 of sensitivity and 0,65 of speciﬁcity.

With respect to texture analysis, Chaddad et al.29 utilized a texture quantiﬁcation over a multi-scale LoG ﬁlter (Laplacian of Gaussian ﬁlter). After a region characterization and statistical analysis, this work found statistically signiﬁcant diﬀerences (p − value ≤ 0,05) in regions such as: left and right cerebellar white matter, right hippocampus, left choroidplexus, and posterior corpus callosum. This work was followed-up by analyzing two particular relevant regions, the hyppocampus and the amygdala, using gray level co-occurrence matrices28. This characterization was done on two small cohorts of ABIDE I composed by 28 subjects from the UM center and 36 subjects of the Pitt center, both with acquisition of 1×1×1mm voxel size. Texture features for the hippocampus yielded an accuracy of 67,85% for the ﬁrst cohort, and for the second one this measure increased to 75%. Finally, in the case of the amygdala none of the cohorts was able to classify the disease with an accuracy better than 50% by using the proposed characterization. Another approach is the one presented by Sen et al.140, which combines structural and functional MRIs to perform subject classiﬁcation of ASD versus control subjects. A feature extraction method from the whole MRI volume is proposed by using an autoencoder that is able to learn a set of 3D ﬁlters. Filtering parameters are used in a convolutional neural network classiﬁer, and a hold out validation using the ABIDE I dataset was performed, resulting in sensitivity and speciﬁcity of 0,49 and 0,73 respectively for structural MRI, and 0,68 and 0,60 when combining both sources of information.

In the case of a combination of voxel based morphometry and neural networks, Kong. et al86 used voxel based morphometry to capture gray matter volume per region, and then generate a connectivity matrix between a given region and all regions from the same hemisphere, this allows to build a feature vector of nearly 10878 features per subject, and these features are classiﬁed by means of a three layer neural network. This strategy yielded a sensitivity of 0,84, speciﬁcity of 0,96 and AUC of 0,97. Note these results were obtained using a single center of the dataset ABIDE I, speciﬁcally, the NYU center. Another related contribution is the one made by Hazlett et al.67, which also used voxel based morphometry with neural networks. In this case, three morphological features were computed (cortical thickness, intra-cranial volume and surface volume) and then corrected by using the age of each subject. These features became as input of a three layer neural network, providing a a sensitivity of 0,88

and speciﬁcity of 0,95. This study was done in a multi-center dataset captured from the NIH-funded Autism Centers of Excellence (ACE) network study, referred to as the ‘Infant Brain Imaging Study’. This dataset was captured in the same machine and with the same conditions for all centers, i.e., it corresponds to a homogeneous dataset.

In summary, state of the art techniques to characterize ASD suggest diﬀerent results when using homogeneous and heterogeneous (multi-site) datasets41,42, which leaves the questions of how to eﬀectively quantify diﬀerences between the two groups, but moreover, how to construct generalizable models that manage to accurately separate ASD and control subjects in heterogeneous datasets.

### 1.4. Contribution and Academic products

Diagnosis of prostate cancer or autism spectrum disorder are not reached by radiological analysis. In fact, in the ﬁrst case, this is achieved by a biopsy procedure to stage the tumor, whereas in the ASD case, diagnosis depends on certain neuro-psychological tests and interviews. During the last years, radiology in case of prostate cancer has been used as a triage to the biopsy procedure, and in ASD to understand diﬀerent patterns of the disease. In both cases the analysis is performed upon the visual information the radiologist detects, yet most of such evaluation is performed at the level of anatomic structures. The study of sub-visual radiological features or local characteristics are not part of the radiology analysis and they have been reported to characterize several pathological processes. These features, known as radiomics have provided imaging biomarkers for tumor localization, segmentation and aggressiveness classiﬁcation in prostate cancer, and correlation of these biomarkers with postmortem ﬁndings in ASD. Nevertheless, such studies are limited by the reduced number of cases when constructing machine learning models or low classiﬁcation performance when using heterogeneous data sets (images coming from diﬀerent centers and acquired from several machines), leaving room for improving disease characterization, i.e., to build generalized models to support medical diagnosis. Since state-of-the-art radiomics applications have shown how higher-order representations are able to provide patterns not easy to analyze in the MRI original domain, this thesis focused on studying this type of representations, speciﬁcally the frequency domain, for characterizing prostate cancer and ASD. Contributions of this thesis are:

An algorithm able to blend the beneﬁts of higher-order features, speciﬁcally the Fourier transform with deep learning strategies (CNNs), to estimate saliency in the frequency domain, with the aim of boosting classiﬁcation performance in diﬀerentiating prostate cancerous and healthy tissue on MRI.

1.4 Contribution and Academic products 9

A preliminary study of the phase information (computed by the Fourier transform), which highlights hidden structures in prostate cancerous and healthy tissue on MRI, showing how these tissue types have diﬀerent spatial supports that may be captured by a neural network.

Two characterization strategies, Zernike moments and Curvelet transform, to highlight brain fold diﬀerences between ASD and control individuals under a region-wise analysis. Anatomical brain regions were represented by a 2D multi-slice mapping to analyze ﬁrst- and second-order relationships. Curvelet-based strategy provided generalizability as consistent results were obtained when evaluating with an independent heterogeneous dataset.

###### Academic products

Results of this work were published in:

Nicol´as Mu´nera Garzo´n, Charlems Alvarez-Jimenez, Fabio Gonzalez, and Eduardo Romero. Adaptive frequency saliency model based on convolutional neural networks: a case study for prostate cancer MRI.¨In 15th International Symposium on Medical Information Processing and Analysis, vol. 11330, p. 113300B. International Society for Optics and Photonics, 2020.

Nicol´as Mu´nera, Javier Almeida, Charlems Alvarez,´ Nelson Velasco, and Eduardo Romero. Autism Spectrum Disorders (ASD) Characterization in Children by Decomposing MRI Brain Regions with Zernike Moments. In Sipaim–Miccai Biomedical Workshop, pp. 42-53. Springer, Cham, 2018.

Charlems Alvarez-Jimenez, Cristian Barrera, Nicol´as Munera, Satish E. Viswanath, and Eduardo Romero. Diﬀerentiating Cancerous and Non-cancerous Prostate Tissue Using Multi-scale Texture Analysis on MRI. In 2019 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), pp. 26952698. IEEE, 2019.

Charlems Alvarez-Jimenez, Nicol´as M´unera-Garzo´n, Maria A. Zuluaga, Nelson F. Velasco, and Eduardo Romero. Autism spectrum disorder characterization in children by capturing local-regional brain changes in MRI. Medical physics 47, no. 1 (2020): 119-131.

### 1.5. Thesis outline

The following chapters describe and present in detail four approaches that were done to contribute in both applications, Prostate Cancer Characterization and Autism Spectrum Disorder characterization as follows:

- Chapter 2: Adaptive frequency saliency model based on convolutional neural networks: a case study for prostate cancer is a contribution for the case of prostate cancer characterization. In this work a model able to learn an adaptive ﬁlter representation in Fourier’s space via back-propagation is presented to preprocess images before submitting them to a convolutional neural network prior to classiﬁcation of cancerous vs non cancerous tissue. Results of classiﬁcation show improved performance after using this method.

- Chapter 3: Uncovering patterns in prostate cancer MRI by using Fourier Transform’s phase space is a contribution based on the work of Oppenheim123. For this approach the phase space of prostate MRI is analyzed in order to obtain a representative spatial support able to highlight hidden structures in cancerous and healthy prostate cancer MRI. Processed images are then compared against a baseline and results of this contribution show classiﬁcation improvement in the set that was processed.

- Chapter 4: Autism spectrum disorder (ASD) characterization in children by decomposing MRI regions with Zernike moments presents a region wise analysis in the multi center heterogeneous datasets ABIDE I and II. This method represents each region in a 2D multislice image that is then characterized using Zernike moments. Subsets of children from ABIDE I and II are used separatedly to provide classiﬁcation results on par with the state of the art.

- Chapter 5: Autism spectrum disorder characterization in children by capturing local-regional brain changes in MRI extends the approach described in chapter 4 by performing the same analysis but this time with a multiscale representation i.e using higher order features, speciﬁcally the Curvelet transform. Classiﬁcation results for subsets of ABIDE I and II are shown and an experiment in which a classiﬁer was trained using the ABIDE II subset and tested on the ABIDE I set is also presented. Finally a region analysis comparing ﬁndings with the state of the art is discussed. Results were competitive with respect to the state of the art for multicenter heterogeneous classiﬁcation and characterization of ASD.

# 2. Adaptive frequency saliency model based on convolutional neural networks: A case study for prostate cancer

This chapter presents an adaptive frequency saliency model (AFSM) that works by sparsely learning a bank of ﬁlters in the frequency domain which maximizes the structural similarity index (SSIM) of the ﬁltered image against an input image. This model was used to boost classiﬁcation performance of healthy vs cancerous tissue in prostate magnetic resonance imaging (MRI) by using it as a pre-processing step prior to transfer learning training with convolutional neural networks (CNN). Results demonstrate a marginal improvement by beating a baseline accuracy of 0,776 ± 0,036 with a result of 0,792 ± 0,016 after the AFSM was used. A complete version of this chapter has been accepted for publication as a research article in the proceedings of 15th International Symposium on Medical Information Processing and Analysis (see reference57)

### 2.1. Introduction

Visual saliency simulates how human-beings gaze on objects that stand out from others, drawing the observer’s attention72. This concept has been widely applied to computer vision related problems, in which segmentation or identiﬁcation of relevant elements of a given scene may be needed. In consequence, models for detecting visual saliency have been mainly oriented to: i) account for depth information (RGBD saliency)51,121, ii) use low and high level features to compute saliency for a given set of objects (co-saliency detection)56,96,106 and iii) by means of temporal patterns on a video sequence63.

Regarding RGBD saliency models, low level features like color, luminance and texture are extracted and then combined with the depth channel of the image51. However this technique relies on the quality of the required depth map, that in some cases is enhanced by means of

a depth contrast feature121. With respect to co-saliency methods, the multiple cue clustering (CCS) method56 creates groups of features where each one corresponds to a relevant region, obtaining then a saliency map. Another co-saliency approach consists in extracting features via graphs96 or comparing features via similarity metrics between relevant regions for a given set of images106. In addition, temporal features, extracted by strategies like the optical ﬂow and background/contrast priors63, can be added to obtain saliency models for video sequences.

The concept of saliency has been mainly explored to capture features from the image domain, but it may also be performed in the frequency. This latter domain was studied by Li et al.97 to improve saliency estimations, and phase spectrum is exploited since it stores where visual information is located. Frequency has been traditionally used to analyze complex patterns in many diﬀerent applications, and very likely it can be useful to ﬁnd out hierarchies and rare patterns in the image.

This article aims to demonstrate the ability of a novel adaptive frequency saliency model (AFSM) to capture relevant information by performing a sparse selection of frequencies. This selection is carried out by customizing an auto-encoder CNN that perform an optimal location of a bank of ﬁlters in the frequency space. The proposed method is challenged by a classiﬁcation task of prostate as cancerous and non-cancerous tissue in magnetic resonance imaging (MRI). Evaluation is carried out by training a particular convolutional neural network (CNN) with a dataset but the testing phase serves to compare the trained model applied to raw images and to images ﬁltered out by the bank of ﬁlters previously found with a small set of images from the two classes.

### 2.2. Methodology

The proposed strategy aims to extract relevant features and to construct a representation with the ability of capturing a set of patterns. The dimensionality reduction obtained by a linear autoencoder is used as the underlying criterion that places optimally a set of bandpass ﬁlters in the frequency space. This model is then used to improve the performance of a convolutional Neural Network (CNN) under a transfer learning paradigm. In such case, the proposed adaptive frequency saliency model (AFSM) acts as a custom autoencoder, setting the allowed frequency spectrum.

2.2 Methodology 13

##### 2.2.1. Feature extraction: Adaptive Frequency Saliency Model

Unlike denoising autoencoders, which learn to reconstruct a clean input from a corrupted signal version, the proposed strategy aims to improve the expressive power of frequency patterns as non linear features stacked when constructing the representation. The proposed strategy, the adaptive frequency saliency model (AFSM), uses the representation provided by the Fourier transform since the resultant patterns may be more interpretable in terms of a particular problem. The feature-extracting function, the encoder, corresponds to a bank of band-pass ﬁlters in the frequency space that selects information required to construct a similar version of the input in terms of the structural similarity index (SSIM). This cost function, the SSIM, drives the maximization of the structural similarity of the ﬁltered image under a particular setup of ﬁlters which should preserve relevant objects, and deal with global diﬀerences and changes rather than pixel-wise metrics. Frequency representation is here convenient for two main reasons: i) sparse selection on this domain decreases the representation trend to follow larger variance directions, and ii) frequency ﬁltering captures very basic features independently of topological locality constraints.

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

Backpropagation to each (𝜔𝑘,𝑢,𝜔𝑘,𝑣)

[Figure 6]

𝐹(𝜔𝑢,𝜔𝑣) 𝐻𝑘(𝜔𝑘,𝑢,𝜔𝑘,𝑣) 𝑆 = ෍

𝐼(𝑥,𝑦) 𝐼𝑟(𝑥,𝑦)

|[Figure 7]|
|---|
|[Figure 8]|

𝐹⨀𝐻𝑘

𝑘

[Figure 9]

[Figure 10]

|[Figure 11]<br><br>[Figure 12]<br><br>[Figure 13]<br><br>[Figure 14]<br><br>[Figure 15]|
|---|

[Figure 16]

[Figure 17]

[Figure 18]

| |
|---|

[Figure 19]

|[Figure 20]<br><br>[Figure 21]|
|---|

[Figure 22]

[Figure 23]

ℱ{𝐼}

=

[Figure 24]

|[Figure 25]|
|---|

ℱ−1 𝑆

[Figure 26]

𝑆𝑆𝐼𝑀(𝐼,𝐼𝑟)

Bank of n filters

|[Figure 27]|
|---|
|[Figure 28]|

[Figure 29]

Input Image

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

Frequency representation

Image Reconstruction

Filtering Cost function

Linear Combination

Figure 2-1.: Pipeline of the proposed adaptive frequency saliency model (AFSM). In this model, an image I(x,y) is mapped to frequency domain using the Fourier transform, obtaining the associated magnitude (||F||) and phase ( F) spectra. The bank of ﬁlters extracts frequency features representing relevant contents which are then back transformed to reconstruct the image. Note that structural similarity index (SSIM) is used as the cost function in back-propagation process.

The AFSM structure is illustrated in Fig. 2-1, in which the input image I(x,y) is mapped to the frequency domain using the Fourier transform, obtaining the associated magnitude (||F||) and phase ( F) spectra. The obtained magnitude is passed through the bank of bandpass ﬁlters Hk(ωk,u,ωk,v), where ωk,u and ωk,v stand for the 2D frequency space coordinates

of the k-th ﬁlter. A linear combination of all ﬁltered versions is then performed and the inverse Fourier transform is computed to reconstruct the input image Ir(x,y). Finally, a back-propagation process drives the displacement of ﬁlters in the frequency space, i.e., every ﬁlter location is changed to extract information that allows the best reconstruction of the input image.

The proposed model is setup with 17 ﬁlters, one static low-pass ﬁlter in the range (−π/4,π/4), and a set of 16 Gaussian band-pass ﬁlters with static width of (σ = π/4) and an initial random position in the frequency space. Back-propagation of the proposed model is setup with a set of 2000 iterations and a learning rate of 0,01. In this investigation, the idea is to perform a feature extraction per class, i.e., estimate a conﬁguration of a bank of band-pass ﬁlters that best represent the information of each class in a particular case of study.

##### 2.2.2. Transfer Learning

###### ImageNET’s pre-trained Inception V3149, a particular convolutional neural network (CNN) architecture, was selected to carry out all the classiﬁcation experiments. The structure of this architecture is illustrated in Fig. 2-2, being the last layer re-trained with images from a speciﬁc case of study, allowing the network to learn from data of new classes.

Training Set

Transfer

Learning

Inception V3 Architecture Convolution Max Pool Avg Pool Concat Dropout Fully Connected Softmax

✓X

Testing Set

Classiﬁcation

Prediction

Model

- Figure 2-2.: Transfer learning pipeline using the Inception V3 architecture: the training subset (70%) is used to re-train the last layer of the structure, providing a classiﬁcation model that is then assessed using the testing subset (30%).

For performing experiments, data is randomly split into 70/30 and two phases are performed: i) the ﬁrst set (70% of data) is used to re-train the last layer of the Inception V3 network, under a transfer learning approach, followed by a validation using a 10% of this data,

reserved to quantify training classiﬁcation performance, and ii) once a classiﬁcation model is obtained, it is assessed by predicting labels for each image of the second set (30% of data), obtaining a testing classiﬁcation measure for the trained model.

A transfer learning scheme is chosen for training, as current data quantity would easily allow to obtain an over-ﬁtted model by designing and training a network from scratch. In this investigation, the Inception V3 architecture was conﬁgured with a training batch of 64 images, 50 epochs, a learning rate of 0,01, and a testing batch size of 100 images.

### 2.3. Evaluation and Results

##### 2.3.1. Case of study: Prostate Cancer Data

The proposed adaptive frequency saliency model is tested using a particular case of study, a classiﬁcation of prostate as cancerous or non-cancerous tissue. Data, from The Cancer Imaging Archive (TCIA)100, contains T2 MRIs of 84 patients. For each patient, one or more lesions (tumors) have been annotated by experts, for a total of 95 lesions. Since each lesion is provided with a 3D coordinate indicating the center of the tumor (segmentation is not available), a 2D square prostate patch around such 3D coordinate is extracted from the MRI. This is done by ﬁrstly setting the slice at the z coordinate and then extracting a square ROI around this point in the orthogonal plane. Note this dataset includes inter-case diﬀerences in terms of image resolution, reason why the size of extracted patches is standardized according to image resolution, i.e., for an image of 320 × 320, a patch of 30 × 30 is extracted, and for an image of 640 × 640, a patch of 56 × 56 is likewise selected. Although patches are deﬁned according to speciﬁc sizes based on the image resolution, some patches could contain not only tumor but also peri-tumor information, which may also be important for disease characterization. Patches are similarly extracted from healthy locations in the prostate, for a total of 95 healthy patches and 95 cancerous patches.

Prostate cancer data is randomly split into 70% (135 patches) and 30% (54 patches) for training and testing respectively. Since this quantity of data is not appropriated for the use of a CNN, an augmentation process (consisting of image ﬂipping, rotating and scaling) is carried out on the training set, obtaining a set of 1200 images (600 per class).

##### 2.3.2. Data Augmentation

Linear transformations are used for data augmentation to improve classiﬁcation accuracy and algorithm convergence during training. These transformations are designed to simulate diﬀerent noise conditions likely to be present in prostate MRI such as subtle rotations (no more than 40º), translations (no more than 10% of patch size), and brightness changes (±20%). Additionally, it is possible for extracted patches to contain tissue variability, i.e., some patches may correspond to cancerous tissue, whereas for some other cases, they may also contain surrounding tissue. As so, a zoom transform (20% in or out) is used to simulate both cases for each extracted patch to enrich data variability.

##### 2.3.3. Experimental setup

Two experiments were carried out. The ﬁrst attempted to perform feature extraction, i.e., estimate the best conﬁguration of a bank of band-pass ﬁlters using the AFSM. For doing so, one patch of each class, cancerous and non-cancerous tissue, is selected and the AFSM is applied. The resulting conﬁgurations, one representing cancerous tissue and other representing non-cancerous tissue, are merged to obtain the Hm bank conﬁguration. The second experiment, illustrated in Fig. 2-3, aims to evaluate the usefulness of the proposed model at extracting relevant features to improve the performance in diﬀerentiating cancerous and non-cancerous tissue. This latter consists in building a CNN model using the training set, and performing two evaluations using the testing set: i) raw images and ii) ﬁltered images using the Hm bank conﬁguration. This process is carried out 20 times, resulting in 20 trained models that are tested using raw and ﬁltered images. Classiﬁcation performance is measured via accuracy metric.

##### 2.3.4. Results

Experiment 1 - Feature extraction: Fig.2-4 shows a bank conﬁguration using the AFSM for the selected patches, one representing healthy tissue (green) and one representing cancerous tissue (magenta). From left to right: the initial conﬁguration of the bank of band-pass ﬁlters, the associated bank conﬁguration for each selected patch, and the resultant Hm as the combination of both green and magenta setups. For each patch three elements are presented: i) original patch, ii) obtained bank conﬁguration after using the AFSM, and iii) SSIM score after using the bank conﬁguration obtained from such patch. In addition, although each bank conﬁguration does not cover the whole frequency space, the structural similarity index scores are not bellow 0,97, i.e. more than 90% of the structure of the image is still preserved

A) Classification using Raw Images B) Classification using Filtered Images

#### ✓X

[Figure 35]

✓X Classification

Testing Set

Filtering

Prediction (Filtered)

Model

Testing Set Prediction (Raw)

Classification Model

| |
|---|

| |
|---|

Patch per class Proposed AFSM

- Figure 2-3.: Workﬂow for the second experiment. The constructed classiﬁcation model is

assessed with: a) raw images, and b) ﬁltered images using the Hm bank conﬁguration.

after ﬁltering.

[Figure 36]

0.9767

Class: Healthy

0.9877

[Figure 37]

[Figure 38]

[Figure 39]

Class: Cancer

|[Figure 40]<br><br>Inital Bank Conﬁgura on|
|---|

Image

Bank

Conﬁgura on

SSIM

Image

Bank Conﬁgura on

SSIM

|Merged Conﬁgura on ( )<br><br>[Figure 41]|
|---|

- Figure 2-4.: Results when using the AFSM. On the left side, the initial bank setup is illustrated. In the center panel, a tissue patch per class is shown with its resultant bank conﬁguration and SSIM score. On the right side, the merged Hm bank conﬁguration is presented.

Experiment 2 - Classiﬁcation performance: For each of the 20 classiﬁcation models, two evaluations are performed, one with the raw images and one with the ﬁltered ones. These results are presented in Fig.2-5 (left side), in which the mean classiﬁcation accuracy is 0,776 ± 0,036 and 0,792 ± 0,016 for raw and ﬁltered images respectively, demonstrating a marginal improvement (p − value = 0,13) by applying the ﬁltering process.

###### Furthermore, the resultant bank conﬁguration Hm demonstrated to preserve relevant information (with ﬁlters passing certain frequencies) and reject image noise (with uncover parts in the frequency spectrum), increasing class separation in this particular case of study and improving stability by reducing the accuracy variability across tests.

###### Classiﬁcation Performance Training performance

1.0

Train Accuracy

0.82

0.9

0.8

0.8

Validation Accuracy Cross Entropy

Accuracy

0.7

0.78

Score

0.6

0.76

0.5

0.74

0.4

0.72

0.3

0.7

0.2

Raw Filtered

0

10 20 30 40 50 60

Epochs

- Figure 2-5.: Box-plots on the left illustrate a comparison when assessing the CNN classiﬁcation model with raw and ﬁltered images using the testing set. In this graph, blue represents classiﬁcation accuracy per test with raw images and green stands for the ﬁltered ones. Curves on the right side of the ﬁgure correspond to smoothed versions of performance measure taken during training on a particular model (Test 2), in which, training cost function (cross entropy) is presented in cyan, validation accuracy in dark magenta and training accuracy in gold.

Although CNNs are able to learn in noisy conditions and still provide reliable performance, it mostly happens when the training set is as heterogeneous to contain such situations enabling the model to generalize better. This statement makes interesting the performed experimentation, as, with fewer data, the ﬁltering process was able to improve the generalization performance using a model trained with a small dataset. Additionally, this lack of data can normally be evidenced as getting higher training accuracy scores rather than validation scores during training as presented on the curve on the right side of Fig.2-5.

### 2.4. Conclusions

This work introduced a model able to extract features from the frequency domain within a particular study case: classiﬁcation between cancerous and non-cancerous tissue. The use of the proposed model demonstrated the need of performing a pre-processing step previous to any classiﬁcation process, preserving the most relevant information in the image and

- 2.4 Conclusions 19

allowing to improve classiﬁcation performance. Future work includes the exploration of phase information to be included in the AFSM structure, i.e., ﬁnd out relevant features by allowing the ﬁlters to also modify the phase spectrum instead of just the magnitude one.

# 3. Uncovering patterns in Prostate Cancer MRI by Using Fourier Transformation Phase Space

This chapter presents a preliminary methodology able to manipulate the phase space of the Fourier Transform in order to study the spatial support of cancerous and non cancerous tissue in Prostate MRI. This method works by randomly selecting a subject per class, extract its phase by using the Fourier Transform and then pre-process the dataset using this phase. This pre-processing method was used to ﬁnd a representative phase of Cancer Gleason 5, Cancer gleason 3 and healthy. The three pre-processed datasets underwent a classiﬁcation scheme via a transfer learning approach. As a result, improved classiﬁcation performance was observed after the dataset was pre-processed using healthy tissue with sensitivity of 0,77, speciﬁcity of 0,80 and an accuracy of 0,78 in comparison with a baseline that obtains sensitivity of 0,69, speciﬁcity of 0,80 and an accuracy of 0,73.

### 3.1. Introduction

The Fourier Transformation is known as a decomposition of a given function into coeﬃcients that represent a given signal within the Fourier Series. Such decomposition is able to uncover rare patterns that are used in description of images in tasks like image classiﬁcation1, Saliency estimations98 and Super resolution133. On the former mentioned applications, the Fourier Transformation is mainly used for feature extraction prior to machine learning or in combination with deep learning methods i.e convolutional neural networks (CNN) or generative models. For instance Tancik et. al151 tackled the problem of low frequency estimation on generative models by proposing a model in which frequency patterns allow accurate reconstruction of images. Another application is in Pratt. et al128 in which a CNN architecture with convolutions transformed to the frequency domain is presented, as a result of this approach, similar performance to state-of-the-art methods was obtained with lower convergence times, concluding how those kind of applications may help to use higher resolution images inside a CNN architecture. These applications put into manifest how the Fourier Transform is able to

provide relevant information of a given image and how this information is useful in diﬀerent image processing tasks.

Back in the 80’s, Oppenheim123, published an article that stated how the phase spectrum of the Fourier Transform could be interpreted in the Image Domain as its spatial support. This means that phase alone is able to provide a description of the image in terms of an undetailed - coarse, yet very informative version of it. Whereas magnitude, clears noise provided by the phase reconstruction alone and provides ﬁnest detail when interpreted in the Image’s Domain.

An application of the Fourier Transform in the medical ﬁeld is magnetic resonance Imaging99 that is an inverse transformation of a tissue response to magnetic radio waves induced at diﬀerent frequencies. One hypothesis is that Normal or healthy tissue for a given organ captured in MRI should preserve some similar and organized structure a.k.a spatial support, whereas in abnormal tissues this support might present diﬀerences. So, in this work, the idea of understanding tissue’s spatial support on MRI is explored by presenting a Phase Spectrum estimator. Then, Phase estimation will be used to preprocess images for a given study case, and a comparison between the proposed approach against a baseline is done by a classiﬁcation scheme via a transfer learning approach.

### 3.2. Methodology

##### 3.2.1. Phase Estimator

To manipulate the phase spectrum of a set of images from a given dataset the following pipeline consisting in two steps is proposed: ﬁrst a small set composed by one subject per class is randomly selected, and then, a preprocessing strategy that uses the phase of this subjects is performed to obtain a processed version of the dataset.

###### Subject selection

For the ﬁrst step, subject representer selection, a pipeline is proposed as depicted in Figure 3-1. Firstly images from the dataset are separated per class, then a random small set of images is selected. Finally this subset of images is used for preprocessing using their phase from their frequency spectrum.

###### Images dataset

[Figure 42]

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

[Figure 49]

[Figure 50]

###### Class A Class B

Random selection of k images

[Figure 51]

[Figure 52]

[Figure 53]

Representers for class A

Representers for class B

- Figure 3-1.: Pipeline of the proposed phase estimator: Images from the dataset are separated per class, then a random set of k images per class is chosen to be used as representers.

###### Pre-processing using phase spectrum

###### 1) Representer phase:

###### 2) Dataset preprocessing:

a) Representer’s phase extraction:

a) Fourier transform b) Phase replacement

𝑅𝑖

ℱ−1

𝑅𝑖

𝑅𝑟

[Figure 54]

ℱ

[Figure 55]

ℱ

[Figure 56]

|𝜑𝑟|
|---|

𝜑𝑟

𝜑𝑖

- Figure 3-2.: Pipeline of the proposed pre-processing strategy built in two steps: from left to right in the ﬁrst step Representer phase, a subject from the subset obtained in 3.2.1 is transformed to the frequency domain to obtain its phase, then in the second step dataset pre-processing, each image of the dataset is transformed to the frequency domain to replace its phase to the one obtained in the ﬁrst step and then to transform back to the Image’s domain by means of the Inverse Fourier Transform

After obtaining a subset of images (representers) using the pipeline described in 3.2.1, each of these images is used to pre-process the dataset as described in Figure 3-2. This preprocessing strategy consists in two steps, in the ﬁrst one, an image (representer) is transformed to the frequency domain using the Fourier transform, then, in the second step, all the dataset is transformed to the frequency domain, and all the obtained phases are replaced with the one obtained in the ﬁrst step. After this replacement, the inverse Fourier transformation is computed to get back to the image’s space.

##### 3.2.2. Transfer Learning

Training Set

Transfer

Learning

Inception V3 Architecture Convolution Max Pool Avg Pool Concat Dropout Fully Connected Softmax

✓X

Testing Set

Classiﬁcation

Prediction

Model

Figure 3-3.: Transfer learning pipeline using the Inception V3 architecture: the training subset (70%) is used to re-train the last layer of the structure, providing a classiﬁcation model that is then assessed using the testing subset (30%).

ImageNET pre-trained InceptionV3149, a particular convolutional neural network (CNN) architecture, was selected to carry out all the classiﬁcation experiments. The structure of this architecture is illustrated in Fig. 3-3, being the last layer re-trained with images from a speciﬁc case of study, allowing the network to learn from data of new classes.

For performing experiments, data is randomly split into 70/30 and two phases are performed: i) the ﬁrst set (70% of data) is used to re-train the last layer of the Inception V3 network, under transfer learning approach, followed by a validation using a 10% of this data, reserved to quantify training classiﬁcation performance, and ii) once a classiﬁcation model is obtained, it is assessed by predicting labels for each image of the second set (30% of data), obtaining a testing classiﬁcation measure for the trained model.

In this investigation, the InceptionV3 architecture was conﬁgured with a training batch of 128 images, 50 epochs, a learning rate of 0,01, and a validation batch of 115 images.

### 3.3. Evaluation and Results

##### 3.3.1. Case of study: Prostate Cancer Data

The analysis using Fourier Transform phase space is tested using a particular case of study, a classiﬁcation of prostate as cancerous or non-cancerous tissue. Data, from The Cancer Imaging Archive (TCIA)100, contains T2 MRIs of 84 patients. For each patient, one or more lesions (tumors) have been annotated by experts, for a total of 95 lesions. Since each lesion is provided with a 3D coordinate indicating the center of the tumor (segmentation is not available), a 2D square prostate patch around such 3D coordinate is extracted from the MRI. This is done by ﬁrstly setting the slice at the z coordinate and then extracting a square ROI around this point in the orthogonal plane. Note this dataset includes inter-case diﬀerences in terms of image resolution, reason why the size of extracted patches is standardized according to image resolution, i.e., for an image of 320 × 320, a patch of 30 × 30 is extracted, and for an image of 640 × 640, a patch of 56 × 56 is likewise selected. Although patches are deﬁned according to speciﬁc sizes based on the image resolution, some patches could contain not only tumor but also peri-tumor information, which may also be important for disease characterization. Patches are similarly extracted from healthy locations in the prostate, for a total of 95 healthy patches and 95 cancerous patches.

Prostate cancer data is randomly split into 70% (135 patches) and 30% (54 patches) for training and testing respectively. Since this quantity of data is not appropriated for the use of a CNN, an augmentation process (consisting of image ﬂipping, rotating and scaling) is carried out on the training set, obtaining a set of 1200 images (600 per class).

##### 3.3.2. Data Augmentation

Linear transformations are used for data augmentation to improve classiﬁcation accuracy and algorithm convergence during training. These transformations are designed to simulate diﬀerent noise conditions likely to be present in prostate MRI such as subtle rotations (no more than 40º), translations (no more than 10% of patch size), and brightness changes (±20%). Additionally, it is possible for extracted patches to contain tissue variability, i.e., some patches may correspond to cancerous tissue, whereas for some other cases, they may also contain surrounding tissue. As so, a zoom transform (20% in or out) is used to simulate both cases for each extracted patch to enrich data variability.

##### 3.3.3. Experimental setup

Two experiments are carried out, the ﬁrst one estimates phase by using the approach explained in section 3.2.1. For this experiment, all images in the training set are used and a subset of three images is used as representers i.e, 2 patches for cancer class (cancer gleason 5 and cancer gleason 3) and one for the healthy class, obtaining three preprocessed datasets. For model training and comparison, each processed dataset is assessed via transfer learning with the Architecture InceptionV3 under the 70 − 30 scheme. This was implemented using Keras.

Hyper parameter optimization: multiple experiments on the non processed data-set (baseline) were carried out varying parameters such as learning rate, batch size, data augmentation and optimizer. The set of parameters that yielded best performance were chosen as follows: learning rate: 0.01, batch size: 386, augmentation: random translations, rotations, shears and lighting transformations, optimizer: stochastic gradient descent (SGD).

For the second experiment, an analysis of the Fourier’s phase space is done as illustrated in ﬁgure 3-4. All the dataset is used and split into each class (Cancer gleason 5, Cancer gleason 3, Cancer gleason 1, Healthy), then all images per class are analyzed as follows: ﬁrst, the Fourier Transform of each image Ic(x,y) is computed obtaining magnitude and phase spectra { ωc(u,v),φc(u,v) }. After that, all phases are stacked into an array of dimensions mxnxk where k is the number of images on the class c and m,n are the spatial resolution of each image. And ﬁnally the dimension k is reduced by computing mean and standard deviation per pixel obtaining two images µ(u,v),σ(u,v).

##### 3.3.4. Results

Experiment 1 - Phase estimation and classiﬁcation Fig.3-5 shows results when using phase preprocessing. From left to right, some cases are displayed, title in green indicates that it corresponds to healthy tissue whereas plum color, indicates that it corresponds to one with cancer. From top to bottom each estimation is used to reconstruct each path, the ﬁrst row is how the original patch looks like, then second and third row show reconstructions when using the proposed approach. It’s noticeable how diﬀerent patterns appear when images are preprocessed with a healthy or cancerous patch, and for this particular case, it was found a particular pattern that highlights more randomness or variability for cancerous subjects Prostate X - 002 and Prostate X - 026 whereas a more plain texture is appreciable for the preprocessed healthy case Prostate X - 084.

B. Phase per

C. Statistics

A. MRI Patches

patch

per pixel

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

[Figure 68]

[Figure 69]

Cancer

{𝜇 𝑢, 𝑣 ,𝜎(𝑢,𝑣)}

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

Healthy

###### Figure 3-4.: Pipeline for extracting statistic images from the dataset, the ﬁgure displays an example for cancer and healthy classes. From left to right: in A. For each image of each class I(x,y) its Fourier transform is computed obtaining magnitude and phase spectrum { ω(u,v),φ(u,v) }. Then all phases of a given class are stacked as displayed in B. After that in C. mean and standard deviation per pixel location (u,v) are computed to obtain statistic values of phase matrices per class.

Prostate X - 002 Prostate X - 084 Prostate X - 026

Patches:

[Figure 82]

[Figure 83]

[Figure 84]

Original Patch

[Figure 85]

[Figure 86]

[Figure 87]

Preprocessed: Cancer Phase

[Figure 88]

[Figure 89]

[Figure 90]

Preprocessed:

Healthy Phase

###### Figure 3-5.: shows reconstruction for some cases, each row represents a reconstruction by using each of the three obtained phase estimations and each column represents a given case.

Classiﬁcation Results: For each of the 3 classiﬁcation models, one evaluation is performed by using the 30% that was reserved for testing. This was done in each of the three processed subsets as shown in table 3-1. Interestingly classiﬁcation performance was degraded for cancer representers whereas performance improved after using a healthy subject for preprocessing.

###### Base Cancer 5 phase Cancer 3 Phase Healthy Phase

Sens Spec Acc Sens Spec Acc Sens Spec Acc Sens Spec Acc 0.69 0.80 0.73 0.80 0.16 0.53 0.69 0.64 0.66 0.77 0.80 0.78

Table 3-1.: Classiﬁcation performance when training and testing preprocessed images: each bold title represents the experiment, metrics sensitivity, speciﬁcity and accuracy are reported per model evaluation in its respective testing subset

Cancer 5 Cancer 3 Cancer 1 Healthy

[Figure 91]

[Figure 92]

[Figure 93]

[Figure 94]

𝜎

- Entropy: 7.33 Variance: 1.78

Entropy: 6.30 Variance: 0.39

Entropy: 5.69 Variance: 0.19

Entropy: 4.35 Variance: 0.06

- Entropy: 7.34 Variance: 0.83

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

𝜇

Entropy: 7.36 Variance: 0.31

Entropy: 7.00 Variance: 0.18

Entropy: 6.86 Variance: 0.07

Figure 3-6.: Shows images of statistical moments for the phase of diﬀerent classes of the dataset, each column represents a diﬀerent class, additionally, the ﬁrst row shows mean µ(u,v) images and the second one shows standard deviation images σ(u,v)

Experiment 2 - Phase space analysis Figure 3-6 displays results of phase analysis by computing statistical moments as explained in section 3.3.3. To carry out this analysis, shanon entropy and variance was computed for each obtained image i.e mean and standard deviation images. For both images variance and entropy show proportional results, additionally, it’s interesting to see how both quantities decrease as health condition of the tissue

improves. Nevertheless it’s important to clarify that samples for each class are unbalanced and this could therefore alter the behaviour of these results.

### 3.4. Conclusions

This work introduces a phase estimator that is able to enhance classiﬁcation performance of healthy vs cancerous tissue on MRI patches from the ProstateX dataset, such improvement holds the hypothesis that spatial support may suggest tissue alteration and such pattern is uncovered by means of the phase of the Fourier Transformation.

# 4. Autism Spectrum Disorders (ASD) Characterization in Children by Decomposing MRI Brain Regions with Zernike Moments

This chapter presents a characterization methodology for Autism Spectrum Disorder in brain magnetic resonance images (MRI) based on Zernike Moments. For doing so a region-wise analysis was carried out by building a 2D multi-slice image per region for which Zernike moments were computed upon. Binary classiﬁcations were performed under a 10-fold cross validation for two children cohorts of the heterogeneous ABIDE I and II datasets. Top performer regions obtained with this methodology were: left supramarginal gyrus, right occipital fusiform cortex, right frontal orbital cortex, right lateral occipital cortex - superior division, right intracalcarine cortex, left lateral occipital cortex - superior division, with top performance of 77% AUC for the ABIDE I cohort and 76% for the ABIDE II one. Results of this work showed how this characterization was able to discriminate both classes in regions reported as relevant for the disease in the state of the art and in a heterogeneous context. A complete version of this chapter has been accepted for publication as a research article in the proceedings of SIPAIM - MICCAI Biomedical Workshop in the 21st International Conference on Medical Image Computing and Computer Assisted Intervention (see reference117)

### 4.1. Introduction

ASD constitutes a group of neurological alterations that represents a wide variety of clinical expressions. About 1 in 59 children has been identiﬁed with ASD according to CDC’s Autism and Developmental Disabilities Monitoring (ADDM) Network. The prevalence in children is higher in boys than in girls, in a proportion of 4 to 112.

Although there exist a large number of syndromes related to autism, the diagnosis remains

until now strictly clinical. A reliable diagnosis requires availability of therapists or physicians, resulting in a bottleneck that diﬃcult early detection of this disorder60. In addition, most of early signs of brain function alteration are not speciﬁc and autistic signs may be observed in patients with no disorder, a source of confusion for many clinicians134.

Currently, ASD diagnosis is performed using neuro-psychological tests that evaluate the patient-environment interaction and high cerebral functions. These tests register several clinician observations, making diagnosis subjective. The gold standard 50 in terms of diagnosis is the Autism Diagnostic Observation Schedule (ADOS)107 and/or the Autism Diagnostic Interview (ADI-R)109. However the probability of misdiagnosis is high69 since the clinician may mislead descriptive labels and inevitably introduces bias by her/his judgment127. Clinicians’ experience may facilitate ASD diagnosis before the second year, yet the average diagnosis age is above 3 years, which suggests many children may not be diagnosed at all. Early ASD diagnosis is critical because earlier treatments can reduce the degree of deterioration and improve the function of both patients and carers4. Curiously, even if modern medical images are at the very base of many decisions, in these kind of pathologies their role is still marginal153. Neuro-imaging could be useful to evaluate relationship between the diﬀerent areas, regions or set of cerebral regions and the cognitive and functional signs that patients present, that is to say, analysis of the structure oﬀers new possibilities of correlating brain changes or alterations at the functional level with ASD signs.

Diﬀerent researches have been done with the purpose of correlating functional alterations presented in ASD and the anatomical structures. The ﬁrst approaches to this theory date back in 1991, when Kemper and Bauman analyzed brains of six autistic patients, ﬁnding main alterations at the level of the limbic system, cerebellum and inferior olive. These brains showed no major morphological changes, yet it was reported a decrease in the neuronal cell size and an increase of the neuronal density at the level of the amygdala and other limbic structures when comparing to controls83. Recent studies have used brain MRI to classify patients with ASD, resulting that main changes were in regions like the basal ganglia, corpus callosum, hippocampus, amygdala and thalamus19,47,90. Participants in this study aged 6-15 years, volunteer ASD and control subjects77.

There is a strong ADS relationship with brain areas responsible for normal language development such as Broca’s area and Wernicke’s area at a level of verbal and non-verbal communication. There is evidence of increase in the volume of the right and left temporal gyrus in T1-MRI studies38,70. Other research has used more than three diﬀerent classiﬁcation techniques (RF, SVM and GBM) using as main feature the size of the cortical and sub-cortical regions, reporting a sensitivity of 57% and 64% of speciﬁcity for the binary classiﬁcation task79.

ASD characterization is diﬃcult by the high variability between diﬀerent medical studies and children development. An automatic morphometry approach has the advantage of including additional information to support early diagnosis, but some approaches based on voxel size, shape, or volume132 ignore local and regional dependencies. A main contribution of the present research is a fully automatic morphometric method that establishes region diﬀerences by using local shape information. The approach starts by a brain segmentation using a known template114. Once the brain is segmented, each region is characterized by the magnitude and phase of the region Zernike Moments which inputs a standard classiﬁer. Classiﬁcation results using such feature space provide representative regions that diﬀerentiate between ASD patients and control subjects.

### 4.2. Methods

The proposed method is divided in ﬁve phases, as illustrated in Figure 4-1, starting by ﬁrstly pre-processing each volume to eliminate diﬀerences coming from acquisition protocols and devices. Afterwards, an atlas39 is elastically registered to each of the cases with the aim of segmenting brain regions. Each segmented region is then arranged in a two-dimensional collage of images, constructed by sequentially copying each slice into a 2D frame, from the top to the bottom of the region. The obtained 2D image is used as input to calculate the Zernike moments per region. The resultant magnitude and phase are used as features that are challenged to a classic classiﬁcation task by means of a conventional Support Vector Machine (SVM).

##### 4.2.1. Pre-processing

Each volume undergoes a pre-processing phase composed by two steps, ﬁrst an intensity correction to reduce intra-site variability since images were not obtained by the same device and, second a brain extraction to remove skull, spinal cord and eye holes. Intensity correction was performed by the FSLMATH tool provided by the Oxford University163, which corrects the bias ﬁeld and normalizes each volume. Afterward, brain extraction was done by using BET (Brain Extraction Tool), which removes non-related brain tissues by using the histogram of the image and triangular tessellations145.

##### 4.2.2. Registration and segmentation

The registration phase was carried out to obtain the corresponding regions from the HarvardOxford Atlas110. For so doing, the MNI152 template114 was elastically registered to each brain. The process begins with an aﬃne registration with 12 freedom degrees and a correction for spatial errors computed by means of the FLIRT Tool (FMRIB’s Linear Image Registration Tool)73. Then, a ﬁner result is obtained by performing elastic registration using the FNIRT163 tool with a quadratic spline which optimizes the processing time and ensures that transformation is as accurate as possible.

[Figure 99]

- Figure 4-1.: Pipeline of proposed strategy 1) pre-processing each volume, 2) a particular atlas is elastically registered to each case and the resultant volume is segmented to 117 regions, 3) each 3D region is mapped into a 2D-collage image, 4) the Zernike moments are computed per region, taking the magnitude and phase per moment as features, and 5) ﬁnally a classiﬁcation task between ASD patients and control subjects to establish discriminative regions is performed.

##### 4.2.3. Anatomic Region representation and Collage

In the present work each segmented region, a volume structure, is represented as a 2D image that contains each axial plane. This collage is built by placing each slice in an squared resolution image, as seen in Figure 4-2. However, note that each volume slice is ﬁt to the size of the region, that is to say, while the volume resolution is 512×512, the resulting image resolution for a particular region slice could be 45 × 57. This representation is convenient

because it allows to describe structural shape changes on each slice without any loss of information from the 3D original volume.

##### 4.2.4. Region-based characterization: Zernike Moments

Zernike moments are considered as shape descriptors by performing a multiscale frequency analysis which is usually represented as a pyramid, where the scales are the diﬀerent pyramid levels and frequency analysis (repetitions) is performed through each of the scales. The complex 2D Zernike moments of order m and n repetitions are deﬁned in the unitary circle103 as:

[Figure 100]

Figure 4-2.: An example of a 2D-image that represents a cortical brain region.

m + 1 π

Zmn =

2π

0

1

f(r,θ)Vmn∗ (r,θ)rdrdθ,r ≤ 1 (4-1)

0

where f(r,θ) stands for the image intensity function, Vmn∗ (r,θ) corresponds to the complex conjugate of Zernike polynomial Vmn(r,θ), and m and n are both integers related as:

(m − |n|) is even and |n| ≤ m (4-2)

For processing a 2D image, Zernike moments are computed by using the discretized form,

- as illustrated in Equation 4-3:

Zmn =

m + 1 π r θ

P(r,θ)Vmn∗ (r,θ) r ≤ 1 (4-3)

In this work, a morphometric analysis was performed by transforming the 2D image into the Zernike space, a representation that has demonstrated describe complex shapes103. This representation allows to characterize each brain region based on shape diﬀerences between ASD patients and control subjects. Each brain region was described by using 9 scales (55 Zernike moments), where each moment consists of magnitude and phase components, obtaining

- at the end a descriptor of 110 features.

##### 4.2.5. Classiﬁer

Support Vector Machines (SVM) are a set of related methods for supervised learning, applicable to both classiﬁcation and regression problems. A SVM classiﬁer sets a maximum-margin hyperplane that lies in a transformed input space and splits the space, while maximizing the distance to the nearest sample examples. The parameters of the hyperplane solution are derived from a quadratic programming optimization problem144. For this investigation, the SVM algorithm was trained with the feature vectors obtained from previous phase.

### 4.3. Experiments and results

The proposed strategy performance was evaluated by using a open access database43. The most important result is the identiﬁcation of a set of brain regions that better diﬀerentiate the two classes, namely ASD patients and control subjects.

##### 4.3.1. Data

For this study, brain T1-MRI cases were used, available in the Autism Brain Imaging Data Exchange ABIDE I and ABIDE II (ﬁrst and second version)40,43. ABIDE databases contain

4.3 Experiments and results 35

2226 cases (ASD individuals and typical controls aged 5-64 years), scanned across 17 medical centers. For this investigation, two subsamples were used, including only male cases with voxel size of 1 × 1 × 1 and ages between 6 and 12 years, based on the criterion of growth and development of the cephalic mass in children up to 12,1 years58, aiming to get an homogeneous population.

The evaluation was then carried out with 196 subjects (98 individuals diagnosed with ASD and 98 controls), 68 from ABIDE I database (Table 4-1) and 128 from ABIDE II database (Table 4-2).

- Table 4-1.: Strict sample phenotypic information for ABIDE I

|Group|Age|Total<br><br>|Mean<br><br>|Standard Deviation|Variance Coeﬃcient|
|---|---|---|---|---|---|
|Autism|6 - 12 years<br><br>|34|10,88<br><br>|1,87<br><br>|16,94%|
|Control<br><br>|6 - 12 years|34<br><br>|10,96|1,75<br><br>|15,77%|

- Table 4-2.: Strict sample phenotypic information for ABIDE II

|Group|Age<br><br>|Total|Mean<br><br>|Standard Deviation<br><br>|Variance Coeﬃcient|
|---|---|---|---|---|---|
|Autism<br><br>|6 - 12 years<br><br>|64|9,85|1,479<br><br>|14,84%|
|Control<br><br>|6 - 12 years<br><br>|64|10,08<br><br>|1,303|12,81%|

##### 4.3.2. Registration and segmentation

The Harvard - Oxford atlas110 was used as the reference space to segment each brain of the experimental group into 96 cortical (48 per hemisphere) and 17 sub-cortical regions. The lateralized template was rigidly and elastically registered to each brain, and the resultant transformation matrix was applied to the atlas parcellation, obtaining the set of brain regions per case. Registration was assessed by measuring the overlapping percentage (Dice Score coeﬃcient44 metrics) between both complete brain volumes, the registered MNI-152 and each case:

2|X ∩ Y | |X| + |Y |

QS =

(4-4)

where: X is the MNI152 template and Y the evaluated brain. Once the elastic registration is performed, each brain is compared with the deformed template to verify that there is a high correspondence between the complete brain volumes. Registration results are shown in Tables 4-3 and 4-4 respectively.

- Table 4-3.: Overlap Analysis for ABIDE I

|Group<br><br>|Analyzed Cases<br><br>|Register|Total Overlap ± SD in%|
|---|---|---|---|
|Control<br><br>|34|Aﬃne Elastic|37,33 ± 6,02 97,62 ± 0,62<br><br>|
|Autism|34<br><br>|Aﬃne Elastic<br><br>|37,26 ± 4,58 97,54 ± 0,66|

- Table 4-4.: Overlap Analysis for ABIDE II

|Group|Analyzed Cases<br><br>|Register<br><br>|Total Overlap ± SD in%|
|---|---|---|---|
|Control<br><br>|64<br><br>|Aﬃne Elastic|30,51 ± 4,33 97,16 ± 0,91<br><br>|
|Autism|64|Aﬃne Elastic<br><br>|33,43 ± 2,91 97,68 ± 0,30|

##### 4.3.3. Region-based characterization: Zernike Moments

In this phase of the proposed approach, there were computed 9 scales of the Zernike transformation, providing the ﬁrst 55 moments of such representation space. This information corresponds to the shape orientations for each used region, and then magnitude and phase per calculated moment are concatenated on a matrix. Zernike moments were calculated the for the n×n 2D region mosaic-image described in the Section 4.2.3, using Matlab136,150. Figure 4-3 illustrates the complex parameters (magnitude and phase) provided by the Zernike moments for a particular region in the polar space.

##### 4.3.4. Classiﬁer

For evaluating the performance of the proposed approach by using a Support Vector Machine (SVM) classiﬁer, a Radial Basis Function (RBF) was selected as kernel because of the high dimensionality of the feature vector per region. A 10-fold cross-validation scheme was used to train and test the constructed model, and four metrics are reported, namely Area Under the Curve (AUC), sensitivity, speciﬁcity and F-Score. It is noteworthy that the regions that showed greater accuracy were cortical regions, especially in those that are related to the normal language development, which play an important role in brain morphological changes on autistic patients such as reported in previous researches45. Table 4-5 presents the classiﬁcation results using the ﬁrst 55 Zernike Moments for cortical brain regions.

###### 4.4 Discussion 37

ABIDE I: Right Orbital Frontal Cortex

90

25

90

20

|120<br><br>150|5<br><br>10<br><br>15<br><br>20<br><br>30<br><br>60|
|---|---|
|210<br><br>240|300<br><br>330<br><br>|

|120<br><br>150|5<br><br>10<br><br>15<br><br>30<br><br>60|
|---|---|
|210<br><br>240|300<br><br>330|

1

1

180 0

180 0

2

2

270

270

Patient Control

- Figure 4-3.: Representation of complex parameters (magnitude and phase) for a cortical region (Right Frontal Orbital Cortex) provided by Zernike Moments. In (a) is presented the distribution of the complex values in a control subject and in (b) the distribution of the complex values in a autistic patient evaluated on the same region.
- Figure 4-4 shows the Area Under Curve (AUC) graph for the most signiﬁcant brain region for ABIDE I (Right Frontal Orbital Cortex) and for ABIDE II (Right Occipital Fusiform Gyrus), found with Zernike Moments characterization.

### 4.4. Discussion

In the present study, we examined the orientations of the shape from each brain region using the Zernike Moments, in a large sample of children with ASD (Autism Spectrum Disorder), relative to TC (Typical Control). This representation does not ﬁnd diﬀerences at the cellular level, but on the surface and how they are related to the abnormal growth of each region. Frontal Orbital Cortex is highly related to aﬀective functions, decision-making and sensory integration87. It is possible to associate alterations in this structure with one of the signs present in autism related to communication and social interaction.45.

Finally, we found associations with severity symptom within a thalamic surface area cluster. These ﬁndings suggest that there are subtle diﬀerences in subcortical morphology in ASD.

Table 4-5.: Classiﬁcation performance for cortical and sub-cortical regions by testing with ABIDE I and ABIDE II. The reported metrics are: area under the curve (AUC), sensitivity (SENS), speciﬁcity (SPEC) and F-Score (F-S).

|DATA|AUC<br><br>|SENS|SPEC<br><br>|F-S|REGIONS|
|---|---|---|---|---|---|

|ABIDE I<br><br>|77%|71%|75%<br><br>|74%<br><br>|Left Supramarginal Gyrus|
|---|---|---|---|---|---|
| | | | | |Right Frontal Orbital Cortex|
| | | | | |Right Intracalcarine Cortex|
| | | | | |Left Superior Parietal Lobule|
| | | | | |Right Thalamus|

|ABIDE II<br><br>|76%|72%<br><br>|72%|72%<br><br>|Right Occipital Fusiform Cortex|
|---|---|---|---|---|---|
| | | | | |Right Lateral Occipital Cortex|
| | | | | |Left Lateral Occipital Cortex|
| | | | | |Left Lingual Gyrus|
| | | | | |Left Paracingulate Gyrus|

Although this study was cross-sectional, our ﬁndings also suggest that there may be atypical developmental of intellectual function and performance deﬁcits in ASD due to this atypical growth36.

### 4.5. Conclusions and future work

This work presents a method for classifying patients diagnosed with ASD and how the anatomy of their brains diﬀers from control subjects in particular regions. The variability of the disorder and the methods used by physicians for diagnosis is not completely reliable. The method used in this research works with high level features in MRI in order to represent the information as orientations in brain shape. The obtained results correspond to regions reported in state-of-the-art methods focused on image analysis based on other high level features. Cortical regions remain relevant in the study of autism due to anatomical variability of the brain, especially those related to the social interaction and communication. As a future

###### 4.5 Conclusions and future work 39

ABIDE I:

Right Frontal Orbital Cortex

- 0.8
- 1

Falsepositiverate

0.6

###### AUC = 0.77

0.4

0.2

0

0 0.2 0.4 0.6 0.8 1

False positive rate

ABIDE II:

Right Occipital Fusiform Gyrus

- 0.8
- 1

Falsepositiverate

0.6

AUC = 0.75

0.4

0.2

0

0 0.2 0.4 0.6 0.8 1

False positive rate

Figure 4-4.: Area under the curve for the most signiﬁcant region per dataset, namely, ABI-

DE I and II.

work, we would like to make an inter-class classiﬁcation to automatically determine the existing classes in autism spectrum disorder as Asperger, Classical Autism, Rett (present only in women) and other non-invasive developmental disorders described by the DSM-V guide.

# 5. Autism spectrum disorder characterization in children by capturing local-regional brain changes in MRI

This chapter presents a characterization methodology for Autism Spectrum Disorder in brain magnetic resonance images (MRI) based on the Curvelet Transform. For doing so a regionwise analysis was carried out by building a 2D multislice image per region characterized by computing the curvelet transform that was parametrized with generalized Gaussian distributions. Binary classiﬁcations were performed under a 10-fold cross validation for two children cohorts of the heterogeneous ABIDE I and II datasets, additional experiments such as hold out validation and a comparison against state-of-the-art approaches was also done. Results of hold out validation obtained 0,69 AUC for the right parahippocampal gyrus. In the case of separated cohorts of ABIDE I and II AUCs of 0,75 and 0,77 were obtained for the right supramarginal gyrus - anterior division (ABIDE I), and the left superior temporal gyrus anterior division (ABIDE II). Finally analyses against state of the art features showed no correlation against features such as voxel based morphometry. This work presented a multiscale descriptor that highlights diﬀerent features or patterns in comparison with state-of-the-art strategies, classiﬁcation results were competitive and showed promising performance for heterogeneous contexts and generability. A complete version of this chapter has been accepted for publication as a research article in the journal of Medical Physics, vol. 47, issue 1 (see reference6)

### 5.1. Introduction

Autism Spectrum Disorders (ASD) are complex neuro-developmental conditions that manifest during the ﬁrst three years of life71. Commonly, aﬀected children exhibit repetitive patterns, limitations in social interaction and communication skills8,124. In 2014, an average

5.1 Introduction 41

of 1 out of 59 children in the United States was identiﬁed as having this disorder (only at age eight)12.

Post-mortem brain studies have shed some light on the physiopathology of this disorder. Histochemical, autoradiographic and biochemical tests have established diﬀerences between ASD patients and control individuals18. These tests demonstrate pathological diﬀerences at local (cellular) and global (region or whole brain) levels, i.e., reduced neuronal size and cell density loss in some brain regions like hippocampus91, cerebellum52, amygdala15, as well as age related changes that produce increased gray/white matter and increased cortical thickness as a result of dysregulated pruning152, or atypical sulcal anatomy in young children with ASD11. In addition, other studies have described morphometric cortical abnormalities in people with autism, speciﬁcally shape changes at the level of the corpus callosum, the central, intraparietal and frontal medial sulci11,25. Unfortunately, these ﬁndings have no relevance in clinical practice and are completely ignored in radiological examinations, even though Magnetic Resonance Imaging (MRI) has been reported as the most used technique to understand ASD71. The main bottleneck consists in the lack of quantitative features that can provide evidence of the state of the disease.

Diﬀerent studies have attempted to determine brain changes mainly using morphometry61,82,131,137 and texture feature analysis30,158. Morphometry is applied under the hypothesis that there exists a signiﬁcant variation in terms of shape, contour and volume of certain brain regions61,131,137. For instance, Sato et al.137 proposed a voxel-based morphometry strategy that revealed reduced gray matter volume in a particular set of regions in adults with ASD, most of these regions constituting the social brain network. Interestingly, classiﬁcation performance was better when using this set of regions. Similarly, Retico et al.131 computed morphometric features such as volume, curvature, regional width and depth to perform a classiﬁcation task for diﬀerentiating between ASD and control subjects using Support Vector Machines (SVM), while Giulianoa et al.61 used ﬁve surface-based features to morphologically describe brain regions. Likewise, texture features have been commonly used to describe brain regions by considering the variability of gray and white matter between ASD and control individuals30,158. As an example, Chaddad et al.30 described brain regions by extracting multiscale texture features (entropy, mean and standard deviation) using Laplacian of Gaussian (LoG) ﬁlters, and performed a statistical analysis to identify the regions that show higher diﬀerences between ASD patients and control subjects.

The main contributions of this work are:

Use of Curvelet transform to characterize regions with Generalized Gaussian Distribution to reduce feature dimensionality.

Quantiﬁcation of local-regional changes in anatomic brain regions by a 2D multislice

image, aiming to capture relationships of a region in the Curvelet space that describe atypical brain folding.

Evaluation in heterogeneous datasets which proves the method can be generalized.

Recent evidence has demonstrated ASD patients may exhibit atypical brain folding patterns as an early manifestation of the altered neurodevelopmental process11. This resultant cortex wrapping should be thought of as not only a change of the volumetric shape but rather

- as an alteration of the topological regional relationships. Highlighting such patterns is not an evident task since diﬀerences need not necessarily be determined at the level of ﬁrstorder relationships (typical 3D analysis). The approach herein proposed is basically a 2D analysis by mapping the set of 2D slices of a 3D region to the same plane (a 2D multislice image) and capturing their diﬀerent relationships by a general transformation. Therefore, this investigation introduces a multiscale descriptor that characterizes 3D brain regions and highlights those ones with diﬀerences between ASD patients and control subjects in MRI studies. Characterization of a brain region is performed by applying the Curvelet transform to the 2D multislice image, the base of the multiscale analysis, where information is frequency-decomposed into a set of sub-bands along diﬀerent scales and orientations. The coeﬃcient distribution of each Curvelet sub-band is approximated by a parametric function, characterizing any sub-band with only three parameters, an important dimensionality reduction. The proposed approach was validated by automatically classifying ASD and control children populations belonging to heterogeneous datasets from the Autism Brain Imaging Data Exchange (ABIDE)40,43, which could help towards generalization.

### 5.2. Materials and Methods

The main goal of this work was to devise an image descriptor that captures local and regional brain changes, aiming thereby to estimate both regional shape alterations and possible cellularity losses15,52,160,161. The resultant descriptor was validated by a conventional classiﬁcation task, which tests the representation aptness to discriminate between control and ASD cases.

##### 5.2.1. Data

Data for this investigation are part of the Autism Brain Imaging Data Exchange (ABIDE)43, an open project including cases collected from 17 institutions, with patients aged between

- 5 and 64 years: a total of 1112 cases from ABIDE I43 and 1114 cases from ABIDE II40.

This study only considered cases corresponding to children between 6 and 13 years, and the purpose of this partition is to analyze and identify pathologic patterns (from ASD children population) that diﬀer from the normal brain growth (represented by control population), and therefore allows early diagnosis. This study includes cases with structural T1-MRI scans with a voxel size of 1 × 1 × 1 mm.

The ABIDE I sample consists of 34 ASD patients and 34 control subjects between 5 and 13 years (mean age 11,46±2,03 and 11,53±1,79 years respectively). In addition, all the children in this sample correspond to male individuals. These cases were collected from six diﬀerent centers (see Table 5-1). The use of data from multiple centers implies that the available set of images is diﬀerent in terms of number of slices per volume, inter-slice distance, image resolution and scanner protocol. The ABIDE II sample is composed of 42 ASD patients and 41 control subjects with ages between 7 and 12 years (mean age 10,09 ± 1,37 and 10,52 ± 1,27 years respectively). In addition, all children in this sample also correspond to male individuals collected from four diﬀerent centers (see Table 5-1). Note two of the four centers for the ABIDE II sample are diﬀerent from the ones in the ABIDE I sample. In addition, the population distribution is quite diﬀerent. Finally, Table 5-1 also shows the scanner model used in each of the centers where the structural magnetic resonance images were acquired, demonstrating data heterogeneity.

Table 5-1.: Data description: ABIDE I and II samples

|Site|ABIDE I| | |ABIDE II<br><br>| | |Scanner Tech.|
|---|---|---|---|---|---|---|---|
| |ASD<br><br>|CNT<br><br>|Tot.|ASD|CNT<br><br>|Tot.| |
|Max Mun|8|5<br><br>|13| | | |Siemens Magnetom Verio|
|Olin<br><br>|2<br><br>|2|4| | | |Siemens Magnetom Allegra|
|SDSU|5<br><br>|6|11<br><br>|10|1|11|GE 3T MR750|
|Trinity|6<br><br>|6|12| | | |Philips 3T Achieva|
|Yale<br><br>|13|14<br><br>|27| | | |Siemens Magnetom Trio|
|KKI|0<br><br>|1|1<br><br>|12<br><br>|27|39<br><br>|Philips 3T Achieva|
|GU| | | |17|11|28<br><br>|Siemens 3T Trio|
|UCD| | | |3<br><br>|2|5<br><br>|Siemens 3T Trio|
|Total<br><br>|34|34|68|42<br><br>|41|83| |

##### 5.2.2. Methods

The pipeline of the proposed strategy is shown in Figure 5-1. The principle behind this characterization strategy is that diﬀerences between local brain patterns should be observable among diﬀerent scales. Overall, pre-processing aims to normalize image intensities,

[Figure 101]

[Figure 102]

[Figure 103]

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

[Figure 111]

[Figure 112]

l

[Figure 113]

[Figure 114]

[Figure 115]

"

[Figure 116]

[Figure 117]

l

!

" ! " ! "

!

[Figure 118]

[Figure 119]

…

Brain Region

1. Region Mosaic

2. Curvelet Transform

SVM Model

3. Generalized Gaussian PDF

[Figure 120]

- Figure 5-1.: The proposed strategy consists in three phases. In (A) each case is preprocessed to normalize image intensities, remove the skull and segment the brain into a set of anatomical regions. In (B) the multiscale descriptor is computed by transforming each segmented region into a 2D multislice image, applying a multiscale analysis with the Curvelet transform and approximating each Curvelet sub-band coeﬃcient distribution by a Generalized Gaussian Distribution to reduce dimensionality. Finally in (C) a conventional classiﬁcation is performed per region to assess the robustness of the feature descriptor in diﬀerentiating ASD patients from control subjects.

remove the skull and segment each case into a set of brain regions. In a second phase, each segmented region (a volume) is mapped to a 2D image by orderly placing upon it each of the volume slices. This 2D image with the collection of slices is analyzed using the Curvelet transform, and the coeﬃcient distribution per Curvelet sub-band is approximated by a Generalized Gaussian Distribution. Therefore, each sub-band ends up by being represented by three parameters. Finally, to evaluate the ability of the constructed multiscale descriptor to diﬀerentiate the two classes, a conventional SVM performs a binary classiﬁcation per region and those regions related with ASD are identiﬁed.

###### Preprocessing

The preprocessing phase is carried out per brain magnetic resonance imaging using FSL software and involves the following steps: a) intensity normalisation (FSLMATHS tool75), b) skull removal (Brain Extraction Tool (BET)146), c) rigid-elastic registration from the MNI152 template to each brain in the dataset (FLIRT-FNIRT tools9,74), and d) the Harvard Oxford atlas111 is registered to each brain using the previously computed elastic transformation matrix, and thereby providing a segmentation mask with 117 regions (96 cortical and 21 sub-cortical).

###### Multiscale descriptor

The construction of the multiscale descriptor per region is illustrated in Figure 5-1.B and herein explained.

Volume representation: For each segmented brain region, the 3D image is mapped to a 2D mosaic, called the 2D multislice image. This new image corresponds to the 3D region mapped to a 2D plane, as illustrated in Figure 5-1.B.1, independently of the number of slices or the size of the region. The obtained mosaic is then zero-padded to ﬁt a squared shape, necessary for the Curvelet characterization. This representation captures main topological relationships of a region in the Curvelet space and can describe structural changes like atypical brain folding without losing of the relevant 3D information. From this point of view, features in this space are not necessarily correlated with measures like surface area, thickness or folding76,148, since the object basic relationships in the Curvelet space do not have the usual Euclidean geometric meaning. Several studies have reported diﬀerences with these measures, but the approach herein presented rather attempts to capture subtle anatomic changes manifested by loss of the global shape which are hardly detected as size or volume alterations. Note each 2D multislice image size is variable to conserve original information and depends on: i) the particular brain region of analysis, ii) the number of slices such region contains, and iii) the image resolution provided by the scanner.

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

| |
|---|

[Figure 125]

| |
|---|

| |
|---|

Figure 5-2.: Description of a brain region given the 2D multislice image representation. From top to bottom, the mosaic (2D multiscale image) is taken as an input for computing the Curvelet transform, whose coeﬃcients are displayed at the center panel, and at the bottom, histograms of three sub-bands are shown as well as their distribution estimations.

Multiscale Analysis: The multiscale analysis is performed by transforming the 2D multislice image to the Curvelet space (as shown in Figure 5-1.B.2), a transformation introduced by its well demonstrated aptness to approximate textures and complex geometrical structures24. The Curvelet transformation is a multiscale geometric mapping that preserves the same good decomposition advantages reported with the Wavelet transform46, but introducing a compact representation of curved geometric structures. In fact, Curvelet functions are known for giving sparse representations of smooth objects with discontinuities along curves24. In this work, the Curvelet representation allows to describe brain regions in terms of their local/regional diﬀerences between ASD patients and control subjects.

A Curvelet frequency space is deﬁned by the convolution between radial R(ω) and angular Φ(ω) windows, being R(ω) the scale and Φ(ω) the phase along the radial direction23. The object proportion between diﬀerent scales is ensured by the special scaling law width ≈ length2, i.e., anisotropy increases as long as scales decrease. In terms of a dyadic spatial decomposition, a Curvelet is characterized by two levels of location: a coarse location in the usual dyadic spatial square and a ﬁner one which anisotropically places the Curvelet within such coarse dyadic square. The term micro-location refers to this ﬁner placement. In addition, the anisotropy property rises two relations, the number of directions and the number of micro-locations are both proportional to the inverse of the scale. This anisotropic characterization of curves was the main motivation to select this representation since we seek to capture distortions of the regional and local shapes. In addition, the proportionality of number of micro-locations with respect to the scale, results crucial to characterize particular texture patterns which are herein supposed to describe tissular arrangements that correlate with the neuropathology. In the Curvelet frequency representation, the scaling law amounts to reﬁne directions every two scales, and the wedge (sub-band) coeﬃcients represent the parabolic relationship for a given scale

This work characterizes brain regions by using the Fast Discrete Curvelet Transform (FDCT), conﬁgured by deﬁning the optimal number of scales and angles to perform the experiments. Since the scale is a resolution-dependent parameter and the smallest resolution of the 2D mustislice images in the dataset is 96 × 96 pixels, the maximum number of scales to be used is 4. Regarding the number of angles, 16 has been reported to achieve the best results for this particular representation89. Therefore, the FDCT representation is split along 4 scales in 16 diﬀerent angles, i.e., due to the dyadic decomposition a set of 81 Curvelet sub-bands are provided.

Dimensionality Reduction: Each sub-band (wedge) contains a set of coeﬃcients that describes a speciﬁc range of frequencies at a particular scale and a determined orientation. Note that the number of coeﬃcients per sub-band varies according to: i) size of the 2D multislice image and ii) the particular scale and orientation of analysis. Therefore, the Generalized

Gaussian Distribution (GGD) is used in this investigation to approximate each coeﬃcient distribution with three parameters, achieving an important dimensionality reduction as well as unifying the size of the feature vector that describes each brain region. This parametric approximation meets each set of coeﬃcients as either a Laplacian, normal or ﬂat distributions (see Figure 5-2). This distribution has demonstrated to give accurate descriptions of the Wavelet or Curvelet coeﬃcients for a given sub-band46,62. In a GGD, µ stands for the mean of the distribution, β models the decay rate from the peak, ρ models the peak width (like the standard deviation σ in a Gaussian distribution) and Γ corresponds to the gamma function37. Therefore, the GGD is used in this work to approximate the set of coeﬃcients per Curvelet sub-band by 3 parameters (as shown in Figure 5-1.B.3). Since 81 sub-bands are computed, a feature vector of 243 components characterizes each brain region.

###### Classiﬁcation

Support Vector Machines (SVM), a discriminant binary classiﬁer32, is used to build a model for each brain region. SVM provides a mapping of each element onto a space, which may establish a linear or non-linear boundary between two classes, as wide as possible. The underlying strategy, the kernel trick, consists in mapping data by a kernel function. A kernel is a function k : X × X → R associated to a mapping 1,...,φ : X → F such that ∀ x,y ∈ X,k(x,y) = ψ1(x),ψ1(y) F, i.e., k calculates the dot product in F. Intuitively, a kernel may be thought of as a function that measures similarity between two objects of the input space. In this work, a binary SVM model per region is trained using the a matrix of f × n size, where f corresponds to 243 features computed in the previous phase (the proposed multiscale descriptor) and n stands for the total of cases (ASD patients and control subjects). Each region is independently analyzed to quantify how discriminative is to separate the two classes based on the proposed multiscale representation. The SVM is conﬁgured using two parameters, box-constraint and sigma. The box-constraint controls the penalty imposed to observations with large residuals while the sigma parameter deﬁnes how linear is the SVM decision boundary. For setting SVM parameters, a Bayesian optimization147 is run over to ﬁnd the best possible values for sigma and box-constraint. In addition, SVM models are tested with two diﬀerent kernels, speciﬁcally a linear function and a radial basis function (RBF).

##### 5.2.3. Evaluation

The set of experiments are hereafter described. The aim of these experiments is not to provide a ﬁnal classiﬁcation per subject but rather to ﬁnd out a set of anatomical brain regions with pathological patterns, in terms of texture features, that describe and quantify this disorder.

- Experiment 1: The aim of this experiment is to evaluate the ability of the proposed multiscale descriptor to diﬀerentiate ASD patients from control subjects with a data set never seen by the trained model. For so doing, ABIDE II sample (83 cases) is used for training the classiﬁcation model which is then tested with the sample of ABIDE I (68 cases) under a hold-one-out validation scheme (cases are individually tested). Classiﬁcation performance is assessed by computing the area under the receiver operating characteristic curve (AUC), since most of state-of-the-art methods report such metric.
- Experiment 2: The aim of this experiment is to identify the most discriminant regions in the classiﬁcation task (ASD patients vs. control subjects), deﬁned as the ability of a region to separate both classes. For each of the 117 regions, 10 iterations of 10-fold (one fold is held-out for testing) cross validation are carried out. Then, for each of the ten iterations, the 117 regions are sorted out by their AUCs, following a descendent order. The ﬁrst ten regions are chosen for the 10 iterations: a region is then discriminant if this is present at least in 7 out of the 10 iterations. Test 2.a is performed for identifying discriminant regions using ABIDE I sample, while Test 2.b does the same using ABIDE II sample.
- Experiment 3: The aim of this experiment is to illustrate the ability of the proposed representation to highlight diﬀerences between ASD patients and control subjects under certain conditions. Test 3.a seeks to visualize global shape diﬀerences or local textural patterns by using information from one sub-band (Curvelet coeﬃcients), and Test 3.b seeks illustrates how the Curvelet sub-band distribution is independent of the particular age or scanner. For this evaluation, the highest scoring regions from Experiment 2 are selected as well as the associated Curvelet sub-bands showing signiﬁcant diﬀerences between the two groups.
- Experiment 4: The aim of this experiment is to compare the proposed representation with three classic measures (normalized volume, thickness and curvature), which have been broadly used for identifying brain regions that exhibit diﬀerences between ASD and control individuals76,148. Test 4.a presents classiﬁcation performance using separately four descriptors (the proposed one and each classic measure), and Test 4.b computes and illustrates the correlation between the Curvelet descriptor and the three classic measures.

### 5.3. Results

##### 5.3.1. Experiment 1

Figure 5-3 shows the classiﬁcation results when the model is trained with the ABIDE II sample and tested with the ABIDE I under a hold-one-out validation scheme (cases individually tested), obtaining AUC scores of 0,69 (right parahippocampal gyrus) and 0,65 (left inferior frontal gyrus) with an RBF and a linear kernel, respectively. In addition, sensitivity of 0,77 and speciﬁcity of 0,59 were obtained when using an RBF kernel. The RBF kernel model outperformed the linear one. In addition, regions with the highest AUC scores are illustrated within each brain. Interestingly, an AUC score of 0,69 demonstrates this model is quite robust to diﬀerent sources of variability since ABIDE is a non-homogeneous data set, i.e., this is multicentric data collection.

Proposed: Linear Kernel

Cortical Area

09

05

02 02

08

06

Proposed: RBF Kernel

Cortical Area

09

05

02

08

08

04

06 07

03

|01 R. Parahippocampal Gyrus (PD)<br><br>02 L. Inferior Frontal Gyrus (PT)<br><br>03 R. Temporal Occipital Fusiform C.<br><br>04 L. Middle Temporal Gyrus (AD)<br><br>05 R. Central Opercular C.<br><br>06 R. Occipital Fusiform Gyrus<br><br>07 R. Inferior Temporal Gyrus (PD)<br><br>08 R. Occipital Pole<br><br>09 R. Angular Gyrus<br><br><br>0.69<br><br>0.67 0.67 0.66 0.66 0.63 0.63 0.63 0.62<br><br>0.59 0.65 0.60 0.53 0.64 0.63 0.53 0.62 0.61<br><br>Color Legend AUC<br><br>RBF Linear|
|---|

Figure 5-3.: Classiﬁcation results when the model is trained using the ABIDE II sample and tested using the ABIDE I. At the top, each brain illustrates regions with the highest AUC scores obtained with an RBF and a linear kernel, respectively. At the bottom, the corresponding AUC scores are presented with the color code associated to each brain region. Abbreviations: right (R), left (L), cortex (C), anterior division (AD), posterior division (PD), pars triangularis (PT).

##### 5.3.2. Experiment 2

- Test 2.a: Figure 5-4 illustrates the resultant discriminant brain regions when using the ABIDE I sample: the upper two brains illustrate regions obtained with an RBF kernel, while the bottom ones show regions obtained with a linear kernel. This test provided regions widely reported as related with ASD, like caudate, inferior frontal gyrus, temporal occipital fusiform cortex and angular gyrus13,102,139, the three latter regions also showed up in Experiment 1. Interestingly, the set of discriminant regions and estimated AUC scores are quite similar independently of the particular used kernel, i.e., the proposed descriptor yields an average AUC of 0,75 ± 0,03 (95% conﬁdence interval: 0,74 − 0,78) for the right supramarginal gyrus (anterior division) with an RBF kernel, and an average AUC of 0,75±0,02 (95% conﬁdence interval: 0,74 − 0,77) with a linear kernel for the same region, as shown in Figure 5-4. In addition, sensitivity/speciﬁcity scores of 0,68/0,71 and 0,76/0,82 were obtained for this top region when using an RBF and a linear kernel, respectively.

Proposed: RBF Kernel

Cortical Area Sub-Cortical Area

03

08

01 04

05

02

07

09

06

Proposed: Linear Kernel

Cortical Area Sub-Cortical Area

03 01

08 04

05

02

07 10

09

06

|0.65±0.03<br>0.66±0.02<br><br>0.72±0.02<br><br>0.62±0.06<br><br>0.75±0.03<br><br>0.70±0.05 0.68±0.02<br><br>0.67±0.02<br><br>0.65±0.04<br><br>0.68±0.10<br><br><br>RBF<br><br>08 R. Middle Frontal Gyrus 0.65±0.03<br><br>07 R. Occipital Pole 0.64±0.03<br><br>02 L. Angular Gyrus 0.71±0.02<br><br>01 R. Supramarginal Gyrus (AD)<br><br>03 L. Juxtapositional Lobule C.<br><br>04 R. Fusiform Operculum C.<br><br>06 R. T. Occipital Fusiform C.<br><br>09 L. Inferior Frontal Gyrus (PT) 10 L. Intracalcarine C.<br><br>05 L. Caudate<br><br><br><br><br>0.75±0.02<br><br>0.71±0.03 0.68±0.01<br><br>0.66±0.03<br><br>0.66±0.05 0.65±0.05<br><br>0.72±0.05<br><br><br>Color Legend AUC<br><br>Linear|
|---|

Figure 5-4.: Discriminant regions when evaluating the proposed multiscale descriptor with the ABIDE I sample: the upper two brains stand for an RBF kernel while the bottom ones represent a linear kernel. The corresponding AUC scores and the associated standard deviations are displayed in the legend. The color code associated to the set of relevant regions is also displayed. Abbreviations: right (R), left (L), cortex (C), temporal (T), anterior division (AD), pars triangularis (PT).

Test 2.b: Similarly, Figure 5-5 shows the resultant discriminant regions when using the ABIDE II sample. The brains represent results obtained when the SVM model is trained with an RBF or a linear kernel. Some of the resultant regions have been reported as being related to ASD, such as superior temporal gyrus and temporal fusiform cortex17,112, the latter also showed up in Experiment 1. AUC scores and the associated standard deviations are shown at the bottom of the ﬁgure. Note the proposed multiscale descriptor provided an average AUC of 0,77 ± 0,04 (95% conﬁdence interval: 0,75 − 0,80) for the left superior temporal gyrus (anterior division) when using an RBF kernel, and 0,77 ± 0,04 (95% conﬁdence interval: 0,74 − 0,80) for the same region with a linear kernel, as shown in Figure 5-5. In addition, sensitivity/speciﬁcity scores of 0,73/0,80 and 0,74/0,71 were obtained for this top region when using an RBF and a linear kernel, respectively.

###### Proposed: Both Kernels

Cortical Area

06

07 02

01

05

03

Sub-Cortical Area

04

05

|01 L. Superior Temporal Gyrus (AD)<br><br>02 L. Supracalcarine Cortex<br><br>03 R. Temporal Fusiform Cortex (AD)<br><br>04 R. Lateral Ventrical<br><br>05 L. Middle Temporal Gyrus (PD)<br><br>06 L. Precuneous Cortex<br><br>07 L. Cuneal Cortex<br><br><br>0.77±0.04 0.75±0.04 0.70±0.04 0.66±0.03 0.65±0.03 0.65±0.03 0.64±0.03 0.70±0.02<br><br>0.77±0.04 0.73±0.03 0.69±0.04 0.64±0.04 0.63±0.05 0.63±0.07<br><br>Color Legend AUC<br><br>RBF Linear|
|---|

Figure 5-5.: Discriminant regions when evaluating the proposed approach with the ABIDE II sample: the same set of brain region was obtained using an RBF or a linear kernel. Color code is in this case diﬀerent since the identiﬁed regions are not exactly the same as the ones resulting when evaluating with the ABIDE I sample. Notice just one discriminant sub-cortical region was obtained. Abbreviations: right (R), left (L), cortex (C), anterior division (AD), posterior division (PD).

##### 5.3.3. Experiment 3

- Test 3.a: Figure 5-6 shows the visual diﬀerences when using two brain regions, the right supramarginal gyrus (A) and the left superior temporal gyrus (B), speciﬁcally using a sub-

band located at the 4th scale and 98π of orientation. For each block, the ﬁrst row corresponds to ASD patients while the second one stands for control subjects. The ﬁrst two columns

illustrate the selected region and the third column shows the reconstructed region volume after using only the relevant Curvelet sub-band. The Curvelet is by nature a multiscale representation, and therefore it naturally separates spatial information at diﬀerent levels of resolution or scales. The aim of this analysis is then to highlight diﬀerences at several scale levels and characterize this disorder in terms of global shape diﬀerences or local textural patterns. The purpose of this ﬁgure is not an interpretation of the diﬀerences, but rather an illustration of the larger visual diﬀerences between the two reconstructed versions of analysis in the third column than between the two ﬁgures in the second column.

B. Original Volume

Region Reconstructed with a subband

A. Original Volume

Reconstructed with a subband

Region

|Control<br><br>Color Legend<br><br>ASD|
|---|

- Figure 5-6.: A: the right supramarginal gyrus (anterior division) while B: the left superior temporal gyrus (anterior division). For each block, ﬁrst two columns illustrate the original volume of the selected region and the third column shows the reconstructed region volume after using a particular sub-band. Each volume represents a subject of a particular class, i.e., ASD patients (orange) or control subjects (blue).

Test 3.b: Figure 5-7 illustrates the spread parameter for 3 Curvelet sub-bands (the ones with p − value < 0,01) from the left superior temporal gyrus. In this ﬁgure, each column represents one of the three sub-bands (the standard deviation of the GGD) as follows: ﬁrst row displays the two groups, ASD (green) and control (orange) subjects, while second and

third rows represents the same groups (same color convention) but distributed by age and scanner (center), respectively. This test demonstrates the same curved characteristic is shifted for the two groups, in this case subtle shape diﬀerences. Speciﬁcally, ﬁrst and second rows demonstrate separability between ASD and control individuals independently of their age following a particular trend, i.e., ASD overall show lower values w.r.t. controls. Regarding scanner, similar values are observed between the group of controls, yet the third and fourth centers report only two and one individuals, respectively. This analysis was extended by performing an ANOVA test, restricted by the diﬀerences in the number of subjects among centers, i.e., three rounds of ANOVA evaluations were performed between the two centers with at least ten individuals as follows: 11 cases from GU vs three random sets of 11 cases from KKI. All computed p-values demonstrate there are no signiﬁcant diﬀerences between scanners: p-values were higher than 0,05 (0,98, 0,49 and 0,99).

##### 5.3.4. Experiment 4

- Test 4.a: Normalized volume was computed with the same parcellation used in the proposed approach, the Harvard-Oxford atlas (HO)111, while thickness and curvature were computed with a diﬀerent parcellation, the Desikan Killiany atlas (DKT)54 since FreeSurfer55, a widely used software, has already implemented a standard pipeline for computing these measures. Because of the use of two atlas, an approximated relation between them was established. A SVM model was separately trained per descriptor. Table 5-2 shows the comparison between the proposed Curvelet approach and each computed measure. In this table, ﬁrst column stands for the relevant regions with HO atlas (obtained in Test 2.b) while the fourth one stands for the approximated regions in the DKT atlas. The remaining columns presents AUC scores when using: Curvelet approach (second), normalized volume (third), thickness (ﬁfth), and curvature (sixth). As expected, the classiﬁcation performance between the Curvelet approach and each classic measure was quite diﬀerent, suggesting the proposed representation captures diﬀerent brain features and patterns, probably local-global discontinuities of the curves outlining the region, not only geometric global estimations like the curvature or the thickness.
- Test 4.b: All the Curvelet sub-bands from the left superior temporal gyrus were analyzed by computing the Pearson correlation coeﬃcient between each sub-band and each classic measure. Figure 5-8 illustrates these results for 3 Curvelet sub-bands (p < 0,01, t-test), evidencing nonlinear correlation between the Curvelet representation and each of the traditional measures. This analysis conﬁrmed the Curvelet approach and the computed measures are describing brain regions in diﬀerent ways, i.e., while the normalized volume is capturing diﬀerences in terms of the region size without any information about shape or the curva-

0.18

0.175

0.20

0.16

0.150

0.14

0.125

0.15

alfaSB10

alfaSB17

alfaSB31

0.12

0.100

0.10

0.10

0.08

0.075

0.06

0.050

0.05

0.04

0.025

ASD CNT

ASD CNT

ASD CNT

Dx

Dx

Dx

0.18

0.175

0.20

0.16

0.150

0.14

0.125

0.15

alfaSB31

alfaSB10

alfaSB17

0.12

Dx

Dx

Dx

0.100

ASD CNT

ASD CNT

ASD CNT

0.10

0.10

0.08

0.075

0.06

0.050

0.05

0.04

0.025

7-8 9-10 11-13

7-8 9-10 11-13

7-8 9-10 11-13

ageRange

ageRange

ageRange

0.18

0.175

0.20

0.16

0.150

0.14

0.125

0.15

alfaSB31

alfaSB17

alfaSB10

0.12

Dx

Dx

Dx

0.100

ASD CNT

ASD CNT

ASD CNT

0.10

0.10

0.08

0.075

0.06

0.050

0.05

0.04

0.025

GU KKI UCD SDSU

GU KKI UCD SDSU

GU KKI UCD SDSU

center

center

center

- Figure 5-7.: Curvelet-based feature analysis. Each column represents a Curvelet sub-band, while the rows stand for: control and autism groups (ﬁrst), the control and autism groups distributed by age ranges (second), and the control and autism groups distributed by scanner/center (third). Green color corresponds to autism spectrum disorder patients (ASD) while orange corresponds to controls subjects (CNT).

ture characterizes a region by approximating a global folding of the surface, the Curvelet approach instead is describing local and regional curves and their edges and discontinuities

- at diﬀerent neighboring levels.

Table 5-2.: From left to right, relevant regions with the Harvard Oxford (HO) atlas obtained with Curvelet approach (ﬁrst), AUC scores when using the Curvelet approach (second) and the normalized volume (third), approximated regions from the Desikan Killiany (DKT) atlas that correlate with the HO atlas (forth), AUC scores when using the thickness (ﬁfth) and the curvature (sixth). Abbreviations: proposed strategy (Prop), normalize volume (Vol), thickness (Thick), curvature (Curv), left (L), right (R), gyrus (G), cortex (C).

|Regions HO Atlas<br><br>|AUC Prop<br><br>|AUC Vol|Regions DKT Atlas<br><br>|AUC Thick|AUC Curv|
|---|---|---|---|---|---|
|L. Superior Temporal G.<br><br>|0.77<br><br>|0.61|L. Superior Temporal<br><br>|0.51<br><br>|0.55|
|L. Supra calcarine C.<br><br>|0.75|0.51<br><br>|L. Peri calcarine<br><br>|0.65|0.49|
|L. Middle Temporal G.|0.71|0.52<br><br>|L. Middle Temporal|0.53|0.66|
|R. Temporal Fusiform C.<br><br>|0.71|0.49<br><br>|R. Fusiform<br><br>|0.34|0.55|
|L. Inferior Temporal G.|0.67<br><br>|0.56<br><br>|L. Inferior Temporal|0.43<br><br>|0.67|
|L. Precuneous C.|0.67<br><br>|0.56|L. Precuneus|0.56<br><br>|0.59|
|R. Para hippocampal G.|0.67<br><br>|0.42<br><br>|R. Para hippocampal|0.53<br><br>|0.62|
|L. Cuneal C.<br><br>|0.66|0.56<br><br>|L. Cuneus<br><br>|0.51|0.44|
|L. Temporal Fusiform C.<br><br>|0.65|0.53|L. Fusiform<br><br>|0.50|0.60|

##### 5.3.5. Computational performance

All the experiments were implemented in MATLAB R18a (Mathworks Inc.), running on a Centos Server with 2 Intel Xeon CPU at 2.2 GHz and 256 GB of RAM. Computational performance was separately assessed by the two processes required to compute the proposed descriptor, namely the multiscale analysis and the dimensionality reduction. Brain regions were described using the 2D Fast Discrete Curvelet Transform (FDCT) implementation (approximately 195,7 ms per case) while the dimensionality reduction was performed using the Generalized Gaussian Distribution (about 52 ms per case). Therefore, computational time for running the proposed descriptor per case is approximately 0,25 s, a quite low computational cost.

0.30

|pe|arsonr|= -0.194|
|---|---|---|

|pe|arsonr|= -0.153|
|---|---|---|

|pe|arsonr|= -0.082|
|---|---|---|

0.25

0.20

0.20

0.20

0.15

0.15

[Figure 126]

[Figure 127]

[Figure 128]

alfaSB10

alfaSB17

alfaSB31

0.15

0.10

0.10

0.10

0.05

0.05

0.05

0.00

0.00

0.00

0.04 0.06 0.08 0.10 0.12 0.14 0.16 0.18

0.04 0.06 0.08 0.10 0.12 0.14 0.16 0.18

0.04 0.06 0.08 0.10 0.12 0.14 0.16 0.18

normVol

normVol

normVol

0.30

|pearso|nr= -0.070|
|---|---|

|pearso|nr= -0.182|
|---|---|

|pearso|nr= -0.145|
|---|---|

0

2

5

0.25

0.20

0.20

[Figure 129]

0.20

[Figure 130]

[Figure 131]

0.15

0.15

alfaSB10

alfaSB17

alfaSB31

0.15

0.10

0.10

0.10

[Figure 132]

0.05

0.05

0.05

0.00

0.00

0.00

2.4 2.6 2.8 3.0 3.2 3.4 3.6

2.4 2.6 2.8 3.0 3.2 3.4 3.6

2.4 2.6 2.8 3.0 3.2 3.4 3.6

thickness

thickness

thickness

0.30

|pear|sonr=|
|---|---|

-0.001

|pear|sonr=|
|---|---|

|pear|sonr=|
|---|---|

-0.103

-0.010

0.20

0.25

0.20

[Figure 133]

0.20

[Figure 134]

0.15

0.15

alfaSB31

alfaSB10

alfaSB17

0.15

[Figure 135]

0.10

[Figure 136]

0.10

0.10

0.05

0.05

0.05

0.00

0.00

0.00

0.08 0.09 0.10 0.11 0.12 0.13 0.14

0.08 0.09 0.10 0.11 0.12 0.13 0.14

0.08 0.09 0.10 0.11 0.12 0.13 0.14

curvature

curvature

curvature

- Figure 5-8.: Relationship between three Curvelet sub-bands (each column) and classical measures like normalized volume (ﬁrst row), thickness (second row) and curvature (third row).

### 5.4. Discussion

This work introduces a multiscale descriptor that characterizes anatomical brain regions in terms of their very basic geometric properties and highlights those ones with diﬀerences between ASD and control subjects. This descriptor has shown to be useful in terms of:

5.4 Discussion 57

- 1. It uses the Curvelet transform to characterize brain regions and the Generalized Gaussian Distribution to reduce dimensionality.
- 2. It quantiﬁes local-regional changes in brain regions by using a 2D multislice image, aiming to capture local-regional edges and other singularities along brain curves in the Curvelet space and hence it sparsely describes atypical brain folding.
- 3. It is evaluated in heterogeneous sets of data which proves generalization.

In addition, at analyzing a 3D region by placing together each of the 3D slices in a plane, regional geometric 3D dependencies are characterized and quantiﬁed. Most of these changes are usually masked in pathology conditions by conventional 3D measures like the volume or the equivalent curvature. This approach instead captures such relationships and express them in terms of local-regional geometric features which in addition are multiscale by nature. The rest of the discussion is organized in two parts: the relation between the identiﬁed relevant regions and the ASD, and a comparison between the obtained results and state-of-the-art strategies (including deep learning approaches).

The proposed Curvelet approach identiﬁed a set of relevant regions, most of them widely reported in the literature as relevant in ASD. Some studies have suggested Broca’s and Wernicke’s areas are commonly aﬀected in ASD individuals, i.e., brain regions involved in producing and understanding language84,165. Parcelled regions within the Broca’s area are revealed by the proposed descriptor, they are the parahippocampal gyrus, the inferior frontal gyrus, the fusiform cortex and the superior temporal gyrus, while those ones contained in the Wernicke’s area are also identiﬁed with the Curvelet descriptor, they are the inferior frontal gyrus, the supramarginal gyrus and the angular gyrus. In addition, the proposed approach also distinguished the juxtapositional lobule cortex region, a part of the supplementary motor area, which has been reported to correlate with ASD129.

Table 5-3 compares the results obtained using the proposed Curvelet approach against stateof-the-art methods (studies using ABIDE I). In this table, each row shows results for a particular method as follows: the ﬁrst part (columns 2-4) presents information about the dataset and the last part (column 5) shows the computed AUC score per method. The proposed approach demonstrates to be competitive with state-of-the-art methods, yet this comparison is not completely fair since the validation sample is in general diﬀerent. In consequence, for comparison purposes, most approaches took diﬀerent cases, i.e., some of them built homogeneous samples (containing cases from a single center, a reduced number of centers or using the same scanner) or non-homogeneous samples (when the capturing conditions or centers are otherwise), being the latter our case.

Regarding homogeneous datasets, Retico et al.131 collected a number of cases with their own

Table 5-3.: Comparison between results obtained with the proposed approach and state of the art methods assessed with ABIDE dataset. Abbreviations: control (CRT), autism spectrum disorders (ASD), area under the receiver operator curve (AUC).

| |CNT|ASD<br><br>|Age|AUC|
|---|---|---|---|---|
|Wang158|54|57|<15<br><br>|0.80 *|
|Katuwal82<br><br>|373|371<br><br>|NR|0.60|
|Katuwal80<br><br>|361|373<br><br>|7 - 64|0.68|
|Parisot125|468<br><br>|403<br><br>|6 to 64|0.75|
|Li95<br><br>|149|161<br><br>|10 to 34<br><br>|0.74|
|Proposed|151|151|6 - 13<br><br>|0.75 - 0.77 **|

- * This result was obtained with cases from a single center: the NYU Langone Medical Center.
- ** This result corresponds to Tests 2.a and 2.b.

scanner and characterized ASD using surface-based features, achieving AUC scores of 0,74 (male) and 0,68 (female), not shown in Table 5-3 since ABIDE is not used. Wang et al.158 built a dataset by selecting subjects from a single center of ABIDE I (the NYU Langone Medical Center) and used a canonical correlation analysis over gray and white matter, obtaining the best reported result, an AUC of 0,80±0,02. Sato et al.137 collected samples captured with the same scanner technology (Siemens 3T TimTrio). In this study, voxel-based morphometry methods were used for characterization and two classiﬁcation tests were performed: using the whole brain and per region. The ﬁrst test provided sensitivity of 0,58 and speciﬁcity of 0,72, while the second one reported sensitivity of 0,81 and speciﬁcity of 0,81 (using a set of regions reported to be part of the Social Network), not shown in Table 5-3 since ABIDE is not used. The task performed by these investigations is certainly much less diﬃcult than ours since they decreased some variability sources yet the herein obtained classiﬁcation performance is competitive with respect to the strategies aforementioned. Moreover, an additional test was performed using the proposed multiscale descriptor and a small set of data from ABIDE II (24 cases from a single center, the Kennedy Krieger Institute - KKI, 12 ASD patients and 12 control subjects) to carry out the binary classiﬁcation under a 3-fold cross validation scheme, obtaining a maximum AUC of 0,88. This expected result was reached under similar experimentation conditions to whom have reported similar ﬁgures and, although under such restricted setup classiﬁcation results do improve, such model may be hardly generalizable.

In terms of non-homogeneous datasets, Katuwal et al.82 assessed a morphometry-based

5.5 Conclusions 59

method by using an heterogeneous dataset, exhibiting low performance, an AUC of 0,60. Katuwal et al.80 proposed a method that correlates morphometry features and patient data (e.g. age and verbal intelligence quotient), obtaining an AUC of 0,68. Interestingly, these works provide evidence about the inﬂuence of using heterogeneous dataset (high data variability). The proposed strategy can be included within this category since it was assessed using heterogeneous children samples from ABIDE, providing AUC scores of 0,75 and 0,77 for ABIDE I and II respectively, and 0,69 when training with ABIDE II and testing with ABIDE I. Following the same approach of using non-homogeneous data, a ﬁnal test was performed by combining ABIDE I and ABIDE II samples into a single one and carrying out a 10-fold cross validation, obtaining an AUC of 0,75 and a set of relevant regions (most of them exactly the same described in Experiments 1 and 2). These results demonstrated the proposed approach is competitive w.r.t. baseline methods when using non-homogeneous datasets.

This last part of the discussion is devoted to the use of deep learning strategies, regardless of whether it is evaluated with homogeneous or non-homogeneous data. Note the following studies use other information sources and the T1-MRI. Parisot et al.125 used a Graph Convolutional Network framework to detect anomalies associated to ASD by combining MRI and phenotypic data, reporting an AUC of 0,75. Akhavan et al.3 trained a deep belief network with structural and functional MRI data of 185 individuals (between 5 to 10 years) from ABIDE, obtaining an accuracy of 0,65 (not shown in Table 5-3 since AUC score is not reported). Li et al.95 used a deep transfer learning neural network with functional MRI data from 4 centers of ABIDE, obtaining a maximum AUC of 0,74. These studies basically demonstrated data availability (e.g. functional MRI, phenotypic data) plays a crucial role for ASD characterization since rather than a disease, this set of symptoms and signs is considered a disorder with a huge variability. The present analysis is nevertheless focused only in structural images, while most studies have mainly used brain representations from selected regions of interest (e.g. brain parcellations deﬁned by anatomical atlases built by experts) to characterize the disease. Some deep learning approaches have aimed to ﬁnd out anatomical landmarks to reduce the variability introduced by such particular brain parcellations104,105. Yet this might help to improve the automatic classiﬁcation, its utility might be limited since these landmarks could hardly correlate with a functional meaning that helps out clinicians to improve their disease understanding and therefore patient management.

### 5.5. Conclusions

This paper introduced a multiscale descriptor that uses a 2D representation and the Curvelet transform to characterize brain regions and identify those ones with diﬀerences between

groups which ended up in the present investigation by being widely reported in the literature as characteristic of ASD, a side eﬀect that may facilitate any ASD quantiﬁcation. This work demonstrated the presented multiscale descriptor highlights diﬀerent features and patterns when comparing with classic measures, probably local-global edges and discontinuities of spatial curves within the region. In addition, it also demonstrated to be competitive with respect to state-of-the-art strategies, including those based on the deep learning, evaluated with heterogeneous databases containing magnetic resonance images with diﬀerences in the number of slices per volume, in the inter-slice distance, in the image resolution and in the scanner protocol, i.e., robust to inter-center variability. Finally, the multiscale descriptor is simple in conceptual terms and shows a low computational cost when characterizing a MRI scan, approximately a quarter of a second. As a future work, a complete pipeline that allows to perform a subject-wise classiﬁcation is planned, as well as the inclusion of other sources of information to characterize ASD like neuropsychological tests, phenotypic data, and functional MRI examinations.

# 6. Conclusions and perspectives

### 6.1. Conclusions

This thesis work presented contributions in the use of higher-order representations in two medical problems which are radiomics characterization of Prostate Cancer and Autism Spectrum Disorder using prostate and brain MRI.

Regarding prostate cancer characterization, the proposed Adaptive Frequency Saliency Model (AFSM) was able to be used as a pre-processing step to outperform a baseline method in the classiﬁcation of prostate cancerous vs non cancerous tissue in MRI showing higher accuracy 0,776±0,036 vs 0,792±0,016. Nonetheless, several repetitions of these experiments concluded that this improvement is not statistically signiﬁcant, which is one main limitation of the presented approach. An additional remark is the small sample size in which the model was trained and evaluated on. Due to that, it required an extensive use of data augmentation and ﬁnally, as the AFSM was used on one random patch per class instead of using all patches of the training set, a more exhaustive evaluation of this method by running this model on all patches from the training set could lead to improvements of this approach in the future.

The second method, was able to manipulate the phase space of the Fourier transform to analyze the spatial support of cancerous and healthy tissue in prostate MRI. Results suggested how spatial support is captured during model training by aﬀecting classiﬁcation performance when using it to preprocess the dataset. Interestingly, when healthy tissue was used, classiﬁcation performance improved. Nevertheless, this method has some limitations, with the ﬁrst one being that phase estimation was done by using a random subject instead of ﬁnding a way to eﬀectively use the information of the training set. Secondly, the analysis of the spatial support of cancerous tissue may have been aﬀected by the way the dataset was annotated i.e, as the dataset only provided central coordinates of the lesion instead of a ROI, some surrounding tissue may change the way its spatial support distributes.

In the case of ASD characterization methods using Zernike Moments and the Curvelet Transform in region-wise analyses, they were able to contribute to the state of the art. Both cases yielded a performance of of 0,77 and 0,75 for cross validation tests in ABIDE I and II. In

62 6 Conclusions and perspectives

the case of the curvelet transform a hold out validation was able to still suggest discriminative power with an AUC 0,69 for the top performer region Right parahippocamapal gyrus posterior division and the correlation analysis against voxel based morphometry proved how this descriptor is highlighting diﬀerent patterns, probably textures and curved discontinuities of the region. In the case of the Zernike approach, one limitation was that the provided description was not multi-scale and those features mostly correlated with shapes which may explain how smaller regions were diﬃcult to obtain as relevant using this approach. As a way to solve both limitations the approach with the Curvelet Transform was done as those features are not only able to describe shapes but also textures and curved discontinuities.

### 6.2. Future work

For the case of prostate cancer, one perspective is to try again both pipelines by using the revised and annotated ProstateX v1 that was recently published34. It contains speciﬁc ROI’s that may allow to conduct better the analysis of spatial support of cancerous tissue in the phase space approach.

In the case of the characterization of ASD and due to the promising results obtained with the Curvelet approach, an evaluation with larger cohorts including diﬀerent age ranges is proposed as future work, so is the inclusion of more subjects with diﬀerent capture protocols such as diﬀerent voxel sizes to conduct larger studies.

# A. Appendix: Diﬀerentiating Cancerous and Non-cancerous Prostate Tissue Using Multi-scale Texture Analysis on MRI

This collaboration presents a multi-scale characterization strategy for prostate cancer in MRI based on the Curvelet Transform to detect areas with high probability of prostate cancer, either in the peripheral zone or the anterior ﬁbromuscular stroma. For doing so tissue patches were extracted from structural T2 MRI and to characterize each patch the curvelet transform is computed and its features are reduced using generalized Gaussian distributions, and then, a reduction of the feature space is performed by doing multiple hypothesis tests (t-test). This characterization is evaluated under a 10 fold cross validation with the AUC metric, obtaining results for for the peripheral zone, anterior stroma and the whole prostate of 0,85, 0,91, 0,87 respectively. A complete version of this collaboration has been accepted for publication as a research article in the proceedings of 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (see reference5).

### A.1. Introduction

Prostate cancer (PCa) is the second most commonly diagnosed cancer, with 13.5% of the total of cases in 2018 (approximately 1.3 million)20. The protocol for detecting PCa starts with detection of altered clinical biomarkers (prostate speciﬁc antigen test and digital rectal exam), followed by radiologic examination (transrectal ultrasound, magnetic resonance imaging), within ﬁnal conﬁrmation via biopsy procedures22. Examination of the extracted tissue yields the ﬁnal diagnosis, i.e., whether cancer is present and its corresponding grade49.

Although biopsy is the most reliable test to conﬁrm the presence of cancer, this invasive procedure is not exempt from complications: 1) a large set of samples is required: in average 12 to 14 samples are removed, a process that may take about 10 to 20 minutes120; 2) adverse

H

[Figure 137]

PCa

Tissue Patch

Healthy (H)

Classification

𝛼𝑖 𝛽𝑖 𝜇𝑖

𝑆𝐵𝑖

| | |
|---|---|
| | |

𝛽𝑖

| | |
|---|---|
| | |

𝑆𝐵1

T-test

𝑆𝐵𝑖

𝛼𝑖 𝛽𝑖 𝜇𝑖

𝛼𝑖

𝜇𝑖

Prostate Cancer (PCa)

Curvelet

Generalized Gaussian

Feature

Relevant

Transform

Pdf estimation

Tables

Subbands

Figure A-1.: Patch of prostate tissue is extracted using the 3D tumor central point annotated by the expert, that is then decomposed by using a multiscale representation (the Curvelet transform). The coeﬃcient distribution per Curvelet subband is represented by three parameters, the relevance per subband is computed, and ﬁnally, diﬀerent classiﬁcation models are constructed to evaluate the representation in the task of diﬀerentiating healthy from cancer tissue patches.

eﬀects: biopsy could produce serious events like infection or bleeding48; and 3) false-negative results: even if many samples are extracted, biopsies can still miss the cancer area, resulting in repeated biopsy procedures119. In particular, a very high rate of false negative biopsies of the prostate has been reported (up to 20%141); a rate likely worse for early-stage prostate cancers. This has led to increasing use of magnetic resonance imaging (MRI) to provide a macro-view of the whole prostate as well as identifying cancer-suspicious locations, as a triage before any invasive procedure.

This problem has been so far approached as a cancer and non-cancer prostate classiﬁcation, and several studies have tried to categorize prostate cancer grades93. These methods achieved such classiﬁcation mainly based on learning strategies or radiomic features. Regarding learning strategies, Wang et al.159 and Yang et al.164 used fully and co-trained convolutional neural networks, respectively, while Lehaire et al.92 performed cancer detection using sparse dictionary learning (DL). On the other hand, radiomics-based strategies have been widely applied, describing the prostate in terms of shape21, texture53,154, histogram statistics155 or a combination of them156.

This work introduces multiscale radiomic features that can be used to detect areas with high probability of prostate cancer, either in the peripheral zone or the anterior ﬁbromuscu-

A.2 Methods 65

lar stroma. The goal of our proposed features is to capture local patterns that diﬀerentiate cancer from non-cancer locations in diﬀerent prostate zones, by mapping the information from prostate patches to the Curvelet space. The proposed approach was validated by automatically classifying cancer and non-cancer MRI patches culled from 84 patients in the Prostate-X2 Challenge dataset.

### A.2. Methods

Diﬀerent histological arrangements produce diﬀerent radiological patterns, this work has investigated how these histopathological conﬁgurations may be used to ﬁnd out radiological regions with high probability of containing cancer. Therefore, the proposed approach aims to identify such changes by selecting relevant information from a multiscale texture analysis. Figure A-1 illustrates the proposed strategy.

The Curvelet transform corresponds to a multi-scale analysis that approximates textures and complex geometrical structures24. This transformation decomposes information at different scales and diﬀerent directions. Formally, it is deﬁned as a convolution between radial R(ω) and angular Φ(ω) windows, being R(ω) the scale and Φ(ω) the phase along the radial direction23. In the Curvelet frequency space, a subband represents a portion of the frequency space (a direction for a particular scale) and the scaling law ensures the object proportion is conserved along diﬀerent scales. The Curvelet frequency-based representation was used in this work to describe each extracted patch, aiming to exploit texture information that matches with prostate tissue patterns.

In this investigation, the Curvelet decomposition comprises 4 scales and 16 directions, for a total of 81 subbands. Since each subband contains a diﬀerent number of frequency coeﬃcients (depending on the scale and direction), the Generalized Gaussian Distribution (GGD) is used to approximate the coeﬃcient distribution per subband, with each subband represented by 3 parameters (µ, β and ρ). Since not all the subbands provide relevant information, a Student’s t-test was then performed to select the most relevant subbands with a statistical signiﬁcance threshold of 0,05, i.e., at least two of the three subband parameters need to be statistically signiﬁcant to be included.

### A.3. Evaluation

##### A.3.1. Data

Data used in this research were obtained from The Cancer Imaging Archive (TCIA) sponsored by the SPIE, NCI/NIH, AAPM, and Radboud University100, a collection including multi-parametric magnetic resonance imaging (mpMRI) of 84 patients. Inter-case diﬀerences in the cohort include changing image resolution (from 320 × 320 to 640 × 640 pixels) as well as intensity range (from 693 to 1740 of pixel depth). The problem of image resolution diﬀerence was addressed by standardizing the size of the extracted patches, as it will be further explained in the experimental setup.

For each patient, one or more lesions (cancerous tumors) had been annotated by experts, for a total of 95 lesions. Each lesion is provided with: 1) a 3D coordinate indicating the center of the tumor (segmentation is not available), and 2) the prostate region where the lesion is located, either the peripheral zone (PZ) or the anterior ﬁbromuscular stroma (AS). From the total number of lesions, 50 are located in the peripheral zone and 45 in the anterior ﬁbromuscular stroma.

A 2D square prostate patch is extracted from each MRI volume. This is done by using the 3D coordinate tumor center provided by the expert to ﬁrst set the slice at the z coordinate and then extract a square ROI around this point in the orthogonal plane. Patches were similarly extracted for healthy locations in the prostate. Healthy tissue was selected from non-annotated areas in the two prostate zones. Speciﬁcally, when a case contained a lesion in the peripheral zone, a healthy tissue patch was extracted from the anterior ﬁbromuscular stroma area and vice versa. For having balanced classes, a total of 95 healthy patches were extracted, 50 for peripheral zone and 45 for anterior ﬁbromuscular stroma area.

##### A.3.2. Experimental setup

For this work, prostate characterization was performed only in T2W axial scans. A set of experiments was performed to evaluate the ability of the multi-scale Curvelet representation to distinguish cancerous and non-cancerous prostate tissue. For so doing, parameter tuning was required. Firstly, the patch size was adapted to the image resolution (for cancerous or non-cancerous prostate tissue), i.e., for an image of 320 × 320, a patch of 30 × 30 was extracted, and for an image of 640 × 640, a patch of 56 × 56 was likewise selected.

Features were evaluated via diﬀerent classiﬁer algorithms: Random forests, AdaBoost and Support vector machines (SVM) with two diﬀerent kernels, namely linear and radial basis

functions (RBF). Implementation details included: 1) for training SVM models, parameter conﬁguration (box-constraint and sigma) was performed using a Bayesian optimization147, and 2) for training decision tree models, AdaBoost and Random Forest, a set of 300 learning cycles were deﬁned for both, and a learning rate of 0,02 was set for the Adaboost method.

Experiments aimed to classify between cancerous and non-cancerous prostate tissue based on constructing diﬀerent zone-speciﬁc models: in the peripheral zone (PZ), in the anterior ﬁbromuscular stroma area (AS), or independently of the prostate zone (WP). All experiments were performed under a 10-fold (one fold held-out for testing) cross-validation scheme and assessed using the area under the curve (AUC).

### A.4. Results and Discussion

Once subband selection process was performed (Student’s t-test, p < 0,05), the set of subbands that were found to be statistically signiﬁcant is shown in Figure A-2. Note that the number of relevant subbands were found to be diﬀerent for the two prostate zones, i.e., 21 for PZ and 41 for AS. In PZ, subbands are concentrated in particular orientations, independent of the scale. However, the subband distribution in case of AS is more uniform along the frequency corona. For discriminating between healthy and cancer patches, independent of the anatomical zone, combination of the PZ and AS subbands was found to be most optimal.

| | |
|---|---|
| | |

| | |
|---|---|
| | |

(a) (b)

Figure A-2.: Resultant relevant subbands after the selection process for: (a) peripheral zone

- PZ, and (b) anterior ﬁbromuscular stroma - AS.

Classiﬁcation with the set of relevant subbands outperformed results obtained with the whole representation. For proving this, three classiﬁcation models were trained per anatomical region using a feature vector composed either by: 1) all the subbands or 2) statistically signiﬁcant subbands alone. Table A-1 shows classiﬁcation performance in terms of AUC

when using a particular set of prostate tissue patches coming from: 1) PZ, 2) AS, and 3) combining the two zones, i.e., the whole prostate (WP). These results show how the selected subbands improved the classiﬁcation using any of three models.

Table A-1.: Area under the curve (AUC) values for distinguishing cancerous and noncancerous tissue when using SVM, AdaBoost and Random Forest classiﬁcation models, and the proposed multiscale Curvelet features.

AUC with all the subbands

AUC with selected subbands

Classiﬁcation Model

SVM - Linear 0.84 0.85 SVM - RBF 0.79 0.80 AdaBoost 0.77 0.74 Random Forest 0.75 0.80

Peripheral zone (PZ)

SVM - Linear 0.89 0.91 SVM - RBF 0.84 0.88 AdaBoost 0.78 0.82 Random Forest 0.77 0.80

Anterior stroma (AS)

SVM - Linear 0.86 0.87 SVM - RBF 0.83 0.84 Adaboost 0.71 0.71 Random Forest 0.74 0.74

Whole prostate (WP)

Table A-1 also shows the dependence of the classiﬁcation on the particular anatomical area. The three models showed a better performance for AS, followed by PZ in case of Adaboost and Random Forest, and WP in case of SVMs. The best results were obtained using an SVM model with a linear kernel, with AUC scores of 0,85 for PZ, 0,91 for AS, and 0,87 for the WP.

A comparison between the proposed representation and the most common approaches reported in the literature was performed using four experiments: three using radiomic features and one using a convolutional neural networks (CNN). Radiomic-based experiments were conﬁgured using the set of features reported by Fehr et al.53, as being useful in separating healthy and cancerous tissue in T2W images: (i) using histogram statistics (mean, standard deviation, skewness and kurtosis), (ii) using Haralick texture features (energy, entropy, co-

rrelation, homogeneity and contrast), and (iii) using a combination of histogram statistics and Haralick texture features. For the convolutional neural network, an Inception V3 architecture was conﬁgured as follows: model shape structure (224 × 224), batch size (32), epochs (50), and image augmentation (re-scale, rotation, shifting, shearing, zooming and ﬂipping transformations). For these 4 experiments: 1) input images were the same extracted patches detailed in the proposed methodology, 2) classiﬁcations tests were independently performed per anatomical zone: PZ, AS and WP, and 3) for radiomic-based experiments, SVM with a linear kernel was used as classiﬁcation model.

Table A-2 presents results of these four experiments, showing the same trends as reported in

- Table A-1: best results when classifying cancer and healthy were observed for AS, followed by the ones for WP and the PZ, in that order. In addition, combination of texture features and histogram statistics outperformed results individually obtained, as well as those obtained with the CNN. Finally, these experiments demonstrate that the proposed multiscale texture descriptor outperformed results obtained when using histogram statistics, Haralick texture features, or CNN strategies.
- Table A-2.: AUC scores for distinguishing cancerous and non-cancerous tissue when using radiomics features (histogram statistics and texture features) or a convolutional neural network (Inception V3 architecture).

State of the art method

AUC

Histogram statistics (HS) 0.59 Haralick features (HF) 0.49 Combination HS and HF 0.51 Inception V3 CNN 0.63

Peripheral zone (PZ)

Histogram statistics (HS) 0.73 Haralick features (HF) 0.84 Combination HS and HF 0.84 Inception V3 CNN 0.79

Anterior stroma (AS)

Histogram statistics (HS) 0.62 Haralick features (HF) 0.67 Combination HS and HF 0.65 Inception V3 CNN 0.67

Whole prostate (WP)

### A.5. Conclusions

This work has presented an strategy that characterizes prostate tissue based on discriminant multiscale texture features, and demonstrated their application for identifying prostate regions with high probability of containing cancer, and therefore assist in the decision where and how to perform biopsy, via MRI. In addition, the multiscale analysis using the Curvelet transform was found to outperform histogram statistics, Haralick texture features, as well as a particular convolutional neural network architecture, in region-wise prostate cancer detection via MRI. Future work includes testing on larger and unbalanced datasets.

# Bibliografı´a

- [1] Afshar, P. ; Mohammadi, A. ; Plataniotis, K. N. ; Oikonomou, A. ; Benali, H.: From Handcrafted to Deep-Learning-Based Cancer Radiomics: Challenges and Opportunities. En: IEEE Signal Processing Magazine 36 (2019), Nr. 4, p. 132–160
- [2] Aggarwal, Shilpa ; Angus, Beth: Misdiagnosis versus missed diagnosis: diagnosing autism spectrum disorder in adolescents. En: Australasian Psychiatry 23 (2015), Nr. 2, p. 120–123
- [3] Aghdam, Maryam A. ; Sharifi, Arash ; Pedram, Mir M.: Combination of rs-fMRI and sMRI Data to Discriminate Autism Spectrum Disorders in Young Children Using Deep Belief Network. En: Journal of Digital Imaging 31 (2018), Mai, Nr. 6, p. 895–903
- [4] Alexeeff, Stacey E. ; Yau, Vincent ; Qian, Yinge ; Davignon, Meghan ; Lynch, Frances ; Crawford, Phillip ; Davis, Robert ; Croen, Lisa A.: Medical Conditions in the First Years of Life Associated with Future Diagnosis of ASD in Children. En: Journal of autism and developmental disorders 47 (2017), Nr. 7, p. 2067–2079
- [5] Alvarez-Jimenez, Charlems ; Barrera, Cristian ; Munera, Nicol´as ; Viswanath, Satish E. ; Romero, Eduardo: Diﬀerentiating Cancerous and Non-cancerous Prostate Tissue Using Multi-scale Texture Analysis on MRI. En: 2019 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) IEEE, 2019, p. 2695–2698
- [6] Alvarez-Jimenez, Charlems ; Munera-Garz´ on´ , Nicola´s ; Zuluaga, Maria A. ; Velasco, Nelson F. ; Romero, Eduardo: Autism spectrum disorder characterization in children by capturing local-regional brain changes in MRI. En: Medical physics 47

(2020), Nr. 1, p. 119–131

- [7] Amaral, David G. ; Schumann, Cynthia M. ; Nordahl, Christine W.: Neuroanatomy of autism. En: Trends in neurosciences 31 (2008), Nr. 3, p. 137–145
- [8] American Psychiatric Association [u. a.]: Diagnostic and statistical manual of mental disorders (DSM-5). American Psychiatric Pub, 2013

- [9] Andersson, Jesper L. ; Jenkinson, Mark ; Smith, Stephen [u. a.]: Non-linear registration, aka Spatial Normalisation FMRIB technical report TR07JA2. En: FMRIB Analysis Group of the University of Oxford 2 (2007), p. 1–21
- [10] Armato, Samuel G. ; Huisman, Henkjan ; Drukker, Karen ; Hadjiiski, Lubomir ; Kirby, Justin S. ; Petrick, Nicholas ; Redmond, George ; Giger, Maryellen L. ; Cha, Kenny ; Mamonov, Artem [u. a.]: PROSTATEx Challenges for computerized classiﬁcation of prostate lesions from multiparametric magnetic resonance images. En: Journal of Medical Imaging 5 (2018), Nr. 4, p. 044501
- [11] Auzias, G. ; Viellard, M. ; Takerkart, S. ; Villeneuve, N. ; Poinso, F. ; Fonseca´ , D. D. ; Girard, N. ; Deruelle, C.: Atypical sulcal anatomy in young children with autism spectrum disorder. En: NeuroImage: Clinical 4 (2014), p. 593–603
- [12] Baio, Jon ; Wiggins, Lisa ; Christensen, Deborah L. ; Maenner, Matthew J. ; Daniels, Julie ; Warren, Zachary ; Kurzius-Spencer, Margaret ; Zahorodny, Walter ; Rosenberg, Cordelia R. ; White, Tiﬀany [u. a.]: Prevalence of autism spectrum disorder among children aged 8 years—autism and developmental disabilities monitoring network, 11 sites, United States, 2014. En: MMWR Surveillance Summaries 67 (2018), Nr. 6, p. 1
- [13] Bastiaansen, Jojanneke A. ; Thioux, Marc ; Nanetti, Luca ; van der Gaag, Christiaan ; Ketelaars, Cees ; Minderaa, Ruud ; Keysers, Christian: Age-Related Increase in Inferior Frontal Gyrus Activity and Social Functioning in Autism Spectrum Disorder. En: Biological Psychiatry 69 (2011), may, Nr. 9, p. 832–838
- [14] Bauman, Margaret L. ; Kemper, Thomas L.: Neuroanatomic observations of the brain in autism: a review and future directions. En: International Journal of Developmental Neuroscience 23 (2005), Nr. 2, p. 183–187. – Autism: Modeling Human Brain Abnormalities in Developing Animal Systems. – ISSN 0736–5748
- [15] Bauman, Margaret L. ; Kemper, Thomas L.: Neuroanatomic observations of the brain in autism: a review and future directions. En: International Journal of Developmental Neuroscience 23 (2005), apr, Nr. 2-3, p. 183–187
- [16] Beig, Niha ; Khorrami, Mohammadhadi ; Alilou, Mehdi ; Prasanna, Prateek ; Braman, Nathaniel ; Orooji, Mahdi ; Rakshit, Sagar ; Bera, Kaustav ; Rajiah, Prabhakar ; Ginsberg, Jennifer ; et al.: Perinodular and Intranodular Radiomic Features on Lung CT Images Distinguish Adenocarcinomas from Granulomas. En: Radiology 290 (2019), Nr. 3, p. 783–792
- [17] Bigler, Erin D. ; Mortensen, Sherstin ; Neeley, E. S. ; Ozonoff, Sally ; Krasny, Lori ; Johnson, Michael ; Lu, Jeﬀrey ; Provencal, Sherri L. ; McMahon, William

- ; Lainhart, Janet E.: Superior Temporal Gyrus, Language Function, and Autism. En: Developmental Neuropsychology 31 (2007), mar, Nr. 2, p. 217–238
- [18] Blatt, Gene J. ; Fatemi, S. H.: Alterations in GABAergic Biomarkers in the Autism Brain: Research Findings and Clinical Implications. En: The Anatomical Record: Advances in Integrative Anatomy and Evolutionary Biology 294 (2011), sep, Nr. 10, p. 1646–1652
- [19] Brambilla, Paolo ; Hardan, Antonio ; di Nemi, Stefania U. ; Perez, Jorge ; Soares, Jair C. ; Barale, Francesco: Brain anatomy and development in autism: review of structural MRI studies. En: Brain research bulletin 61 (2003), Nr. 6, p. 557–569
- [20] Bray, Freddie ; Ferlay, Jacques ; Soerjomataram, Isabelle [u. a.]: Global Cancer Statistics 2018: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries. En: CA Cancer J Clin (2018)
- [21] Cameron, Andrew ; Khalvati, Farzad ; Haider, Masoom A. ; Wong, Alexander: MAPS: a quantitative radiomics approach for prostate cancer detection. En: IEEE Transactions on Biomedical Engineering 63 (2016), Nr. 6, p. 1145–1156
- [22] for Cancer (UK, National Collaborating C. [u. a.]: Prostate cancer: diagnosis and treatment. (2008)
- [23] Candes, Emmanuel ; Demanet, Laurent ; Donoho, David ; Ying, Lexing: Fast Discrete Curvelet Transforms. En: Multiscale Modeling & Simulation 5 (2006), jan, Nr. 3, p. 861–899
- [24] Candes, Emmanuel J. ; Donoho, David L.: Curvelets: A surprisingly eﬀective nonadaptive representation for objects with edges / Stanford Univ Ca Dept of Statistics.

2000. – Informe de Investigaci´on

- [25] Casanova, Manuel F. ; El-Baz, Ayman S. ; Kamat, Shweta S. ; Dombroski, Brynn A. ; Khalifa, Fahmi ; Elnakib, Ahmed ; Soliman, Ahmed ; AllisonMcNutt, Anita ; Switala, Andrew E.: Focal cortical dysplasias in autism spectrum disorders. En: Acta Neuropathologica Communications 1 (2013), Nr. 1, p. 67
- [26] Castillo T, Jose M. ; Arif, Muhammad ; Niessen, Wiro J. ; Schoots, Ivo G. ; Veenland, Jifke F. [u. a.]: Automated classiﬁcation of signiﬁcant prostate cancer on MRI: A systematic review on the performance of machine learning applications. En: Cancers 12 (2020), Nr. 6, p. 1606
- [27] Chaddad, Ahmad ; Daniel, Paul ; Niazi, Tamim: Radiomics evaluation of histological heterogeneity using multiscale textures derived from 3D wavelet transformation of multispectral images. En: Frontiers in oncology 8 (2018), p. 96

- [28] Chaddad, Ahmad ; Desrosiers, Christian ; Hassan, Lama ; Tanougast, Camel: Hippocampus and amygdala radiomic biomarkers for the study of autism spectrum disorder. En: BMC neuroscience 18 (2017), Nr. 1, p. 1–12
- [29] Chaddad, Ahmad ; Desrosiers, Christian ; Toews, Matthew: Multi-scale radiomic analysis of sub-cortical regions in MRI related to autism, gender and age. En: Scientiﬁc reports 7 (2017), Nr. 1, p. 1–17
- [30] Chaddad, Ahmad ; Desrosiers, Christian ; Toews, Matthew: Multi-scale radiomic analysis of sub-cortical regions in MRI related to autism, gender and age. En: Scientiﬁc Reports 7 (2017), mar, Nr. 1
- [31] Corino, Valentina D. ; Montin, Eros ; Messina, Antonella ; Casali, Paolo G. ; Gronchi, Alessandro ; Marchiano`, Alfonso ; Mainardi, Luca T.: Radiomic analysis of soft tissues sarcomas can distinguish intermediate from high-grade lesions. En: Journal of Magnetic Resonance Imaging 47 (2018), Nr. 3, p. 829–840
- [32] Cortes, Corinna ; Vapnik, Vladimir: Support-vector networks. En: Machine learning 20 (1995), Nr. 3, p. 273–297
- [33] Courchesne, Eric ; Karns, CM ; Davis, HR ; Ziccardi, R ; Carper, RA ; Tigue, ZD ; Chisum, HJ ; Moses, P ; Pierce, K ; Lord, C [u. a.]: Unusual brain growth patterns in early life in patients with autistic disorder: an MRI study. En: Neurology 57 (2001), Nr. 2, p. 245–254
- [34] Cuocolo, Renato ; Stanzione, Arnaldo ; Castaldo, Anna ; De Lucia, Davide R. ; Imbriaco, Massimo: Quality control and whole-gland, zonal and lesion annotations for the PROSTATEx challenge public dataset. En: European Journal of Radiology

(2021), p. 109647

- [35] Cuocolo, Renato ; Stanzione, Arnaldo ; Ponsiglione, Andrea ; Romeo, Valeria ; Verde, Francesco ; Creta, Massimiliano ; La Rocca, Roberto ; Longo, Nicola ; Pace, Leonardo ; Imbriaco, Massimo: Clinically signiﬁcant prostate cancer detection on MRI: A radiomic shape features study. En: European Journal of Radiology 116

(2019), p. 144 – 149. – ISSN 0720–048X

- [36] Dager, Stephen R. ; Wang, L ; Friedman, SD ; Shaw, DW ; Constantino, JN ; Artru, AA ; Dawson, G ; Csernansky, JG: Shape mapping of the hippocampus in young children with autism spectrum disorder. En: American Journal of Neuroradiology 28 (2007), Nr. 4, p. 672–677
- [37] Davis, Philip J.: Leonhard Euler’s integral: A historical proﬁle of the Gamma function: In memoriam: Milton Abramowitz. En: The American Mathematical Monthly 66

(1959), Nr. 10, p. 849–869

- [38] De Fosse´, Lies ; Hodge, Steven M. ; Makris, Nikos ; Kennedy, David N. ; Caviness, Verne S. ; McGrath, Lauren ; Steele, Shelley ; Ziegler, David A. ; Herbert, Martha R. ; Frazier, Jean A. [u. a.]: Language-association cortex asymmetry in autism and speciﬁc language impairment. En: Annals of neurology 56 (2004), Nr. 6, p. 757–766
- [39] Desikan, Rahul S. ; Segonne´ , Florent ; Fischl, Bruce ; Quinn, Brian T. ; Dickerson, Bradford C. ; Blacker, Deborah ; Buckner, Randy L. ; Dale, Anders M. ; Maguire, R P. ; Hyman, Bradley T. [u. a.]: An automated labeling system for subdividing the human cerebral cortex on MRI scans into gyral based regions of interest. En: Neuroimage 31 (2006), Nr. 3, p. 968–980
- [40] Di Martino, Adriana ; O’Connor, David ; Chen, Bosi ; Alaerts, Kaat ; Anderson, Jeﬀrey S. ; Assaf, Michal ; Balsters, Joshua H. ; Baxter, Leslie ; Beggiato, Anita ; Bernaerts, Sylvie [u. a.]: Enhancing studies of the connectome in autism using the autism brain imaging data exchange II. En: Scientiﬁc data 4 (2017), p. 170010
- [41] Di Martino, Adriana ; O’connor, David ; Chen, Bosi ; Alaerts, Kaat ; Anderson, Jeﬀrey S. ; Assaf, Michal ; Balsters, Joshua H. ; Baxter, Leslie ; Beggiato, Anita ; Bernaerts, Sylvie [u. a.]: Enhancing studies of the connectome in autism using the autism brain imaging data exchange II. En: Scientiﬁc data 4 (2017), Nr. 1, p. 1–15
- [42] Di Martino, Adriana ; Yan, Chao-Gan ; Li, Qingyang ; Denio, Erin ; Castellanos, Francisco X. ; Alaerts, Kaat ; Anderson, Jeﬀrey S. ; Assaf, Michal ; Bookheimer, Susan Y. ; Dapretto, Mirella [u. a.]: The autism brain imaging data exchange: towards a large-scale evaluation of the intrinsic brain architecture in autism. En: Molecular psychiatry 19 (2014), Nr. 6, p. 659–667
- [43] Di Martino, Adriana ; Yan, Chao-Gan ; Li, Qingyang ; Denio, Erin ; Castellanos, Francisco X. ; Alaerts, Kaat ; Anderson, Jeﬀrey S. ; Assaf, Michal ; Bookheimer, Susan Y. ; Dapretto, Mirella [u. a.]: The autism brain imaging data exchange: towards a large-scale evaluation of the intrinsic brain architecture in autism. En: Molecular psychiatry 19 (2014), Nr. 6, p. 659–667
- [44] Dice, Lee R.: Measures of the amount of ecologic association between species. En: Ecology 26 (1945), Nr. 3, p. 297–302
- [45] Dichter, Gabriel S. ; Felder, Jennifer N. ; Bodfish, James W.: Autism is characterized by dorsal anterior cingulate hyperactivation during social target detection. En: Social cognitive and aﬀective neuroscience 4 (2009), Nr. 3, p. 215–226

- [46] Do, M.N. ; Vetterli, M.: Wavelet-based texture retrieval using generalized Gaussian density and Kullback-Leibler distance. En: IEEE Transactions on Image Processing 11 (2002), Nr. 2, p. 146–158
- [47] Ecker, Christine ; Marquand, Andre ; Mourao-Miranda˜ , Janaina ; Johnston, Patrick ; Daly, Eileen M. ; Brammer, Michael J. ; Maltezos, Stefanos ; Murphy, Clodagh M. ; Robertson, Dene ; Williams, Steven C. [u. a.]: Describing the brain in autism in ﬁve dimensions—magnetic resonance imaging-assisted diagnosis of autism spectrum disorder using a multiparameter classiﬁcation approach. En: The Journal of Neuroscience 30 (2010), Nr. 32, p. 10612–10623
- [48] Eichler, Klaus ; Hempel, Susanne ; Wilby, Jennifer [u. a.]: Diagnostic value of systematic biopsy methods in the investigation of prostate cancer: a systematic review. En: J Urol 175 (2006), Nr. 5, p. 1605–1612
- [49] Epstein, Jonathan I.: An update of the Gleason grading system. En: J Urol 183

(2010), Nr. 2, p. 433–440

- [50] Falkmer T., Falkmer M. ; C., Horlin: Diagnostic procedures in autism spectrum disorders: a systematic literature review. En: Eur Child Adolesc Psychiatry 22 (2013), Nr. 10, p. 329–340
- [51] Fang, Yuming ; Wang, Junle ; Narwaria, Manish ; Le Callet, Patrick ; Lin, Weisi: Saliency detection for stereoscopic images. En: IEEE Transactions on Image Processing 23 (2014), Nr. 6, p. 2625–2636
- [52] Fatemi, S H. ; Halt, Amy R. ; Realmuto, George ; Earle, Julie ; Kist, David A. ; Thuras, Paul ; Merz, Amelia: Purkinje cell size is reduced in cerebellum of patients with autism. En: Cellular and molecular neurobiology 22 (2002), Nr. 2, p. 171–175
- [53] Fehr, Duc ; Veeraraghavan, Harini ; Wibmer, Andreas [u. a.]: Automatic classiﬁcation of prostate cancer Gleason scores from multiparametric magnetic resonance images. En: Proceedings of the National Academy of Sciences 112 (2015), Nr. 46, p. E6265–E6273
- [54] Fischl, B.: Automatically Parcellating the Human Cerebral Cortex. En: Cerebral Cortex 14 (2004), Januar, Nr. 1, p. 11–22
- [55] Fischl, B. ; Dale, A. M.: Measuring the thickness of the human cerebral cortex from magnetic resonance images. En: Proceedings of the National Academy of Sciences 97

(2000), September, Nr. 20, p. 11050–11055

- [56] Fu, Huazhu ; Cao, Xiaochun ; Tu, Zhuowen: Cluster-based co-saliency detection. En: IEEE Transactions on Image Processing 22 (2013), Nr. 10, p. 3766–3778

- [57] Garzon´ , Nicola´s M. ; Alvarez-Jimenez, Charlems ; Gonzalez, Fabio ; Romero, Eduardo: Adaptive frequency saliency model based on convolutional neural networks: a case study for prostate cancer MRI. En: 15th International Symposium on Medical Information Processing and Analysis Vol. 11330 International Society for Optics and Photonics, 2020, p. 113300B
- [58] Giedd, Jay N.: Structural magnetic resonance imaging of the adolescent brain. En: Annals of the New York Academy of Sciences 1021 (2004), Nr. 1, p. 77–85
- [59] Gillies, Robert J. ; Kinahan, Paul E. ; Hricak, Hedvig: Radiomics: Images Are More than Pictures, They Are Data. En: Radiology 278 (2016), Nr. 2, p. 563–577. – PMID: 26579733
- [60] Ginn, Nicole C. ; Clionsky, Leah N. ; Eyberg, Sheila M. ; Warner-Metzger, Christina ; Abner, John-Paul: Child-directed interaction training for young children with autism spectrum disorders: Parent and child outcomes. En: Journal of Clinical Child & Adolescent Psychology 46 (2017), Nr. 1, p. 101–109
- [61] Giuliano, A. ; Gori, I. ; Muratori, F. ; Saviozzi, I. ; Oliva, P. ; Tancredi, R. ; Cosenza, A. ; Tosetti, M. ; Calderoni, S. ; Retico, A.: Machine learning techniques implemented ON structural MRI features at diﬀerent spatial scales for preschoolers with autism spectrum disorders. En: Physica Medica 32 (2016), feb, p. 128
- [62] Gomez´ , F. ; Romero, E.: Rotation invariant texture characterization using a curvelet based descriptor. En: Pattern Recognition Letters 32 (2011), dec, Nr. 16, p. 2178–2186
- [63] Guo, Fang ; Wang, Wenguan ; Shen, Jianbing ; Shao, Ling ; Yang, Jian ; Tao, Dacheng ; Tang, Yuan Y.: Video saliency detection using object proposals. En: IEEE transactions on cybernetics 48 (2017), Nr. 11, p. 3159–3170
- [64] Haffner, Je´r´emie ; Lemaitre, Laurent ; Puech, Philippe ; Haber, Georges-Pascal ; Leroy, Xavier ; Jones, J S. ; Villers, Arnauld: Role of magnetic resonance imaging before initial biopsy: comparison of magnetic resonance imaging-targeted and systematic biopsy for signiﬁcant prostate cancer detection. En: BJU international 108

(2011), Nr. 8b, p. E171–E178

- [65] Han, Yu ; Yang, Yang ; sheng Shi, Zhe ; ding Zhang, An ; feng Yan, Lin ; chuan Hu, Yu ; lan Feng, Lan ; Ma, Jiao ; Wang, Wen ; bin Cui, Guang: Distinguishing brain inﬂammation from grade II glioma in population without contrast enhancement: a radiomics analysis based on conventional MRI. En: European Journal of Radiology 134 (2021), p. 109467. – ISSN 0720–048X

- [66] Haralick, R. M.: Statistical and structural approaches to texture. En: Proceedings of the IEEE 67 (1979), Nr. 5, p. 786–804
- [67] Hazlett, Heather C. ; Gu, Hongbin ; Munsell, Brent C. ; Kim, Sun H. ; Styner, Martin ; Wolff, Jason J. ; Elison, Jed T. ; Swanson, Meghan R. ; Zhu, Hongtu ; Botteron, Kelly N. [u. a.]: Early brain development in infants at high risk for autism spectrum disorder. En: Nature 542 (2017), Nr. 7641, p. 348–351
- [68] Hectors, Stefanie J. ; Wagner, Mathilde ; Bane, Octavia ; Besa, Cecilia ; Lewis, Sara ; Remark, Romain ; Chen, Nelson ; Fiel, M I. ; Zhu, Hongfa ; Gnjatic, Sacha [u. a.]: Quantiﬁcation of hepatocellular carcinoma heterogeneity with multiparametric magnetic resonance imaging. En: Scientiﬁc reports 7 (2017), Nr. 1, p. 1–12
- [69] Hedley, Darren ; Brewer, Neil ; Nevill, Rose ; Uljarevic´, Mirko ; Butter, Eric ; Mulick, James A.: The relationship between clinicians’ conﬁdence and accuracy, and the inﬂuence of child characteristics, in the screening of autism spectrum disorder. En: Journal of autism and developmental disorders 46 (2016), Nr. 7, p. 2340–2348
- [70] Herbert, Martha R. ; Harris, Gordon J. ; Adrien, Kristen T. ; Ziegler, David A. ; Makris, Nikos ; Kennedy, Dave N. ; Lange, Nicholas T. ; Chabris, Chris F. ; Bakardjiev, Anna ; Hodgson, James [u. a.]: Abnormal asymmetry in language association cortex in autism. En: Annals of neurology 52 (2002), Nr. 5, p. 588–596
- [71] Ismail, Marwa M. T. ; Keynton, Robert S. ; Mostapha, Mahmoud M. M. O. ; ElTanboly, Ahmed H. ; Casanova, Manuel F. ; Gimel’farb, Georgy L. ; El-Baz, Ayman: Studying Autism Spectrum Disorder with Structural and Diﬀusion Magnetic Resonance Imaging: A Survey. En: Frontiers in Human Neuroscience 10 (2016), may
- [72] Itti, Laurent ; Koch, Christof ; Niebur, Ernst: A model of saliency-based visual attention for rapid scene analysis. En: IEEE Transactions on Pattern Analysis & Machine Intelligence (1998), Nr. 11, p. 1254–1259
- [73] Jenkinson, Mark ; Bannister, Peter ; Brady, Michael ; Smith, Stephen: Improved optimization for the robust and accurate linear registration and motion correction of brain images. En: Neuroimage 17 (2002), Nr. 2, p. 825–841
- [74] Jenkinson, Mark ; Bannister, Peter ; Brady, Michael ; Smith, Stephen: Improved Optimization for the Robust and Accurate Linear Registration and Motion Correction of Brain Images. En: NeuroImage 17 (2002), oct, Nr. 2, p. 825–841
- [75] Jenkinson, Mark ; Beckmann, Christian F. ; Behrens, Timothy E. ; Woolrich, Mark W. ; Smith, Stephen M.: Fsl. En: Neuroimage 62 (2012), Nr. 2, p. 782–790

- [76] Jiao, Yun ; Chen, Rong ; Ke, Xiaoyan ; Chu, Kangkang ; Lu, Zuhong ; Herskovits, Edward H.: Predictive models of autism spectrum disorder based on brain regional cortical thickness. En: NeuroImage 50 (2010), April, Nr. 2, p. 589–599
- [77] Jiao Y, Zuhong L.: Predictive models of autism spectrum disorder based on brain regional cortical thickness. En: Neuroimage. 50(2) (2010), apr, Nr. 10.1016, p. 589–599
- [78] Karthik, R ; Menaka, R ; Chellamuthu, C: A comprehensive framework for classiﬁcation of brain tumour images using SVM and curvelet transform. En: International Journal of Biomedical Engineering and Technology 17 (2015), Nr. 2, p. 168–177
- [79] Katuwal, G. J. ; Cahill, N. D. ; Baum, S. A. ; Michael, A. M.: The predictive power of structural MRI in Autism diagnosis. En: 2015 37th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), 2015.

– ISSN 1094–687X, p. 4270–4273

- [80] Katuwal, Gajendra J. ; Baum, Steﬁ A. ; Cahill, Nathan D. ; Michael, Andrew M.: Divide and Conquer: Sub-Grouping of ASD Improves ASD Detection Based on Brain Morphometry. En: PLOS ONE 11 (2016), apr, Nr. 4, p. e0153331
- [81] Katuwal, Gajendra J. ; Cahill, Nathan D. ; Baum, Steﬁ A. ; Michael, Andrew M.: The predictive power of structural MRI in Autism diagnosis. En: 2015 37th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) IEEE, 2015, p. 4270–4273
- [82] Katuwal, Gajendra J. ; Cahill, Nathan D. ; Baum, Steﬁ A. ; Michael, Andrew M.: The predictive power of structural MRI in Autism diagnosis. En: 2015 37th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), IEEE, aug 2015
- [83] Kemper, Thomas L. ; Bauman, Margaret L.: The contribution of neuropathologic studies to the understanding of autism. En: Neurologic clinics 11 (1993), Nr. 1, p. 175–187
- [84] KNAUS, TRACEY A. ; SILVER, ANDREW M. ; LINDGREN, KRISTEN A. ; HADJIKHANI, NOUCHINE ; TAGER-FLUSBERG, HELEN: fMRI activation during a language task in adolescents with ASD. En: Journal of the International Neuropsychological Society 14 (2008), Oktober, Nr. 6, p. 967–979
- [85] Knopf, Alison: Autism prevalence increases from 1 in 60 to 1 in 54: CDC. En: The Brown University Child and Adolescent Behavior Letter 36 (2020), Nr. 6, p. 4–4
- [86] Kong, Yazhou ; Gao, Jianliang ; Xu, Yunpei ; Pan, Yi ; Wang, Jianxin ; Liu, Jin: Classiﬁcation of autism spectrum disorder by combining brain connectivity and deep neural network classiﬁer. En: Neurocomputing 324 (2019), p. 63–68

- [87] Kringelbach, Morten L.: The human orbitofrontal cortex: linking reward to hedonic experience. En: Nature Reviews Neuroscience 6 (2005), Nr. 9, p. 691
- [88] Kumar, Virendra ; Gu, Yuhua ; Basu, Satrajit ; Berglund, Anders ; Eschrich, Steven A. ; Schabath, Matthew B. ; Forster, Kenneth ; Aerts, Hugo J. ; Dekker, Andre ; Fenstermacher, David [u. a.]: Radiomics: the process and the challenges. En: Magnetic resonance imaging 30 (2012), Nr. 9, p. 1234–1248
- [89] Larson, David R. (Ed.) ; Massopust, Peter (Ed.) ; Nashed, Zuhair (Ed.) ; Nguyen, Minh C. (Ed.) ; Papadakis, Manos (Ed.) ; Zayed, Ahmed (Ed.): Frames and Operator Theory in Analysis and Signal Processing. American Mathematical Society, 2008
- [90] Lauvin, M.-A. ; Martineau, J. ; Destrieux, C. ; Andersson, F. ; BonnetBrilhault, F. ; Gomot, M. ; El-Hage, W. ; Cottier, J.-P.: Functional morphological imaging of autism spectrum disorders: Current position and theories proposed. En: Diagnostic and Interventional Imaging 93 (2012), Nr. 3, p. 139 – 147. – ISSN 2211–5684
- [91] Lawrence, YA ; Kemper, TL ; Bauman, ML ; Blatt, GJ: Parvalbumin-, calbindin, and calretinin-immunoreactive hippocampal interneuron density in autism. En: Acta Neurologica Scandinavica 121 (2010), Nr. 2, p. 99–108
- [92] Lehaire, Jerome ; Flamary, R´emi ; Rouviere` , Olivier ; Lartizien, Carole: Computer-aided diagnostic system for prostate cancer detection and characterization combining learned dictionaries and supervised classiﬁcation. En: Image Processing (ICIP), 2014 IEEE International Conference on IEEE, 2014, p. 2251–2255
- [93] Lemaˆıtre, Guillaume ; Mart´ı, Robert ; Freixenet, Jordi [u. a.]: Computer-aided detection and diagnosis for prostate cancer based on mono and multi-parametric MRI: a review. En: Computers in biology and medicine 60 (2015), p. 8–31
- [94] Lewis, Sara ; Hectors, Stefanie ; Taouli, Bachir: Radiomics of hepatocellular carcinoma. En: Abdominal Radiology (2020), p. 1–13
- [95] Li, Hailong ; Parikh, Nehal A. ; He, Lili: A Novel Transfer Learning Approach to Enhance Deep Neural Network Classiﬁcation of Brain Functional Connectomes. En: Frontiers in Neuroscience 12 (2018), Juli
- [96] Li, Hongliang ; Ngan, King N.: A co-saliency model of image pairs. En: IEEE Transactions on Image Processing 20 (2011), Nr. 12, p. 3365–3375
- [97] Li, Jia ; Duan, Ling-Yu ; Chen, Xiaowu ; Huang, Tiejun ; Tian, Yonghong: Finding the secret of image saliency in the frequency domain. En: IEEE transactions on pattern analysis and machine intelligence 37 (2015), Nr. 12, p. 2428–2440

- [98] Li, Jian ; Levine, Martin D. ; An, Xiangjing ; Xu, Xin ; He, Hangen: Visual saliency based on scale-space analysis in the frequency domain. En: IEEE transactions on pattern analysis and machine intelligence 35 (2012), Nr. 4, p. 996–1010
- [99] Liang, Zhi-Pei ; Lauterbur, Paul C.: Principles of magnetic resonance imaging: a signal processing perspective. SPIE Optical Engineering Press, 2000
- [100] Litjens, Geert ; Debats, Oscar ; Barentsz, Jelle ; Karssemeijer, Nico ; Huisman, Henkjan: Computer-Aided Detection of Prostate Cancer in MRI. En: IEEE Transactions on Medical Imaging 33 (2014), may, Nr. 5, p. 1083–1092
- [101] Litjens, Geert ; Debats, Oscar ; Barentsz, Jelle ; Karssemeijer, Nico ; Huisman, Henkjan. SPIE-AAPM PROSTATEx Challenge Data. 2017
- [102] Liu, Jieke ; Yao, Li ; Zhang, Wenjing ; Xiao, Yuan ; Liu, Lu ; Gao, Xin ; Shah, Chandan ; Li, Siyi ; Tao, Bo ; Gong, Qiyong [u. a.]: Gray matter abnormalities in pediatric autism spectrum disorder: a meta-analysis with signed diﬀerential mapping. En: European child & adolescent psychiatry 26 (2017), Nr. 8, p. 933–945
- [103] Liu, Maofu ; He, Yanxiang ; Ye, Bin: Image zernike moments shape feature evaluation based on image reconstruction. En: Geo-spatial Information Science 10 (2007), Nr. 3, p. 191–195
- [104] Liu, Mingxia ; Zhang, Jun ; Adeli, Ehsan ; Shen, Dinggang: Landmark-based deep multi-instance learning for brain disease diagnosis. En: Medical Image Analysis 43

(2018), Januar, p. 157–168

- [105] Liu, Mingxia ; Zhang, Jun ; Nie, Dong ; Yap, Pew-Thian ; Shen, Dinggang: Anatomical Landmark Based Deep Feature Representation for MR Images in Brain Disease Diagnosis. En: IEEE Journal of Biomedical and Health Informatics 22 (2018), September, Nr. 5, p. 1476–1485
- [106] Liu, Zhi ; Zou, Wenbin ; Li, Lina ; Shen, Liquan ; Le Meur, Olivier: Co-saliency detection based on hierarchical segmentation. En: IEEE Signal Processing Letters 21

(2013), Nr. 1, p. 88–92

- [107] Lord, Catherine ; Risi, Susan ; Lambrecht, Linda ; Cook, Edwin H. ; Leventhal, Bennett L. ; DiLavore, Pamela C. ; Pickles, Andrew ; Rutter, Michael: The Autism Diagnostic Observation Schedule—Generic: A standard measure of social and communication deﬁcits associated with the spectrum of autism. En: Journal of autism and developmental disorders 30 (2000), Nr. 3, p. 205–223
- [108] Lord, Catherine ; Rutter, Michael ; DiLavore, Pamela C. [u. a.]: Autism Diagnostic Observation Schedule–Generic. En: Dissertation Abstracts International Section A: Humanities and Social Sciences (1999)

- [109] Lord, Catherine ; Rutter, Michael ; Le Couteur, Ann: Autism Diagnostic Interview-Revised: a revised version of a diagnostic interview for caregivers of individuals with possible pervasive developmental disorders. En: Journal of autism and developmental disorders 24 (1994), Nr. 5, p. 659–685
- [110] Makris, Nikos ; Goldstein, Jill M. ; Kennedy, David ; Hodge, Steven M. ; Caviness, Verne S. ; Faraone, Stephen V. ; Tsuang, Ming T. ; Seidman, Larry J.: Decreased volume of left and total anterior insular lobule in schizophrenia. En: Schizophrenia research 83 (2006), Nr. 2, p. 155–171
- [111] Makris, Nikos ; Goldstein, Jill M. ; Kennedy, David ; Hodge, Steven M. ; Caviness, Verne S. ; Faraone, Stephen V. ; Tsuang, Ming T. ; Seidman, Larry J.: Decreased volume of left and total anterior insular lobule in schizophrenia. En: Schizophrenia Research 83 (2006), apr, Nr. 2-3, p. 155–171
- [112] Martino, Adriana D. ; Kelly, Clare ; Grzadzinski, Rebecca ; Zuo, Xi-Nian ; Mennes, Maarten ; Mairena, Maria A. ; Lord, Catherine ; Castellanos, F. X. ; Milham, Michael P.: Aberrant Striatal Functional Connectivity in Children with Autism. En: Biological Psychiatry 69 (2011), may, Nr. 9, p. 847–856
- [113] Mayerhoefer, Marius E. ; Materka, Andrzej ; Langs, Georg ; Haggstr¨ om¨ , Ida ; Szczypinski´ , Piotr ; Gibbs, Peter ; Cook, Gary: Introduction to radiomics. En: Journal of Nuclear Medicine 61 (2020), Nr. 4, p. 488–495
- [114] Mazziotta, John C. ; Toga, Arthur W. ; Evans, Alan ; Fox, Peter ; Lancaster, Jack: A probabilistic atlas of the human brain: Theory and rationale for its development: The international consortium for brain mapping (icbm). En: Neuroimage 2

(1995), Nr. 2, p. 89–101

- [115] Meselhy Eltoukhy, Mohamed ; Faye, Ibrahima ; Belhaouari Samir, Brahim: A comparison of wavelet and curvelet for breast cancer diagnosis in digital mammogram. En: Computers in Biology and Medicine 40 (2010), Nr. 4, p. 384–391. – ISSN 0010–4825
- [116] Morrison, James: DSM-5® Guı´a para el diagn´stico clı´nico. Editorial El Manual Moderno, 2015
- [117] Munera´ , Nicol´as ; Almeida, Javier ; Alvarez´ , Charlems ; Velasco, Nelson ; Romero, Eduardo: Autism Spectrum Disorders (ASD) Characterization in Children by Decomposing MRI Brain Regions with Zernike Moments. En: Sipaim–Miccai Biomedical Workshop Springer, 2018, p. 42–53
- [118] Murphy, Gillian ; Haider, Masoom ; Ghai, Sangeet ; Sreeharsha, Boraiah: The expanding role of MRI in prostate cancer. En: American Journal of Roentgenology 201 (2013), Nr. 6, p. 1229–1238

- [119] Nelson, Adam W. ; Harvey, Rebecca C. ; Parker, Richard A. [u. a.]: Repeat prostate biopsy strategies after initial negative biopsy: meta-regression comparing cancer detection of transperineal, transrectal saturation and MRI guided biopsy. En: PloS one 8 (2013), Nr. 2, p. e57480
- [120] Niederhuber, John E. ; Armitage, James O. ; Doroshow, James H. [u. a.]: Abeloﬀ’s Clinical Oncology. En: Bangkok Med J 10 (2015)
- [121] Niu, Yuzhen ; Geng, Yujie ; Li, Xueqing ; Liu, Feng: Leveraging stereopsis for saliency analysis. En: 2012 IEEE Conference on Computer Vision and Pattern Recognition IEEE, 2012, p. 454–461
- [122] Nketiah, Gabriel ; Elschot, Mattijs ; Kim, Eugene ; Teruel, Jose R. ; Scheenen, Tom W. ; Bathen, Tone F. ; Selnæs, Kirsten M.: T2-weighted MRI-derived textural features reﬂect prostate cancer aggressiveness: preliminary results. En: European radiology 27 (2017), Nr. 7, p. 3050–3059
- [123] Oppenheim, Alan V. ; Lim, Jae S.: The importance of phase in signals. En: Proceedings of the IEEE 69 (1981), Nr. 5, p. 529–541
- [124] Ozonoff, Sally ; Iosif, Ana-Maria ; Baguio, Fam ; Cook, Ian C. ; Hill, Monique M. ; Hutman, Ted ; Rogers, Sally J. ; Rozga, Agata ; Sangha, Sarabjit ; Sigman, Marian ; Steinfeld, Mary B. ; Young, Gregory S.: A Prospective Study of the Emergence of Early Behavioral Signs of Autism. En: Journal of the American Academy of Child & Adolescent Psychiatry 49 (2010), mar, Nr. 3, p. 256–266.e2
- [125] Parisot, Sarah ; Ktena, Soﬁa I. ; Ferrante, Enzo ; Lee, Matthew ; Guerrero, Ricardo ; Glocker, Ben ; Rueckert, Daniel: Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer’s disease. En: Medical Image Analysis 48 (2018), aug, p. 117–130
- [126] Patro, Badri N. ; Lunayach, Mayank ; Namboodiri, Vinay P.: Uncertainty Class Activation Map (U-CAM) Using Gradient Certainty Method. En: IEEE Transactions on Image Processing 30 (2021), p. 1910–1924
- [127] Posada De la Paz, M ; Ferrari Arroyo, MJ ; Tourino˜ Aguilera, E ; Boada Munoz˜ , L: Investigaci´on epidemiolo´gica en el autismo: una visio´n integradora. En: Rev. neurol.(Ed. impr.) (2005), p. s191–198
- [128] Pratt, Harry ; Williams, Bryan ; Coenen, Frans ; Zheng, Yalin: Fcnn: Fourier convolutional neural networks. En: Joint European Conference on Machine Learning and Knowledge Discovery in Databases Springer, 2017, p. 786–798

- [129] Puzzo, Ignazio ; Cooper, Nicholas R. ; Vetter, Petra ; Russo, Riccardo: EEG activation diﬀerences in the pre-motor cortex and supplementary motor area between normal individuals with high and low traits of autism. En: Brain Research 1342 (2010), Juni, p. 104–110
- [130] Retico, Alessandra ; Gori, Ilaria ; Giuliano, Alessia ; Muratori, Filippo ; Calderoni, Sara: One-class support vector machines identify the language and default mode regions as common patterns of structural alterations in young children with autism spectrum disorders. En: Frontiers in neuroscience 10 (2016), p. 306
- [131] Retico, Alessandra ; Gori, Ilaria ; Giuliano, Alessia ; Muratori, Filippo ; Calderoni, Sara: One-Class Support Vector Machines Identify the Language and Default Mode Regions As Common Patterns of Structural Alterations in Young Children with Autism Spectrum Disorders. En: Frontiers in Neuroscience 10 (2016), jun
- [132] Riddle, Kaitlin ; Cascio, Carissa J. ; Woodward, Neil D.: Brain structure in autism: a voxel-based morphometry analysis of the Autism Brain Imaging Database Exchange (ABIDE). En: Brain imaging and behavior (2016), p. 1–11
- [133] Robinson, M D. ; Toth, Cynthia A. ; Lo, Joseph Y. ; Farsiu, Sina: Eﬃcient Fourierwavelet super-resolution. En: IEEE Transactions on Image Processing 19 (2010), Nr. 10, p. 2669–2681
- [134] Rodr´ıguez-Barrionuevo, AC ; Rodr´ıguez-V., MA: Diagno´stico cl´ınico del autismo. En: Revista de Neurolog´ıa 34 (2002), Nr. 1, p. 72–77
- [135] Rutter, Michael ; Le Couteur, A ; Lord, C [u. a.]: Autism diagnostic interviewrevised. En: Los Angeles, CA: Western Psychological Services 29 (2003), Nr. 2003, p. 30
- [136] Saki, Fatemeh ; Tahmasbi, Amir ; Soltanian-Zadeh, Hamid ; Shokouhi, Shahriar B.: Fast opposite weight learning rules with application in breast cancer diagnosis. En: Computers in biology and medicine 43 (2013), Nr. 1, p. 32–41
- [137] Sato, Wataru ; Kochiyama, Takanori ; Uono, Shota ; Yoshimura, Sayaka ; Kubota, Yasutaka ; Sawada, Reiko ; Sakihama, Morimitsu ; Toichi, Motomi: Reduced Gray Matter Volume in the Social Brain Network in Adults with Autism Spectrum Disorder. En: Frontiers in Human Neuroscience 11 (2017), aug
- [138] Schumann, Cynthia M. ; Nordahl, Christine W.: Bridging the gap between MRI and postmortem research in autism. En: Brain Research 1380 (2011), p. 175–186. – The Emerging Neuroscience of Autism Spectrum Disorders. – ISSN 0006–8993

- [139] Sears, Lonnie L. ; Vest, Cortney ; Mohamed, Somaia ; Bailey, James ; Ranson, Bonnie J. ; Piven, Joseph: An MRI study of the basal ganglia in autism. En: Progress in Neuro-Psychopharmacology and Biological Psychiatry 23 (1999), may, Nr. 4, p. 613–624
- [140] Sen, Bhaskar ; Borle, Neil C. ; Greiner, Russell ; Brown, Matthew R.: A general prediction model for the detection of ADHD and Autism using structural and functional MRI. En: PloS one 13 (2018), Nr. 4, p. e0194856
- [141] Serefoglu, Ege C. ; Altinova, Serkan ; Ugras, Nevzat S. ; Akincioglu, Egemen ; Asil, Erem ; Balbay, Derya: How reliable is 12-core prostate biopsy procedure in the detection of prostate cancer? En: Canadian Urological Association Journal 6

(2012), mar, Nr. 2

- [142] Serefoglu, Ege C. ; Altinova, Serkan ; Ugras, Nevzat S. ; Akincioglu, Egemen ; Asil, Erem ; Balbay, M D.: How reliable is 12-core prostate biopsy procedure in the detection of prostate cancer? En: Canadian Urological Association Journal 7 (2013), Nr. 5-6, p. E293
- [143] Shen, Mark D. ; Nordahl, Christine W. ; Li, Deana D. ; Lee, Aaron ; Angkustsiri, Kathleen ; Emerson, Robert W. ; Rogers, Sally J. ; Ozonoff, Sally ; Amaral, David G.: Extra-axial cerebrospinal ﬂuid in high-risk and normal-risk children with autism aged 2–4 years: a case-control study. En: The Lancet Psychiatry 5 (2018), Nr. 11, p. 895–904
- [144] Shmilovici, Armin: Support vector machines. En: Data mining and knowledge discovery handbook. Springer, 2009, p. 231–247
- [145] Smith, Stephen M.: Fast robust automated brain extraction. En: Human brain mapping 17 (2002), Nr. 3, p. 143–155
- [146] Smith, Stephen M.: Fast robust automated brain extraction. En: Human Brain Mapping 17 (2002), nov, Nr. 3, p. 143–155
- [147] Snoek, Jasper ; Larochelle, Hugo ; Adams, Ryan P.: Practical bayesian optimization of machine learning algorithms. En: Advances in neural information processing systems, 2012, p. 2951–2959
- [148] Sparks, B. F. ; Friedman, S. D. ; Shaw, D. W. ; Aylward, E. H. ; Echelard, D. ; Artru, A. A. ; Maravilla, K. R. ; Giedd, J. N. ; Munson, J. ; Dawson, G. ; Dager, S. R.: Brain structural abnormalities in young children with autism spectrum disorder. En: Neurology 59 (2002), Juli, Nr. 2, p. 184–192

- [149] Szegedy, Christian ; Vanhoucke, Vincent ; Ioffe, Sergey ; Shlens, Jon ; Wojna, Zbigniew: Rethinking the inception architecture for computer vision. En: Proceedings of the IEEE conference on computer vision and pattern recognition, 2016, p. 2818–2826
- [150] Tahmasbi, Amir ; Saki, Fatemeh ; Shokouhi, Shahriar B.: Classiﬁcation of benign and malignant masses based on Zernike moments. En: Computers in biology and medicine 41 (2011), Nr. 8, p. 726–735
- [151] Tancik, Matthew ; Srinivasan, Pratul P. ; Mildenhall, Ben ; Fridovich-Keil, Sara ; Raghavan, Nithin ; Singhal, Utkarsh ; Ramamoorthi, Ravi ; Barron, Jonathan T. ; Ng, Ren: Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains. En: arXiv preprint arXiv:2006.10739 (2020)
- [152] Vaccarino, Flora M. ; Smith, Karen M.: Increased Brain Size in Autism—What It Will Take to Solve a Mystery. En: Biological Psychiatry 66 (2009), August, Nr. 4, p. 313–315
- [153] Vila T., M: Rendimiento del estudio diagno´stico del autismo. La aportacio´n de La neuroimagen, las pruebas metabo´licas y los estudios gen´eticos. En: Revista de neurologı´a 38 (2004), Nr. 1, p. 15–20
- [154] Viswanath, Satish E. ; Bloch, Nicholas B. ; Chappelow, Jonathan C. [u. a.]: Central gland and peripheral zone prostate tumors have signiﬁcantly diﬀerent quantitative imaging signatures on 3 Tesla endorectal, in vivo T2-weighted MR imagery. En: Journal of Magnetic Resonance Imaging 36 (2012), Nr. 1, p. 213–224
- [155] Vos, PC ; Barentsz, JO ; Karssemeijer, N ; Huisman, HJ: Automatic computeraided detection of prostate cancer based on multiparametric magnetic resonance image analysis. En: Physics in Medicine & Biology 57 (2012), Nr. 6, p. 1527
- [156] Wang, Haibo ; Viswanath, Satish ; Madabhushi, Anant: Discriminative Scale Learning (DiScrn): Applications to Prostate Cancer Detection from MRI and Needle Biopsies. En: Scientiﬁc Reports 7 (2017), sep, Nr. 1
- [157] Wang, Haofan ; Du, Mengnan ; Yang, Fan ; Zhang, Zijian: Score-cam: Improved visual explanations via score-weighted class activation mapping. En: arXiv preprint arXiv:1910.01279 (2019)
- [158] Wang, Liye ; Wee, Chong Y. ; Tang, Xiaoying ; Yap, Pew T. ; Shen, Dinggang: Multi-task feature selection via supervised canonical graph matching for diagnosis of autism spectrum disorder. En: Brain Imaging and Behavior 10 (2015), mar, Nr. 1, p. 33–40

- [159] Wang, Y. ; Zheng, B. ; Gao, D. ; Wang, J.: Fully convolutional neural networks for prostate cancer detection using multi-parametric magnetic resonance images: an initial investigation. En: 2018 24th International Conference on Pattern Recognition (ICPR), 2018. – ISSN 1051–4651, p. 3814–3819
- [160] Whitney, Elizabeth R. ; Kemper, Thomas L. ; Bauman, Margaret L. ; Rosene, Douglas L. ; Blatt, Gene J.: Cerebellar Purkinje Cells are Reduced in a Subpopulation of Autistic Brains: A Stereological Experiment Using Calbindin-D28k. En: The Cerebellum 7 (2008), jun, Nr. 3, p. 406–416
- [161] Whitney, Elizabeth R. ; Kemper, Thomas L. ; Rosene, Douglas L. ; Bauman, Margaret L. ; Blatt, Gene J.: Density of cerebellar basket and stellate cells in autism: Evidence for a late developmental loss of Purkinje cells. En: Journal of Neuroscience Research 87 (2009), aug, Nr. 10, p. 2245–2254
- [162] Wibmer, Andreas ; Hricak, Hedvig ; Gondo, Tatsuo ; Matsumoto, Kazuhiro ; Veeraraghavan, Harini ; Fehr, Duc ; Zheng, Junting ; Goldman, Debra ; Moskowitz, Chaya ; Fine, Samson W. [u. a.]: Haralick texture analysis of prostate MRI: utility for diﬀerentiating non-cancerous prostate from prostate cancer and diﬀerentiating prostate cancers with diﬀerent Gleason scores. En: European radiology 25 (2015), Nr. 10, p. 2840–2850
- [163] Woolrich, Mark W. ; Jbabdi, Saad ; Patenaude, Brian ; Chappell, Michael ; Makni, Salima ; Behrens, Timothy ; Beckmann, Christian ; Jenkinson, Mark ; Smith, Stephen M.: Bayesian analysis of neuroimaging data in FSL. En: Neuroimage 45 (2009), Nr. 1, p. S173–S186
- [164] Yang, Xin ; Liu, Chaoyue ; Wang, Zhiwei [u. a.]: Co-trained convolutional neural networks for automated detection of prostate cancer in multi-parametric MRI. En: Medical image analysis 42 (2017), p. 212–227
- [165] Yasuhara, Akihiro: Correlation between EEG abnormalities and symptoms of autism spectrum disorder (ASD). En: Brain and Development 32 (2010), November, Nr. 10, p. 791–798
- [166] Ye, Wenwu ; Yao, Jin ; Xue, Hui ; Li, Yi: Weakly Supervised Lesion Localization With Probabilistic-CAM Pooling. En: arXiv preprint arXiv:2005.14480 (2020)
- [167] Yip, Stephen S F. ; Aerts, Hugo J W L.: Applications and limitations of radiomics. En: Physics in Medicine and Biology 61 (2016), jun, Nr. 13, p. R150–R166
- [168] Zhang, Biqi ; Chang, Ken ; Ramkissoon, Shakti ; Tanguturi, Shyam ; Bi, Wenya L. ; Reardon, David A. ; Ligon, Keith L. ; Alexander, Brian M. ; Wen,

###### Patrick Y. ; Huang, Raymond Y.: Multimodal MRI features predict isocitrate dehydrogenase genotype in high-grade gliomas. En: Neuro-oncology 19 (2017), Nr. 1, p. 109–117

