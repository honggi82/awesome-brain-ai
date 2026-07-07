## Automatic segmentation of MR brain images with a convolutional neural network

Pim Moeskopsa,b, Max A. Viergevera, Adri¨enne M. Mendrika, Linda S. de Vriesb, Manon J.N.L. Bendersb and Ivana Iˇsguma

aImage Sciences Institute, University Medical Center Utrecht, The Netherlands bDepartment of Neonatology, University Medical Center Utrecht, The Netherlands

### arXiv:1704.03295v1[cs.CV]11Apr2017

Abstract—Automatic segmentation in MR brain images is important for quantitative analysis in large-scale studies with images acquired at all ages.

This paper presents a method for the automatic segmentation of MR brain images into a number of tissue classes using a convolutional neural network. To ensure that the method obtains accurate segmentation details as well as spatial consistency, the network uses multiple patch sizes and multiple convolution kernel sizes to acquire multi-scale information about each voxel. The method is not dependent on explicit features, but learns to recognise the information that is important for the classiﬁcation based on training data. The method requires a single anatomical MR image only.

The segmentation method is applied to ﬁve different data sets: coronal T2-weighted images of preterm infants acquired at 30 weeks postmenstrual age (PMA) and 40 weeks PMA, axial T2weighted images of preterm infants acquired at 40 weeks PMA, axial T1-weighted images of ageing adults acquired at an average age of 70 years, and T1-weighted images of young adults acquired at an average age of 23 years. The method obtained the following average Dice coefﬁcients over all segmented tissue classes for each data set, respectively: 0.87, 0.82, 0.84, 0.86 and 0.91.

The results demonstrate that the method obtains accurate segmentations in all ﬁve sets, and hence demonstrates its robustness to differences in age and acquisition protocol.

Index Terms—Deep learning, convolutional neural networks, automatic image segmentation, preterm neonatal brain, adult brain, MRI.

I. INTRODUCTION

# A

CCURATE automatic brain image segmentation in magnetic resonance (MR) images is a prerequisite for the

quantitative assessment of the brain in large-scale studies with images acquired at all ages [1]–[9]. Especially the ﬁeld of neonatal brain image segmentation has developed rapidly in the last ten years. A popular approach for brain image segmentation is the use of (population speciﬁc) atlases [10]– [17], but also pattern recognition methods are used [18],

- [19], sometimes in combination with an atlas-based approach
- [20]–[22]. To obtain anatomically correct segmentations, these methods need explicit spatial and intensity information. For atlas-based methods spatial information is provided in the form of an atlas which is deformed to match the image at hand. For methods based on pattern recognition spatial information

This paper has been published in May 2016 as: Moeskops, P., Viergever, M. A., Mendrik, A. M., de Vries, L. S., Benders, M. J., and Iˇsgum, I. (2016). Automatic segmentation of MR brain images with a convolutional neural network. IEEE Transactions on Medical Imaging, 35(5), 1252–1261.

is included in the feature set as distances within an atlas space [22], distances to a brain mask [19], probabilistic results of a previous segmentation step [18], [19], or by imposing anatomical constraints [18]. Intensity information is, in pattern recognition methods, included as a set of features based on (local) intensity, and atlas-based methods are typically performed by matching intensity information between the atlas and target images.

The explicit deﬁnition of such spatial and intensity features could be avoided by using convolutional neural networks (CNNs). CNNs have shown to be successful in several computer vision tasks including the recognition of handwriting

- [23] and, more recently, the ImageNet challenge, where 1.2 million 2D pictures are classiﬁed into 1000 different classes
- [24]. In recent years, CNNs also gained popularity in the ﬁeld of medical image analysis [25]–[34]. In contrast to classical machine learning methods, CNNs do not require a set of handcrafted features for the classiﬁcation, but learn sets of convolution kernels that are speciﬁcally trained for the classiﬁcation problem at hand. While classical machine learning methods applied to image segmentation would use e.g. Gaussian or Haar-like kernels to acquire appearance information, CNNs optimise sets of kernels based on the provided training data. In this way, the system can automatically extract information that is relevant for the task. If spatial and intensity information within the image are important to distinguish between classes, this can be learned from the provided information, much like a human observer would recognise objects within a (medical) image.

CNNs have also been used for brain image segmentation. Zhang et al. [32] presented a method using CNNs for the segmentation of three tissue types: white matter (WM), gray matter (GM), and cerebrospinal ﬂuid (CSF), in MR brain images of 6–8 months old infants, which have low contrast between WM and GM. The method uses 2D patches of a single size from one image plane in T1-weighted, T2-weighted and fractional anisotropy images as input for a CNN. Prior to the classiﬁcation, all voxels that do not belong to either of the three tissue types, i.e. skull, cerebellum and brain stem are excluded using in-house tools. De Br´ebisson et al. [31] presented a method for the segmentation of adult T1-weighted MR brain images in 134 regions as provided by the MICCAI challenge on multi-atlas labelling 1. The method uses multiple

1https://masi.vuse.vanderbilt.edu/workshop2012

parallel networks of 2D patches in orthogonal planes, a 3D patch, and distances to a previous segmentation step.

Recent MICCAI challenges in neonatal [35] and adult [36] MR brain image segmentation show that various segmentation methods achieve accurate results, but also that different methods are better at different aspects of brain image segmentation. The best results per tissue type in both the NeoBrainS12 2 and the MRBrainS13 3 challenges were not obtained by a single best performing method. These challenges also show that, despite the overall accurate segmentations achieved by these automatic methods, various inaccuracies are still present.

This paper presents a method for the automatic segmentation of anatomical MR brain images into a number of classes based on a multi-scale CNN. The multi-scale approach allows the method to obtain accurate segmentation details as well as spatial consistency. Unlike previous work that employs CNNs for a brain image segmentation task [31], the proposed method allows omitting the explicit deﬁnition of spatial features. Furthermore, unlike previous work used for brain image segmentation [32], the method uses multiple patch and kernel sizes combined. This approach allows the method to learn multi-scale features that estimate both intensity and spatial characteristics. In contrast to using these multiple patch and kernel sizes, other approaches to multi-scale CNNs, used in different applications, provide multi-scale features by directly using the feature maps after the ﬁrst convolution layer as additional input for a fully connected layer [37], [38].

Additionally, unlike previous work on brain image segmentation, the method is applied to the segmentation of images of developing neonates at different ages as well as young adults and ageing adults, and to coronal as well as axial images. This allows demonstrating that the method is able to adapt to the segmentation task at hand based on training data.

The paper is organised as follows. Section II provides a general description of the method. Section III describes the ﬁve test data sets that were used. Section IV-A describes the preprocessing that was performed. Section IV-B provides the parameter settings of the CNN that were determined experimentally with a subset of the data. Section IV-C lists the evaluation experiments and their results. Section IV-D compares the obtained results with the results in the recent literature and in the NeoBrainS12 and MRBrainS13 challenges. Section IV-E illustrates the inﬂuence of the multi-scale approach, and Section IV-F illustrates the inﬂuence of the single-plane approach. Finally, Section V discusses the results.

II. METHOD

Each voxel in the image is classiﬁed to one of the brain tissue classes using a CNN. Information about each voxel is provided in the form of image patches where the voxel of interest is in the centre. To allow the method to use multiscale information about each voxel, multiple patch sizes are used. The larger scales implicitly provide spatial information, because they are large enough to recognise where in the image the voxel is located, while the smaller scales provide detailed

- 2http://neobrains12.isi.uu.nl/mainResults.php
- 3http://mrbrains13.isi.uu.nl/results.php

75

51

25

9

7

5

9

7

25 5

51

75

Convolution and max pooling

34

24

23

24 24

11

7

5

3

7

5

11

3 23 34

Convolution and max pooling

14

32

10

32

5

5

32

3

5

3 3

3

3

14

5

10

3

Convolution and max pooling

5

48

4

48

3

48

3

4

5

Fully connected

256 256 256

Output

N

Fig. 1: Schematic overview of the convolutional neural network. The number of output classes, N, was set to 9 (8 tissue classes and background) for the neonatal images, to 8 (7 tissue classes and background) for the ageing adult images, and to 7 (6 tissue classes and background) for the young adult images. After the third convolution layer, max-pooling is only performed for the two largest patch sizes.

information about the local neighbourhood of the voxel. For each of these patch sizes, different kernel sizes are trained, i.e. larger kernel sizes are used for larger patches. This multiscale approach allows the network to incorporate local details as well as global spatial consistency.

