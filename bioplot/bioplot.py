import matplotlib

one_letter_to_three_letter = {
    'A' : 'ALA',
    'R' : 'ARG',
    'N' : 'ASN',
    'D' : 'ASP',
    'B' : 'ASX',
    'C' : 'CYS',
    'E' : 'GLU',
    'Q' : 'GLN',
    'Z' : 'GLX',
    'G' : 'GLY',
    'H' : 'HIS',
    'I' : 'ILE',
    'L' : 'LEU',
    'K' : 'LYS',
    'M' : 'MET',
    'F' : 'PHE',
    'P' : 'PRO',
    'S' : 'SER',
    'T' : 'THR',
    'W' : 'TRP',
    'Y' : 'TYR',
    'V' : 'VAL',}

# RasMol Color
'''
Amino Acid  Color      Triple        Amino Acid    Color  Triple
  ASP,GLU   bright red [230,10,10]     CYS,MET     yellow [230,230,0]
  LYS,ARG   blue       [20,90,255]     SER,THR     orange [250,150,0]
  PHE,TYR   mid blue   [50,50,170]     ASN,GLN     cyan   [0,220,220]
  GLY       light grey [235,235,235]   LEU,VAL,ILE green  [15,130,15]
  ALA       dark grey  [200,200,200]   TRP         pink   [180,90,180]
  HIS       pale blue  [130,130,210]   PRO         flesh  [220,150,130]
'''
one_letter_aa_to_color = {
    'A' : [200, 200, 200],
    'R' : [20, 90, 255],
    'N' : [0, 220, 220],
    'D' : [230, 10, 10],
    'B' : [230, 10, 10],
    'C' : [230, 230, 0],
    'E' : [230, 10, 10],
    'Q' : [0, 220, 220],
    'Z' : [0, 220, 220],
    'G' : [235, 235, 235],
    'H' : [130, 130, 210],
    'I' : [15, 130, 15],
    'L' : [15, 130, 15],
    'K' : [20, 90, 255],
    'M' : [230, 230, 0],
    'F' : [50, 50, 170],
    'P' : [220, 150, 130],
    'S' : [250, 150, 0],
    'T' : [250, 150, 0],
    'W' : [180, 90, 180],
    'Y' : [50, 50, 170],
    'V' : [15, 130, 15],}


class Bioplot(object):
    def __init__(self, ax):
        self.ax = ax

    def aaplot2d(self, seq: str, colors: list=None, autoscale: bool=True, max_width=25):
        aa_length = len(seq)
        height = aa_length // max_width + 1
        left = np.zeros(height)
        for idx, s in enumerate(seq):
            if colors is None:
                c = np.array(one_letter_aa_to_color[s]) / 255
            else:
                c = colors[idx]
                
            _y = np.zeros(height)

            _y = - ((idx + 1)// (max_width) + 1)
            print(_y, idx, idx // max_width, left)
            self.ax.barh(_y, 0.8, left=left, color=c)
            left[idx // (max_width-1)] += 1            

    def aaplot3d(self):
        pass
    

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.figure()
    ax = fig.add_subplot(111)
    bplot = Bioplot(ax)
    seq = "AABBCC"
    seq = "MEKEKKVKYFLRKSAFGLASVSAAFLVGSTVFAVDSPIEDTPIIRNGGELTNLLGNSETTLALRNEESATADLTAAAVADTVAAAAAENAGAAAWEAAAAADALAKAKADALKEFNKYGVSDYYKNLINNAKTVEGVKDLQAQVVESAKKARISEATDGLSDFLKSQTPAEDTVKSIELAEAKVLANRELDKYGVSDYHKNLINNAKTVEGVKDLQAQVVESAKKARISEATDGLSDFLKSQTPAEDTVKSIELAEAKVLANRELDKYGVSDYYKNLINNAKTVEGVKALIDEILAALPKTDTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTEKPEVIDASELTPAVTTYKLVINGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTEKPEVIDASELTPAVTTYKLVINGKTLKGETTTKAVDAETAEKAFKQYANDNGVDGVWTYDDATKTFTVTEMVTEVPGDAPTEPEKPEASIPLVPLTPATPIAKDDAKKDDTKKEDAKKPEAKKEDAKKAETLPTTGEGSNPFFTAAALAVMAGAGALAVASKRKED"
    seq = "MEKEKKVKYFLRKSAFGLASVSAAFLVGSTVFAVDSPIEDTPIIRNGGELTNLL"
    color = [0.1, 0.2, 0.3, 0.1, 0.2, 0.3]
    bplot.aaplot2d(seq)
    plt.show()
