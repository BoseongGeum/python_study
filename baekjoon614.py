MOD = 1000000007

# 팩토리얼을 구하고 모듈러 연산을 적용한 결과를 반환
def factorial_mod(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

# 모듈러 역원을 페르마의 소정리를 이용해 구함
def mod_inverse(a, mod):
    return pow(a, mod - 2, mod)

# 이항 계수를 구함
def binomial_coefficient(n, k, mod):
    if k == 0 or k == n:
        return 1
    numerator = factorial_mod(n, mod)
    denominator = (factorial_mod(k, mod) * factorial_mod(n - k, mod)) % mod
    return (numerator * mod_inverse(denominator, mod)) % mod

# 입력 받기
n, k = map(int, input().split())

# 결과 출력
print(binomial_coefficient(n, k, MOD))
