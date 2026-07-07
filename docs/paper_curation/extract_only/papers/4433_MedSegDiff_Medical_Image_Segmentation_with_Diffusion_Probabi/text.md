# arXiv:2211.00611v5[cs.CV]15Jan2023

## MedSegDiﬀ: Medical Image Segmentation with Diﬀusion Probabilistic Model

Junde Wu1, Rao Fu2, Huihui Fang1, Yu Zhang2, Yehui Yang1, Haoyi Xiong1, Huiying Liu3, and Yanwu Xu1 ( )

- 1 Baidu Research
- 2 Mind Vogue Lab

3 Institute for Infocomm Research, A*STAR

Abstract. Diﬀusion probabilistic model (DPM) recently becomes one of the hottest topic in computer vision. Its image generation application such as Imagen, Latent Diﬀusion Models and Stable Diﬀusion have shown impressive generation capabilities, which aroused extensive discussion in the community. Many recent studies also found it is useful in many other vision tasks, like image deblurring, super-resolution and anomaly detection. Inspired by the success of DPM, we propose the ﬁrst DPM based model toward general medical image segmentation tasks, which we named MedSegDiﬀ. In order to enhance the step-wise regional attention in DPM for the medical image segmentation, we propose dynamic conditional encoding, which establishes the state-adaptive conditions for each sampling step. We further propose Feature Frequency Parser (FF-Parser), to eliminate the negative eﬀect of high-frequency noise component in this process. We verify MedSegDiﬀ on three medical segmentation tasks with diﬀerent image modalities, which are optic cup segmentation over fundus images, brain tumor segmentation over MRI images and thyroid nodule segmentation over ultrasound images. The experimental results show that MedSegDiﬀ outperforms state-of-the-art (SOTA) methods with considerable performance gap, indicating the generalization and eﬀectiveness of the proposed model. Our code is released at https://github.com/WuJunde/MedSegDiff.

Keywords: diﬀusion probabilistic model, medical image segmentation, brain tumor, optic cup, thyroid nodule

### 1 Introduction

Medical image segmentation is the process of partitioning a medical image into meaningful regions. Segmentation is a fundamental step in many medical image analysis applications such as diagnosis, surgical planning, and image-guided surgery. This is important because it allows doctors and other medical professionals to better understand what they’re looking at. It also makes it easier to compare images and track changes over time. In recent years, there has been a growing interest in automatic medical image segmentation methods. These

methods have the potential to reduce the time and eﬀort required for manual segmentation, and to improve the consistency and accuracy of results. With the development of the deep learning techniques, more and more studies successfully applied the neural network (NN) based models to the medical image segmentation tasks, from the popular convolution neural networks (CNN) [11] to the recent vision transformers (ViT) [3,22,12,28].

Very recently, diﬀusion probabilistic model (DPM)[9] gained popularity as a powerful class of generative models[27], that is able to generate images with high diversity and synthesis quality. Recent large diﬀusion models, such as DALLE2[17], Imagen[19], and Stable Diﬀusion[18] have shown incredible generation capability. Diﬀusion models are originally applied in ﬁelds in which there is no absolute ground-truth. However, recent studies show that it is also eﬀective for the problems in which the ground-truth is unique, like super-resolution[20] and deblurring[24].

Inspired by the recent success of DPM, we design a unique DPM-based segmentation model for the medical image segmentation tasks. To our knowledge, we are the ﬁrst to propose the DPM-based model under the background of general medical image segmentation with diﬀerent image modalities. We note that in tasks of medical image segmentation, the lesions/organs are often ambiguous and hard to discriminate from the background. In that case, an adaptive calibration process is the key to obtain a delicate result. Following this mindset, we propose dynamic conditional encoding over vanilla DPM to design the proposed model, named MedSegDiﬀ. Note that in the iterative sampling process, MedSegDiﬀ conditions each of the step with image prior, in order to learn the segmentation map from it. Toward the adaptive regional attention, we integrate the segmentation map of current step into the image prior encoding at each step. The speciﬁc implementation is to fuse the current-step segmentation mask with the image prior on the feature level with a multi-scale manner. In this way, the corrupted current-step mask helps to dynamically enhance the condition features, thus improves the reconstruction accuracy. In order to eliminate the high-frequency noises in the corrupted given mask in this process, we further propose the feature frequency parser (FF-Parser) to ﬁlter the features in the Fourier space. FF-Parsers are adopted on each skip connection path for the multi-scale integration. We verify MedSegDiﬀ on three diﬀerent medical segmentation tasks, the optic-cup segmentation, the brain tumor segmentation, and the thyroid nodule segmentation. The images of these tasks have diﬀerent modalities, which are the fundus images, brain CT images, the ultrasound images respectively. MedSegDiﬀ outperforms the previous SOTA on all three tasks with diﬀerent modalities, which shows the generalization and eﬀectiveness the proposed method. In brief, the contributions of the paper are:

- – The ﬁst to propose DPM-based model toward general medical image segmentation.
- – Dynamic conditional encoding strategy is proposed for step-wise attention.
- – FF-Parser is proposed to eliminate the negative eﬀects of high-frequency components.

- – SOTA performance on three diﬀerent medical segmentation tasks with different image modalities.

### 2 Method

We design our model based on diﬀusion model mentioned in[9]. Diﬀusion models are generative models composed of two stages, a forward diﬀusion stage and a reverse diﬀusion stage. In the forward process, the segmentation label x0 is gradually added Gaussian noise through a series of steps T. In the reverse process, a neural network is trained to recover the original data by reversing the noising process, which can be represented as:

pθ(x0:T−1|xT) = ΠtT=1pθ(xt−1|xt), (1)

where θ is reverse process parameters. Starting from a Gaussian noise, pθ(xT) = N(xT;0,In×n), where I is the raw image, the reverse process transforms the latent variable distribution pθ(xT) to the data distribution pθ(x0). To be symmetrical to the forward process, the reverse process recovers the noise image step by step to obtain the ﬁnal clear segmentation.

Following the standard implementation of DPM, we adopt a UNet as the network for the learning. An illustration is shown in Figure 1. In order to achieve the segmentation, we condition the step estimation function by raw image prior, which can be represented as:

θ(xt,I,t) = D((EtI + Etx,t),t), (2)

where EtI is the conditional feature embedding, in our case, the raw image embedding, Etx is the segmentation map feature embedding of the current step. The two components are added and sent to a UNet decoder D for the reconstruction. The step index t is integrated with the added embedding and decoder features. In each of these, it is embedded using a shared learned look-up table, following [9].

#### 2.1 Dynamic Conditional Encoding

In most conditional DPM, the conditional prior will be a unique given information. However, medical image segmentation is notorious for its ambiguous objects. The lesions or tissues are often hard to discriminate from its background. The low-contrast image modalities, such as MRI or ultrasound images, make it even worse. Given only a static image I as the condition for each step will be hard to learn. To address this problem, we propose a dynamic conditional encoding for each step. We note that on the one hand, the raw image contains the accurate segmentation target information but hard to discriminate from the background, on the other hand, the current-step segmentation map contains the enhanced target regions but not accurate. This motivated us to integrate the

[Figure 1]

Fig.1: An illustration of MedSegDiﬀ. For the clarity, the time step encoding is omitted in the ﬁgure.

current-step segmentation information xt into the conditional raw image encoding for the mutual complement. To be speciﬁc, we implement the integration on the feature level. In the raw image encoder, we enhance its intermediate feature with the current-step encoding features. Each scale of the conditional feature map mkI is fused with the xt encoding features mkx with the same shape, k is the index of layer. The fusion is implemented by an attentive-like mechanism A. In particular, two feature maps are ﬁrst applied layer normalization and multiply together to get an aﬃnity map. Then we multiply the aﬃnity map with the condition encoding features to enhance the attentive region, which is:

A(mkI,mkx) = (LN(mkI) ⊗ LN(mkx)) ⊗ mkI, (3)

where ⊗ implies element-wise multiplication, LN denotes layer normalization. The operation is applied on the middle two stages, where each is the convolutional stage implemented following ResNet34. Such a strategy helps MedSegDiﬀ dynamically localize and calibrate the segmentation. Although eﬀective the strategy it is, another speciﬁc problem is that integrating xt embedding will induce extra high-frequency noise. To address this problem, we propose FF-Parser to constrain the high-frequency components in the features.

#### 2.2 FF-Parser