For each of the patch sizes, a separate network branch is used; only the output layer is shared. This allows the weights and biases in the CNN to be speciﬁcally optimised for each patch size and corresponding kernel size. Multiple convolution layers are used; after each convolution, the resulting images are sub-sampled by extracting the highest responses with maxpooling. While the dimensions of the patches decrease in each layer, the number of kernels that are trained increases.

After the convolution layers, separate fully connected layers are used for each input patch size. To perform the ﬁnal classiﬁcation, these layers are connected to a single softmax output layer with one node for each class (including a background class).

Because the number of samples per tissue class might vary between the classes, a deﬁned number of samples is extracted

per class from each training image. In this way, the number of samples used in the training procedure is the same for each class, which avoids a bias towards larger tissue classes. To provide the network with as many training samples as possible, in every epoch, a new random selection of samples is made and provided to the network in a randomised order. Rectiﬁed linear units [39] are used for all nodes because of their speed in training CNNs [24]. Drop-out [40] is used on the fully connected layers to decrease the effect of overﬁtting on the training set. Mini-batch learning and RMSprop [41] are used to train the network and cross-entropy is used as cost function to optimise the weights and biases.

- A schematic of the CNN that is used in this study is shown

in Figure 1. The parameters that are used in the experiments are described in Section IV-B.

III. DATA

The method was applied to the segmentation of 3 different sets of volumetric T2-weighted MR brain images of preterm infants and 2 sets of volumetric T1-weighted MR brain images of adults, hence, 5 different sets of images in total. Because of the inverted contrast between WM and GM in neonatal images as compared with adult images, T2-weighted images of neonates provide a similar contrast between these tissue types as T1-weighted images of adults.

Basic information about the images is listed in Table I.

- A. Neonatal images

In total, 22 images of preterm infants were acquired on a Philips Achieva 3T scanner in accordance with standard clinical practice in the neonatal intensive care unit of the University Medical Center Utrecht (UMCU), The Netherlands. Permission from the medical ethical review committee of the UMCU and informed parental consent were obtained. 10 coronal images were acquired at an age of 30.9 ± 0.6 (mean ± standard deviation) weeks postmenstrual age (PMA). For 5 of these patients a coronal follow-up image was acquired at 41.3 ± 1.3 weeks PMA. Furthermore, 7 axial images (of different patients) were acquired at an age of 41.3 ± 0.5 weeks PMA. No brain pathology was visible on these images.

The neonatal images were manually segmented by experts into 8 classes: cerebellum (CB), myelinated white matter (mWM), basal ganglia and thalami (BGT), ventricular cerebrospinal ﬂuid (vCSF), unmyelinated white matter (uWM), brain stem (BS), cortical grey matter (cGM), and extracerebral cerebrospinal ﬂuid (eCSF).

Detailed information about the acquisition and the manual segmentation protocol can be found in the paper by Iˇsgum et al. [35] and on the NeoBrainS12 website 4. Iˇsgum et al. also evaluated the inter-observer variability for the manual segmentations of the data in the NeoBrainS12 challenge.

- B. Ageing adult images

20 axial images of adults were acquired on a Philips Achieva 3T scanner at an age of 70.5 ± 4.0 years, as provided

4http://neobrains12.isi.uu.nl/reference.php

by the MRBrainS13 challenge. Permission from the medical ethical review committee of the UMCU was obtained and all participants signed an informed consent form. The patients had a varying degree of atrophy and white matter lesions.

The ageing adult images were manually segmented by experts into the same classes as the neonatal images. However, because all WM is myelinated in adults, only one WM class was made, resulting in 7 different classes. Possible white matter lesions were included in the WM segmentation.

Detailed information about the acquisition and the manual segmentation protocol can be found in the paper by Mendrik et al. [36] and on the MRBrainS13 website 5.

C. Young adult images

15 images from the OASIS project [43] were acquired on a Siemens Vision 1.5T scanner at an age of 23.0 ± 4.1 years, as provided by the MICCAI challenge on multi-atlas labelling [44]. The images were acquired in the sagittal plane with a voxel size of 1.0 × 1.0 × 1.25 mm3 and were subsequently resized to an isotropic resolution of 1.0 × 1.0 × 1.0 mm3 6.

The images were manually segmented, in the coronal plane, into 134 classes. To match the tissue deﬁnitions used in this paper, these classes were merged into the same tissue classes as used for the other images. Because no eCSF was segmented in these images, this resulted in 6 tissue classes.

Detailed information about the acquisition can be found in the paper by Marcus et al. [43] and on the OASIS website 7. Detailed information about the manual segmentation protocol can be found on the NeuroMorphometrics website 8 9.

D. Evaluation

The automatic segmentations were evaluated in 3D using the Dice coefﬁcient and the mean surface distance between the manual and automatic segmentations.

IV. EXPERIMENTS AND RESULTS

The parameter settings of the CNN were deﬁned in preliminary leave-one-subject-out experiments with 5 of the images acquired at 30 weeks PMA. This set of images was selected such that it included none of the patients with a follow-up image acquired at 40 weeks PMA. This allowed independent evaluation on the remaining 5 images acquired at 30 weeks PMA as well as on the images of the other 4 test sets by training with representative training data.

A. Preprocessing

Prior to the segmentation, the neonatal images were bias corrected using the method of Likar et al. [45]. The adult images were bias corrected as provided in the MRBrainS13 challenge and the multi-atlas labelling challenge. To limit the number of voxels considered in the classiﬁcation, brain masks

- 5http://mrbrains13.isi.uu.nl/details.php
- 6https://masi.vuse.vanderbilt.edu/workshop2012
- 7http://www.oasis-brains.org/
- 8http://neuromorphometrics.org:8080/Seg/
- 9http://braincolor.mindboggle.info/protocols/

TABLE I: Acquisition parameters for the images used in this paper.

| |Cor. 30 wks Cor. 40 wks Ax. 40 wks Ageing adults Young adults|
|---|---|
|Age Acquisition protocol Number of images Reconstruction matrix Reconstructed voxel sizes [mm3]|30 weeks PMA 40 weeks PMA 40 weeks PMA 70 years 23 years<br><br>Coronal T2-weighted Coronal T2-weighted Axial T2-weighted Axial T1-weighted Sagittal T1-weighted<br><br>10 5 7 20 15<br><br>384 × 384 × 50 512 × 512 × 110 512 × 512 × 50 240 × 240 × 48 256 × 256 × (261–334)<br><br>0.34 × 0.34 × 2.0 0.35 × 0.35 × 1.2 0.35 × 0.35 × 2.0 0.96 × 0.96 × 3.0 1.0 × 1.0 × 1.0<br><br>|

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

|[Figure 5]|
|---|

|[Figure 6]|
|---|

|[Figure 7]|
|---|

|[Figure 8]|
|---|

|[Figure 9]|
|---|

|[Figure 10]|
|---|

|[Figure 11]|
|---|

|[Figure 12]|
|---|

|[Figure 13]|
|---|

|[Figure 14]|
|---|

|[Figure 15]|
|---|

|[Figure 16]|
|---|

|[Figure 17]|
|---|

|[Figure 18]|
|---|

|[Figure 19]|
|---|

|[Figure 20]|
|---|

|[Figure 21]|
|---|

|[Figure 22]|
|---|

|[Figure 23]|
|---|

|[Figure 24]|
|---|

|[Figure 25]|
|---|

|[Figure 26]|
|---|

|[Figure 27]|
|---|

|[Figure 28]|
|---|

|[Figure 29]|
|---|

|[Figure 30]|
|---|

|[Figure 31]|
|---|

|[Figure 32]|
|---|

|[Figure 33]|
|---|

|[Figure 34]|
|---|

|[Figure 35]|
|---|

|[Figure 36]|
|---|

|[Figure 37]|
|---|

|[Figure 38]|
|---|

|[Figure 39]|
|---|

|[Figure 40]|
|---|

|[Figure 41]<br><br>[Figure 42]|
|---|

|[Figure 43]|
|---|

|[Figure 44]|
|---|

|[Figure 45]|
|---|

|[Figure 46]|
|---|

|[Figure 47]|
|---|

|[Figure 48]|
|---|

|[Figure 49]|
|---|

|[Figure 50]|
|---|

|[Figure 51]|
|---|

|[Figure 52]|
|---|

|[Figure 53]|
|---|

|[Figure 54]|
|---|

