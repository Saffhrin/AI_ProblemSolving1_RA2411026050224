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
└── insurance_claim/
    ├── insurance_claim_system.py   # Main Python program (console)
    └── index.html                  # Interactive web interface
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
policy_active      = True
documents_valid    = True
accident_reported  = True
premium_paid       = False
fraud_detected     = False
```

### Rules
```
IF policy_active AND documents_valid THEN approve_claim
IF accident_reported AND NOT fraud_detected THEN accident_valid
IF accident_valid AND approve_claim THEN final_approve
IF fraud_detected THEN reject_claim
IF NOT premium_paid THEN reject_claim
IF NOT policy_active THEN reject_claim
```

### Output
```
[INPUT FACTS]
policy_active                  = TRUE
documents_valid                = TRUE
accident_reported              = TRUE
premium_paid                   = FALSE
fraud_detected                 = FALSE

[INFERENCE TRACE]
  [FIRED] Rule 1: policy_active AND documents_valid → approve_claim = TRUE
  [FIRED] Rule 2: accident_reported AND NOT fraud_detected → accident_valid = TRUE
  [FIRED] Rule 3: accident_valid AND approve_claim → final_approve = TRUE
  [FIRED] Rule 5: NOT premium_paid → reject_claim = TRUE

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
- **Repository:** AI_ProblemSolving_RA2411026050224
- **Problem:** Rule-Based Insurance Claim Decision System
- **Method:** Propositional Logic — Rule-Based Inference (Forward Chaining)