We connect FF-parser in the path ways of the feature integration. The function of it is to constrain the noise-related components in the xt features. Our main idea is to learn a parameterized attentive (weight) map applying on the Fourier-space features. Given a decoder feature map m ∈ RH×W×C, we ﬁrst perform 2D FFT(fast fourier transform) along the spatial dimensions, which we can represented as:

M = F[m] ∈ CH×W×C, (4)

where F[·] denotes the 2D FFT. We then modulate the spectrum of m by multiplying a parameterized attentive map A ∈ CH×W×C to M:

M = A ⊗ M, (5)

where ⊗ denotes the element-wise product. Finally, we reverse M back to the spatial domain by adopting inverse FFT:

m = F−1[M ]. (6)

FF-Parser can be regarded as a learnable version of frequency ﬁlters which are wildly applied in the digital image processing [16]. Diﬀerent from the spacial attention, it globally adjusts the components of the speciﬁc frequencies. Thus it can be learn to constrain the high-frequency component for the adaptive integration.

[Figure 2]

- Fig.2: An illustration of FF-Parser. FFT denotes Fast Fourier Transform.

#### 2.3 Training and Architecture

MedSegDiﬀ is trained following the standard process of DPM [9]. Speciﬁcally, the loss can be represented as:

0, ,t[|| − θ( aˆtx0 + 1 − aˆt ,Ii,t)||2]. (7)

L = Ex

In each of the iteration, a random couple of raw image Ii and segmentation label Si will be sampled for the training. The iteration number is sampled from a uniform distribution and from a Gaussian distribution.

The main architecture of MedSegDiﬀ is a modiﬁed ResUNet[26], which we implement it with a ResNet encoder following a UNet decoder. The detailed network setting is following [14]. I and xt are encoded with two individual encoders.

The encoder is consisted of three convolution stages. Each stage contains several residual blocks. The number of residual blocks in each stage is following that of ResNet34. Each residual block is composed of two convolutional blocks, each one consists of group-norm and SiLU[5] active layer and a convolutional layer. The residual block receives the time embedding through a linear layer, SiLU activation, and another linear layer. The result is then added to the output of the ﬁrst convolutional block. The obtained EI and Ex

t are added together and sent to the last encoding stage. A standard convolutional decoder is connected to predict the ﬁnal result.

### 3 Experiments

#### 3.1 Dataset

We conduct the experiments on three diﬀerent medical tasks with diﬀerent image modalities, which are optic-cup segmentation from fundus images, brain tumor segmentation from MRI images, and thyroid nodule segmentation from ultrasound images. The experiments of glaucoma, thyroid cancer and melanoma diagnosis are conducted on REFUGE-2 dataset [6], BraTs-2021 dataset [2] and DDTI dataset [15], which contain 1200, 2000, 8046 samples, respectively. The datasets are publicly available with both segmentation and diagnosis labels. Train/validation/test sets are split following the default settings of the dataset.

#### 3.2 Implementation Details

We experiment with huge, large, basic, and small variants of our model, MedSegDiﬀ++, MedSegDiﬀ-L, MedSegDiﬀ-B, and MedSegDiﬀ-S, respectively.

In MedSegDiﬀ-S, MedSegDiﬀ-B MedSegDiﬀ-L, MedSegDiﬀ++, we use UNet with 4x, 5x, 6x, 6x downsamples respectively. In the experiments, we employ 100 diffusion steps for the inference, which is much smaller than most of the previous studies[9,14]. All the experiments are implemented with the PyTorch platform and trained/tested on 4 Tesla P40 GPU with 24GB of memory except MedSegDiﬀ++ and MedSegDiﬀ-L. All images are uniformly resized to the dimension of 256×256 pixels. The networks are trained in an end-to-end manner using AdamW[13] optimizer. MedSegDiﬀ-B and MedSegDiﬀ-S are trained with 32 batch size, MedSegDiﬀ-L and MedSegDiﬀ++ are trained with 64 batch size. The learning rate is initially set to 1 ×10−4. All models are set 25 times of ensemble in the inference. We use STAPLE[23] algorithm to fuse the diﬀerent samples. The diﬀusion based competitor EnsemDiﬀ[25] is reproduced with the same setting for the fair comparison.

