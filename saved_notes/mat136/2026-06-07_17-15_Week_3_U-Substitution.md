# Week 3 U-Substitution
*Generated on 2026-06-07_17-15*

# Week 3 U-Substitution

## 📌 Overview
This lecture covers the concept of u-substitution in integral calculus, which is a technique used to evaluate definite integrals by substituting a function into another function. The main goal of this lecture is to understand how to apply u-substitution to solve various types of problems.

## 🖋️ Key Definitions

* **u-substitution**: A technique used to evaluate definite integrals by substituting a function into another function.
* **u** (upper case): The new variable introduced in the substitution process.
* **du** (lower case u): The differential of the new variable u, which is equal to g(x) dx.

## 🧠 Main Concepts

### U-Substitution Process
The u-substitution process involves the following steps:
1. Choose a function u = g(x) where g(x) is continuous over an interval.
2. Find the derivative of u with respect to x, which is du/dx = g'(x).
3. Rewrite the original integral in terms of u and du.
4. Evaluate the new integral.

### Types of Integrals
There are two types of integrals that can be evaluated using u-substitution:
1. **Definite integrals**: Integrals with a specific upper and lower bound, such as ∫[a,b] f(x) dx.
2. **Indefinite integrals**: Integrals without a specific upper and lower bound, such as ∫f(x) dx.

### Rules of u-Substitution
There are two rules to keep in mind when applying u-substitution:
1. **Change the bounds**: When changing the bounds of integration, make sure to change them accordingly.
2. **Apply FTC 2**: If the original integral is a definite integral, apply the Fundamental Theorem of Calculus (FTC) 2 to evaluate it.

## 📝 Formulas & Theorems

* **u-Substitution Formula**:
∫[a,b] f(g(x))g'(x) dx = ∫[g(a),g(b)] f(u) du
* **Fundamental Theorem of Calculus (FTC) 2**:
If F is an antiderivative of f, then ∫[a,b] f(x) dx = F(b) - F(a)

## 📚 Worked Examples

### Example 1: Evaluate ∫[0,π] x^2 sin(x) dx
Let u = x^2, then du/dx = 2x. Rewrite the integral in terms of u and du:
∫[0,π] x^2 sin(x) dx = ∫[u=0,u=π^2] u sin(u^(1/2)) (du/dx) dx
Apply FTC 2 to evaluate the integral:
∫[0,π] x^2 sin(x) dx = [u sin(u^(1/2))] from 0 to π^2 - ∫[0,π^2] u sin(u^(1/2)) (du/dx) dx
Simplify and evaluate the remaining integral:
∫[0,π] x^2 sin(x) dx = [u sin(u^(1/2))] from 0 to π^2 - ∫[0,π^2] u sin(u^(1/2)) du

### Example 2: Evaluate ∫[1,3] (x-1)^2 sin(x-1) dx
Let u = x-1, then du/dx = 1. Rewrite the integral in terms of u and du:
∫[1,3] (x-1)^2 sin(x-1) dx = ∫[u=0,u=2] u^2 sin(u) (du/dx) dx
Apply FTC 2 to evaluate the integral:
∫[1,3] (x-1)^2 sin(x-1) dx = [u^2 sin(u)] from 0 to 2 - ∫[0,2] u^2 sin(u) du

## 📝 Key Takeaways

* U-substitution is a powerful technique for evaluating definite integrals.
* Change the bounds of integration when applying u-substitution.
* Apply FTC 2 to evaluate definite integrals after substitution.

Note: These notes are a summary of the key concepts and formulas covered in Week 3 of MAT6. They are intended to serve as a study guide and should not be considered a comprehensive review of the material.