|[Figure 55]|
|---|

|[Figure 56]|
|---|

|[Figure 57]|
|---|

|[Figure 58]|
|---|

|[Figure 59]|
|---|

|[Figure 60]|
|---|

|[Figure 61]|
|---|

|[Figure 62]|
|---|

|[Figure 63]|
|---|

|[Figure 64]|
|---|

|[Figure 65]|
|---|

|[Figure 66]|
|---|

|[Figure 67]|
|---|

|[Figure 68]|
|---|

|[Figure 69]|
|---|

|[Figure 70]|
|---|

|[Figure 71]|
|---|

|[Figure 72]|
|---|

|[Figure 73]|
|---|

|[Figure 74]|
|---|

|[Figure 75]|
|---|

|[Figure 76]|
|---|

|[Figure 77]|
|---|

- Fig. 2: Trained convolution kernels in the ﬁrst layer after 10 epochs using the 5 training images acquired at 30 weeks PMA,

and the kernels indicated in red applied to a test image. From left to right: the T2-weighted test image, the kernels of 5 × 5 voxels, the image convolved with the indicated 5 × 5 kernel, the kernels of 7 × 7 voxels, the image convolved with the indicated 7 × 7 kernel, the kernels of 9 × 9 voxels, and the image convolved with the indicated 9 × 9 kernel.

1 2 3 4 5 6 7 8 9 10 Epochs

0.4

0.5

0.6

0.7

0.8

0.9

1.0

Dicecoefficient

Cerebellum

|Average (25k) Average (50k)<br><br>|
|---|

1 2 3 4 5 6 7 8 9 10 Epochs

0.4

0.5

0.6

0.7

0.8

0.9

1.0

Dicecoefficient

Myelinated white matter

|Average (25k) Average (50k)<br><br>|
|---|

1 2 3 4 5 6 7 8 9 10 Epochs

0.4

0.5

0.6

0.7

0.8

0.9

1.0

Dicecoefficient

Basal ganglia and thalami

|Average (25k) Average (50k)<br><br>|
|---|

1 2 3 4 5 6 7 8 9 10 Epochs

0.4

0.5

0.6

0.7

0.8

0.9

1.0

Dicecoefficient

Ventricular cerebrospinal fluid

|Average (25k) Average (50k)<br><br>|
|---|

1 2 3 4 5 6 7 8 9 10 Epochs

0.4

0.5

0.6

0.7

0.8

0.9

1.0

Dicecoefficient

Unmyelinated white matter

|Average (25k) Average (50k)<br><br>|
|---|

1 2 3 4 5 6 7 8 9 10 Epochs

0.4

0.5

0.6

0.7

0.8

0.9

1.0

Dicecoefficient

Brain stem

|Average (25k) Average (50k)<br><br>|
|---|

1 2 3 4 5 6 7 8 9 10 Epochs

0.4

0.5

0.6

0.7

0.8

0.9

1.0

Dicecoefficient

Cortical grey matter

|Average (25k) Average (50k)<br><br>|
|---|

1 2 3 4 5 6 7 8 9 10 Epochs

0.4

0.5

0.6

0.7

0.8

0.9

1.0

Dicecoefficient

Extracerebral cerebrospinal fluid

|Average (25k) Average (50k)<br><br>|
|---|

- Fig. 3: Dice coefﬁcients (automatic vs. reference segmentation volumes) of the 5 test images acquired at 30 weeks PMA for each training epoch when 25 000 (red) and 50 000 (blue) training samples were randomly selected from each class of each of the 5 training images acquired at 30 weeks PMA.

were generated with BET [46]. In each of the experiments, the samples from the training images were only selected from within the brain mask volumes. For each test image, only voxels within the brain mask volume were considered in the classiﬁcation. The intensities were scaled such that for all

images, the range of intensities within the brain mask was between 0 and 1023.

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

- Fig. 4: Segmentation results for CB (brown), mWM (pink), BGT (green), vCSF (orange), (u)WM (blue), BS (purple), cGM (yellow), eCSF (red) in coronal images acquired at 30 weeks PMA (ﬁrst column), coronal images acquired at 40 weeks PMA (second column), axial images acquired at 40 weeks PMA (third colum), axial images of ageing adults (fourth colum), and

images of young adults in the coronal plane (ﬁfth column). The T2- or T1-weighted image is shown at the top, the manual segmentation in the middle, and the automatic segmentation at the bottom. The images are scaled separately and therefore do not show differences in size.

- B. CNN parameters

For all voxels within the brain mask, three in-plane patches with sizes of 25 × 25, 51 × 51 and 75 × 75 voxels are extracted, where the voxel of interest is in the centre. Because of the large slice thickness relative to the in-plane voxel size in 4 of the 5 image sets, orthogonal or 3D patches are not used, i.e. only information from the imaging plane is used for the segmentation of volumetric images.

A CNN with multiple convolution layers is used; a schematic of the network is shown in Figure 1. In the ﬁrst layers 24 kernels are trained for each patch size. For the patches of 25 × 25 voxels, kernels of 5 × 5 voxels are used, for the patches of 51 × 51 voxels, kernels of 7 × 7 voxels are used, and for the patches of 75 × 75 voxels, kernels of 9 × 9 voxels are used. Max-pooling with kernels of 2 × 2 voxels is performed on the convolved images. The output images are input for the second layer, where 32 kernels of 3 × 3, 5 × 5 and 7 × 7 voxels are used. Again, max-pooling with kernels of 2 × 2 voxels is performed on the convolved images. In the third layer, 48 kernels of 3 × 3, 3 × 3 and 5 × 5 voxels are used. After this layer, max-pooling is only performed for the

two largest patches, because for the smallest patch only an image of 3 × 3 voxels is left after three convolution layers. The contiguous even-sized max-pooling kernels cannot exactly cover the odd-sized patches. Therefore, before all max-pooling operations, the values are mirrored along the borders. The output of the third layer is input to fully connected layers with 256 nodes for each patch size. These nodes are subsequently connected to the softmax output layer with 9 nodes (8 tissue classes and background) for the neonatal images, 8 nodes (7 tissue classes and background) for the ageing adult images, and 7 nodes (6 tissue classes and background) for the young adult images. An example of the trained kernels in the ﬁrst layer and an example of the convolution responses for images acquired at 30 weeks PMA is shown in Figure 2.

The tissue classes consist of a very different number of voxels in these images. For example, in the images acquired at 30 weeks PMA, mWM consists of about 200 voxels, while uWM consists of 400 000 voxels. Therefore, to better balance the number of training samples of each class a ﬁxed number of samples are extracted per class from each training image. If a class contains less than this number of samples, all samples are used. Multiple epochs are used in the training process, where

- TABLE II: Results of the presented method in terms of Dice coefﬁcients and mean surface distances (mean ± standard deviation). The results are listed for (from top to bottom): (1) the coronal images acquired at 30 weeks PMA where 5 training images and 5 test images were used, (2) the 5 coronal images acquired at 30 weeks PMA that are test images in the NeoBrainS12 (NBS12) challenge in leave-one-subject-out (LOSO) cross-validation with all 10 images, (3) the 5 coronal images acquired at 40 weeks PMA in LOSO cross-validation, (4) the 7 axial images acquired at 40 weeks PMA in LOSO cross-validation, (5) the 5 axial images acquired at 40 weeks PMA that are test images in the NBS12 challenge in LOSO cross-validation with all 7 images, (6) the images of ageing adults from the MRBrainS12 challenge where 5 training images and 15 test images were used, (7) the images of young adults from the multi-atlas labelling challenge where 5 training images and 10 test images were used, and (8) the images of young adults from the multi-atlas labelling challenge where 15 training and 20 test images were used.

