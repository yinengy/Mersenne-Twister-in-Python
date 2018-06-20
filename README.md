# Mersenne Twister in Python 

Try to rebuild the pseudo-random algorithm *Mersenne Twister*, which is used in python's random library. 

Also with a basic *Random* class and some simple methods for easly testing.

## MT19937.py 

Main part of the algorithm.

Convert the pseudocode in [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) to python code.

Coefficients follow the standard of *MT19937-32*.

## RandomClass.py 

A class named *Random*.

### Usage
Firstly, build a Random object. if no input, seed will default to 0.
``` python
>>> name = Random(seed)
```


.random():
return uniform ditribution in [0,1)
``` python
>>> name.random()
0.1786995275775844
```


.randint(a,b):
return random int in [a,b)
``` python
>>> name.randin(1,10)
9
```