#### 3.3 Main Results

We compare with SOTA segmentation methods proposed for the three speciﬁc tasks and general medical image segmentation methods. The main results are

shown in Table 1. In the table, ResUnet[26] and BEAL[21] are proposed for optic disc/cup segmentation, TransBTS[22] and EnsemDiﬀ[25] are proposed for the brain tumor segmentation, MTSeg[7] and UltraUNet[4] are proposed for the Thyroid Nodule segmentation, CENet[8], MRNet[11], SegNet[1], nnUNet[10] and TransUNet[3] are proposed for the general medical image segmentation. We evaluate the segmentation performance by Dice score and IoU.

In Table 1, we compare with the methods implemented with various network architectures, including CNN (ResUNet, BEAL, nnUNet, SegNet), vision transformer (TransBTS, TransUNet) and DPM (EnsemDiﬀ). We can see the advanced network architectures commonly gain better results. For example, in optic-cup segmentation, ViT-based general segmentation method: TransUNet is even better than the CNN-based task toward method: BEAL. On brain tumor segmentation, recently proposed DPM-based segmentation method EnsemDiﬀ outperforms all those previous ViT-based competitors, i.e., TransBTS and TransUNet. MedSegDiﬀ not only adopts the recent successful DPM, but also designs an appropriate strategy over it speciﬁcally towards the general medical image segmentation task. We can see MedSegDiﬀ outperforms all the other methods on three diﬀerent tasks, which shows the generalization toward diﬀerent medical segmentation tasks and diﬀerent image modalities. Comparing against DPM-based model proposed speciﬁcally for the brain tumor segmentation, i.e., EnsemDiﬀ, it improves 2.3% on Dice and 2.4% on IoU, which indicates the eﬀectiveness of our unique techniques, i.e, dynamic conditioning and FF-Parser.

[Figure 3]

- Fig.3: The visual comparison of Top-4 general medical image segmentation methods in Table 1. From top to down are brain-tumor segmentation, opticcup segmentation and thyroid nodule segmentation, respectively.

Figure 3 shows several typical examples generated by our MedSegDiﬀ and other SOTA methods. It can be seen the target lesions/tissues are all ambiguous

on the images so that they are hard to be recognized by human eyes. Comparing with these computer-aided methods, it is obvious that the segmentation maps generated by the proposed method are more accurate than the other methods, especially for the ambiguous regions. To be beneﬁted from DPM together with the proposed dynamic conditioning and FF-Parser, it can better localize and calibrate the segmentation on the low-contrast or ambiguous images.

- Table 1: The comparison of MedSegDiﬀ with SOTA segmentation methods. Best results are denoted as bold. The grey background denotes the methods are proposed for that/these particular tasks.

| |Optic-Cup|Brain-Turmor<br><br>|Thyroid Nodule|
|---|---|---|---|
| |Dice IoU|Dice IoU<br><br>|Dice IoU|
|ResUnet BEAL|80.1 72.3 83.5 74.1<br><br>|- -<br><br>- -<br><br><br>|- -<br>- -<br>|
|TransBTS EnsemDiﬀ|- -<br><br>- -<br>|87.6 78.3<br><br>88.7 80.9<br><br><br>|- -<br><br>- -<br>|
|MTSeg UltraUNet|- -<br><br>- -<br><br><br>|- -<br>- -<br>|82.3 75.2 84.5 76.2<br><br>|
|CENet MRNet SegNet nnUNet TransUNet<br><br>|78.6 69,4 84.2 75.1 80.4 70.7<br><br>84.9 75.1<br><br>85.6 75.9<br><br><br>|76.2 68.9 83.4 75.6 80.2 72.9 88.2 80.4 86.6 79.0<br><br>|78.9 71.2<br><br>80.4 73.4<br><br>81.7 74.5 84.2 76.2 83.5 75.1<br><br><br>|
|MedSegDiﬀ-S MedSegDiﬀ-B MedSegDiﬀ-L MedSegDiﬀ++<br><br>|81.2 71.7<br><br>85.9 76.2<br><br>86.9 78.5<br><br>87.5 79.1<br><br><br>|82.3 73.6<br><br>88.9 81.2<br><br>89.9 82.3<br><br>90.5 82.8<br><br><br>|80.8 73.7 84.8 76.4 86.1 79.6 86.6 80.2<br><br>|