|Dice coefﬁcient| | | |
|---|---|---|---|
| |Image set|Experiment<br><br>|CB mWM BGT vCSF (u)WM BS cGM eCSF|
|1<br>2<br>|Cor. 30 wks<br><br>|5 training, 5 test LOSO 10, NBS12|0.92 ± 0.02 0.69 ± 0.06 0.91 ± 0.02 0.88 ± 0.05 0.96 ± 0.00 0.87 ± 0.02 0.84 ± 0.01 0.91 ± 0.02 0.91 ± 0.02 0.74 ± 0.06 0.89 ± 0.02 0.91 ± 0.01 0.96 ± 0.00 0.88 ± 0.02 0.83 ± 0.02 0.91 ± 0.02<br><br>|
|3|Cor. 40 wks<br><br>|LOSO 5, NBS12<br><br>|0.93 ± 0.01 0.56 ± 0.05 0.86 ± 0.02 0.85 ± 0.04 0.92 ± 0.00 0.78 ± 0.05 0.82 ± 0.01 0.86 ± 0.02|
|4<br><br>5<br><br><br>|Ax. 40 wks<br><br>|LOSO 7 LOSO 7, NBS12|0.93 ± 0.01 0.55 ± 0.05 0.91 ± 0.02 0.81 ± 0.03 0.92 ± 0.01 0.84 ± 0.02 0.88 ± 0.02 0.84 ± 0.04<br><br>0.93 ± 0.01 0.56 ± 0.06 0.91 ± 0.02 0.81 ± 0.03 0.93 ± 0.01 0.85 ± 0.02 0.87 ± 0.02 0.83 ± 0.04<br>|
|6<br><br>|Ageing adults|5 training, 15 test<br><br>|0.90 ± 0.03 - 0.81 ± 0.03 0.92 ± 0.02 0.88 ± 0.02 0.90 ± 0.02 0.84 ± 0.01 0.76 ± 0.04|
|7<br>8<br>|Young adults<br><br>|5 training, 10 test 15 training, 20 test|0.95 ± 0.01 - 0.85 ± 0.01 0.85 ± 0.04 0.94 ± 0.01 0.92 ± 0.01 0.91 ± 0.01 -<br><br>0.95 ± 0.01 - 0.86 ± 0.02 0.86 ± 0.05 0.93 ± 0.02 0.93 ± 0.01 0.91 ± 0.03 -<br>|

|Mean surface distance [mm]| | | |
|---|---|---|---|
| |Image set<br><br>|Experiment|CB mWM BGT vCSF (u)WM BS cGM eCSF|
|1<br><br>2<br><br><br>|Cor. 30 wks<br><br>|5 training, 5 test LOSO 10, NBS12|0.42 ± 0.32 0.90 ± 0.70 0.49 ± 0.20 0.23 ± 0.07 0.12 ± 0.01 0.29 ± 0.02 0.13 ± 0.02 0.10 ± 0.02 0.40 ± 0.11 0.59 ± 0.34 0.49 ± 0.16 0.22 ± 0.08 0.12 ± 0.01 0.25 ± 0.08 0.11 ± 0.01 0.10 ± 0.02<br><br>|
|3|Cor. 40 wks<br><br>|LOSO 5, NBS12<br><br>|0.72 ± 0.32 0.94 ± 0.44 0.96 ± 0.50 0.45 ± 0.11 0.15 ± 0.01 0.87 ± 0.56 0.12 ± 0.01 0.17 ± 0.02|
|4<br><br>5<br><br><br>|Ax. 40 wks<br><br>|LOSO 7 LOSO 7, NBS12<br><br>|1.04 ± 0.38 0.82 ± 0.30 0.49 ± 0.20 0.67 ± 0.62 0.13 ± 0.02 0.39 ± 0.12 0.11 ± 0.02 0.19 ± 0.04 1.14 ± 0.30 0.68 ± 0.24 0.46 ± 0.19 0.43 ± 0.14 0.12 ± 0.02 0.35 ± 0.08 0.11 ± 0.02 0.19 ± 0.05|
|6|Ageing adults|5 training, 15 test<br><br>|2.01 ± 2.10 - 0.67 ± 0.17 0.43 ± 0.67 0.28 ± 0.05 2.41 ± 2.21 0.23 ± 0.02 0.48 ± 0.10|
|7<br>8<br>|Young adults<br><br>|5 training, 10 test 15 training, 20 test<br><br>|1.17 ± 0.80 - 0.75 ± 0.07 0.52 ± 0.12 0.21 ± 0.05 0.64 ± 0.28 0.28 ± 0.06 0.61 ± 0.25 - 0.72 ± 0.23 0.52 ± 0.25 0.28 ± 0.17 0.46 ± 0.19 0.39 ± 0.23 -|

- TABLE III: Average Dice coefﬁcients reported in the recent literature on neonatal brain image segmentation and the best results per tissue class in the NeoBrainS12 and MRBrainS13 challenges. It should be noted that the results from the literature are as reported and therefore evaluated on different data sets. The results can therefore not be directly compared but can only provide an indication. Results that are not evaluated or provided in the listed paper are indicated with a ’-’. The results of the proposed method are listed in Table II.

|Source<br><br>|Acquisition|Age<br><br>|Test images|CB mWM BGT vCSF uWM BS cGM eCSF<br><br>|WM GM CSF|
|---|---|---|---|---|---|
|Gui et al., 2012 [42] Cardoso et al., 2013 [16] Makropoulos et al., 2014 [17] Wang et al., 2015 [18] Moeskops et al., 2015 [19]|3T coronal T1 and T2<br><br>1.5T T1<br><br>3T axial T1 and T2<br><br>3T isotropic T1, T2 and FA<br><br>3T coronal T2 3T coronal T2<br><br><br>|40 weeks PMA 40 weeks PMA 40 weeks PMA 40 weeks PMA 30 weeks PMA 40 weeks PMA|10 5 20 5 5<br><br>|0.87 0.78 0.88 - 0.94 0.90 0.92 0.87 - 0.84 0.94 0.91 0.74 0.76 0.93 - 0.84 0.84 - 0.92 - -<br><br>- - - - - - - -<br><br>- - - - 0.95 - 0.81 0.89<br><br>- - - - 0.92 - 0.80 0.85<br><br><br>|- - 0.84<br>- - -<br>- - -<br><br><br>0.92 0.89 0.84<br><br>- - -<br>- - -<br>|
|NeoBrainS12<br><br>|3T axial T1 and T2 3T coronal T1 and T2 3T coronal T1 and T2|40 weeks PMA 30 weeks PMA 40 weeks PMA<br><br>|5 5 5<br><br>|0.92 0.47 0.92 0.86 0.90 0.83 0.86 0.79<br><br>0.88 0.69 0.84 0.88 0.91 0.76 0.71 0.83<br><br>0.92 0.48 0.88 0.84 0.89 0.75 0.77 0.77<br><br><br>|0.92 - 0.80 0.90 - 0.84 0.84 - 0.79|
|MRBrainS13<br><br>|3T axial T1, T1 IR and T2 FLAIR<br><br>|70 years|15|- - - - - - - -<br><br>|0.89 0.86 0.84|

- TABLE IV: Comparison of the proposed method on the NeoBrainS12 challenge. The results are ranked according to the average Dice coefﬁcient over all 8 tissue classes. Therefore, only methods that have segmented the full set of 8 tissue classes are included in this comparison. The average was computed over the 3 test images that were segmented by each of the methods.

*Note that because no training data was provided for the coronal images acquired at 40 weeks PMA, the average over the 3 test images in the LOSO cross-validation experiment (Table II: Experiment 3) is listed.

|Image set<br><br>|Rank|Method|Dice|
|---|---|---|---|
|Cor. 30 wks|1<br><br>2<br><br>3<br><br>4<br><br><br>|Proposed Picsl upenn UCL DTC<br><br>|0.827 0.737 0.728 0.721<br><br>|

|Image set|Rank<br><br>|Method<br><br>|Dice|
|---|---|---|---|
|Ax. 40 wks<br><br>|1<br><br>2<br><br>3<br><br>4<br><br><br>|Proposed<br><br>DTC UCL Picsl upenn<br><br>|0.805 0.789 0.756 0.737<br><br>|

|Image set<br><br>|Rank|Method|Dice|
|---|---|---|---|
|Cor. 40 wks<br><br>|1<br><br>2<br><br>3<br><br>4<br><br><br>|Proposed<br><br>DTC UCL Picsl upenn<br><br>|0.819* 0.765 0.680 0.649|

a new set of random samples is extracted in each epoch. The performance on the test images acquired at 30 weeks PMA for each epoch using 25 000 and 50 000 training samples is shown in Figure 3. Based on this evaluation, in all experiments, 10 epochs and 50 000 training samples per class from each image are used.

- C. Evaluation experiments

The performance for the images acquired at 30 weeks PMA was evaluated on the independent set of 5 images not included in the parameter estimation, using the other 5 images

- as training data. For the other image sets, the method was retrained using representative training data. Because of the limited number of available training images, the performance on the coronal and axial images acquired at 40 weeks PMA was evaluated in leave-one-subject-out cross-validation for each set. The average Dice coefﬁcients and mean surface distances for each tissue class are shown per set in Table II:

