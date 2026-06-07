# Week 3 U-substitution
*Generated on 2026-06-07_17-11*

# Week 3 U-substitution

**Week 3 U-Substitution**

**📌 Overview**
This week, we will be covering the concept of U-substitution in calculus. U-substitution is a technique used to evaluate definite integrals by substituting a new variable u into the original integral. This allows us to simplify the integral and find its antiderivative.

**📖 Key Definitions**

* **U-Substitution**: A technique used to evaluate definite integrals by substituting a new variable u into the original integral.
* **g(x)**: The function that defines the substitution, where g0(x) is continuous over an interval.
* **f(u)**: The function that results from substituting u into f(x).
* **du**: The differential of u, which is equal to g0(x) dx.

**🧠 Main Concepts**

### Concept Name: U-Substitution Rules

The following rules are used when performing U-substitution:

1. **Let u = g(x)**: Define the substitution by letting u be a function of x.
2. **Find du**: Find the differential of u, which is equal to g0(x) dx.
3. **Substitute into f(x)**: Substitute u into f(x) to get f(u).
4. **Change the bounds**: Change the bounds of the integral by substituting the new limits a and b with g(a) and g(b), respectively.

### Concept Name: Substitution in Definite Integrals

When performing U-substitution on definite integrals, we have:

**Theorem 1.8: Substitution for Definite Integrals**

If u = g(x), then:

∫[a,b] f(g(x))g'(x) dx = ∫[g(a),g(b)] f(u) du

where:

* u = g(x)
* du = g'(x) dx
* f(u) is the function resulting from substituting u into f(x)

### Concept Name: Substitution in Indefinite Integrals

When performing U-substitution on indefinite integrals, we have:

**Theorem 1.8: Substitution for Indefinite Integrals**

If u = g(x), then:

∫f(g(x))g'(x) dx = F(u) + C

where:

* u = g(x)
* du = g'(x) dx
* F(u) is the antiderivative of f(u)

### Concept Name: Examples and Applications

Examples of U-substitution include:

* ∫e^x sin(x) dx (let u = e^x, then du = e^x dx)
* ∫(2x + 1)^3 dx (let u = 2x + 1, then du = 2dx)

Applications of U-substitution include:

* Evaluating definite integrals
* Finding antiderivatives of functions

**📐 Formulas & Theorems**

* **Theorem 1.8: Substitution for Definite Integrals**
∫[a,b] f(g(x))g'(x) dx = ∫[g(a),g(b)] f(u) du
* **Theorem 1.8: Substitution for Indefinite Integrals**
∫f(g(x))g'(x) dx = F(u) + C

**✏️ Worked Examples**

### Example 1: Evaluating a Definite Integral using U-Substitution

Evaluate ∫[0,π] e^x sin(x) dx.

Let u = e^x, then du = e^x dx. We have:

∫[0,π] e^x sin(x) dx = ∫[e^0,e^π] e^u cos(u) du

Using the substitution formula, we get:

∫[e^0,e^π] e^u cos(u) du = ∫[1,e^π] e^u cos(u) du

Evaluating this integral, we get:

∫[1,e^π] e^u cos(u) du = [e^u sin(u) + e^u cos(u)] from 1 to e^π

Simplifying, we get:

[e^π sin(e^π) + e^π cos(e^π)] - [e^1 sin(1) + e^1 cos(1)]

### Example 2: Finding an Antiderivative using U-Substitution

Find the antiderivative of ∫(2x + 1)^3 dx.

Let u = 2x + 1, then du = 2dx. We have:

∫(2x + 1)^3 dx = ∫u^3 (1/2)du

Using the power rule, we get:

∫u^3 (1/2)du = (1/8)u^4 + C

Substituting back u = 2x + 1, we get:

(1/8)(2x + 1)^4 + C

**⭐ Key Takeaways**

* U-substitution is a technique used to evaluate definite integrals by substituting a new variable u into the original integral.
* The substitution formula for definite integrals is ∫[a,b] f(g(x))g'(x) dx = ∫[g(a),g(b)] f(u) du.
* The substitution formula for indefinite integrals is ∫f(g(x))g'(x) dx = F(u) + C.
* U-substitution can be used to evaluate definite integrals and find antiderivatives of functions.

---

**Week 3 U-Substitution**

**📌 Overview**
This week, we will be covering the concept of u-substitution in integral calculus. U-substitution is a technique used to evaluate definite integrals by making a substitution that simplifies the integral.

**📖 Key Definitions**

* **U-Substitution**: A method for evaluating definite integrals by making a substitution that simplifies the integral.
* **Substitution**: A change of variable in an integral, where we replace a part of the original function with a new function.

**🧠 Main Concepts**

### Concept: U-Substitution

U-substitution is a technique used to evaluate definite integrals by making a substitution that simplifies the integral. The general form of u-substitution is:

