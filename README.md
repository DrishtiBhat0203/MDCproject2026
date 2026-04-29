# Design and Implementation of a Secure SQL Injection Detection and Prevention System

## Overview
This project focuses on understanding how SQL Injection attacks work and how they can be detected and prevented.

The project has two parts:
- A **Python-based detection system** that analyzes user input, logs suspicious activity, and blocks repeated attempts
- A **web-based login system (PHP & MySQL)** that demonstrates both a vulnerable implementation and a secure version using prepared statements

This helped in understanding both detection and prevention practically.

---

##  Objective
- Detect SQL injection attempts from user input  
- Reduce false positives using regex  
- Maintain logs of suspicious activity  
- Implement attempt-based blocking  
- Understand prevention using prepared statements  

---

## Working

### Python Detection System
- Takes username and password as input  
- Converts input to lowercase for consistent checking  
- Uses regex to detect SQL keywords and patterns  
- Classifies risk into LOW, MEDIUM, and HIGH  
- Tracks attempts using a file  
- Logs suspicious activity  
- Blocks user after 3 attempts  

---

###  PHP Web Demonstration

#### Vulnerable Version
- SQL query is created directly using user input  
- No protection mechanism  
- Susceptible to SQL injection  

#### Secure Version
- Uses prepared statements  
- Input is handled safely  
- SQL query structure remains fixed  

---

##  Detection Logic
- Regex with word boundary (`\b`) is used to reduce false positives  
- Example: "doctor" is not detected as "or"  

Checks include:
- Keywords: `OR`, `SELECT`, `DROP`, `UNION`, `INSERT`, `DELETE`  
- Special characters: `'`, `--`, `;`  

---

##  Features
- SQL Injection Detection  
- Reduced False Positives  
- Risk Classification  
- Logging System  
- Attempt Tracking  
- Blocking Mechanism  
- Demonstration of Vulnerable vs Secure System  

---

## Project Structure
MDCproject2026/
│
├── sql_detector.py
├── README.md
└── web_demo/
├── vulnerable_login.php
└── secure_login.php

---

##  Limitations
- Limited set of predefined SQL keywords  
- Rule-based detection approach  
- Cannot detect highly complex or obfuscated attacks  
- Python module is not connected to a real-time database  

---

##  Future Scope
- Integration with real database systems  
- Improvement in detection rules  
- Implementation in full web applications  
- Use of advanced detection techniques  

---

## Observation
It was observed that when SQL queries are directly constructed using user input, the query logic can be manipulated.  
After applying prepared statements, the same type of input does not affect the query, making the system secure.

---

## Learning
- Understanding SQL injection attacks  
- Importance of secure query handling  
- Difference between detection and prevention  
- Practical implementation of security concepts  

---

## Author
Drishti Bhat