- Experiments 1, 3, and 4. The segmentation results in one slice of one image of each of the test sets are shown in Figure 4.

A subset of the neonatal images used in this paper is used

- as test data in the NeoBrainS12 challenge. This includes 5 of the coronal images acquired at 30 weeks PMA, all 5 images acquired at 40 weeks PMA, and 5 of the axial images acquired
- at 40 weeks PMA. Therefore, to allow an indication of the performance in comparison with the results in the challenge, the average results for the axial images acquired at 40 weeks are presented separately for the 5 test images in the challenge (Table II: Experiment 5). For the coronal images acquired at 30 weeks PMA an additional experiment is done in the same fashion as for the other images: leave-one-subject-out crossvalidation with all ten images where the average over the test images in the challenge is listed in Table II: Experiment 2.

Given that a larger set of manually annotated images of ageing adults was available, their performance was evaluated using 5 images as training data and 15 images to test the performance (Table II: Experiment 6, and Figure 4). This furthermore allowed (indirect) comparison with the results of the MRBrainS13 challenge, which is performed using the same training and test images, except that only 3 combined tissue classes, namely WM, GM, and CSF are evaluated in the challenge.

Similar to the images of ageing adults, the images of young adults were evaluated using 5 images as training data and 10 images to test the performance (Table II: Experiment 7, and Figure 4). Additionally, the performance on the independent test set of 20 images [44] is evaluated using all 15 images as training data (Table II: Experiment 8).

- D. Comparison with previous methods

For comparison purposes, Table III lists segmentation results in terms of average Dice coefﬁcients reported in the recent literature on neonatal MR brain image segmentation. Note that these methods used different scans that were segmented possibly using different tissue deﬁnitions. Hence, these results can only be used as an indication. Furthermore, Table III lists the best results per tissue class at the time of writing in the

NeoBrainS12 and MRBrainS13 challenges. Note that in these challenges, the best results for different tissue types are not necessarily obtained by a single method.

To directly compare the method with previous methods, it was also evaluated in the NeoBrainS12 challenge using only the training images provided by the challenge. Table

- IV compares the results of the proposed method with other methods that have segmented the same tissue classes in the same images. Comparison has been performed by averaging the Dice coefﬁcients over all tissue classes in all test images. Detailed comparison per tissue class is available on the NeoBrainS12 website 10.

- E. Multi-scale approach

To show the inﬂuence of combining different patch sizes in the network, the method was additionally trained using each of the three patch sizes separately. A segmentation result for the lateral sulcus and the hippocampus in an image acquired at 30 weeks PMA using only the patches of 25 × 25, 51 × 51 and 75 × 75 voxels, as well as those three patches combined, is shown in Figure 5. The results in terms of Dice coefﬁcients and mean surface distance over all 5 test images acquired at 30 weeks PMA are shown in Table V: Experiments 1, 3, 5 and 7.

In addition, the proposed multi-scale approach was compared with the multi-scale approach of Sermanet and LeCun [37]. To allow fair comparison with the other experiments, we used the largest patch size, i.e. 75 × 75 voxels, as input. To acquire multi-scale information in this approach, the output of the ﬁrst, second and third layers provide combined input for the fully connected layer (Table V: Experiment 6).

- F. Single-plane approach

To motivate the choice of providing the network with patches from the acquisition planes only, the method was additionally evaluated using patches from consecutive slices, patches from the orthogonal planes, and 3D patches.

First, the method was trained for the images acquired at 30 weeks PMA using three consecutive slices for each of the three patch sizes (25 × 25, 51 × 51 and 75 × 75). Instead of a network with three branches, i.e. one for each of the three patch sizes (Figure 1), now a network with nine branches, i.e. three for each of the three patch sizes, was used (Table

- V: Experiment 8). Because of the large anatomical variation between slices due to the large slice thickness in 4 of the 5 image sets, separate branches allow the network to extract the relevant information by optimising dedicated kernels for each of the nine provided input patches.

Second, the method was trained for the images acquired at 30 weeks PMA using patches from the orthogonal planes (coronal, sagittal and axial) for each of the three patch sizes. Because these images are highly anisotropic, they were ﬁrst interpolated to isotropic resolution using an interpolation factor of 6 in the out-of-plane direction. This resulted in voxel sizes of 0.34 × 0.34 × 0.33. Again, these orthogonal patches

10http://neobrains12.isi.uu.nl/mainResults.php

of three sizes were input for a network with nine branches (Table V: Experiment 9).

Third, two networks with interpolated 3D input patches and 3D convolutions were evaluated for the images acquired at 30 weeks PMA, one with input patches of 25 × 25 × 25 voxels, and one with input patches of 51 × 51 × 51 voxels (Table V:

- Experiments 2 and 4). Fourth, because the images of the young adults were already

acquired with a (nearly) isotropic resolution, the performance of the network with three orthogonal patches for each of the three patch sizes was evaluated for this set as well. This network was evaluated for the segmentation of the 6 combined tissue classes (Table V: Experiment 11), as well as for the segmentation of all 134 classes. The average Dice coefﬁcient for the segmentation of 134 classes in the 20 test images was 0.7353 overall, 0.7170 for the cortical regions, and 0.7850 for the non-cortical regions. This performance would result in the 9th overall ranking out of 26 participants on the MICCAI challenge on multi-atlas labelling [44].

V. DISCUSSION

We have presented a method for the automatic segmentation of MR brain images, which has been evaluated on manually segmented preterm neonatal and adult images. Accurate segmentation results were obtained in images acquired at different ages (preterm neonatal vs. ageing adult) and with different acquisition protocols (coronal vs. axial, T2- vs. T1weighted). The method uses CNNs to automatically extract the relevant information from the training data to learn convolution kernels, which allows adaptation to the problem at hand. Postprocessing of the segmentation results, which is typically performed in brain image segmentation tasks, was here not necessary.

The method achieved accurate segmentations in terms of Dice coefﬁcients for all tissue classes except mWM in the neonatal images. mWM consists, especially in the images acquired at 30 weeks PMA, of very few voxels, hence each mislabelled voxel strongly inﬂuences the Dice coefﬁcient. Furthermore, this tissue is poorly visible in T2-weighted images and slightly better visible in T1-weighted images, which makes the manual annotation very difﬁcult and prone to interobserver variability [35]. This consequently has inﬂuence on the performance of the neighbouring tissue classes, which can be seen from e.g. the performance on BS for the coronal images acquired at 40 weeks PMA (Table II: Experiment 3). Even though the performance in terms of Dice coefﬁcients is lowest for mWM, the location of the tissue class is quite well recognised by the method, even based on T2-weighted images only. This can be seen from the mean surface distances (Table II) and from Figure 4: e.g. for the coronal images acquired

- at 40 weeks PMA, where mWM is recognised but does not follow the exact shape of the manual segmentation.

The method uses patches of three different sizes. Because of the highly anisotropic voxel sizes in 4 of the 5 evaluated image sets, the use of orthogonal or 3D patches would result in anisotropic patches, non-square/cubic patches, or strongly resampled data. Therefore, only in-plane information

was used, i.e. the volumetric images were segmented using information from the imaging plane only. This corresponds to the way a human observer performs annotation of these images: by selecting voxels that belong to each of the tissue types in a single image plane based on trained anatomical knowledge. This approach is further motivated by additional experiments using patches from consecutive slices and using (resampled) orthogonal patches (Table V: Experiments 8, 9 and 11), which did not provide information that allowed more accurate classiﬁcation. The performance in terms of average Dice coefﬁcient over all tissue classes remained 0.87 for the anisotropic images acquired at 30 weeks PMA, and improved slightly, from 0.90 to 0.91, for the (nearly) isotropic images of young adults. The limited increase in performance for the images of young adults was possibly inﬂuenced by the manual segmentations, which have been performed in the coronal plane and are therefore less accurate in the other planes. Furthermore, experiments with interpolated 3D patches of single sizes suggested that 3D convolutions also do not necessarily result in increased performance (Table V: Experiments 2 and 4), possibly inﬂuenced by the large increase in number of weights and biases in the optimisation. The performance of a multi-scale 3D CNN was not evaluated because training a network with three large 3D input patches would become computationally infeasible.

