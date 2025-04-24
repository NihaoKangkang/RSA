# RSA
This project includes implementations of the Euclidean algorithm and the Extended Euclidean algorithm (包含欧几里得算法及扩展欧几里得算法的实现).

### Author: Kyi Wong
**Email:** kyiwong97@gmail.com  

## Objective  

To implement the standard RSA algorithm and compute the modular multiplicative inverse.

## Main Algorithm
1. Compute $n = p \times q$
2. Calculate $\phi(n) = (p-1) \times (q-1)$
3. Choose $e$ such that $0 < e < \phi(n)$
4. Compute $d = \mathrm{inverse}(e, \phi(n))$
5. Encryption: $c = m^e \mod n$
6. Decryption: $m = c^d \mod n$