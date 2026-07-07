# arXiv:2209.07162v1[eess.IV]15Sep2022

## Brain Imaging Generation with Latent Diﬀusion Models

Walter H. L. Pinaya1 , Petru-Daniel Tudosiu1 , Jessica Daﬄon2,3, Pedro F Da Costa4,5, Virginia Fernandez1, Parashkev Nachev6, Sebastien Ourselin1, and M. Jorge Cardoso1

1 Department of Biomedical Engineering, School of Biomedical Engineering & Imaging Sciences, King’s College London, UK 2 Data Science and Sharing Team, Functional Magnetic Resonance Imaging Facility, National Institute of Mental Health, Bethesda, MD, 20892, USA

- 3 Machine Learning Team, Functional Magnetic Resonance Imaging Facility, National Institute of Mental Health, Bethesda, MD, 20892, USA
- 4 Institute of Psychiatry, Psychology & Neuroscience, King’s College London, UK 5 Centre for Brain and Cognitive Development, Birkbeck College, UK

6 Institute of Neurology, University College London, UK

Abstract. Deep neural networks have brought remarkable breakthroughs

in medical image analysis. However, due to their data-hungry nature, the modest dataset sizes in medical imaging projects might be hindering their full potential. Generating synthetic data provides a promising alternative, allowing to complement training datasets and conducting medical image research at a larger scale. Diﬀusion models recently have caught the attention of the computer vision community by producing photorealistic synthetic images. In this study, we explore using Latent Diﬀusion Models to generate synthetic images from high-resolution 3D brain images. We used T1w MRI images from the UK Biobank dataset (N=31,740) to train our models to learn about the probabilistic distribution of brain images, conditioned on covariables, such as age, sex, and brain structure volumes. We found that our models created realistic data, and we could use the conditioning variables to control the data generation eﬀectively. Besides that, we created a synthetic dataset with 100,000 brain images and made it openly available to the scientiﬁc community.

Keywords: Synthetic data · Diﬀusion models · Generative models · Brain Imaging.

### 1 Introduction

Deep neural networks fuelled several ground-breaking advancements in areas such as natural language processing and computer vision, where part of these improvements was attributed to the large amount of rich data used to train these networks, with some public datasets reaching millions of images and text

Equal contribution

sentences [8,26]. During the same period, medical image analysis also made remarkable breakthroughs by applying deep neural networks to solve tasks such as segmentation, structure detection, and computer-aided diagnosis (detailed review available at [20,27]). However, one current limitation of medical imaging projects is the lack of availability of large datasets. Medical data are costly and laborious to collect, and privacy concerns create challenges to data sharing by restricting publicly available medical datasets to up to a few thousand examples. This limitation creates a bottleneck on models’ generalizability and hampers the rate at which cutting-edge methods are deployed in the clinical routine.

Generating synthetic data with privacy guarantees provides a promising alternative, allowing meaningful research to be carried out at scale [15,14,33]. Together with traditional data augmentation techniques (e.g., geometric transformations), these synthetic data could complement real data to dramatically increase the training set of machine learning models. Generative models learn the probability density function underlying the data they are trained on and can create realistic representations of examples which are diﬀerent from the ones present in the training data by sampling from the learned distribution. However, generating meaningful synthetic data is not easy, especially when considering complex organs like the brain.

Nowadays, Generative Adversarial Networks (GANs) have been applied in various ﬁelds to create synthetic images, producing realistic and clear images and achieving impressive performance [7,32]. In the medical ﬁeld, for example, [17] combine variational autoencoders with GANs to generate various modalities of whole brain volumes from a small training set and achieved a better performance compared to several baselines. However, since their study resized the images to a small volume before training, with a size of 64 × 64 × 64 voxels, their synthetic medical images did not replicate many essential ﬁner details. In addition, due to the prevalence of 3D high-resolution data in the ﬁeld, researchers tend to have their models restrained by the amount of GPU memory available. To mitigate this problem, [31] proposed a 3D GAN with a hierarchical structure which is able to generate a low-resolution version of the image and anchor the generation of high-resolution sub-volumes on it. With this approach, the authors were able to generate impressive realistic 3D thorax CT and brain MRI with resolutions up to 256 × 256 × 256 voxels. Despite generating great interest, GANs still come with inherent challenges, such as being notoriously unstable during training and failing to converge or to capture the variability of the generated data due to mode collapse issues [16].

