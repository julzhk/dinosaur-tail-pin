import subprocess
from sense_hat import SenseHat
from collections import deque
from time import sleep
from random import choice
""" thanks to 
        http://soundbible.com/suggest.php?q=dinosaur
    for the dinosaur sounds
"""
class SoundPlayer(object):
    soundfiles = [
        'TRex.mp3',
        'Dragon.mp3',
        'Pterodactyl.mp3',
        'TRex.mp3',
        'Zombie.mp3',
        'Halloween.mp3',
        'Raptor.mp3',
        'TRexRoar.mp3'
    ]

    def play(self,
 filename=None):
        if filename is None:
            filename = choice(self.soundfiles)
        self.player = subprocess.Popen(["omxplayer",
                                        filename,
                                        ],
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
    def stop(self):
        self.player = None

class Rolling_Avg(deque):
    """ Deque is a list with a fixed length; append new item,
 pops oldest item
    This class adds the 'avg' rolling average calculation
    r = Rolling_Avg(max_len=3)
    r.append(1)
    r.append(2)
    r.append(3)
    r.append(4)
    r.avg()
    >> 4.5
    """
    def avg(self):
        return sum(self) / len(self)

def intensity(*args):
    """ given some numbers,
 average of the squares of them:
    intensity(1,
2,
2)
    >>> 3.0
    """
    r = sum([a * a for a in args]) / len(args)
    return r


sense = SenseHat()
is_quiet = True
rolling_av = Rolling_Avg(maxlen=10)
player = SoundPlayer()
while True:
    sleep(0.1)
    raw = sense.get_compass_raw()
    curr = intensity(*raw.values())
    rolling_av.append(curr)
    rolling_av_avg = rolling_av.avg()
    print('{:.0f}'.format(curr - rolling_av_avg))
    if not is_quiet and curr < rolling_av_avg * 1.2:
        print('go quiet')
        player.stop()
        is_quiet=True

    if is_quiet and curr > rolling_av_avg * 1.5:
        print('roar')
        is_quiet = False
        player.play()