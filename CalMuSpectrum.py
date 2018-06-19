#!/usr/bin/python
import numpy as np


#This program will return a MuEffective vs. Wavelength Spectrum
#The Efficiency from the Simulation (calculated witha a fit function) is compared
#to the Transmission percentage of data to return a Mueff vs Wavelength spectrum



Waves1 = [600, 599, 598, 597, 596, 595, 594, 593, 592, 591, 590, 589, 588, 587, 586,
          585, 584, 583, 582, 581, 580, 579, 578, 577, 576, 575, 574, 573, 572, 571,
          570, 569, 568, 567, 566, 565, 564, 563, 562, 561, 560, 559, 558, 557, 556,
          555, 554, 553, 552, 551, 550, 549, 548, 547, 546, 545, 544, 543, 542, 541,
          540, 539, 538, 537, 536, 535, 534, 533, 532, 531, 530, 529, 528, 527, 526,
          525]

Waves2 = [524, 523, 522, 521, 520, 519, 518, 517, 516, 515, 514, 513, 512, 511, 510,
          509, 508, 507, 506, 505, 504, 503, 502, 501, 500, 499, 498, 497, 496, 495,
          494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480,
          479, 478, 477, 476, 475, 474, 473, 472, 471, 470, 469, 468, 467, 466, 465,
          464, 463, 462, 461, 460, 459, 458, 457, 456, 455, 454, 453, 452, 451, 450]

Waves3 = [449, 448, 447, 446, 445, 444, 443, 442, 441, 440, 439, 438, 437, 436, 435,
          434, 433, 432, 431, 430, 429, 428, 427, 426, 425, 424, 423, 422, 421, 420,
          419, 418, 417, 416, 415, 414, 413, 412, 411, 410, 409, 408, 407, 406, 405,
          404, 403, 402, 401, 400, 399, 398, 397, 396, 395, 394, 393, 392, 391, 390,
          389, 388, 387, 386, 385, 384, 383, 382, 381, 380]

#HighDoseRate
TranData10_1  = [90.2621, 90.2957, 90.2623, 90.2538, 90.2554, 90.2620, 90.2424, 90.2251, 90.2044,
               90.2205, 90.2018, 90.1875, 90.1706, 90.1580, 90.1513, 90.1443, 90.1410, 90.1309,
               90.1361, 90.1527, 90.1035, 90.0795, 90.0991, 90.0723, 90.0722, 90.0687, 90.0579,
               90.0425, 90.0242, 90.0249, 90.0287, 89.9773, 90.0019, 89.9821, 89.9908, 89.9603,
               89.9375, 89.9619, 89.9842, 89.9608, 89.9538, 89.9044, 89.8916, 89.8654, 89.8790,
               89.8553, 89.8248, 89.8386, 89.8283, 89.8093, 89.8032, 89.8116, 89.7625, 89.7824,
               89.7627, 89.7566, 89.7247, 89.7311, 89.6930, 89.6879, 89.6764, 89.6527, 89.6109,
               89.6225, 89.5872, 89.5905, 89.5425, 89.5305, 89.5239, 89.5155, 89.4874, 89.4625,
               89.4368, 89.4323, 89.4071, 89.3663]
TranData10_2  = [89.3759, 89.3691, 89.3461, 89.3118, 89.3075, 89.2617, 89.2303, 89.2333, 89.2038,
                 89.1895, 89.1906, 89.1456, 89.1105, 89.1001, 89.0592, 89.0575, 89.0229, 89.0154,
                 88.9627, 88.9333, 88.9125, 88.8748, 88.8591, 88.8386, 88.7809, 88.7652, 88.7111,
                 88.6733, 88.6441, 88.6178, 88.5773, 88.5279, 88.5123, 88.4634, 88.4467, 88.4006,
                 88.3567, 88.3419, 88.2832, 88.2335, 88.2106, 88.1571, 88.1332, 88.0892, 88.0479,
                 88.0051, 87.9600, 87.9357, 87.8735, 87.8598, 87.8157, 87.7601, 87.7088, 87.6690,
                 87.6115, 87.5533, 87.5205, 87.4625, 87.4284, 87.3376, 87.2891, 87.2080, 87.1606,
                 87.0897, 86.9903, 86.9457, 86.8275, 86.7602, 86.7146, 86.6253, 86.5405, 86.4525,
                 86.3557, 86.2825, 86.2039]

TranData10_3  = [86.0953, 86.0021, 85.8952, 85.8045, 85.7100, 85.5956, 85.4854, 85.4048, 85.2471,
                 85.1629, 85.0319, 84.9500, 84.7907, 84.6798, 84.5467, 84.4089, 84.2420, 84.1257,
                 83.9357, 83.8068, 83.5925, 83.4000, 83.2028, 82.9718, 82.7691, 82.4678, 82.1861,
                 81.8555, 81.5580, 81.1706, 80.7882, 80.2983, 79.7677, 79.1864, 78.4330, 77.5392,
                 76.3629, 74.8550, 72.8775, 70.3492, 67.0830, 62.9762, 57.9656, 51.9878, 45.2120,
                 37.8602, 30.4388, 23.2939, 16.9424, 11.6712, 7.62320, 4.71990, 2.79300, 1.58800,
                 0.87930, 0.49140, 0.28430, 0.17780, 0.12480, 0.09790, 0.08400, 0.07930, 0.07590,
                 0.07320, 0.07250, 0.07210, 0.07110, 0.07130, 0.07070, 0.07030]