Recently, diﬀusion models caught the attention of the machine learning community by showing promising results when synthesizing natural images. They have rivalled GANs in sample quality [9] while building upon a solid theoretical foundation. Not only have they reported impressive photorealism unconditioned images, but they have also been used to create images conditioned in classes and text sentences (using techniques like classiﬁer-free guidance [13]), with exceptional results on models like Latent Diﬀusion Models [23], DALLE 2 [22], and Imagen [25].

VAE-GAN LSGAN

[Figure 1]

[Figure 2]

Real Images

Sample 1 Sample 2

[Figure 3]

[Figure 4]

LDM (Ours)

[Figure 5]

[Figure 6]

LDM + DDIM (Ours)

[Figure 7]

[Figure 8]

Fig. 1. Real and synthetic samples of head MRI generated using VAE-GAN, LSGAN, LDM and LDM+DDIM.

In this study, we used diﬀusion models to create synthetic MRI images of the adult human brain. For that, we used 31,740 training images from the UK Biobank [30]to train our models. In order to eﬃciently scale the application of diﬀusion models to these high-resolution 3D data, we combined our diﬀusion models with compression models following the architecture of Latent Diﬀusion Models (LDM) [23]. Furthermore, we conditioned the image generations on age, gender, ventricular volume, and brain volume relative to the intracranial volume in order to generate realistic examples of brain scans with speciﬁc covariate values. We compared our synthetic images to state-of-the-art methods based on GANs, and we made our synthetic dataset comprising 100,000 brain images publicly available to the scientiﬁc community.

### 2 Methods

#### 2.1 Datasets and Image Preprocessing

In this study, we used images from the UK Biobank (UKB) [30] to train our generative models. The UKB is a study that aims to follow the health and wellbeing of volunteer participants across the United Kingdom. Here, we used an early release of the project’s data comprising 31,740 participants with T1w images. The dataset consists of healthy individuals aged between 44 and 82 years with average age of 63.6 ± 7.5 years (average ± SD) and 14,942 male subjects (47%). In our experiments, we also conditioned for the volume of ventricular cerebrospinal ﬂuid (min-max: 6995.68 - 171375.0 mm3; UKB Data-Field 25004) and brain volume normalised for head size (min-max: 1144240 - 1793910 mm3; UKB Data-Field 25009). All variables used for model conditioning were normalised using min-max normalisation before feeding them to our models.

For the image pre-processing, we used UniRes1 [2,3] to perform a rigid body registration to a common MNI space. The ﬁnal images had 1 mm3 as voxel size, and we cropped the image to obtain a volume of the head measuring 160 × 224 × 160 voxels.

#### 2.2 Generative models

In our experiments, we used LDMs, which combine the use of autoencoders to compress the input data into a lower-dimensional latent representation with the generative modelling properties of diﬀusion models. The compression model was an essential step to allow us to scale to high-resolution medical images. We trained the autoencoder with a combination of L1 loss, perceptual loss [34], a patch-based adversarial objective [10], and a KL regularization of the latent space. The encoder maps the brain image to a latent representation with a size of 20 × 28 × 20. After training the compression model, the latent representations of the training set are used as input to the diﬀusion model. Diﬀusion models [12,28] are generative models that convert Gaussian noise into samples from a learned data distribution via an iterative denoising process. Given a latent representation of an example from our training set, the diﬀusion process gradually destroys the structure of the data via a ﬁxed Markov chain over 1000 steps by adding Gaussian noise using a ﬁxed linear variance schedule. The reverse process is also modelled as a Markov chain which learns to recover the original input from the noisy one. We conditioned our models according to age, gender, ventricular volume, and brain volume relative to the intracranial volume. To perform this conditioning, we used a hybrid approach combining the concatenation of the conditioning with the input data and the use of cross-attention mechanisms, as proposed in [23]. Training and model details are available in the supplementary material.

