'''
[getmusic in line terminal]
   about:
      a easy method ofr getting music's without write a code
_______________________________
Reinan Br
'''

from tubemp3.getmusic import getmusic as gm
from tubemp3 import get_from_link as gfl
import sys

#name_music = sys.argv[1]
link_music = sys.argv[1]
def main():
   gfl(link_music).download_mp3()