#### 3.4 Ablation Study

We do comprehensive ablation study to verify the eﬀectiveness of the proposed dynamic conditioning and FF-Parser. The results are shown in Table 2, where Dy-Cond denotes dynamic conditioning. We evaluate the performance by Dice score(%) on all three tasks. From the table, we can see Dy-Cond gains considerable improvements over vanilla DPM. On the case which the region localization is important, i.e., optic-cup segmentation, it improves 2.1%. On the cases which the images are low-contrast, like brain tumor and thyroid nodule segmentation, it improves 1.6% and 1.8% respectively. It shows Dy-Cond is a generally eﬀective strategy on DPM for both of the cases. FF-Parser which established over Dy-Cond mitigates the high-frequency noises thus further optimize the segmentation results. It helps MedSegDiﬀ further improve near 1% performance and achieve the best on all three tasks.

- Table 2: An ablation study on dynamic condition encoding and FF-Parser. Dice score(%) is used as the metric.

|Dy-Cond FF-Parser<br><br>|OpticCup BrainTumor ThyroidNodule|
|---|---|
| |84.6 88.2 84.1<br><br>86.7 89.8 85.9<br><br>87.5 90.5 86.6<br>|

### 4 Conclusion

In this paper, we provided a scheme for DPM-based general medical image segmentation, named MedSegDiﬀ. We propose two novel techniques to promise the performance of it, i.e., the dynamic conditional encoding and FF-Parser. The comparison experiments are conducted on three medical image segmentation tasks with diﬀerent image modalities, which shows our model outperforms previous SOTA. As the ﬁrst DPM application in general medical image segmentation, we believe MedSegDiﬀ will serve as an essential benchmark for future research.

### References

- 1. Badrinarayanan, V., Kendall, A., Cipolla, R.: Segnet: A deep convolutional encoder-decoder architecture for image segmentation. IEEE transactions on pattern analysis and machine intelligence 39(12), 2481–2495 (2017)
- 2. Baid, U., Ghodasara, S., Mohan, S., Bilello, M., Calabrese, E., Colak, E., Farahani, K., Kalpathy-Cramer, J., Kitamura, F.C., Pati, S., et al.: The rsna-asnr-miccai brats 2021 benchmark on brain tumor segmentation and radiogenomic classiﬁcation. arXiv preprint arXiv:2107.02314 (2021)
- 3. Chen, J., Lu, Y., Yu, Q., Luo, X., Adeli, E., Wang, Y., Lu, L., Yuille, A.L., Zhou, Y.: Transunet: Transformers make strong encoders for medical image segmentation. arXiv preprint arXiv:2102.04306 (2021)
- 4. Chu, C., Zheng, J., Zhou, Y.: Ultrasonic thyroid nodule detection method based on u-net network. Computer Methods and Programs in Biomedicine 199, 105906

(2021)

- 5. Elfwing, S., Uchibe, E., Doya, K.: Sigmoid-weighted linear units for neural network function approximation in reinforcement learning. Neural Networks 107, 3–11

(2018)

- 6. Fang, H., Li, F., Fu, H., Sun, X., Cao, X., Son, J., Yu, S., Zhang, M., Yuan, C., Bian, C., et al.: Refuge2 challenge: Treasure for multi-domain learning in glaucoma assessment. arXiv preprint arXiv:2202.08994 (2022)
- 7. Gong, H., Chen, G., Wang, R., Xie, X., Mao, M., Yu, Y., Chen, F., Li, G.: Multitask learning for thyroid nodule segmentation with thyroid region prior. In: 2021 IEEE 18th International Symposium on Biomedical Imaging (ISBI). pp. 257–261. IEEE (2021)
- 8. Gu, Z., Cheng, J., Fu, H., Zhou, K., Hao, H., Zhao, Y., Zhang, T., Gao, S., Liu, J.: Ce-net: Context encoder network for 2d medical image segmentation. IEEE transactions on medical imaging 38(10), 2281–2292 (2019)
- 9. Ho, J., Jain, A., Abbeel, P.: Denoising diﬀusion probabilistic models. Advances in Neural Information Processing Systems 33, 6840–6851 (2020)
- 10. Isensee, F., Jaeger, P.F., Kohl, S.A., Petersen, J., Maier-Hein, K.H.: nnu-net: a self-conﬁguring method for deep learning-based biomedical image segmentation. Nature methods 18(2), 203–211 (2021)
- 11. Ji, W., Yu, S., Wu, J., Ma, K., Bian, C., Bi, Q., Li, J., Liu, H., Cheng, L., Zheng, Y.: Learning calibrated medical image segmentation via multi-rater agreement modeling. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 12341–12351 (2021)
- 12. Liu, C., Zhao, R., Shi, Z.: Remote-sensing image captioning based on multilayer aggregated transformer. IEEE Geoscience and Remote Sensing Letters 19, 1–5

