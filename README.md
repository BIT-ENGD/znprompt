Ａ simple library for voice prompt.

When a training job is done, you'd like to hear a voice prompt, right?
## install

python setupy.py install 

## example:
```
from znprompt import znprompt


test=znprompt()  

test.finish()   # play a voice to notify it's finished.
test.error()   # play a voice to nitify  it's broken.
```