1 https://github.com/brudfors/UniRes

### 3 Experiments

#### 3.1 Sampling Quality

- Fig. 1 shows images generated using LDMs compared to real images and the baselines (i.e., VAE-GAN [18] and LSGAN [21]). Unlike the baselines, we observe that the LDMs were able to sample high-quality images with sharp details and realistic textures. Besides that, training the diﬀusion models at such a high resolution was much more stable and easier to achieve convergence when compared to the GAN-based baselines. The baselines required a meticulous design of the interaction between discriminator and generator, and they presented problems of mode collapse, showcasing the problems of GAN-based applied in such high-resolution 3D images. Therefore, we will reﬁne and expand our comparisons with other baselines in future works.

We also obtained quantitative metrics about the performance of our models. We used the Fréchet Inception Distance (FID) [11]to measure how realistic the synthetic images are. A small FID indicates that the distribution of the generated images is similar to the distribution of the real images. The FID was calculated using an approach similar to [31], where features were extracted using a pretrained Med3D [5]. We also measured the generation diversity with the MultiScale Structural Similarity Metric (MS-SSIM) and 4-G-R-SSIM [24,4,19], where a value close to 0 suggests high diversity. Here, we presented the MS-SSIM for comparison with previous studies, but we also added the 4-G-R-SSIM as it has been shown to have better image quality assessment. We compute the average values from 1000 sample pairs. Table 1 shows the quantitative results for diﬀerent models used for the image synthesis.

Table 1. Quantitative evaluation of the synthetic images on the UK Biobank. We used the Fréchet Inception Distance (FID) to verify how realistic are the images and the multi-scale structural similarity metric (MS-SSIM) and 4-G-R-SSIM to evaluate generation diversity. We used 50 timesteps when sampling our models with DDIM sampler.

FID ↓ MS-SSIM ↓ 4-G-R-SSIM ↓ LSGAN 0.0231 0.9997 0.9969 VAE-GAN 0.1576 0.9671 0.8719 LDM 0.0076 0.6555 0.3883 LDM + DDIM 0.0080 0.6704 0.3957 Real images 0.0005 0.6536 0.3909

Recently, diﬀerent methods have been proposed to speed up the reverse process (e.g., Denoising Diﬀusion Implicit Models - DDIM), reducing by 10× 50× the number of necessary reverse steps [29]. Using the DDIM sampler, we reduced

##### the number of timesteps from 1000 steps to only 50. This improved our sampling time from an average of 142.3±1.6s per sample to 7.6±0.2 s per sample @ NVIDIA TITAN RTX with minimum loss in performance (Table 1). Because of this boost in processing time and a minimal performance loss, we are using the LDM with the DDIM sampler for all the remaining analyses.

[Figure 9]

[Figure 10]

[Figure 11]

[Figure 12]

[Figure 13]

Ventricular Volume

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

[Figure 18]

Brain volume nomalize for head size

- Fig. 2. Conditioned sampling varying the ventricular volume and the brain volume normalized by the intracranial volume. In both rows, we kept the other variables constant.
- 3.2 Conditioning Evaluation

Using the hybrid conditioning approach [23], we were able to condition our models and generate brain images where we can specify the age, sex, ventricular volume, and brain volume. As we can observe in Fig. 2, our model was able to learn representations conditioned on regional (i.e., ventricular volume) and global (i.e., brain volume) volumes.