The results using each of the three patches separately show that each patch focusses on a different aspect of the segmentation problem. The smallest patch allows detailed analysis of local texture but misses spatial consistency. The largest patch results in a smooth segmentation but misses small details. This can especially be seen for the segmentation of cGM; the average Dice coefﬁcients for each of the patch sizes separately is 0.78, while the combined patches result in an average Dice coefﬁcient of 0.84 (Table V: Experiments 1, 3, 5 and 7). This can also be observed in Figure 5: the internal CSF in the lateral sulcus is recognised using only the smallest patch size, but not with the two larger sizes. On the other hand, spatially inconsistent results are obtained for the segmentation of the hippocampus using only the smallest patch size, whereas the largest patch size shows better consistency in that respect. In both cases, the result with the three patches combined shows the most accurate segmentation. The kernels and responses in the ﬁrst layer (Figure 2) show that different kernels enhance different parts of the image and the larger kernels operate on a larger scale. In addition, the proposed multi-scale approach is compared with the multi-scale approach of Sermanet and LeCun [37] and shows better performance for every tissue class.

The method is based on T2-weighted images for the neonatal images and on T1-weighted images in adults. Furthermore, the segmentation of both coronal and axial images was evaluated. This shows that the method is able to adapt to different acquisition protocols based on representative training data. Furthermore, being able to segment the images based on a single T1- or T2-weighted image, instead of relying on multiple acquisitions, allows omitting registration between images and thus precludes possible registration errors.

The segmentation method was applied to MR images of the

[Figure 93]

[Figure 94]

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

[Figure 99]

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

[Figure 104]

(a) Image (b) Reference (c) 25 × 25 (d) 51 × 51 (e) 75 × 75 (f) 3 patch sizes

- Fig. 5: Segmentation results in a T2-weighted image (left) acquired at 30 weeks PMA for the lateral sulcus (top) and the hippocampus (bottom) using (from left to right), manual segmentation, only a patch of 25 × 25 voxels, only a patch of 51 × 51 voxels, only a patch of 75 × 75 voxels, and these 3 patch sizes combined. The tissues are labelled as follows: CB in brown, mWM in pink, BGT in green, vCSF in orange, uWM in blue, BS in purple, cGM in yellow, and eCSF in red.

- TABLE V: Results in terms of Dice coefﬁcients and mean surface distance (mean ± standard deviation). For the images acquired at 30 weeks PMA the results are shown using patches of (1) 25 × 25, (2) 25 × 25 × 25, (3) 51 × 51, (4) 51 × 51 × 51 and (5) 75 × 75 voxels separately, (6) 75 × 75 voxels, where the output of the ﬁrst, second and third layers are combined input for the fully connected layer, (7) the three 2D patch sizes combined, (8) three consecutive slices for all three patch sizes, and (9) three interpolated orthogonal planes for all three patch sizes. For the images of young adults the results are shown using (10) the three 2D patch sizes combined, and (11) three interpolated orthogonal planes for all three patch sizes. The experiments are performed using 5 images as training data and 5 images to test the performance for the images acquired at 30 weeks PMA, and 5 images as training data and 10 images to test the performance for the images of young adults. Experiment 7 is therefore the same as Experiment 1 of Table II, and Experiment 10 is therefore the same as Experiment 7 of Table II.

|Dice coefﬁcient| | | |
|---|---|---|---|
| |Image set|Experiment|CB mWM BGT vCSF (u)WM BS cGM eCSF|
|1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>6<br><br>7<br><br>8<br><br>9<br><br><br>|Cor. 30 wks<br><br>|25×25 patch 25×25×25 patch 51×51 patch 51×51×51 patch 75×75 patch 75×75, multi-scale<br><br>|0.69 ± 0.04 0.33 ± 0.13 0.70 ± 0.05 0.76 ± 0.06 0.91 ± 0.02 0.58 ± 0.03 0.78 ± 0.02 0.86 ± 0.02 0.78 ± 0.03 0.60 ± 0.03 0.77 ± 0.04 0.78 ± 0.02 0.92 ± 0.01 0.79 ± 0.02 0.75 ± 0.02 0.85 ± 0.02<br><br>0.90 ± 0.02 0.57 ± 0.08 0.87 ± 0.02 0.84 ± 0.04 0.94 ± 0.01 0.85 ± 0.01 0.78 ± 0.02 0.88 ± 0.02 0.82 ± 0.02 0.48 ± 0.14 0.77 ± 0.06 0.70 ± 0.07 0.90 ± 0.01 0.77 ± 0.02 0.67 ± 0.03 0.80 ± 0.01<br>0.91 ± 0.01 0.62 ± 0.08 0.88 ± 0.02 0.85 ± 0.06 0.94 ± 0.01 0.85 ± 0.01 0.78 ± 0.02 0.88 ± 0.02 0.89 ± 0.02 0.61 ± 0.07 0.89 ± 0.01 0.83 ± 0.07 0.94 ± 0.01 0.86 ± 0.02 0.74 ± 0.03 0.86 ± 0.01<br>|
| | |3 patch sizes<br><br>|0.92 ± 0.02 0.69 ± 0.06 0.91 ± 0.02 0.88 ± 0.05 0.96 ± 0.00 0.87 ± 0.02 0.84 ± 0.01 0.91 ± 0.02|
| | |3 patch sizes, slices 3 patch sizes, ortho|0.92 ± 0.01 0.68 ± 0.08 0.90 ± 0.01 0.89 ± 0.05 0.96 ± 0.00 0.87 ± 0.02 0.84 ± 0.01 0.91 ± 0.02<br><br>0.93 ± 0.01 0.68 ± 0.06 0.90 ± 0.01 0.89 ± 0.03 0.96 ± 0.00 0.88 ± 0.02 0.83 ± 0.01 0.91 ± 0.01<br>|
|10<br><br>11<br>|Young adults<br><br>|3 patch sizes|0.95 ± 0.01 - 0.85 ± 0.01 0.85 ± 0.04 0.94 ± 0.01 0.92 ± 0.01 0.91 ± 0.01 -|
| | |3 patch sizes, ortho|0.96 ± 0.01 - 0.88 ± 0.01 0.84 ± 0.04 0.94 ± 0.01 0.93 ± 0.02 0.91 ± 0.01 -|

|Mean surface distance [mm]| | | |
|---|---|---|---|
| |Image set<br><br>|Experiment|CB mWM BGT vCSF (u)WM BS cGM eCSF|
|1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>6<br><br>7<br><br>8<br><br>9<br><br><br>|Cor. 30 wks<br><br>|25×25 patch 25×25×25 patch 51×51 patch 51×51×51 patch 75×75 patch 75×75, multi-scale<br><br>|8.12 ± 1.25 2.83 ± 0.94 3.82 ± 0.99 1.53 ± 0.65 0.40 ± 0.07 2.09 ± 0.74 0.21 ± 0.03 0.18 ± 0.04 4.76 ± 0.95 1.40 ± 0.62 2.12 ± 0.55 0.85 ± 0.58 0.31 ± 0.04 0.91 ± 0.09 0.21 ± 0.03 0.19 ± 0.04<br><br>0.47 ± 0.23 1.41 ± 0.64 0.79 ± 0.18 0.33 ± 0.09 0.19 ± 0.01 0.53 ± 0.21 0.19 ± 0.04 0.14 ± 0.03<br>1.82 ± 0.71 1.97 ± 0.70 2.66 ± 1.30 1.58 ± 0.65 0.36 ± 0.02 0.88 ± 0.13 0.25 ± 0.04 0.26 ± 0.05 0.32 ± 0.16 1.33 ± 0.53 0.63 ± 0.16 0.29 ± 0.11 0.16 ± 0.01 0.36 ± 0.09 0.15 ± 0.02 0.15 ± 0.02 0.46 ± 0.18 1.19 ± 0.51 0.56 ± 0.13 0.33 ± 0.11 0.19 ± 0.02 0.29 ± 0.04 0.19 ± 0.03 0.18 ± 0.03<br>|
| | |3 patch sizes<br><br>|0.42 ± 0.32 0.90 ± 0.70 0.49 ± 0.20 0.23 ± 0.07 0.12 ± 0.01 0.29 ± 0.02 0.13 ± 0.02 0.10 ± 0.02|
| | |3 patch sizes, slices 3 patch sizes, ortho|0.33 ± 0.15 0.72 ± 0.37 0.55 ± 0.15 0.25 ± 0.08 0.12 ± 0.01 0.35 ± 0.04 0.11 ± 0.01 0.10 ± 0.02 0.19 ± 0.05 0.65 ± 0.56 0.70 ± 0.38 0.21 ± 0.05 0.12 ± 0.01 0.25 ± 0.04 0.12 ± 0.02 0.10 ± 0.02<br><br>|
|10<br>11<br>|Young adults<br><br>|3 patch sizes<br><br>|1.17 ± 0.80 - 0.75 ± 0.07 0.52 ± 0.12 0.21 ± 0.05 0.64 ± 0.28 0.28 ± 0.06 -|
| | |3 patch sizes, ortho<br><br>|0.65 ± 0.19 - 0.64 ± 0.20 0.77 ± 0.67 0.20 ± 0.05 0.52 ± 0.35 0.27 ± 0.06 -|