#410 - 500nm
#LowDoseRate
#TranData10 = [67.8551, 70.5562, 72.6745, 74.2998, 75.6362, 76.6348, 77.5308, 78.2662, 78.8080,
#              79.2604, 79.7564, 80.2382, 80.6584, 80.9926, 81.3757, 81.6644, 81.9992, 82.2830,
#              82.5323, 82.7281, 82.9676, 83.1639, 83.3762, 83.5774, 83.7456, 83.9235, 84.0666,
#              84.2165, 84.3427, 84.4841, 84.6756, 84.7660, 84.9065, 85.0539, 85.1755, 85.3169,
#              85.4136, 85.5766, 85.6759, 85.8206, 85.9108, 85.9615, 86.0736, 86.1450, 86.3456,
#              86.4380, 86.5572, 86.6275, 86.7326, 86.9051, 87.0099, 87.1066, 87.1874, 87.2452,
#              87.3423, 87.3991, 87.4872, 87.5614, 87.6289, 87.7041, 87.7229, 87.7337, 87.7907,
#              87.8613, 87.9190, 87.9404, 88.0473, 88.0864, 88.1164, 88.2057, 88.2262, 88.2866,
#              88.3255, 88.3730, 88.4180, 88.4923, 88.5089, 88.5810, 88.5922, 88.6212, 88.6732,
#              88.6975, 88.7506, 88.7800, 88.8360, 88.8531, 88.9060, 88.9093, 88.9607, 89.0202,
#              89.0192]

#TranData6 = [72.3600, 74.3720, 75.9457, 77.1469, 78.1127, 78.8856, 79.5379, 80.0134, 80.4696,
#             80.8722, 81.2141, 81.5993, 81.8885, 82.2136, 82.5207, 82.7341, 82.9575, 83.1777,
#             83.4068, 83.6213, 83.8181, 83.9232, 84.1003, 84.2116, 84.3946, 84.5547, 84.6815,
#             84.7731, 84.9588, 85.0552, 85.1740, 85.2855, 85.3894, 85.5095, 85.5786, 85.7380,
#             85.7890, 85.8866, 85.9635, 86.0760, 86.2081, 86.2893, 86.3454, 86.4343, 86.4933,
#             86.5860, 86.6852, 86.7265, 86.8297, 86.8840, 86.9638, 87.0550, 87.1682, 87.2447,
#             87.2740, 87.3627, 87.4240, 87.4389, 87.5261, 87.5499, 87.6008, 87.6203, 87.6510,
#             87.6696, 87.7245, 87.7658, 87.8242, 87.8943, 87.9197, 87.9662, 88.0102, 88.0250,
#             88.1097, 88.1591, 88.1879, 88.2474, 88.2363, 88.2996, 88.3434, 88.3725, 88.4039,
#             88.4907, 88.5012, 88.5304, 88.5857, 88.6110, 88.6332, 88.6586, 88.6710, 88.7398,
#             88.7885]



#TranData4  = [76.3641, 77.9742, 79.2849, 80.2297, 81.0126, 81.6138, 82.0738, 82.4983, 82.8674,
#              83.1516, 83.3961, 83.6989, 83.9745, 84.2014, 84.3896, 84.5813, 84.7267, 84.8817,
#              85.0631, 85.2088, 85.3591, 85.4567, 85.5912, 85.6826, 85.7857, 85.9017, 85.9683,
#              86.0301, 86.1617, 86.2197, 86.3020, 86.4172, 86.4925, 86.5647, 86.6189, 86.7151,
#              86.7524, 86.8291, 86.8602, 86.9545, 87.0417, 87.1179, 87.1181, 87.1755, 87.2416,
#              87.2832, 87.3575, 87.4046, 87.4525, 87.5060, 87.5807, 87.6405, 87.7449, 87.7680,
#              87.8121, 87.8531, 87.9141, 87.9327, 87.9918, 88.0104, 88.0240, 88.0598, 88.0606,
#              88.0612, 88.1134, 88.1457, 88.1890, 88.2384, 88.2476, 88.2749, 88.2853, 88.3364,
#              88.3759, 88.4202, 88.4125, 88.4973, 88.4595, 88.5009, 88.5240, 88.5587, 88.5722,
#              88.6238, 88.6277, 88.6550, 88.7020, 88.6903, 88.7106, 88.7479, 88.7487, 88.7900,
#              88.8494]


MuResults  = [None]*70;
start    = 0.003
stop     = 0.09
total    = 200000
step     = (stop-start)/total
minimum  = 100;
Diff     = [None]*total;
Results = [None]*total;

for j in range (len(Waves3)):

    k = 0;

    for i in np.arange(start,stop,step):
         #10 mm fit function
        Eff     = 100 * np.exp(-0.105095-10.0157*(i));
        Diff[k]  = abs(TranData10_3[j] - Eff);

        #6 mm fit function
        #Eff   = 100 * np.exp(-0.10241-6.029*(i))
        #Diff[k]  = abs(TranData6[j] - Eff);

        #4 mm fit function
        #Eff   = 100 * np.exp(-0.1019-4.0212*(i))
        #Diff[k]  = abs(TranData4[j] - Eff);

        MuValue = k*step+start;
        Results[k] = MuValue;
        k = k + 1;
    mink      = Diff.index(min(Diff))
    MuResults[j] = Results[mink];
    if MuResults[j] < 0.00001:
        MuResults[j] = 100;


f = open('Abs_Spectrum_10mm_HDR.txt','w')

print>>f, 'Wavelength \t\tMuEffective'
for w,mr in zip(Waves3,MuResults):
    print>>f, "%.7f \t\t%.7f" % (w, mr)

f.close()
