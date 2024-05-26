# Simple SNARK

This repo contains a collection of scripts and files related to the _How SNARKs Compress Infinite
Computation Video_.

In this video we wanted to visually demonstrate the math in a more intuitive and step-by-step way so
that you may understand how SNARKs are succinct while not being shy about the math.

In the visualizations / resulting video we attempt to explain:
1. The Schwartz-Zippel Lemma: Why comparing two bounded polynomials at a given point is enough to
   determine whether they're equal or not
2. How any computation can be turned into a set of polynomials
3. How to construct a quotient check to efficiently verify that our computation has the desired
   result at the specified points.