In order to quantitatively evaluate the conditioning, we used SynthSeg 2 [1] to measure the volumes of the ventricles of 1000 synthetic brains. In this analysis, we measured the combination of the left and right lateral ventricles and the left and right inferior lateral ventricles. We then computed the Pearson correlation between the obtained volumes and the inputted conditioning values. Using this approach, we observed a high correlation coeﬃcient of 0.972, which demonstrates the eﬀectiveness of conditioning on our model (Fig. 3).

2 https://github.com/BBillot/SynthSeg

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

- Fig. 3. Conditioning analysis. Left) Correlation between inputted ventricular volume vs ventricular measured with SynthSeg. Right) Correlation between inputted age and predicted brain age.

Additionally, we veriﬁed how well the eﬀectiveness of conditioning brain generation by age. To this end, we used discriminative models to perform the task of brain age prediction, where we predict chronological age based on the brain image. In our study, we used the 3D convolution neural network proposed in [6], trained on the same training set used in the LDM training. After training the model, we verify how well the predicted age approximated the inputted age of the synthetic dataset. As shown in Fig. 3, our model presented a high correlation between the inputted conditioning and the predicted age (r=0.692).

Finally, we veriﬁed how our model extrapolates the conditioning variables for values never shown during training. Fig. 4 presents samples where we used a normalised ventricular value higher than 1; in this case, we can see abnormally huge ventricles when using values of 1.5 and 1.9. If we use a negative value (e.g., -0.5), an image without ventricles is generated. Similarly, if we use negative values for the brain normalised for head size, the brain exhibits signs of neurodegeneration, showing smaller volumes of white and grey matter. These ﬁndings suggest that our models learned the concepts behind these conditioning variables during training.

#### 3.3 Synthetic Dataset

We made a synthetic dataset of 100,000 human brain images generated by our model openly available to the community. This dataset is available at Academics Torrents3, FigShare4, and HDRUK Gateway5, together with the conditioning information.

- 3 https://academictorrents.com/details/63aeb864bbe2115ded0aa0d7d36334c026f0660b
- 4 https://ﬁgshare.com/
- 5 https://www.healthdatagateway.org/

Normalised Ventricular Volume

[Figure 19]

[Figure 20]

[Figure 21]

Normalised Brain Volume

[Figure 22]

[Figure 23]

[Figure 24]

-0.1 -0.3 -0.5 1.5

1.9 -0.5

- Fig. 4. Extrapolating values of conditioning variables. During the training of the models, the inputted values of the conditioning variables were scaled between 0 and 1. In this experiment, we tried values outside of this range, and we observed that our model could extrapolate the representation of brain and ventricular volumes, showing that it learned the concept of these variables.

### 4 Conclusions

In our study, we were able to train diﬀusion models to eﬀectively generate synthetic brain images that replicate properties from the training images. As it is the case with natural image generation, our diﬀusion models outperform alternative GANs-based methods in an unconditioned scenario. Additionally, we demonstrated how our methods could be conditioned on covariates such as age, sex, and brain structure volumes to produce the expected representation. In future works, we will develop models that use other scanning modalities as conditioning, such as images and radiological reports. By making the synthetic dataset openly available, this work also addresses one of the biggest limitations in medical machine learning – the challenge of obtaining large imaging datasets – while not posing threats to privacy infringements. In sum, our results show that LDMs are promising models to be explored in medical image generation.

Acknowledgements WHLP and MJC are supported by Wellcome Innovations [WT213038/Z/18/Z]. PTD is supported by the EPSRC Research Council, part of the EPSRC DTP, grant Ref: [EP/R513064/1]. JD is supported by the Intramural Research Program of the NIMH (ZIC-MH002960 and ZIC-MH002968). PFDC is supported by the European Union’s HORIZON 2020 Research and Innovation Programme under the Marie Sklodowska-Curie Grant Agreement No 814302. PN is supported by Wellcome Innovations [WT213038/Z/18/Z] and the UCLH NIHR Biomedical Research Centre. This research has been conducted using the UK Biobank Resource (Project number: 58292).