developing, the young adult, and the ageing brain. No images acquired between these three age ranges were evaluated, but the method can likely be straightforwardly applied to images acquired at other ages. The method might however be limited in the application to images with abnormalities that are not included in the training set.

Additional evaluation in the segmentation of 134 classes as provided in the MICCAI challenge on multi-atlas labelling demonstrated that the approach can straight-forwardly be applied to a different segmentation task, without any parameter tuning. This resulted in an overall average Dice coefﬁcient of 0.7353 as compared with 0.725 reported by de Br´ebisson et al. [31].

A brain mask [46] is used to limit the number of samples considered in the classiﬁcation. Because the results of this brain mask were not always consistent for the images of ageing adults, a very conservative setting for the fractional intensity parameter was chosen for these images such that almost the whole head was included in the mask. It might be possible to completely omit the use of a brain mask, but this would also increase the computational load.

CNNs are known to need a large number of training samples. Because we applied CNNs in a voxel classiﬁcation task, many training samples were available. They were, however, extracted from a limited number of training images. More training images could therefore increase the performance. In addition, including diverse training data from different data sets in a single training step could generalise the problem and would in this way not require retraining the network. This generalisability over a more diverse data set might, however, be achieved at the cost of a decreased performance on each of the data sets that are included.

Many adjustments to the architecture of the network are possible, including more or different patch and kernel sizes, a different number of convolution layers, or a different number of nodes or layers in the fully connected network. Several settings were evaluated in preliminary experiments, but future work could focus on additional optimisation in this respect. Note that the network architecture provides a search space for the method and all weights and biases are optimised by the system. Small variations in the architecture are therefore not likely to have a large effect on the performance.

VI. CONCLUSION

The presented CNN method for the automatic segmentation of MR brain images shows accurate segmentation results in images acquired at different ages and with different acquisition protocols.

ACKNOWLEDGMENT

The authors gratefully acknowledge the support of NVIDIA Corporation with the donation of the Tesla K40 GPU used in this research.

The authors thank Bennett Landman for providing the data of the MICCAI challenge on multi-atlas labelling.

REFERENCES

- [1] D. H. Salat, R. L. Buckner, A. Z. Snyder, D. N. Greve, R. S. Desikan, E. Busa, J. C. Morris, A. M. Dale, and B. Fischl, “Thinning of the cerebral cortex in aging,” Cereb Cortex, vol. 14, no. 7, pp. 721–730, 2004.
- [2] J. Dubois, M. Benders, C. Borradori-Tolsa, A. Cachia, F. Lazeyras, R. Ha-Vinh Leuchter, S. V. Sizonenko, S. K. Warﬁeld, J. F. Mangin, and P. S. H¨uppi, “Primary cortical folding in the human newborn: an early marker of later functional development.,” Brain, vol. 131, pp. 2028– 2041, Aug 2008.
- [3] C. E. Rodriguez-Carranza, P. Mukherjee, D. Vigneron, J. Barkovich, and C. Studholme, “A framework for in vivo quantiﬁcation of regional brain folding in premature neonates.,” NeuroImage, vol. 41, pp. 462–478, Jun 2008.
- [4] M. Thambisetty, J. Wan, A. Carass, Y. An, J. L. Prince, and S. M. Resnick, “Longitudinal changes in cortical thickness associated with normal aging,” NeuroImage, vol. 52, no. 4, pp. 1215–1223, 2010.
- [5] L. J. Hogstrom, L. T. Westlye, K. B. Walhovd, and A. M. Fjell, “The structure of the cerebral cortex across adult life: age-related patterns of surface area, thickness, and gyriﬁcation,” Cereb Cortex, vol. 23, no. 11, pp. 2521–2530, 2013.
- [6] G. Li, L. Wang, F. Shi, A. E. Lyall, W. Lin, J. H. Gilmore, and D. Shen, “Mapping longitudinal development of local cortical gyriﬁcation in infants from birth to 2 years of age,” J Neurosci, vol. 34, no. 12, pp. 4228–4238, 2014.
- [7] A. E. Lyall, F. Shi, X. Geng, S. Woolson, G. Li, L. Wang, R. M. Hamer, D. Shen, and J. H. Gilmore, “Dynamic development of regional cortical thickness and surface area in early childhood,” Cereb Cortex, vol. 25, no. 8, pp. 2204–2212, 2014.
- [8] R. Wright, V. Kyriakopoulou, C. Ledig, M. Rutherford, J. Hajnal, D. Rueckert, and P. Aljabar, “Automatic quantiﬁcation of normal cortical folding patterns from fetal brain MRI,” NeuroImage, vol. 91, pp. 21–32, 2014.
- [9] P. Moeskops, M. J. Benders, K. J. Kersbergen, F. Groenendaal, L. S. de Vries, M. A. Viergever, and I. Iˇsgum, “Development of cortical morphology evaluated with longitudinal MR brain images of preterm infants,” PLOS ONE, vol. 10, no. 7, p. e0131552, 2015.
- [10] B. Fischl, D. H. Salat, E. Busa, M. Albert, M. Dieterich, C. Haselgrove, A. van der Kouwe, R. Killiany, D. Kennedy, S. Klaveness, A. Montillo, N. Makris, B. Rosen, and A. M. Dale, “Whole brain segmentation: automated labeling of neuroanatomical structures in the human brain.,” Neuron, vol. 33, no. 3, pp. 341–355, 2002.
- [11] M. Prastawa, J. H. Gilmore, W. Lin, and G. Gerig, “Automatic segmentation of MR images of the developing newborn brain.,” Med Image Anal, vol. 9, no. 5, pp. 457–466, 2005.
- [12] H. Xue, L. Srinivasan, S. Jiang, M. Rutherford, A. D. Edwards, D. Rueckert, and J. V. Hajnal, “Automatic segmentation and reconstruction of the cortex from neonatal MRI.,” NeuroImage, vol. 38, no. 3, pp. 461–477, 2007.
- [13] N. I. Weisenfeld and S. K. Warﬁeld, “Automatic segmentation of newborn brain MRI.,” NeuroImage, vol. 47, no. 2, pp. 564–572, 2009.
- [14] P. A. Habas, K. Kim, F. Rousseau, O. A. Glenn, A. J. Barkovich, and C. Studholme, “Atlas-based segmentation of developing tissues in the human brain with quantitative validation in young fetuses.,” Hum Brain Mapp, vol. 31, no. 9, pp. 1348–1358, 2010.
- [15] F. Shi, Y. Fan, S. Tang, J. H. Gilmore, W. Lin, and D. Shen, “Neonatal brain image segmentation in longitudinal MRI studies.,” NeuroImage, vol. 49, no. 1, pp. 391–400, 2010.
- [16] M. J. Cardoso, A. Melbourne, G. S. Kendall, M. Modat, N. J. Robertson, N. Marlow, and S. Ourselin, “AdaPT: An adaptive preterm segmentation algorithm for neonatal brain MRI.,” NeuroImage, vol. 65, pp. 97–108, 2013.
- [17] A. Makropoulos, I. Gousias, C. Ledig, P. Aljabar, A. Serag, J. Hajnal, A. D. Edwards, S. Counsell, and D. Rueckert, “Automatic whole brain MRI segmentation of the developing neonatal brain.,” IEEE Trans Med Imaging, vol. 33, no. 9, pp. 1818–1831, 2014.
- [18] L. Wang, Y. Gao, F. Shi, G. Li, J. H. Gilmore, W. Lin, and D. Shen, “LINKS: Learning-based multi-source integration framework for segmentation of infant brain images,” NeuroImage, vol. 108, pp. 160–172, 2015.
- [19] P. Moeskops, M. J. Benders, S. M. Chit¸ˇa, K. J. Kersbergen, F. Groenendaal, L. S. de Vries, M. A. Viergever, and I. Iˇsgum, “Automatic segmentation of MR brain images of preterm infants using supervised classiﬁcation,” NeuroImage, vol. 118, pp. 628–641, 2015.

