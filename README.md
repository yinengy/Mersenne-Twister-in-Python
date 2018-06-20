# Mersenne Twister in Python 

Try to rebuild the pseudo-random algorithm *Mersenne Twister*, which is used in python's random library. 

Also with a basic *Random* class and some simple methods for easily testing.

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

&nbsp;

**.random()**:

return uniform ditribution in [0,1)
``` python
>>> name.random()
0.1786995275775844
```

&nbsp;

**.randint(begin_number, end_number)**:

return random int in [a,b)
``` python
>>> name.randin(1,10)
9
```

&nbsp;

**.shuffle(sequence)**:

shuffle the input sequence
``` python
>>> name.shuffle([1,2,3,4,5])
[2, 1, 5, 3, 4]
```

&nbsp;

**.choice(sequence, replace=True, size=1)**:

choice an element randomly in the sequence.

replace: choose with replacement or not.

size: the number of element to be chosen, if size != 1, will return a list contains those element.
``` python
>>> name.choice([1,2,3,4,5])
1
>>> name.choice([1,2,3,4,5],size=3)
[2, 3, 2]
>>> name.choice([1,2,3,4,5],replace=False,size=3)
[2, 5, 1]
```

&nbsp;

**.bern(p)**:

generate a Bernoulli Random Variable

p: the probability of True

```
>>> name.bern(0.5)
True
>>> name.bern(0.5)
False
```

&nbsp;

**.binomial(n, p)**:

generate a Binomial Random Variable

n: total times

p: probability of success
```
>>> name.binomial(10, 0.5)
6
>>> name.binomial(10, 0.5)
3
```


&nbsp;

**.geometric(p)**:

generate a Geometric Random Variable
            
p: probability of success
```
>>> name.geometric(0.5)
1
>>> name.geometric(0.5)
2
```


## Randomness Testing

The file *Testing for Randomness.ipynb* contains several basic randomness testing result for this algorithm.