### References

- 1. Billot, B., Greve, D.N., Puonti, O., Thielscher, A., Van Leemput, K., Fischl, B., Dalca, A.V., Iglesias, J.E.: Synthseg: Domain randomisation for segmentation of

brain mri scans of any contrast and resolution. arXiv preprint arXiv:2107.09559

(2021)

- 2. Brudfors, M., Balbastre, Y., Nachev, P., Ashburner, J.: Mri super-resolution using multi-channel total variation. In: Annual Conference on Medical Image Understanding and Analysis. pp. 217–228. Springer (2018)
- 3. Brudfors, M., Balbastre, Y., Nachev, P., Ashburner, J.: A tool for super-resolving multimodal clinical mri. arXiv preprint arXiv:1909.01140 (2019)
- 4. Chen, G.H., Yang, C.L., Xie, S.L.: Gradient-based structural similarity for image quality assessment. In: 2006 international conference on image processing. pp. 2929–2932. IEEE (2006)
- 5. Chen, S., Ma, K., Zheng, Y.: Med3d: Transfer learning for 3d medical image analysis. arXiv preprint arXiv:1904.00625 (2019)
- 6. Cole, J.H., Poudel, R.P., Tsagkrasoulis, D., Caan, M.W., Steves, C., Spector, T.D., Montana, G.: Predicting brain age with deep learning from raw imaging data results in a reliable and heritable biomarker. NeuroImage 163, 115–124 (2017)
- 7. Creswell, A., White, T., Dumoulin, V., Arulkumaran, K., Sengupta, B., Bharath, A.A.: Generative adversarial networks: An overview. IEEE signal processing magazine 35(1), 53–65 (2018)
- 8. Deng, J., Dong, W., Socher, R., Li, L.J., Li, K., Fei-Fei, L.: Imagenet: A largescale hierarchical image database. In: 2009 IEEE conference on computer vision and pattern recognition. pp. 248–255. Ieee (2009)
- 9. Dhariwal, P., Nichol, A.: Diﬀusion models beat gans on image synthesis. Advances in Neural Information Processing Systems 34, 8780–8794 (2021)
- 10. Esser, P., Rombach, R., Ommer, B.: Taming transformers for high-resolution image synthesis. In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. pp. 12873–12883 (2021)
- 11. Heusel, M., Ramsauer, H., Unterthiner, T., Nessler, B., Hochreiter, S.: Gans trained by a two time-scale update rule converge to a local nash equilibrium. Advances in neural information processing systems 30 (2017)
- 12. Ho, J., Jain, A., Abbeel, P.: Denoising diﬀusion probabilistic models. Advances in Neural Information Processing Systems 33, 6840–6851 (2020)
- 13. Ho, J., Salimans, T.: Classiﬁer-free diﬀusion guidance. In: NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications (2021)
- 14. Jordon, J., Szpruch, L., Houssiau, F., Bottarelli, M., Cherubin, G., Maple, C., Cohen, S.N., Weller, A.: Synthetic data–what, why and how? arXiv preprint arXiv:2205.03257 (2022)
- 15. Jordon, J., Wilson, A., van der Schaar, M.: Synthetic data: Opening the data ﬂoodgates to enable faster, more directed development of machine learning methods. arXiv preprint arXiv:2012.04580 (2020)
- 16. Kodali, N., Abernethy, J., Hays, J., Kira, Z.: On convergence and stability of gans. arXiv preprint arXiv:1705.07215 (2017)
- 17. Kwon, G., Han, C., Kim, D.s.: Generation of 3d brain mri using auto-encoding generative adversarial networks. In: International Conference on Medical Image Computing and Computer-Assisted Intervention. pp. 118–126. Springer (2019)
- 18. Larsen, A.B.L., Sønderby, S.K., Larochelle, H., Winther, O.: Autoencoding beyond pixels using a learned similarity metric. In: International conference on machine learning. pp. 1558–1566. PMLR (2016)
- 19. Li, C., Bovik, A.C.: Content-partitioned structural similarity index for image quality assessment. Signal Processing: Image Communication 25(7), 517–526 (2010)
- 20. Lundervold, A.S., Lundervold, A.: An overview of deep learning in medical imaging focusing on mri. Zeitschrift für Medizinische Physik 29(2), 102–127 (2019)

