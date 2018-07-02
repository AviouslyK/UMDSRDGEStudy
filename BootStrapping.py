import numpy

#Program to calculate Znot_prime and Mu2_prime iterations



#Declare Wavelength Range
Waves = [380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 
         390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 
         400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 
         410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 
         420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 
         430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 
         440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 
         450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 
         460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 
         470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 
         
         480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 
         490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 
         500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 
         510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 
         520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 
         530, 531, 532, 533, 534, 535, 536, 537]

#Declare rod thicknesses
t4  = 4
t6  = 6
t10 = 10


##Low Dose Rate Data

#4 mm
MuEff4 = [1.741534, 1.728474, 1.710086, 1.684342, 1.650651, 1.605875, 1.549960, 1.482974, 1.404919, 1.319150, 
          1.223578, 1.124498, 1.023141, 0.920591, 0.820568, 0.721059, 0.626180, 0.537728, 0.456145, 0.382367, 
          0.316700, 0.259471, 0.210543, 0.169635, 0.136004, 0.109021, 0.087585, 0.070945, 0.058252, 0.048568, 
          0.041322, 0.035910, 0.031844, 0.028788, 0.026358, 0.024499, 0.022853, 0.021626, 0.020528, 0.019637, 
          0.018849, 0.018029, 0.017258, 0.016607, 0.016013, 0.015570, 0.014977, 0.014461, 0.013994, 0.013619, 
          0.013137, 0.012762, 0.012449, 0.012127, 0.011827, 0.011501, 0.011249, 0.010984, 0.010709, 0.010420, 
          0.010252, 0.009930, 0.009709, 0.009472, 0.009268, 0.009098, 0.008898, 0.008698, 0.008527, 0.008309, 
          0.008042, 0.007878, 0.007771, 0.007561, 0.007435, 0.007275, 0.007072, 0.006929, 0.006742, 0.006618, 
          0.006462, 0.006314, 0.006147, 0.006091, 0.005886, 0.005688, 0.005549, 0.005389, 0.005349, 0.005248, 
          0.005106, 0.005031, 0.004969, 0.004926, 0.004804, 0.004659, 0.004523, 0.004410, 0.004337, 0.004239, 

          0.004229, 0.004076, 0.003957, 0.003902, 0.003887, 0.003770, 0.003721, 0.003665, 0.003605, 0.003458, 
          0.003395, 0.003295, 0.003206, 0.003127, 0.002990, 0.003013, 0.002885, 0.002890, 0.002829, 0.002759, 
          0.002709, 0.002678, 0.002643, 0.002600, 0.002514, 0.002451, 0.002365, 0.002332, 0.002274, 0.002235, 
          0.002201, 0.002124, 0.002101, 0.002028, 0.001995, 0.001944, 0.001898, 0.001915, 0.001898, 0.001791, 
          0.001753, 0.001701, 0.001720, 0.001631, 0.001582, 0.001608, 0.001506, 0.001525, 0.001513, 0.001442, 
          0.001354, 0.001315, 0.001296, 0.001274, 0.001270, 0.001234, 0.001239, 0.001200]

#6mm
MuEff6 = [1.1841509, 1.1816043, 1.1797769, 1.1772963, 1.1707134, 1.1606960, 1.1472791, 1.1247809, 1.0920316, 1.0483807, 
          0.9899321, 0.9217421, 0.8456049, 0.7651559, 0.6834930, 0.6026615, 0.5246485, 0.4510683, 0.3832058, 0.3216421, 
          0.2669278, 0.2190760, 0.1783487, 0.1441771, 0.1160036, 0.0933822, 0.0754009, 0.0613368, 0.0506188, 0.0424816, 
          0.0362892, 0.0316406, 0.0282051, 0.0255608, 0.0234427, 0.0217695, 0.0204030, 0.0193319, 0.0183487, 0.0175055, 
          0.0168247, 0.0160149, 0.0154315, 0.0147153, 0.0141596, 0.0136884, 0.0131462, 0.0126664, 0.0122605, 0.0118288, 
          0.0114444, 0.0111227, 0.0107803, 0.0104713, 0.0101996, 0.0098841, 0.0096267, 0.0094070, 0.0091516, 0.0088815, 
          0.0086634, 0.0084270, 0.0082149, 0.0079955, 0.0077703, 0.0075740, 0.0074284, 0.0071870, 0.0069954, 0.0068504, 
          0.0066446, 0.0064471, 0.0063030, 0.0061287, 0.0059968, 0.0058307, 0.0056171, 0.0054985, 0.0053593, 0.0052461, 
          0.0050455, 0.0049290, 0.0047946, 0.0046543, 0.0045452, 0.0043840, 0.0041781, 0.0041020, 0.0039854, 0.0039007, 
          0.0037997, 0.0037161, 0.0036644, 0.0036549, 0.0035785, 0.0034536, 0.0033595, 0.0032815, 0.0031890, 0.0030913, 
          
          0.0030270, 0.0029528, 0.0028338, 0.0027596, 0.0026879, 0.0025946, 0.0025150, 0.0024618, 0.0023561, 0.0022748, 
          0.0022270, 0.0020970, 0.0020466, 0.0019827, 0.0018893, 0.0018277, 0.0017663, 0.0017289, 0.0016515, 0.0015757, 
          0.0015200, 0.0014754, 0.0014007, 0.0013404, 0.0013253, 0.0012522, 0.0011979, 0.0011329, 0.0010749, 0.0010198, 
          0.0010043, 0.0009522, 0.0008986, 0.0008432, 0.0007680, 0.0007524, 0.0007061, 0.0006833, 0.0006435, 0.0006067, 
          0.0005792, 0.0005044, 0.0004907, 0.0004300, 0.0003897, 0.0003923, 0.0003102, 0.0003287, 0.0002564, 0.0002401, 
          0.0001954, 0.0001434, 0.0001228, 0.0000965, 0.0001063, 0.0000954, 0.0000341, 0.0000065]

