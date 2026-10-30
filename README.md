# Traveling Salesperson Problem (TSP) with Local Search Algorithms

Python implementations of two optimization heuristics—**Hill Climbing** and **Simulated Annealing variant**—to find the shortest round-trip path visiting four major Iranian cities: **Tehran**, **Mashhad**, **Isfahan**, and **Shiraz**.

---

## 📌 Problem Overview

The problem is modeled as a classic **Traveling Salesperson Problem (TSP)**:
- Find the shortest route that visits every city exactly once and returns to the starting city.
- Cities are indexed as:
  - `0`: Tehran
  - `1`: Mashhad
  - `2`: Isfahan
  - `3`: Shiraz
- Inter-city travel costs are defined using a **symmetric distance matrix**.

---

## 🚀 Implemented Algorithms

This repository provides two different heuristic approaches to solve the TSP instance:

### 1. Hill Climbing 
- **Concept**: A pure greedy descent strategy.
- **Mechanism**:
  - Samples successor tours randomly.
  - Transitions to a successor if and only if its total distance is strictly less than the current best.
  - Stops as soon as no generated successor improves upon the current solution (terminates at a local minimum).

### 2. Simulated Annealing 
- **Concept**: An exploration-oriented approach designed to avoid getting trapped in local optima.
- **Mechanism**:
  - Always accepts improving solutions.
  - Accepts worse candidate paths probabilistically
  - Uses weighted sampling over candidate solutions and the current best path to make the next move.

---

## 🛠 Project Structure
```text
├── hill_climbing.py       # Greedy local search implementation
├── simulated_annealing.py # Probabilistic search using Boltzmann-style selection
└── README.md
