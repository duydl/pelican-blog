Title: Wave and Fourier Transform
Tags: Physics
Date: 2020-5-03 10:20
Modified: 2020-5-03 19:30

<b>Fourier Series</b>

The initial shape of the string can be expressed as:
$$ 
y(x,0) = \begin{cases} \frac{3a}{L} x &\text{for } 0 \leq x < \frac{L}{3}\\ \frac{3a}{2L}(L-x) &\text{for } \frac{L}{3} \leq x \leq L \end{cases}
$$
$$ 
y(x,0) = \begin{cases} \frac{3a}{L} x &\text{for } 0 \leq x < \frac{L}{3}\\ \frac{3a}{2L}(L-x) &\text{for } \frac{L}{3} \leq x \leq L \end{cases}
$$
We are goin to express the above function in the form:
$$
y(x,0) = \sum_k A_k \sin kx
$$ 
for $k = \dfrac{n\pi}{L}$. 

We can extract $A_k$ using the "orthogonality" of the sine function: 
$$ 
\int^L_0 \sin(k_n x) \sin(k_m x)  dx = \begin{cases} \frac{L}{2} &\text{ if } m = n \\ 0 &\text { if } m \neq n \end{cases}.
$$ 

We have: 
$$\begin{aligned}
A_k &= \frac{2}{L} \int_0^L y(x,0)\sin (k x) d x \\
&= \frac{2}{L} \left[\frac{3a}{L} \int_0^{L/3}  x \sin (kx) dx + \frac{3a}{2L}\int_{L/3}^{L}(L-x)\sin (kx) dx \right] 
\end{aligned}$$

As $\int x \sin x dx = -x \cos x + \int \cos x d x = -x \cos x + \sin x + C$, we have:
$$\begin{aligned}
\int _0 ^{L/3} x \sin (kx) dx &= \frac{1}{k^2}\left( -kx \cos (kx) \Big|_0^{L/3} + \sin(kx)\Big |_0^{L/3}\right) \\ 
& = \frac{1}{k^2} \left(-\frac{kL}{3} \cos\frac{kL}{3} + \sin \frac{kL}{3}\right) 
\end{aligned}$$

$$\begin{aligned}
\int_{L/3}^{L}(L-x)\sin (kx) dx  =& - \frac{L}{k} \cos (kx) \Big|_{L/3}^{L}  -\frac{1}{k^2}\left( -kx \cos (kx) \Big|_{L/3}^{L} + \sin(kx)\Big |_{L/3}^{L}\right) \\ 
=& -\frac{L}{k} \cos kL + \frac{L}{k} \cos \frac{kL}{3}  \\
& - \frac{1}{k^2} \left(-kL \cos kL + \frac{kL}{3} \cos\frac{kL}{3}+ \sin kL - \sin \frac{kL}{3}\right) 
\end{aligned}$$

Then:
$$\begin{aligned}
A_k =& \frac{6a}{k^2L^2} \left(-\frac{kL}{3} \cos\frac{kL}{3} + \sin \frac{kL}{3}\right) -\frac{3a}{kL} \cos kL + \frac{3a}{kL} \cos \frac{kL}{3}\\
&- \frac{3a}{k^2L^2} \left(-kL \cos kL + \frac{kL}{3} \cos\frac{kL}{3}+ \sin kL - \sin \frac{kL}{3}\right)\\
=& -\frac{3a}{k^2L^2}\sin kL + \frac{9a}{k^2L^2}\sin \frac{kL}{3} + [...]  \\
=& \frac{9a}{k^2L^2}\sin \frac{kL}{3}
\end{aligned}$$

Or: 
$$
A_n = \frac{9a}{n^2\pi^2}\sin \frac{n\pi}{3}
$$

Now we can express $y(x,0)$ in the form $\sum_k A_k \sin kx$:
$$
y(x, 0)=\sum_{k} A_{k} \sin (k x)=\sum_{n=1}^{\infty} \frac{9a}{n^2\pi^2}\sin \frac{n\pi}{3}\sin \frac{n\pi x}{L}
$$

If we expand this for $n =$ 1, 2, **3**, 4, 5, **6**, $...$, we would get:
$$
y(x, 0)= \frac{9a}{\pi^2} \left\{ \frac{\sqrt{3}}{2}\sin \frac{\pi x}{L} + \frac{\sqrt{3}}{8}\sin \frac{2\pi x}{L} + 0 - \frac{\sqrt{3}}{32}\sin \frac{4\pi x}{L} - \frac{\sqrt{3}}{50}\sin \frac{5\pi x}{L} + 0  + \dots \right\}
$$

# Testing
* Let's check whether this Fourier Series could express the initial shape of the string with the following script.
We let $a = 1$ and $L = 1$:


```python
%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np

def func(n, x):
    return 9/(n**2*np.pi**2)*np.sin(n*np.pi/3)*np.sin(n*np.pi*x)

def sum(k, x):
    return_value = 0
    for i in range(k):
        return_value += func(i+1, x)
    return return_value

x_range = np.arange(0., 1., 0.001)
fig, axs = plt.subplots(3,2, figsize=(20, 12), facecolor='w', edgecolor='k')
fig.subplots_adjust(hspace = .5, wspace=.2)
axs = axs.ravel()

for i in range(6):
    axs[i].plot(x_range, sum(i+1, x_range), "r--", linewidth=3.0)
    axs[i].plot(x_range, 3*x_range*(x_range < 1/3) + 3/2*(1-x_range)*(x_range > 1/3), linewidth=2.0)
    axs[i].set_title("n = " + str(i+1))
plt.show()
```


![png](images/output_12_0.png)


* Below are some normal modes of the string vibration:


```python
for i in range(6):
    plt.plot(x_range, func(i+1, x_range), label='Normal Mode: n = %s' % str(i+1))
plt.legend(loc = 'upper right')
plt.show()
```


![png](images/output_14_0.png)


# Conclusion
The vibrations of a string with the given initial shape is as below:
$$
y(x, t)=\sum_{n=1}^{\infty}\left[\frac{9 a}{n^{2} \pi^{2}} \sin \left(\frac{n \pi}{3}\right) \sin \left(\frac{n \pi}{L} x\right) \cos \left(\frac{n \pi}{L} \sqrt{\frac{T}{\mu}} t\right)\right]
$$