#10mm
MuEff10 = [0.7184181, 0.7185662, 0.7176814, 0.7173882, 0.7173882, 0.7170955, 0.7165133, 0.7150725, 0.7130898, 0.7081653, 
           0.6992334, 0.6833554, 0.6555475, 0.6141494, 0.5607905, 0.5013510, 0.4390745, 0.3795690, 0.3228745, 0.2705075, 
           0.2242705, 0.1839540, 0.1493865, 0.1204620, 0.0966067, 0.0773939, 0.0621436, 0.0503055, 0.0412382, 0.0343132, 
           0.0291109, 0.0252261, 0.0222749, 0.0200099, 0.0182669, 0.0169080, 0.0157943, 0.0148615, 0.0141146, 0.0134089, 
           0.0128059, 0.0122163, 0.0116842, 0.0111614, 0.0106882, 0.0102938, 0.0099155, 0.0095498, 0.0092230, 0.0089330, 
           0.0086254, 0.0083659, 0.0081154, 0.0078928, 0.0076731, 0.0074933, 0.0073087, 0.0070802, 0.0069384, 0.0067404, 
           0.0065012, 0.0063852, 0.0062039, 0.0060105, 0.0058481, 0.0056768, 0.0055206, 0.0053436, 0.0051933, 0.0050434, 
           0.0049235, 0.0047797, 0.0046456, 0.0045267, 0.0043486, 0.0042230, 0.0040887, 0.0039673, 0.0038440, 0.0036929, 
           0.0035884, 0.0034789, 0.0033707, 0.0032990, 0.0031919, 0.0030919, 0.0030120, 0.0028841, 0.0028220, 0.0027400, 
           0.0026550, 0.0026043, 0.0025150, 0.0024698, 0.0023805, 0.0023227, 0.0022625, 0.0021858, 0.0021425, 0.0020733, 

           0.0020022, 0.0019177, 0.0018467, 0.0017771, 0.0017497, 0.0016656, 0.0016333, 0.0015735, 0.0015380, 0.0014918, 
           0.0014434, 0.0014177, 0.0013510, 0.0013114, 0.0012709, 0.0012664, 0.0012077, 0.0011885, 0.0011574, 0.0010931, 
           0.0010892, 0.0010296, 0.0009991, 0.0009727, 0.0009456, 0.0009168, 0.0008782, 0.0008453, 0.0008338, 0.0008058, 
           0.0007814, 0.0007220, 0.0007047, 0.0006919, 0.0006675, 0.0006446, 0.0006182, 0.0005920, 0.0005451, 0.0005703, 
           0.0005397, 0.0004977, 0.0004710, 0.0004611, 0.0004066, 0.0004061, 0.0003914, 0.0003635, 0.0003591, 0.0003285, 
           0.0002807, 0.0002878, 0.0002748, 0.0002276, 0.0002226, 0.0002147, 0.0001861, 0.0001508]

#Making the Assumption that Mu2 = Mueff10 (From Set V1)
Mu2 = [0.714384, 0.713819, 0.712973, 0.713253, 0.711859, 0.711307, 0.710350, 0.706732, 0.702356, 0.696607, 
       0.681319, 0.657080, 0.621741, 0.574877, 0.520241, 0.462144, 0.403128, 0.346753, 0.294368, 0.246502, 
       0.203975, 0.166763, 0.134978, 0.108266, 0.086482, 0.068764, 0.054821, 0.043953, 0.035676, 0.029369, 
       0.024622, 0.021096, 0.018424, 0.016432, 0.014906, 0.013761, 0.012807, 0.012077, 0.011415, 0.010807, 
       0.010336, 0.009861, 0.009497, 0.009095, 0.008753, 0.008389, 0.008145, 0.007867, 0.007631, 0.007400, 
       0.007145, 0.006991, 0.006766, 0.006628, 0.006430, 0.006267, 0.006110, 0.005980, 0.005792, 0.005696, 
       0.005542, 0.005443, 0.005259, 0.005165, 0.005036, 0.004903, 0.004793, 0.004688, 0.004563, 0.004455, 
       0.004329, 0.004238, 0.004154, 0.004042, 0.003940, 0.003842, 0.003739, 0.003687, 0.003610, 0.003474, 
       0.003423, 0.003309, 0.003227, 0.003173, 0.003080, 0.003025, 0.002921, 0.002882, 0.002816, 0.002778, 
       0.002712, 0.002647, 0.002601, 0.002543, 0.002480, 0.002430, 0.002414, 0.002343, 0.002316, 0.002265, 
       
       0.002216, 0.002169, 0.002119, 0.002092, 0.002032, 0.002006, 0.001950, 0.001883, 0.001866, 0.001817, 
       0.001765, 0.001746, 0.001691, 0.001673, 0.001617, 0.001572, 0.001542, 0.001509, 0.001467, 0.001406, 
       0.001388, 0.001323, 0.001300, 0.001283, 0.001240, 0.001217, 0.001184, 0.001125, 0.001116, 0.001078, 
       0.001076, 0.001030, 0.001018, 0.000979, 0.000929, 0.000930, 0.000914, 0.000881, 0.000884, 0.000849, 
       0.000798, 0.000793, 0.000755, 0.000729, 0.000721, 0.000732, 0.000686, 0.000658, 0.000653, 0.000625, 
       0.000597, 0.000565, 0.000556, 0.000549, 0.000535, 0.000482, 0.000486, 0.000446]