- [20] H. A. Vrooman, C. A. Cocosco, F. van der Lijn, R. Stokking, M. A. Ikram, M. W. Vernooij, M. M. B. Breteler, and W. J. Niessen, “Multispectral brain tissue segmentation using automatically trained k-nearestneighbor classiﬁcation.,” NeuroImage, vol. 37, no. 1, pp. 71–81, 2007.
- [21] V. Srhoj-Egekher, M. J. Benders, M. A. Viergever, and I. Iˇsgum, “Automatic neonatal brain tissue segmentation with MRI,” in SPIE Medical Imaging, pp. 86693X–86693X, International Society for Optics and Photonics, 2013.
- [22] P. Anbeek, I. Iˇsgum, B. J. van Kooij, C. P. Mol, K. J. Kersbergen, F. Groenendaal, M. A. Viergever, L. S. de Vries, and M. J. Benders, “Automatic segmentation of eight tissue classes in neonatal brain MRI,” PLOS ONE, vol. 8, no. 12, p. e81895, 2013.
- [23] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, “Gradient-based learning applied to document recognition,” Proceedings of the IEEE, vol. 86, no. 11, pp. 2278–2324, 1998.
- [24] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “ImageNet classiﬁcation with deep convolutional neural networks,” in Advances in neural information processing systems, pp. 1097–1105, 2012.
- [25] A. Prasoon, K. Petersen, C. Igel, F. Lauze, E. Dam, and M. Nielsen, “Deep feature learning for knee cartilage segmentation using a triplanar convolutional neural network,” in Medical Image Computing and Computer-Assisted Intervention–MICCAI 2013, pp. 246–253, Springer, 2013.
- [26] H. R. Roth, L. Lu, A. Seff, K. M. Cherry, J. Hoffman, S. Wang, J. Liu, E. Turkbey, and R. M. Summers, “A new 2.5 D representation for lymph node detection using random sets of deep convolutional neural network observations,” in Medical Image Computing and ComputerAssisted Intervention–MICCAI 2014, pp. 520–527, Springer, 2014.
- [27] M. Veta, P. J. van Diest, S. M. Willems, H. Wang, A. Madabhushi, A. Cruz-Roa, F. Gonzalez, A. B. Larsen, J. S. Vestergaard, A. B. Dahl, et al., “Assessment of algorithms for mitosis detection in breast cancer histopathology images,” Med Image Anal, vol. 20, no. 1, pp. 237–248, 2015.
- [28] H. R. Roth, A. Farag, L. Lu, E. B. Turkbey, and R. M. Summers, “Deep convolutional networks for pancreas segmentation in CT imaging,” in SPIE Medical Imaging, pp. 94131G–94131G, International Society for Optics and Photonics, 2015.
- [29] H. R. Roth, L. Lu, A. Farag, H.-C. Shin, J. Liu, E. B. Turkbey, and R. M. Summers, “DeepOrgan: Multi-level deep convolutional networks for automated pancreas segmentation,” in Medical Image Computing and Computer-Assisted Intervention–MICCAI 2015, pp. 556–564, Springer, 2015.
- [30] Y. Bar, I. Diamant, L. Wolf, and H. Greenspan, “Deep learning with non-medical training used for chest pathology identiﬁcation,” in SPIE Medical Imaging, pp. 94140V–94140V, International Society for Optics and Photonics, 2015.
- [31] A. de Br´ebisson and G. Montana, “Deep neural networks for anatomical brain segmentation,” in CVPR Bioimage Computing Workshop, 2015.
- [32] W. Zhang, R. Li, H. Deng, L. Wang, W. Lin, S. Ji, and D. Shen, “Deep convolutional neural networks for multi-modality isointense infant brain image segmentation,” NeuroImage, vol. 108, pp. 214–224, 2015.
- [33] F. Ciompi, B. de Hoop, S. J. van Riel, K. Chung, E. T. Scholten, M. Oudkerk, P. A. de Jong, M. Prokop, and B. van Ginneken, “Automatic classiﬁcation of pulmonary peri-ﬁssural nodules in computed tomography using an ensemble of 2D views and a convolutional neural network out-of-the-box,” Med Image Anal, vol. 26, no. 1, pp. 195–202, 2015.

- [34] J. M. Wolterink, T. Leiner, M. A. Viergever, and I. Iˇsgum, “Automatic coronary calcium scoring in cardiac CT angiography using convolutional neural networks,” in Medical Image Computing and Computer-Assisted Intervention–MICCAI 2015, pp. 589–596, Springer, 2015.
- [35] I. Iˇsgum, M. J. Benders, B. Avants, M. J. Cardoso, S. J. Counsell, E. F. Gomez, L. Gui, P. H¨uppi, K. J. Kersbergen, A. Makropoulos, et al., “Evaluation of automatic neonatal brain segmentation algorithms: the NeoBrainS12 challenge,” Med Image Anal, vol. 20, no. 1, pp. 135–151, 2015.
- [36] A. M. Mendrik, K. L. Vincken, H. J. Kuijf, M. Breeuwer, W. H. Bouvy, J. de Bresser, A. Alansary, M. de Bruijne, A. Carass, A. El-Baz, A. Jog, R. Katyal, A. R. Khan, F. van der Lijn, Q. Mahmood, R. Mukherjee, A. van Opbroek, S. Paneri, S. Pereira, M. Persson, M. Rajchl, D. Sarikaya, Orjan¨ Smedby, C. A. Silva, H. A. Vrooman, S. Vyas, C. Wang, L. Zhao, G. J. Biessels, , and M. A. Viergever, “MRBrainS challenge: Online evaluation framework for brain image segmentation in 3T MRI scans,” Computational Intelligence and Neuroscience, 2015.
- [37] P. Sermanet and Y. LeCun, “Trafﬁc sign recognition with multi-scale convolutional networks,” in Neural Networks (IJCNN), The 2011 International Joint Conference on, pp. 2809–2813, IEEE, 2011.
- [38] J. Li, C. Niu, and M. Fan, “Multi-scale convolutional neural networks for natural scene license plate detection,” in Advances in Neural Networks– ISNN 2012, pp. 110–119, Springer, 2012.
- [39] V. Nair and G. E. Hinton, “Rectiﬁed linear units improve restricted Boltzmann machines,” in Proceedings of the 27th International Conference on Machine Learning (ICML-10), pp. 807–814, 2010.
- [40] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, “Dropout: A simple way to prevent neural networks from overﬁtting,” The Journal of Machine Learning Research, vol. 15, no. 1, pp. 1929–1958, 2014.
- [41] T. Tieleman and G. Hinton, “Lecture 6.5-rmsprop: Divide the gradient by a running average of its recent magnitude,” in COURSERA: Neural Networks for Machine Learning, vol. 4, 2012.
- [42] L. Gui, R. Lisowski, T. Faundez, P. S. H¨uppi, F. Lazeyras, and M. Kocher, “Morphology-driven automatic segmentation of MR images of the neonatal brain.,” Med Image Anal, vol. 16, no. 8, pp. 1565–1579, 2012.
- [43] D. S. Marcus, T. H. Wang, J. Parker, J. G. Csernansky, J. C. Morris, and R. L. Buckner, “Open access series of imaging studies (OASIS): crosssectional MRI data in young, middle aged, nondemented, and demented older adults,” J Cognitive Neurosci, vol. 19, no. 9, pp. 1498–1507, 2007.
- [44] B. A. Landman, A. Ribbens, B. Lucas, C. Davatzikos, B. Avants, C. Ledig, D. Ma, D. Rueckert, D. Vandermeulen, F. Maes, G. Erus, J. Wang, H. Holmes, H. Wang, J. Doshi, J. Kornegay, J. Manjon, A. Hammers, A. Akhondi-Asl, A. J. Asman, and S. K. Warﬁeld, MICCAI 2012 workshop on multi-atlas labeling. CreateSpace Independent Publishing Platform, 2012.
- [45] B. Likar, M. A. Viergever, and F. Pernus, “Retrospective correction of MR intensity inhomogeneity by entropy minimization,” IEEE Trans Med Imaging, vol. 20, pp. 1398–1410, 2001.
- [46] S. M. Smith, “Fast robust automated brain extraction.,” Hum Brain Mapp, vol. 17, no. 3, pp. 143–155, 2002.

