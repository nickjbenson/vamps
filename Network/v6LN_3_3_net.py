# v6LN_3_3_net.py
# Input:  Muscle Lengths
# Output: Nose Position

import numpy as np

class Network(object):
    def __init__(self):
        # Note: This is not a generic Network implementation,
        # but a manually re-expressed set of network
        # weights as trained (and originally implemented) in
        # MATLAB.
        # v6LN_3_3_net, a closed-loop network with 3 hidden
        # layers and 3 delay states in both the input layer and
        # output-feedback-in layer, specifically, as trained
        # on 18-muscle-length input and 3-coordinate output
        # (position in 3-space).

        # Input Layer #
        self.x1_step1_xoffset = np.array([[0.3484404],[1.0337],[0.5897193],[0.5897193],[1.035131],[0.3484404],[0.6375437],[0.6939231],[0.7936453],[0.7936453],[0.7288762],[0.6375437],[1.366086],[1.003382],[0.8599294],[0.9178694],[1.003382],[1.326977]])
        self.x1_step1_gain = np.array([[1.43496563544296],[0.747091014362825],[0.847861187488095],[0.847861187488095],[0.742028572552215],[1.43496563544296],[0.831110355539452],[0.97588781271776],[0.847035652620006],[0.853519168354821],[0.987247818651263],[0.828149702799846],[0.946420307151246],[0.80049758930151],[0.820607893197554],[0.845498435278321],[0.800516493241439],[0.929432813625485]])
        self.x1_step1_ymin = np.array([-1.])

        # Layer 1 #
        self.b1 = np.array([[0.86937103248159175],[0.62728873725396583],[0.2880600122307686]])
        self.IW1_1 = np.array([[-0.05578690028675537,0.11343399612853987,-0.020572306649900909,0.056231123288524587,0.087107140223611115,-0.0084703923519431398,-0.37402787686281869,-0.06409154222314388,0.28274523786729439,0.34960716945962605,-0.1028840642567323,-0.4133144334091523,0.44431544918217419,0.27433457617325346,0.8115371324935684,0.78976114982958023,0.24006868930834738,0.47624503613678482,0.093849856901534412,-0.35049990637049611,-0.012492369346179456,-0.15617889186196091,-0.28870787048300717,-0.017957063828464858,0.92865096490479393,0.047769040328288173,-0.58180512746878743,-0.59420358114042304,0.025223787543498716,1.0704404449587888,-1.3717541983763846,-0.56690422879279145,-1.8147892936875683,-1.7942376607496175,-0.46834606055697675,-1.5099333947924267,-0.03702770137043683,0.22311785107633533,0.034937108226917389,0.10318216640604495,0.18727077194891281,0.025763169305020098,-0.54836890342982314,0.01099176600864041,0.3005237100833289,0.24551549331348241,0.068063649405594201,-0.65344093488647714,0.91600334939094474,0.29488957408174549,1.0025778462836226,1.008236383839608,0.23525452205496919,1.0220841547481367],[0.020452102535162331,-0.10179474817604296,-0.016026994976632819,-0.05146496934158442,-0.00087801989424592629,0.0013393247146351863,0.32915964859821056,-0.0011983428475642295,-0.16337906225550264,-0.19606668869689764,0.028480375122919309,0.3051893174822326,-0.40850565495011198,-0.18797839121324378,-0.59298834302916592,-0.55672514087363356,-0.17688449243098345,-0.38743767261475792,-0.02046451190389896,0.26277620058944279,0.039357600083663763,0.11761092425213088,0.11350633254081105,0.017663829459748748,-0.6683207964212694,0.0053010934139429491,0.34442203986369085,0.37306927212592955,0.01034615729494728,-0.77865072690519199,1.0191953415134571,0.36255053556438227,1.2570479982444318,1.2467003480794763,0.31220998950336126,1.1108187928502979,-0.001178080256008063,-0.15068033481069384,-0.025240360994732064,-0.068499197886095139,-0.10267853843436965,-0.01798314285266309,0.33450285596271695,-0.0003456440742180926,-0.17972140713734838,-0.17695601750583126,-0.032603712597636975,0.47064330742521382,-0.60218607618532749,-0.17866085137128368,-0.66678071757885948,-0.69454790736308125,-0.1410011559638337,-0.71523454319777557],[0.019233280534927382,-0.062447454027926029,0.0037689881214396375,0.021405532295605614,-0.0086248644389033367,0.0055569429597101165,0.092978694777290205,0.028299064910255429,-0.095963347187307882,-0.16488978597249671,0.12881464045445684,0.035343202005901568,-0.09432245365581042,-0.025517765339469443,-0.1942995900745767,-0.17502439792849286,-0.099621751442776574,-0.020255033579812218,-0.026952486479897866,0.120431143458573,0.019386947941746488,-0.003180721758930851,0.088717631603524874,-0.015659369795769235,-0.2248022885406214,-0.019226811067596827,0.17197918345918189,0.25450484954095381,-0.10615636757801238,-0.26221946699858339,0.34210395968035406,0.1139594536575925,0.46995230227651413,0.46629479725721995,0.19127936225815212,0.3349763566880497,0.006909246047461127,-0.0544910284465377,-0.023598929038465895,-0.018672669638408832,-0.07672879808272233,0.010747865796860422,0.1293474498259313,-0.0069862582130903505,-0.076989563474315695,-0.090914910293878548,-0.020371774982562839,0.22681070114594137,-0.24389215339296738,-0.088830644174198836,-0.27384373943129037,-0.29052834181731596,-0.092095028858945341,-0.31215820788405479]])
        self.LW1_2 = np.array([[-2.2880926800966788,8.3046157103077203,11.165407175430913,3.1801722532726018,-1.4070203157128409,-7.2779110060917338,-1.3606750287090721,-1.805161132430614,1.1627282223494653],[-4.4412177973511202,-10.744877886082367,-4.061576081636014,3.4471583284240301,5.7299937398869618,1.7319011692003792,-0.83957815181832729,-0.2716024808356538,0.19185800176216958],[-6.2187062550984757,2.4615184296722115,-5.8505965454856037,5.4901395006079596,-4.1188700569085768,4.4913445837531247,-1.6157660562516234,1.9347541985851435,-1.0644564538842487]])

        # Layer 2 #
        self.b2 = np.array([[0.36196252178728949],[0.082377663021200198],[-0.22193325494037569]])
        self.LW2_1 = np.array([[-0.1954529569839529,-0.20034799025613526,-0.23053635648296672],[-0.0082594450793135564,-0.18890787157028985,0.14947281725982903],[0.18816847611922347,0.1725670439642624,-0.17246269692479335]])

        # Output 1 #
        self.y1_step1_ymin = np.array([-1])
        self.y1_step1_gain = np.array([[0.114681075655736],[0.123040745311932],[0.186388790801788]])
        self.y1_step1_xoffset = np.array([[-8.776001],[-7.807098],[-5.60557]])

    def get_network_vars(self):
        return (self.x1_step1_xoffset,
                self.x1_step1_gain,
                self.x1_step1_ymin,
                self.b1,
                self.IW1_1,
                self.LW1_2,
                self.b2,
                self.LW2_1,
                self.y1_step1_ymin,
                self.y1_step1_gain,
                self.y1_step1_xoffset)