#Declaring the Mu1 Iterations
Mu1_1     = [None]*158;
Mu1_2     = [None]*158;
Mu1_3     = [None]*158;
Mu1_4     = [None]*158;
Mu1_5     = [None]*158;
Mu1_6     = [None]*158;
Mu1_7     = [None]*158;
Mu1_8     = [None]*158;
Mu1_9     = [None]*158;
Mu1_10    = [None]*158;
Mu1_11    = [None]*158;
Mu1_12    = [None]*158;
Mu1_13    = [None]*158;
Mu1_14    = [None]*158;
Mu1_15    = [None]*158;
Mu1_16    = [None]*158;
Mu1_17    = [None]*158;
Mu1_18    = [None]*158;
Mu1_19    = [None]*158;
Mu1_20    = [None]*158;
Mu1_21    = [None]*158;
Mu1_22    = [None]*158;
Mu1_23    = [None]*158;
Mu1_24    = [None]*158;
Mu1_25    = [None]*158;
Mu1_26    = [None]*158;
Mu1_27    = [None]*158;
Mu1_28    = [None]*158;
Mu1_29    = [None]*158;
Mu1_30    = [None]*158;
Mu1_31    = [None]*158;
Mu1_32    = [None]*158;
Mu1_33    = [None]*158
Mu1_34    = [None]*158
Mu1_35    = [None]*158
Mu1_36    = [None]*158
Mu1_37    = [None]*158
Mu1_38    = [None]*158;
Mu1_39    = [None]*158;
Mu1_40    = [None]*158;
Mu1_41    = [None]*158;
Mu1_42    = [None]*158;
Mu1_43    = [None]*158;
Mu1_44    = [None]*158;
Mu1_45    = [None]*158;
Mu1_46    = [None]*158;
Mu1_47    = [None]*158;
Mu1_48    = [None]*158
Mu1_49    = [None]*158
Mu1_50    = [None]*158
Mu1_51    = [None]*158
Mu1_52    = [None]*158

#Declaring the Znot Iterations
Znot_1     = [None]*158;
Znot_2     = [None]*158;
Znot_3     = [None]*158;
Znot_4     = [None]*158;
Znot_5     = [None]*158;
Znot_6     = [None]*158;
Znot_7     = [None]*158;
Znot_8     = [None]*158;
Znot_9     = [None]*158;
Znot_10    = [None]*158;
Znot_11    = [None]*158;
Znot_12    = [None]*158;
Znot_13    = [None]*158;
Znot_14    = [None]*158;
Znot_15    = [None]*158;
Znot_16    = [None]*158;
Znot_17    = [None]*158;
Znot_18    = [None]*158;
Znot_19    = [None]*158;
Znot_20    = [None]*158;
Znot_21    = [None]*158;
Znot_22    = [None]*158;
Znot_23    = [None]*158;
Znot_24    = [None]*158;
Znot_25    = [None]*158;
Znot_26    = [None]*158;
Znot_27    = [None]*158;
Znot_28    = [None]*158;
Znot_29    = [None]*158;
Znot_30    = [None]*158;
Znot_31    = [None]*158;
Znot_32    = [None]*158;
Znot_33    = [None]*158;
Znot_34    = [None]*158
Znot_35    = [None]*158
Znot_36    = [None]*158
Znot_37    = [None]*158
Znot_38    = [None]*158;
Znot_39    = [None]*158;
Znot_40    = [None]*158;
Znot_41    = [None]*158;
Znot_42    = [None]*158;
Znot_43    = [None]*158;
Znot_44    = [None]*158;
Znot_45    = [None]*158;
Znot_46    = [None]*158;
Znot_47    = [None]*158;
Znot_48    = [None]*158
Znot_49    = [None]*158
Znot_50    = [None]*158
Znot_51    = [None]*158
Znot_52    = [None]*158

