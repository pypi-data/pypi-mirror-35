# Kinda

## About

Kinda is a pythonic library for comparing floating point values with
[Python operator functions](https://docs.python.org/2/library/operator.html#mapping-operators-to-functions).

## Arguments

The implementation and documentation are identical to
[math.isclose](https://docs.python.org/3/library/math.html#number-theoretic-and-representation-functions).

## Comparisons

### Equality

```py
>>> import kinda
>>> # a == b
>>> kinda.eq(1.0000, 1.0000)
True
>>> # a != b (default precision)
>>> kinda.eq(0.9999, 1.0001)
False
```

### Precision

All `math.isclose()` arguments are accepted in all functions.

* `abs_tol`: absolute tolerance (`abs(a - b)`)
* `rel_tol`: percentage tolerance (1% = .01)

```py
>>> # reduce absolute precision
>>> kinda.eq(0.9999, 1.0001, abs_tol=0.0002)
True
>>> # precision: 1%
>>> kinda.eq(1.0000, 1.0500, rel_tol=0.01)
False
>>> # precision: 5%
>>> kinda.eq(1.0000, 1.0500, rel_tol=0.05)
True
```

### Inequality

```py
>>> import kinda
>>> [kinda.ne(0.9999, 1.0001), kinda.ne(1.0000, 1.0000)]
[True, False]
```

### Less/Greater Than

```py
>>> import kinda
>>> # [a < b, a > b]
>>> [kinda.lt(1.0000, 1.0001), kinda.gt(1.0001, 1.0000)]
[True, True]
```

### Less/Greater Than or Equal To

```py
>>> import kinda
>>> kinda.le(1.0000, 1.0001) and kinda.ge(1.0000, 1.0001)
[True, False]
>>> kinda.le(1.0000, 1.0000) and kinda.ge(1.0000, 1.0000)
[True, True]
>>> kinda.le(1.0000, 0.9999) and kinda.ge(1.0000, 0.9999)
[False, True]
```