∫f(u) \* du = F(u)

where f(u) is the original function and F(u) is the antiderivative.

### Substitution Rules

There are three main rules for u-substitution:

1. **Power Rule**: If f(x) = x^n, then ∫x^n dx = (x^(n+1))/(n+1) + C
2. **Product Rule**: If f(x) = u \* v, then ∫u \* v du = u \* ∫v du - ∫(∂u/∂x) \* ∫v du dx
3. **Quotient Rule**: If f(x) = u/v, then ∫u/v du = (1/v) \* ∫u du - (∂u/∂x)/v \* ∫v du dx

### Conditions for U-Substitution

For u-substitution to work, the following conditions must be met:

1. The original function f(x) must be a function of x.
2. The substitution u = g(x) must be one-to-one and continuous.
3. The derivative of the substitution u = g(x) must exist.

### Example 1

Evaluate ∫(x^2 + 1) dx using u-substitution.

Solution:

Let u = x^2 + 1, then du/dx = 2x.

∫(x^2 + 1) dx = ∫u du
= (1/2) \* u^2 + C
= (1/2) \* (x^2 + 1)^2 + C

### Example 2

Evaluate ∫cos(ln x) dx using u-substitution.

Solution:

Let u = ln x, then du/dx = 1/x.

∫cos(ln x) dx = ∫e^u du
= e^u + C
= e^(ln x) + C
= x + C

### Example 3

Evaluate ∫|v(t)| dt using u-substitution.

Solution:

Let v(t) = t - 8t + 6, then u = t - 8t + 6.

∫|v(t)| dt = ∫|u| du
= ∫u du (since u is always positive)
= (1/2) \* u^2 + C
= (1/2) \* (t - 8t + 6)^2 + C

### Average Value of a Function

The average value of a function f(x) over an interval [a, b] is given by:

Average Value = (1/(b-a)) \* ∫[a,b] f(x) dx

This formula can be used to find the average temperature, average cost, or any other type of average.

### Worked Examples

#### Example 4

Evaluate ∫(3t^2 + 2t - 5) dt using u-substitution.

Solution:

Let u = t^2 + 2t - 5, then du/dt = 2t + 2.

∫(3t^2 + 2t - 5) dt = ∫u du
= (1/2) \* u^2 + C
= (1/2) \* (t^2 + 2t - 5)^2 + C

#### Example 5

Evaluate ∫cos(3x) dx using u-substitution.

Solution:

Let u = 3x, then du/dx = 3.

∫cos(3x) dx = ∫e^(iu) du
= (1/3i) \* e^iu + C
= (1/(3i)) \* cos(3x) + C

### Key Takeaways

* U-substitution is a technique used to evaluate definite integrals by making a substitution that simplifies the integral.
* The general form of u-substitution is ∫f(u) \* du = F(u).
* There are three main rules for u-substitution: power rule, product rule, and quotient rule.
* For u-substitution to work, the following conditions must be met: the original function f(x) must be a function of x, the substitution u = g(x) must be one-to-one and continuous, and the derivative of the substitution u = g(x) must exist.

I hope these study notes help you understand u-substitution better!

---

**Week 3 U-Substitution**

**📌 Overview**
This week, we will be covering the concept of u-substitution in calculus. U-substitution is a technique used to solve definite integrals by making a substitution that simplifies the integral.

**📖 Key Definitions**

* **U-Substitution**: A method for solving definite integrals by making a substitution that simplifies the integral.
* **Substitution**: A change of variable in an integral, where we replace a function with another function to simplify the integral.

**🧠 Main Concepts**

### Concept: U-Substitution

U-substitution is a technique used to solve definite integrals by making a substitution that simplifies the integral. The general form of u-substitution is:

∫f(u)du = ?

where f(u) is a function of u, and du is the differential of u.

### Concept: Choosing the Right Substitution

Choosing the right substitution is crucial in u-substitution. We need to choose a substitution that simplifies the integral. Here are some tips for choosing the right substitution:

* Look for a function that can be easily integrated.
* Look for a function that has a simple antiderivative.
* Use the chain rule to simplify the integral.

### Concept: Applying U-Substitution

To apply u-substitution, we need to follow these steps:

1. Choose a substitution that simplifies the integral.
2. Make the substitution and rewrite the integral in terms of u.
3. Integrate the function with respect to u.
4. Substitute back to get the final answer.

### Concept: Examples of U-Substitution

Here are some examples of u-substitution:

* ∫(x^2 + 1)dx = ∫u^2du
* ∫(sin(x))dx = ∫(cos(u))du
* ∫(e^x)dx = ∫(e^u)du

### Concept: Worked Examples

**Example 1**

Evaluate ∫(t - 8t + 6)(t - 3)dt from t = 0 to t = 3.

Solution:

