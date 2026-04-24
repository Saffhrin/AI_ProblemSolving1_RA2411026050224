# Rule-Based Insurance Claim Decision System

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Logic](https://img.shields.io/badge/AI-Propositional%20Logic-green) ![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## Problem Description

An insurance company needs an automated system to evaluate whether a claim should be **approved or rejected** based on predefined logical rules.

The system uses **Propositional Logic** with facts such as:
- Policy validity (`policy_active`)
- Document verification (`documents_valid`)
- Accident reporting (`accident_reported`)
- Premium payment (`premium_paid`)
- Fraud detection (`fraud_detected`)

---

## Algorithm Used

### Rule-Based Inference — Forward Chaining (Propositional Logic)

The system implements **forward chaining**, a data-driven inference method:

1. A **Knowledge Base (KB)** is initialized with user-provided facts (True/False)
2. **Rules** in the form `IF condition(s) THEN outcome` are parsed
3. The engine iterates over all rules until no new facts can be derived
4. Rules support `AND` conjunctions and `NOT` negation
5. Chained inference: derived facts can trigger further rules
6. Final **decision** is read from the KB: `final_approve`, `approve_claim`, or `reject_claim`

---

## Folder Structure

```
AI_ProblemSolving_/
├── README.md
|── index.html
└── insurance_claim/
    ├── insurance_claim_system.py   # Main Python program (console)
    
```

---

## Execution Steps

### Python (Console)

```bash
# Clone the repository
git clone https://github.com/yourusername/AI_ProblemSolving_
cd AI_ProblemSolving_/insurance_claim

# Run the program
python insurance_claim_system.py
```

Then select:
- `1` → Interactive mode (enter your own facts and rules)
- `2` → Demo mode (runs the sample input from the problem statement)

### Web Interface

https://saffhrin.github.io/AI_ProblemSolving1_RA2411026050224/

---

## Sample Input & Output

### Input Facts
```
Policy is active               = TRUE
Documents are valid            = TRUE
Accident is Reported           = TRUE
Premium has been Paid          = FALSE
Fraud Detected                 = FALSE
```

### Rules
```
IF Policy is active  AND Documents are valid THEN Approve the Claim
IF Accident is Reported AND NOT Fraud Detected THEN Accident is Valid
IF  Accident is Valid AND Approve the Claim THEN Final Approval Granted
IF Fraud Detected THEN Reject the Claim
IF NOT Premium has been Paid THEN Reject the Claim
IF NOT Policy is active THEN Reject the Claim
```

### Output
```
[INPUT FACTS]
Policy is active               = TRUE
Documents are valid            = TRUE
Accident is Reported           = TRUE
Premium has been Paid          = FALSE
Fraud Detected                 = FALSE

[INFERENCE TRACE]
  [FIRED] Rule 1: Policy is active AND Documents are valid  → Approve the Claim
  [FIRED] Rule 2: Accident is Reported AND NOT Fraud Detected → Accident is Valid 
  [FIRED] Rule 3: Accident is Valid  AND Approve the Claim →  Final Approval Granted
  [FIRED] Rule 5: NOT Premium has been Paid  → Reject the Claim

==============================
  DECISION: CLAIM REJECTED
==============================
```

> reject_claim fires because premium was not paid — rejection takes precedence.

---

## Technologies Used

| Component | Technology |
|-----------|------------|
| Core logic | Python 3.x |
| Web UI | HTML + CSS + Vanilla JavaScript |
| Inference method | Forward Chaining (Propositional Logic) |
| Rule syntax | `IF cond1 AND NOT cond2 THEN outcome` |

---

## Key Design Decisions

- **Forward chaining** was chosen because we start from known facts and derive conclusions — the natural direction for claim evaluation
- **NOT support** enables rules like `IF NOT fraud_detected THEN ...` for nuanced logic
- **Chained inference** allows multi-step reasoning (e.g., `accident_valid` triggers `final_approve`)
- **Reject priority**: if `reject_claim` is derived at any point, the claim is rejected

---

## Author
- **Contributed by:** X.P.Saffhrin , RA2411026050224
- **Repository:** AI_ProblemSolving1_RA2411026050224
- **Problem:** Rule-Based Insurance Claim Decision System
- **Method:** Propositional Logic — Rule-Based Inference (Forward Chaining)