#These will include averages of past Mu1 iterations
Mu1sIT0   = [None]*158;
Mu1sIT1   = [None]*158;
Mu1sIT2   = [None]*158;
Mu1sIT3   = [None]*158;
Mu1sIT4   = [None]*158;
Mu1sIT5   = [None]*158;
Mu1sIT6   = [None]*158;
Mu1sIT7   = [None]*158;
Mu1sIT8   = [None]*158;
Mu1sIT9   = [None]*158;
Mu1sIT10  = [None]*158;
Mu1sIT11  = [None]*158;
Mu1sIT12  = [None]*158;
Mu1sIT13  = [None]*158;
Mu1sIT14  = [None]*158;
Mu1sIT15  = [None]*158;
Mu1sIT16  = [None]*158;
Mu1sIT17  = [None]*158;
Mu1sIT18  = [None]*158;
Mu1sIT19  = [None]*158;
Mu1sIT20  = [None]*158;
Mu1sIT20  = [None]*158;
Mu1sIT21  = [None]*158;
Mu1sIT22  = [None]*158;
Mu1sIT23  = [None]*158;
Mu1sIT24  = [None]*158;
Mu1sIT25  = [None]*158;
Mu1sIT26  = [None]*158;
Mu1sIT27  = [None]*158;
Mu1sIT28  = [None]*158;
Mu1sIT29  = [None]*158;
Mu1sIT30  = [None]*158;
Mu1sIT31  = [None]*158;
Mu1sIT32  = [None]*158;
Mu1sIT33  = [None]*158;
Mu1sIT34  = [None]*158
Mu1sIT35  = [None]*158
Mu1sIT36  = [None]*158
Mu1sIT37  = [None]*158
Mu1sIT38  = [None]*158;
Mu1sIT39  = [None]*158;
Mu1sIT40  = [None]*158;
Mu1sIT41  = [None]*158;
Mu1sIT42  = [None]*158;
Mu1sIT43  = [None]*158;
Mu1sIT44  = [None]*158;
Mu1sIT45  = [None]*158;
Mu1sIT46  = [None]*158;
Mu1sIT47  = [None]*158;
Mu1sIT48  = [None]*158
Mu1sIT49  = [None]*158
Mu1sIT50  = [None]*158
Mu1sIT51  = [None]*158
Mu1sIT52  = [None]*158

#These will include averages of past Znot iterations
ZnotsIT0  = [None]*158
ZnotsIT1  = [None]*158;
ZnotsIT2  = [None]*158;
ZnotsIT3  = [None]*158;
ZnotsIT4  = [None]*158;
ZnotsIT5  = [None]*158;
ZnotsIT6  = [None]*158;
ZnotsIT7  = [None]*158;
ZnotsIT8  = [None]*158;
ZnotsIT9  = [None]*158;
ZnotsIT10 = [None]*158;
ZnotsIT11 = [None]*158;
ZnotsIT12 = [None]*158;
ZnotsIT13 = [None]*158;
ZnotsIT14 = [None]*158;
ZnotsIT15 = [None]*158;
ZnotsIT16 = [None]*158;
ZnotsIT17 = [None]*158;
ZnotsIT18 = [None]*158;
ZnotsIT19 = [None]*158;
ZnotsIT20 = [None]*158;
ZnotsIT21 = [None]*158;
ZnotsIT22 = [None]*158;
ZnotsIT23 = [None]*158;
ZnotsIT24 = [None]*158;
ZnotsIT25 = [None]*158;
ZnotsIT26 = [None]*158;
ZnotsIT27 = [None]*158;
ZnotsIT28 = [None]*158;
ZnotsIT29 = [None]*158;
ZnotsIT30 = [None]*158;
ZnotsIT31 = [None]*158;
ZnotsIT32 = [None]*158;
ZnotsIT33 = [None]*158;
ZnotsIT34 = [None]*158
ZnotsIT35 = [None]*158
ZnotsIT36 = [None]*158
ZnotsIT37 = [None]*158
ZnotsIT38 = [None]*158;
ZnotsIT39 = [None]*158;
ZnotsIT40 = [None]*158;
ZnotsIT41 = [None]*158;
ZnotsIT42 = [None]*158;
ZnotsIT43 = [None]*158;
ZnotsIT44 = [None]*158;
ZnotsIT45 = [None]*158;
ZnotsIT46 = [None]*158;
ZnotsIT47 = [None]*158;
ZnotsIT48 = [None]*158
ZnotsIT49 = [None]*158
ZnotsIT50 = [None]*158
ZnotsIT51 = [None]*158
ZnotsIT52 = [None]*158

##0th iterations

#Calculated in excel
ZnotsIT0_AVG = 0.9118 

