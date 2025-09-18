# Loops in Python (for, while, and controls)

## Overview

In programming, **loops** allow us to perform **repetitive tasks** efficiently without writing the same code multiple times.  
In DevOps, loops are extremely useful for automating tasks like provisioning servers, monitoring, backups, and log analysis.

This day covers:
- **For Loops** – Iterating over sequences (lists, tuples, strings, ranges)
- **While Loops** – Running until a condition is met
- **Loop Control Statements** – `break` and `continue`
- **DevOps Use Cases** – Practical scenarios in automation with `for` and `while`

## Folder Contents

### 1. [01-loops.md](01-loops.md)
- Introduction to loops  
- `for` loop basics with examples  
- `while` loop basics with examples  

### 2. [02-loop-controls.md](02-loop-controls.md)
- Loop control statements:  
  - `break` → exit the loop early  
  - `continue` → skip current iteration  
- Practice exercise: Log file analysis (finding `ERROR` lines)

### 3. [03-for-loop-devops-usecases.md](03-for-loop-devops-usecases.md)
- Real-world DevOps examples using **for loops**:
  - Server provisioning  
  - Deploying configs to environments  
  - Backup and restore  
  - Log rotation and cleanup  
  - Monitoring and reporting  
  - Cloud resource management  
- Examples provided in **Bash** and **Python**

### 4. [04-while-loop-devops-usecases.md](04-while-loop-devops-usecases.md)
- DevOps scenarios where **while loops** are useful:
  - Service health checks  
  - Retrying failed deployments  
  - Waiting for resources (e.g., pods, VMs) to be ready  
  - Monitoring log files continuously

## Why Loops Matter in DevOps?

- Automating **repeated tasks** (server setup, log management, monitoring)  
- Handling **dynamic infrastructure** (cloud scaling, container orchestration)  
- Enabling **CI/CD pipelines** to loop through build/test/deploy steps  
- Writing **idempotent automation scripts**  

## Next Steps
- Practice writing `for` and `while` loops with **real DevOps tasks**.  
- Combine loops with **conditions** and **functions** for more powerful automation.  
- Move towards **Day-10** where we’ll explore **functions and modular scripts** for DevOps.