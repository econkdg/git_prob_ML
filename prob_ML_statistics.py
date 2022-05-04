# ====================================================================================================
# statistics
# ====================================================================================================
# how to generate random numbers(samples or data)

# simulation
# experiment

# data sampled from population / process / generative model

# import library
import numpy as np
import matplotlib.pyplot as plt

# generate random number(1D)
m = 1000

# rand: uniform distribution
# U(0,1)
x1 = np.random.rand(m, 1)  # sampling

# U(a,b)
a = 1
b = 5
x2 = a + (b-a)*np.random.rand(m, 1)

# randn: Gaussian(normal) distribution
# N(0,1^2) -> standard normal distribution
x3 = np.random.randn(m, 1)  # x3 = np.random.normal(0, 1, m)

# N(5,2^2)
x4 = 5 + 2*np.random.randn(m, 1)

# randint: random intergers
x5 = np.random.randint(1, 6, size=(1, m))  # 1~5
# ----------------------------------------------------------------------------------------------------
# sample mean and sample size

# statistics
# numerically understand statistics

# U(0,1)
m = 100
x = np.random.rand(m, 1)

#xbar = 1/m*np.sum(x, axis = 0)
#np.mean(x, axis = 0)

xbar = 1/m*np.sum(x)
np.mean(x)

varbar = (1/(m - 1))*np.sum((x - xbar)**2)
np.var(x)

print(xbar)
print(np.mean(x))
print(varbar)
print(np.var(x))

# various sample size m
m = np.arange(10, 2000, 20)
means = []

for i in m:
    x = np.random.normal(10, 30, i)
    means.append(np.mean(x))

plt.figure(figsize=(10, 6))
plt.plot(m, means, 'bo', markersize=4)
plt.axhline(10, c='k', linestyle='dashed')
plt.xlabel('# of smaples (= sample size)', fontsize=15)
plt.ylabel('sample mean', fontsize=15)
plt.ylim([0, 20])
plt.show()
# ----------------------------------------------------------------------------------------------------
# CLT & LLN

N = 100
m = np.array([10, 40, 160])  # sample of size m

# sample mean
S1 = []
S2 = []
S3 = []

for i in range(N):
    S1.append(np.mean(np.random.rand(m[0], 1)))
    S2.append(np.mean(np.random.rand(m[1], 1)))
    S3.append(np.mean(np.random.rand(m[2], 1)))

plt.figure(figsize=(10, 6))
plt.subplot(1, 3, 1), plt.hist(S1, 21), plt.xlim(
    [0, 1]), plt.title('m = ' + str(m[0])), plt.yticks([])
plt.subplot(1, 3, 2), plt.hist(S2, 21), plt.xlim(
    [0, 1]), plt.title('m = ' + str(m[1])), plt.yticks([])
plt.subplot(1, 3, 3), plt.hist(S3, 21), plt.xlim(
    [0, 1]), plt.title('m = ' + str(m[2])), plt.yticks([])
plt.show()
# ====================================================================================================