(2022)

- 13. Loshchilov, I., Hutter, F.: Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101 (2017)
- 14. Nichol, A.Q., Dhariwal, P.: Improved denoising diﬀusion probabilistic models. In: International Conference on Machine Learning. pp. 8162–8171. PMLR (2021)
- 15. Pedraza, L., Vargas, C., Narváez, F., Durán, O., Muñoz, E., Romero, E.: An open access thyroid ultrasound image database. In: 10th International symposium on medical information processing and analysis. vol. 9287, pp. 188–193. SPIE (2015)
- 16. Pitas, I.: Digital image processing algorithms and applications. John Wiley & Sons

(2000)

- 17. Ramesh, A., Dhariwal, P., Nichol, A., Chu, C., Chen, M.: Hierarchical textconditional image generation with clip latents. arXiv preprint arXiv:2204.06125

(2022)

- 18. Rombach, R., Blattmann, A., Lorenz, D., Esser, P., Ommer, B.: High-resolution image synthesis with latent diﬀusion models. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 10684–10695 (2022)
- 19. Saharia, C., Chan, W., Saxena, S., Li, L., Whang, J., Denton, E., Ghasemipour, S.K.S., Ayan, B.K., Mahdavi, S.S., Lopes, R.G., et al.: Photorealistic textto-image diﬀusion models with deep language understanding. arXiv preprint arXiv:2205.11487 (2022)
- 20. Saharia, C., Ho, J., Chan, W., Salimans, T., Fleet, D.J., Norouzi, M.: Image superresolution via iterative reﬁnement. IEEE Transactions on Pattern Analysis and Machine Intelligence (2022)
- 21. Wang, S., Yu, L., Li, K., Yang, X., Fu, C.W., Heng, P.A.: Boundary and entropydriven adversarial learning for fundus image segmentation. In: International Conference on Medical Image Computing and Computer-Assisted Intervention. pp. 102–110. Springer (2019)
- 22. Wang, W., Chen, C., Ding, M., Yu, H., Zha, S., Li, J.: Transbts: Multimodal brain tumor segmentation using transformer. In: International Conference on Medical Image Computing and Computer-Assisted Intervention. pp. 109–119. Springer

(2021)

- 23. Warﬁeld, S.K., Zou, K.H., Wells, W.M.: Simultaneous truth and performance level estimation (staple): an algorithm for the validation of image segmentation. IEEE transactions on medical imaging 23(7), 903–921 (2004)
- 24. Whang, J., Delbracio, M., Talebi, H., Saharia, C., Dimakis, A.G., Milanfar, P.: Deblurring via stochastic reﬁnement. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 16293–16303 (2022)
- 25. Wolleb, J., Sandkühler, R., Bieder, F., Valmaggia, P., Cattin, P.C.: Diﬀusion models for implicit image segmentation ensembles. arXiv preprint arXiv:2112.03145

(2021)

- 26. Yu, S., Xiao, D., Frost, S., Kanagasingam, Y.: Robust optic disc and cup segmentation with deep learning for glaucoma detection. Computerized Medical Imaging and Graphics 74, 61–71 (2019)
- 27. Zhao, R., Shi, Z.: Text-to-remote-sensing-image generation with structured generative adversarial networks. IEEE Geoscience and Remote Sensing Letters 19, 1–5

(2021)

- 28. Zhao, R., Shi, Z., Zou, Z.: High-resolution remote sensing image captioning based on structured attention. IEEE Transactions on Geoscience and Remote Sensing 60, 1–14 (2021)