ZnotsIT0 = [0.69661, 0.70401, 0.71481, 0.72819, 0.74864, 0.77046, 0.79969, 0.83543, 0.87090, 0.89477, 
            0.93705, 0.99059, 1.04773, 1.11003, 1.15321, 1.19274, 1.22005, 1.24863, 1.26369, 1.27062, 
            1.28674, 1.30836, 1.33512, 1.37061, 1.39951, 1.44442, 1.48808, 1.53591, 1.58364, 1.63455, 
            1.67729, 1.71288, 1.74933, 1.76376, 1.77642, 1.77149, 1.78956, 1.77783, 1.78557, 1.77655, 
            1.76858, 1.75015, 1.74623, 1.70875, 1.68388, 1.67198, 1.64806, 1.63200, 1.61874, 1.59096, 
            1.59583, 1.57328, 1.55946, 1.53350, 1.53239, 1.52918, 1.51806, 1.49123, 1.51330, 1.47761, 
            1.43126, 1.44326, 1.44631, 1.40702, 1.38561, 1.36149, 1.35319, 1.30680, 1.28781, 1.28443, 
            1.29885, 1.26087, 1.22511, 1.22671, 1.18555, 1.16586, 1.13949, 1.10435, 1.08574, 1.08188, 
            1.02855, 1.03808, 1.02507, 0.98661, 0.99811, 0.96764, 0.95345, 0.91314, 0.89109, 0.85971, 
            0.85106, 0.85562, 0.82854, 0.85245, 0.84339, 0.82972, 0.79427, 0.79638, 0.76801, 0.74542, 
            
            0.71479, 0.69752, 0.66511, 0.61772, 0.62900, 0.57149, 0.57767, 0.58680, 0.53924, 0.54358, 
            0.55038, 0.50510, 0.50363, 0.47237, 0.47905, 0.49461, 0.46966, 0.47294, 0.46786, 0.45845, 
            0.45578, 0.46574, 0.43403, 0.40767, 0.44223, 0.41678, 0.40767, 0.42463, 0.40200, 0.40285, 
            0.37894, 0.36674, 0.33897, 0.35958, 0.36808, 0.34192, 0.31770, 0.32388, 0.25156, 0.31923, 
            0.35240, 0.27797, 0.29809, 0.30049, 0.23586, 0.21792, 0.23271, 0.25736, 0.21655, 0.22641, 
            0.19937, 0.22862, 0.21809, 0.16280, 0.18689, 0.26355, 0.18497, 0.19715]

#Assuming Mu1It0 = Mueff4
Mu1sIT0      = MuEff4[:]



##Begin Iterations

Iterations = list(range(35));