Let u = t - 3, then du/dt = 1, and du = dt.

∫(u + 5)du = (u^2/2) + 5u

Substitute back: ∫((t - 3) + 5)(t - 3)dt from t = 0 to t = 3.

= [(t - 3)^2/2] + 5(t - 3)

Evaluate the integral from t = 0 to t = 3:

= [(3^2)/2] + 5(3 - 3)
= (9/2) + 0
= 4.5

**Example 2**

Evaluate ∫(x^2 + 1)dx from x = 0 to x = 6.

Solution:

Let u = x^2, then du/dx = 2x, and du = 2xdx.

∫(u + 1)(2x)du = (u^2/2) + u

Substitute back: ∫((x^2)^2 + 1)(2x)dx from x = 0 to x = 6.

= [(x^4)/2] + x

Evaluate the integral from x = 0 to x = 6:

= [(6^4)/2] + 6
= (1296/2) + 6
= 648 + 6
= 654

**Example 3**

Evaluate ∫(e^x)dx from x = 0 to x = 1.

Solution:

Let u = e^x, then du/dx = e^x, and du = e^xdx.

∫udu = (u^2)/2

Substitute back: ∫(e^x)e^xdx from x = 0 to x = 1.

= [(e^x)^2]/2

Evaluate the integral from x = 0 to x = 1:

= [(e^1)^2]/2
= (e^2)/2

**📐 Formulas & Theorems**

* **U-Substitution Formula**: ∫f(u)du = ?
* **Chain Rule Formula**: (d/dx)(f(g(x))) = f'(g(x)) \* g'(x)

**✏️ Worked Examples**

### Example 1

Evaluate ∫(t - 8t + 6)(t - 3)dt from t = 0 to t = 3.

Solution:

Let u = t - 3, then du/dt = 1, and du = dt.

∫(u + 5)du = (u^2/2) + 5u

Substitute back: ∫((t - 3) + 5)(t - 3)dt from t = 0 to t = 3.

= [(t - 3)^2/2] + 5(t - 3)

Evaluate the integral from t = 0 to t = 3:

= [(3^2)/2] + 5(3 - 3)
= (9/2) + 0
= 4.5

### Example 2

Evaluate ∫(x^2 + 1)dx from x = 0 to x = 6.

Solution:

Let u = x^2, then du/dx = 2x, and du = 2xdx.

∫(u + 1)(2x)du = (u^2/2) + u

Substitute back: ∫((x^2)^2 + 1)(2x)dx from x = 0 to x = 6.

= [(x^4)/2] + x

Evaluate the integral from x = 0 to x = 6:

= [(6^4)/2] + 6
= (1296/2) + 6
= 648 + 6
= 654

### Example 3

Evaluate ∫(e^x)dx from x = 0 to x = 1.

Solution:

Let u = e^x, then du/dx = e^x, and du = e^xdx.

∫udu = (u^2)/2

Substitute back: ∫(e^x)e^xdx from x = 0 to x = 1.

= [(e^x)^2]/2

Evaluate the integral from x = 0 to x = 1:

= [(e^1)^2]/2
= (e^2)/2

**⭐ Key Takeaways**

* U-substitution is a technique used to solve definite integrals by making a substitution that simplifies the integral.
* Choosing the right substitution is crucial in u-substitution.
* The chain rule can be used to simplify the integral.
* The formula for u-substitution is ∫f(u)du = ?.

**Additional Notes**

* U-substitution is a powerful tool for solving definite integrals.
* It is often used when the function being integrated has a complex or difficult-to-integrate form.
* Practice makes perfect! Try working through some examples of u-substitution to become more comfortable with the technique.

---

**Week 3 U-Substitution**

**📌 Overview**
This week, we will be covering the concept of U-substitution in calculus. U-substitution is a technique used to evaluate definite integrals by making a substitution that simplifies the integral.

**📖 Key Definitions**

* **U-substitution**: A technique used to evaluate definite integrals by making a substitution that simplifies the integral.
* **Substitution**: A change of variable in an integral, where we replace x with a new function u(x) or v(t).

**🧠 Main Concepts**

### Concept: U-Substitution

U-substitution is a technique used to evaluate definite integrals by making a substitution that simplifies the integral. The general form of U-substitution is:

∫f(u) \* u' (x) dx = ∫f(u) du

where f(u) is the function being integrated, u(x) is the substitution function, and u'(x) is the derivative of the substitution function.

### Concept: Substitution

Substitution is a change of variable in an integral, where we replace x with a new function u(x) or v(t). The main types of substitutions are:

* **Simple substitution**: Replacing x with u(x)
* **Composite substitution**: Replacing x with u(x), and then replacing u(x) with v(u(x))

### Concept: Chain Rule

The chain rule is a fundamental concept in calculus that deals with the derivative of composite functions. The chain rule states that if we have a composite function f(g(x)), then the derivative of f(g(x)) is given by:

f'(g(x)) \* g'(x)

This rule can be applied to U-substitution to simplify the integral.

### Concept: Right-Endpoint Approximation

A right-endpoint approximation is an estimate of the area under a curve using the right endpoint of each subinterval. The formula for right-endpoint approximation is:

∫[a, b] f(x) dx ≈ Δx \* [f(a) + f(b)]/2

### Concept: Left-Endpoint Approximation

A left-endpoint approximation is an estimate of the area under a curve using the left endpoint of each subinterval. The formula for left-endpoint approximation is:

∫[a, b] f(x) dx ≈ Δx \* [f(a) + f(b)]

### Concept: Skunk Problem

The skunk problem is a classic example used to illustrate U-substitution. The problem states that a skunk runs out on the road 6 meters away and it takes 8 seconds to stop. Will you hit the skunk? We can use U-substitution to solve this problem.

### Concept: Example 1

Evaluate the definite integral ∫[0, 10] x^2 dx using U-substitution.

Step 1: Make a substitution u = x^2
Step 2: Find the derivative of u with respect to x: du/dx = 2x
Step 3: Substitute u and du into the integral:
∫[0, 10] x^2 dx = ∫[u(0), u(10)] u du
Step 4: Evaluate the integral:
∫[u(0), u(10)] u du = [u^2/2] from u(0) to u(10)
= [(10)^2/2] - [(0)^2/2]
= 50

### Concept: Example 2

Evaluate the definite integral ∫[0, π] sin(x) dx using U-substitution.

Step 1: Make a substitution u = sin(x)
Step 2: Find the derivative of u with respect to x: du/dx = cos(x)
Step 3: Substitute u and du into the integral:
∫[0, π] sin(x) dx = ∫[u(0), u(π)] u du
Step 4: Evaluate the integral:
∫[u(0), u(π)] u du = [-cos(u)] from u(0) to u(π)
= -cos(π) + cos(0)
= -(-1) + 1
= 2

### Concept: Bonus Problem

Evaluate the definite integral ∫[0, 10] e^x dx using U-substitution.

Step 1: Make a substitution u = e^x
Step 2: Find the derivative of u with respect to x: du/dx = e^x
Step 3: Substitute u and du into the integral:
∫[0, 10] e^x dx = ∫[u(0), u(10)] u du
Step 4: Evaluate the integral:
∫[u(0), u(10)] u du = [u^2/2] from u(0) to u(10)
= [(10)^2/2] - [(0)^2/2]
= 50

**📐 Formulas & Theorems**

* **U-Substitution Formula**: ∫f(u) \* u' (x) dx = ∫f(u) du
* **Chain Rule Formula**: f'(g(x)) \* g'(x)

**✏️ Worked Examples**

### Example 1

Evaluate the definite integral ∫[0, 10] x^2 dx using U-substitution.

Step 1: Make a substitution u = x^2
Step 2: Find the derivative of u with respect to x: du/dx = 2x
Step 3: Substitute u and du into the integral:
∫[0, 10] x^2 dx = ∫[u(0), u(10)] u du
Step 4: Evaluate the integral:
∫[u(0), u(10)] u du = [u^2/2] from u(0) to u(10)
= [(10)^2/2] - [(0)^2/2]
= 50

### Example 2

Evaluate the definite integral ∫[0, π] sin(x) dx using U-substitution.

Step 1: Make a substitution u = sin(x)
Step 2: Find the derivative of u with respect to x: du/dx = cos(x)
Step 3: Substitute u and du into the integral:
∫[0, π] sin(x) dx = ∫[u(0), u(π)] u du
Step 4: Evaluate the integral:
∫[u(0), u(π)] u du = [-cos(u)] from u(0) to u(π)
= -cos(π) + cos(0)
= -(-1) + 1
= 2

### Example 3

Evaluate the definite integral ∫[0, 10] e^x dx using U-substitution.

Step 1: Make a substitution u = e^x
Step 2: Find the derivative of u with respect to x: du/dx = e^x
Step 3: Substitute u and du into the integral:
∫[0, 10] e^x dx = ∫[u(0), u(10)] u du
Step 4: Evaluate the integral:
∫[u(0), u(10)] u du = [u^2/2] from u(0) to u(10)
= [(10)^2/2] - [(0)^2/2]
= 50

**⭐ Key Takeaways**

* U-substitution is a technique used to evaluate definite integrals by making a substitution that simplifies the integral.
* The general form of U-substitution is ∫f(u) \* u' (x) dx = ∫f(u) du
* The chain rule can be applied to U-substitution to simplify the integral.
* Right-endpoint approximation and left-endpoint approximation are estimates of the area under a curve using the right endpoint and left endpoint of each subinterval, respectively.

---

