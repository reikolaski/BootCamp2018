def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1: return 1
<<<<<<< HEAD
    for i in range(2, int(n**.5) + 1):
=======
    for i in range(2, int(n**.5)+1):
>>>>>>> 3e81012ab754861db0fb7d588b4f9b4c23c4c209
        if n % i == 0: return i
    return n