- 21. Mao, X., Li, Q., Xie, H., Lau, R.Y., Wang, Z., Paul Smolley, S.: Least squares generative adversarial networks. In: Proceedings of the IEEE international conference on computer vision. pp. 2794–2802 (2017)
- 22. Ramesh, A., Dhariwal, P., Nichol, A., Chu, C., Chen, M.: Hierarchical textconditional image generation with clip latents. arXiv preprint arXiv:2204.06125

(2022)

- 23. Rombach, R., Blattmann, A., Lorenz, D., Esser, P., Ommer, B.: High-resolution image synthesis with latent diﬀusion models. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 10684–10695 (2022)
- 24. Rouse, D.M., Hemami, S.S.: Analyzing the role of visual structure in the recognition of natural image content with multi-scale ssim. In: Human Vision and Electronic Imaging XIII. vol. 6806, pp. 410–423. SPIE (2008)
- 25. Saharia, C., Chan, W., Saxena, S., Li, L., Whang, J., Denton, E., Ghasemipour, S.K.S., Ayan, B.K., Mahdavi, S.S., Lopes, R.G., et al.: Photorealistic textto-image diﬀusion models with deep language understanding. arXiv preprint arXiv:2205.11487 (2022)
- 26. Schuhmann, C., Vencu, R., Beaumont, R., Kaczmarczyk, R., Mullis, C., Katta, A., Coombes, T., Jitsev, J., Komatsuzaki, A.: Laion-400m: Open dataset of clip-ﬁltered 400 million image-text pairs. arXiv preprint arXiv:2111.02114 (2021)
- 27. Shen, D., Wu, G., Suk, H.I.: Deep learning in medical image analysis. Annual review of biomedical engineering 19, 221 (2017)
- 28. Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., Ganguli, S.: Deep unsupervised learning using nonequilibrium thermodynamics. In: International Conference on Machine Learning. pp. 2256–2265. PMLR (2015)
- 29. Song, J., Meng, C., Ermon, S.: Denoising diﬀusion implicit models. arXiv preprint arXiv:2010.02502 (2020)
- 30. Sudlow, C., Gallacher, J., Allen, N., Beral, V., Burton, P., Danesh, J., Downey, P., Elliott, P., Green, J., Landray, M., et al.: Uk biobank: an open access resource for identifying the causes of a wide range of complex diseases of middle and old age. PLoS medicine 12(3), e1001779 (2015)
- 31. Sun, L., Chen, J., Xu, Y., Gong, M., Yu, K., Batmanghelich, K.: Hierarchical amortized gan for 3d high resolution medical image synthesis. IEEE Journal of Biomedical and Health Informatics (2022)
- 32. Wang, L., Chen, W., Yang, W., Bi, F., Yu, F.R.: A state-of-the-art review on image synthesis with generative adversarial networks. IEEE Access 8, 63514–63537 (2020)
- 33. Wang, T., Lei, Y., Fu, Y., Wynne, J.F., Curran, W.J., Liu, T., Yang, X.: A review on medical imaging synthesis using deep learning and its clinical applications. Journal of applied clinical medical physics 22(1), 11–36 (2021)
- 34. Zhang, R., Isola, P., Efros, A.A., Shechtman, E., Wang, O.: The unreasonable eﬀectiveness of deep features as a perceptual metric. In: Proceedings of the IEEE conference on computer vision and pattern recognition. pp. 586–595 (2018)