#loop over iterations
for j in range (len(Iterations)):

    #loop over wavelength range
    for i in range(len(Waves)):


        if j == 0:
            # only use the average Znot for this first iteration
            #Znot = ZnotsIT0_AVG
            Znot = ZnotsIT0[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_1[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT1[i] = numpy.average([Mu1sIT0[i], Mu1_1[i]])

        if j == 1:
            
            Znot = ZnotsIT1[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_2[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT2[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1_2[i]])

        if j == 2:
            
            Znot = ZnotsIT2[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_3[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT3[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1_3[i]])

        if j == 3:
            
            Znot = ZnotsIT3[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_4[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT4[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1_4[i]])


        if j == 4:
            
            Znot = ZnotsIT4[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_5[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT5[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1_5[i]])
            

        if j == 5:
            
            Znot = ZnotsIT5[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_6[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT6[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1_6[i]])
            

        if j == 6:
            
            Znot = ZnotsIT6[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_7[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT7[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1_7[i]])
            

        if j == 7:
            
            Znot = ZnotsIT7[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_8[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT8[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1_8[i]])
            

        if j == 8:
            
            Znot = ZnotsIT8[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_9[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT9[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1_9[i]])
            

        if j == 9:
            
            Znot = ZnotsIT9[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_10[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT10[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1_10[i]])
            

        if j == 10:
            
            Znot = ZnotsIT10[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_11[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT11[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1_11[i]])
            


        if j == 11:
            
            Znot = ZnotsIT11[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_12[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT12[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1_12[i]])


        if j == 12:
            
            Znot = ZnotsIT12[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_13[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT13[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1_13[i]])
            

        if j == 13:
            
            Znot = ZnotsIT13[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_14[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT14[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                         Mu1_14[i]])
            

        if j == 14:
            
            Znot = ZnotsIT14[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_15[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT15[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1_15[i]])
            
        if j == 15:
            
            Znot = ZnotsIT15[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_16[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT16[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1sIT15[i], Mu1_16[i]])
            

        if j == 16:
            
            Znot = ZnotsIT16[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_17[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT17[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1_17[i]])
            

        if j == 17:
            
            Znot = ZnotsIT17[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_18[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT18[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1_18[i]])
            
        if j == 18:
            
            Znot = ZnotsIT18[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_19[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT19[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1_19[i]])
            
        if j == 19:
            
            Znot = ZnotsIT19[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_20[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT20[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1_20[i]])
            
        if j == 20:
            
            Znot = ZnotsIT20[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_21[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT21[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1_21[i]])
            

        if j == 21:
            
            Znot = ZnotsIT21[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_22[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT22[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1_22[i]])
            

        if j == 22:
            
            Znot = ZnotsIT22[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_23[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT23[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1_23[i]])
            

        if j == 23:
            
            Znot = ZnotsIT23[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_24[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT24[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1sIT23[i], Mu1_24[i]])
            

        if j == 24:
            
            Znot = ZnotsIT24[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_25[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT25[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                                     Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1sIT23[i], Mu1sIT24[i], Mu1_25[i]])
            

        if j == 25:
            
            Znot = ZnotsIT25[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_26[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT26[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                         Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1sIT23[i], Mu1sIT24[i], Mu1sIT25[i], Mu1_26[i]])
            

        if j == 26:
            
            Znot = ZnotsIT26[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_27[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT27[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                         Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1sIT23[i], Mu1sIT24[i], Mu1sIT25[i], Mu1sIT26[i], 
                                         Mu1_27[i]])
            

        if j == 27:
            
            Znot = ZnotsIT27[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_28[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT28[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                         Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1sIT23[i], Mu1sIT24[i], Mu1sIT25[i], Mu1sIT26[i], 
                                         Mu1sIT27[i], Mu1_28[i]])
            
        if j == 28:
            
            Znot = ZnotsIT28[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_29[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT29[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                         Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1sIT23[i], Mu1sIT24[i], Mu1sIT25[i], Mu1sIT26[i], 
                                         Mu1sIT27[i], Mu1sIT28[i], Mu1_29[i]])
            

        if j == 29:
            
            Znot = ZnotsIT29[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_30[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT30[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                         Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1sIT23[i], Mu1sIT24[i], Mu1sIT25[i], Mu1sIT26[i], 
                                         Mu1sIT27[i], Mu1sIT28[i], Mu1sIT29[i], Mu1_30[i]])
            

        if j == 30:
            
            Znot = ZnotsIT30[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_31[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT31[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                         Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1sIT23[i], Mu1sIT24[i], Mu1sIT25[i], Mu1sIT26[i], 
                                         Mu1sIT27[i], Mu1sIT28[i], Mu1sIT29[i], Mu1sIT30[i], Mu1_31[i]])
            

        if j == 31:
            
            Znot = ZnotsIT31[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_32[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT32[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                         Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1sIT23[i], Mu1sIT24[i], Mu1sIT25[i], Mu1sIT26[i], 
                                         Mu1sIT27[i], Mu1sIT28[i], Mu1sIT29[i], Mu1sIT30[i], Mu1sIT31[i], Mu1_32[i]])
            

        if j == 32:
            
            Znot = ZnotsIT32[i]
            # the three equations we derived for Mu1 in terms of Znot
            Mu1a = ((t10*(MuEff10[i]-Mu2[i]))/(2*Znot)) + Mu2[i]

            Mu1b = ((t6*(MuEff6[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            
            Mu1c = ((t4*(MuEff4[i]-Mu2[i]))/(2*Znot)) + Mu2[i]
            # take their average
            Mu1_33[i]  = (Mu1a + Mu1b + Mu1c)/3;
            
            
            
            #takes the average of previous iterations
            Mu1sIT33[i] = numpy.average([Mu1sIT0[i], Mu1sIT1[i], Mu1sIT2[i], Mu1sIT3[i], Mu1sIT4[i], Mu1sIT5[i], Mu1sIT6[i], Mu1sIT7[i], Mu1sIT8[i], Mu1sIT9[i], Mu1sIT10[i], Mu1sIT11[i], Mu1sIT12[i], Mu1sIT13[i], 
                                         Mu1sIT14[i], Mu1sIT15[i], Mu1sIT16[i], Mu1sIT17[i], Mu1sIT18[i], Mu1sIT19[i], Mu1sIT20[i], Mu1sIT21[i], Mu1sIT22[i], Mu1sIT23[i], Mu1sIT24[i], Mu1sIT25[i], Mu1sIT26[i], 
                                         Mu1sIT27[i], Mu1sIT28[i], Mu1sIT29[i], Mu1sIT30[i], Mu1sIT31[i], Mu1sIT32[i], Mu1_33[i]])




# Begin Znot Iteration

        if j == 0:
            
            # the three separate equations for Znot in terms of Mu2
            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT1[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT1[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT1[i]-Mu2[i]))

            # this is the 'pure' first iteration, without any averages of past iterations
            Znot_1[i]  = (Znota + Znotb + Znotc)/3;
            # takes the average of all previous iterations
            ZnotsIT1[i] = numpy.average([ZnotsIT0[i], Znot_1[i]])


        if j == 1:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT2[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT2[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT2[i]-Mu2[i]))

            Znot_2[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT2[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], Znot_2[i]])

        if j == 2:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT3[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT3[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT3[i]-Mu2[i]))

            Znot_3[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT3[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], Znot_3[i]])
            

        if j == 3:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT4[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT4[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT4[i]-Mu2[i]))

            Znot_4[i]  = (Znota + Znotb + Znotc)/3;

            
            ZnotsIT4[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], Znot_4[i]])


        if j == 4:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT5[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT5[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT5[i]-Mu2[i]))

            Znot_5[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT5[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], Znot_5[i]])
                        

        if j == 5:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT6[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT6[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT6[i]-Mu2[i]))

            Znot_6[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT6[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], Znot_6[i]])
            

        if j == 6:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT7[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT7[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT7[i]-Mu2[i]))

            Znot_7[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT7[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], Znot_7[i]])
            

        if j == 7:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT8[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT8[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT8[i]-Mu2[i]))

            Znot_8[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT8[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], Znot_8[i]])


        if j == 8:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT9[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT9[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT9[i]-Mu2[i]))

            Znot_9[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT9[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], Znot_9[i]])


        if j == 9:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT10[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT10[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT10[i]-Mu2[i]))

            Znot_10[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT10[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], Znot_10[i]])


        if j == 10:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT11[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT11[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT11[i]-Mu2[i]))

            Znot_11[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT11[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], Znot_11[i]])


        if j == 11:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT12[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT12[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT12[i]-Mu2[i]))

            Znot_12[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT12[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], Znot_12[i]])


        if j == 12:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT13[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT13[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT13[i]-Mu2[i]))

            Znot_13[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT13[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          Znot_13[i]])


        if j == 13:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT14[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT14[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT14[i]-Mu2[i]))

            Znot_14[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT14[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], Znot_14[i]])


        if j == 14:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT15[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT15[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT15[i]-Mu2[i]))

            Znot_15[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT15[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], Znot_15[i]])


        if j == 15:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT16[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT16[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT16[i]-Mu2[i]))

            Znot_16[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT16[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], Znot_16[i]])


        if j == 16:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT17[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT17[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT17[i]-Mu2[i]))

            Znot_17[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT17[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], Znot_17[i]])


        if j == 17:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT18[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT18[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT18[i]-Mu2[i]))

            Znot_18[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT18[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], Znot_18[i]])


        if j == 18:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT19[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT19[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT19[i]-Mu2[i]))

            Znot_19[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT19[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], Znot_19[i]])


        if j == 19:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT20[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT20[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT20[i]-Mu2[i]))

            Znot_20[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT20[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], Znot_20[i]])


        if j == 20:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT21[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT21[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT21[i]-Mu2[i]))

            Znot_21[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT21[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], Znot_21[i]])


        if j == 21:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT22[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT22[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT22[i]-Mu2[i]))

            Znot_22[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT22[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], Znot_22[i]])


        if j == 22:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT23[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT23[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT23[i]-Mu2[i]))

            Znot_23[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT23[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], ZnotsIT22[i], Znot_23[i]])


        if j == 23:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT24[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT24[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT24[i]-Mu2[i]))

            Znot_24[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT24[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], ZnotsIT22[i], ZnotsIT23[i], Znot_24[i]])
            

        if j == 24:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT25[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT25[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT25[i]-Mu2[i]))

            Znot_25[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT25[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], ZnotsIT22[i], ZnotsIT23[i], ZnotsIT24[i], 
                                          Znot_25[i]])
            

        if j == 25:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT26[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT26[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT26[i]-Mu2[i]))

            Znot_26[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT26[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], ZnotsIT22[i], ZnotsIT23[i], ZnotsIT24[i], 
                                          ZnotsIT25[i], Znot_26[i]])
            

        if j == 26:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT27[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT27[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT27[i]-Mu2[i]))

            Znot_27[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT27[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], ZnotsIT22[i], ZnotsIT23[i], ZnotsIT24[i], 
                                          ZnotsIT25[i], ZnotsIT26[i], Znot_27[i]])
            

        if j == 27:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT28[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT28[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT18[i]-Mu2[i]))

            Znot_28[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT28[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], ZnotsIT22[i], ZnotsIT23[i], ZnotsIT24[i], 
                                          ZnotsIT25[i], ZnotsIT26[i], ZnotsIT27[i], Znot_28[i]])
            

        if j == 28:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT29[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT29[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT29[i]-Mu2[i]))

            Znot_29[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT29[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], ZnotsIT22[i], ZnotsIT23[i], ZnotsIT24[i], 
                                          ZnotsIT25[i], ZnotsIT26[i], ZnotsIT27[i], ZnotsIT28[i], Znot_29[i]])
            

        if j == 29:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT30[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT30[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT30[i]-Mu2[i]))

            Znot_30[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT30[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], ZnotsIT22[i], ZnotsIT23[i], ZnotsIT24[i], 
                                          ZnotsIT25[i], ZnotsIT26[i], ZnotsIT27[i], ZnotsIT28[i], ZnotsIT29[i], Znot_30[i]])
            

        if j == 30:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT31[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT31[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT31[i]-Mu2[i]))

            Znot_31[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT31[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], ZnotsIT22[i], ZnotsIT23[i], ZnotsIT24[i], 
                                          ZnotsIT25[i], ZnotsIT26[i], ZnotsIT27[i], ZnotsIT28[i], ZnotsIT29[i], ZnotsIT30[i], Znot_31[i]])
            

        if j == 31:
            

            Znota = (t10*(MuEff10[i]-Mu2[i]))/(2*(Mu1sIT32[i]-Mu2[i]))
   
            Znotb = (t6*(MuEff6[i]-Mu2[i]))/(2*(Mu1sIT32[i]-Mu2[i]))

            Znotc = (t4*(MuEff4[i]-Mu2[i]))/(2*(Mu1sIT32[i]-Mu2[i]))

            Znot_32[i]  = (Znota + Znotb + Znotc)/3;


            ZnotsIT32[i] = numpy.average([ZnotsIT0[i], ZnotsIT1[i], ZnotsIT2[i], ZnotsIT3[i], ZnotsIT4[i], ZnotsIT5[i], ZnotsIT6[i], ZnotsIT7[i], ZnotsIT8[i], ZnotsIT9[i], ZnotsIT10[i], ZnotsIT11[i], ZnotsIT12[i], 
                                          ZnotsIT13[i], ZnotsIT14[i], ZnotsIT15[i], ZnotsIT16[i], ZnotsIT17[i], ZnotsIT18[i], ZnotsIT19[i], ZnotsIT20[i], ZnotsIT21[i], ZnotsIT22[i], ZnotsIT23[i], ZnotsIT24[i], 
                                          ZnotsIT25[i], ZnotsIT26[i], ZnotsIT27[i], ZnotsIT28[i], ZnotsIT29[i], ZnotsIT30[i], ZnotsIT31[i], Znot_32[i]])
            

#print parameter values
print 'Wavelength \t\tMu1sIT0 \t\tMu1sIT1 \t\tMu1sIT2 \t\tMu1sIT3 \t\tMu1sIT4 \t\tMu1sIT5 \t\tMu1sIT6 \t\tMu1sIT7 \t\tMu1sIT8 \t\tMu1sIT9 \t\tMu1sIT10 \t\tMu1sIT11 \t\tMu1sIT12 \t\tMu1sIT13 \t\tMu1sIT14 \t\tMu1sIT15 \t\tMu1sIT16 \t\tMu1sIT17 \t\tMu1sIT18 \t\tMu1sIT19 \t\tMu1sIT20 \t\tMu1sIT21 \t\tMu1sIT22 \t\tMu1sIT23 \t\tMu1sIT24 \t\tMu1sIT25 \t\tMu1sIT26 \t\tMu1sIT27 \t\tMu1sIT28 \t\tMu1sIT29 \t\tMu1sIT30 \t\tMu1sIT31 \t\tMu1sIT32 \t\tMu1s33 \t\tZnotsIT0 \t\tZnotsIT1 \t\tZnotsIT2 \t\tZnotsIT3 \t\tZnotsIT4 \t\tZnotsIT5 \t\tZnotsIT6 \t\tZnotsIT7 \t\tZnotsIT8 \t\tZnotsIT9 \t\tZnotsIT10 \t\tZnotsIT11 \t\tZnotsIT12 \t\tZnotsIT13 \t\tZnotsIT14 \t\tZnotsIT15 \t\tZnotsIT16 \t\tZnotsIT17 \t\tZnotsIT18 \t\tZnotsIT19 \t\tZnotsIT20 \t\tZnotsIT21 \t\tZnotsIT22 \t\tZnotsIT23 \t\tZnotsIT24 \t\tZnotsIT25 \t\tZnotsIT26 \t\tZnotsIT27 \t\tZnotsIT28 \t\tZnotsIT29 \t\tZnotsIT30 \t\tZnotsIT31 \t\tZnotsIT32'

for w,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20,z21,z22,z23,z24,z25,z26,z27,z28,z29,z30,z31,z32 in zip(Waves,Mu1sIT0,Mu1sIT1,Mu1sIT2,Mu1sIT3,Mu1sIT4,Mu1sIT5,Mu1sIT6,Mu1sIT7,Mu1sIT8,Mu1sIT9,Mu1sIT10,Mu1sIT11,Mu1sIT12,Mu1sIT13,Mu1sIT14,Mu1sIT15,Mu1sIT16,Mu1sIT17,Mu1sIT18,Mu1sIT19,Mu1sIT20,Mu1sIT21,Mu1sIT22,Mu1sIT23,Mu1sIT24,Mu1sIT25,Mu1sIT26,Mu1sIT27,Mu1sIT28,Mu1sIT29,Mu1sIT30,Mu1sIT31,Mu1sIT32,Mu1sIT33,ZnotsIT0,ZnotsIT1,ZnotsIT2,ZnotsIT3,ZnotsIT4,ZnotsIT5,ZnotsIT6,ZnotsIT7,ZnotsIT8,ZnotsIT9,ZnotsIT10,ZnotsIT11,ZnotsIT12,ZnotsIT13,ZnotsIT14,ZnotsIT15,ZnotsIT16,ZnotsIT17,ZnotsIT18,ZnotsIT19,ZnotsIT20,ZnotsIT21,ZnotsIT22,ZnotsIT23,ZnotsIT24,ZnotsIT25,ZnotsIT26,ZnotsIT27,ZnotsIT28,ZnotsIT29,ZnotsIT30,ZnotsIT31,ZnotsIT32):
    print "%.3f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f\t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f" % ( w,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20,z21,z22,z23,z24,z25,z26,z27,z28,z29,z30,z31,z32)

