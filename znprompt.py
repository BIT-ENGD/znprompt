
from playsound import playsound
import os 

SELF_DIR=os.path.split(os.path.realpath(__file__))[0]
FINISH_WAV=SELF_DIR+os.sep+"wave/train_done.wav"
ERROR_WAV=SELF_DIR+os.sep+"wave/train_error.wav"
class znprompt(object):
    def __init__(self) -> None:
        self.finish_wav=FINISH_WAV
        self.error_wav=ERROR_WAV

    
    def finish(self):
        playsound(self.finish_wav)

    def error(self):
        playsound(self.error_wav)



if __name__ == "__main__":

    testobj = znprompt()

    testobj.finish()
    testobj.error()