# Performance Modeling of Industrial DNN Applications
Deep Neural Network (DNN) applications provide an increasing number of solutions in industry (e.g., for seismic analysis, workers safety, anomaly detection in surveilled videos, in smart oil fields) that typically run on  private or public cloud platforms (i.e., Amazon Cloud and Chameleon). Due to uncertain performance and heterogeneous resources, both inherent to the cloud and fog computing environments, the inference time of the DNN applications are stochastic. Such stochasticity, if not captured, can potentially lead to low Quality of Service (QoS) or even a disaster in the industry. To capture the stochasticity we focus on statistically modelling the inference time of four categorically different DNN applications on both Amazon and Chameleon cloud platforms. Therefore, this repository is the benchmark of inference execution times of four different categories of DNN-based applications. The applications are given below -
1. Fire Detection
2. Human Activity Recognition
3. Oil Spill Detection
4. Acuistic Impedence Estimation

We deployed the pretrained models of the applications in the cloud platforms and run the inference operations with test data to capture the time of inference. For each application, we run the inference operations thirty times and consider it as sample data to model the performance. The detailed performance modeling of the applications are provided in the paper named "Performance Modeling of Deep Neural Network Applications on Heterogeneous Cloud Resources" that is submitted in IGSC 2020.

