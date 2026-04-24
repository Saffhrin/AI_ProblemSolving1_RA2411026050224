# Rule-Based Insurance Claim Decision System

## Problem Description

An insurance company needs an automated system to evaluate whether a claim should be **Approved** or **Rejected** based on predefined logical rules.

The system uses **Propositional Logic** with the following claim details:

- Is the Policy Active?
- Are the Documents Valid?
- Has the Accident been Reported?
- Has the Premium been Paid?
- Was any Fraud Detected?

---

## Algorithm Used

### Rule-Based Inference — Forward Chaining (Propositional Logic)

The system uses **forward chaining**, a data-driven inference method:

1. A **Knowledge Base** is initialized with the user-provided claim facts
2. **Rules** in the form `IF condition THEN outcome` are evaluated
3. The engine loops through all rules until no new facts can be derived
4. Rules support **AND** conditions and **NOT** (negation)
5. Derived facts can trigger further rules (chained reasoning)
6. A **final decision** is produced — Approved or Rejected

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

### Run the Python Program

```bash
# Clone the repository
git clone https://github.com/yourusername/AI_ProblemSolving_
cd AI_ProblemSolving_/insurance_claim

# Run the program
python insurance_claim_system.py
```

Select a mode when prompted:

| Mode | Description |
|------|-------------|
| 1 | Interactive — Enter your own facts and rules |
| 2 | Demo — Runs the built-in sample claim |
| 3 | Batch — Compares multiple scenarios at once |
| 4 | Exit |

### Run the Web Interface

Open `index.html` in any browser — no installation needed.

Or visit the live site:

https://saffhrin.github.io/AI_ProblemSolving1_RA2411026050224/

---

## Sample Input & Output

### Claim Facts Provided

| Fact | Value |
|------|-------|
| Policy is Active | Yes |
| Documents are Valid | Yes |
| Accident is Reported | Yes |
| Premium has been Paid | No |
| Fraud Detected | No |

### Rules Applied

| Rule | Description |
|------|-------------|
| Rule 1 | IF Policy is Active AND Documents are Valid → Approve the Claim |
| Rule 2 | IF Accident is Reported AND NOT Fraud Detected → Accident is Valid |
| Rule 3 | IF Accident is Valid AND Approve the Claim → Final Approval Granted |
| Rule 4 | IF Fraud Detected → Reject the Claim |
| Rule 5 | IF NOT Premium has been Paid → Reject the Claim |
| Rule 6 | IF NOT Policy is Active → Reject the Claim |

### Output

```
─────────────────────────────────────────────────────────────────
  EVALUATION REPORT
─────────────────────────────────────────────────────────────────

INPUT FACTS:
  Policy is Active                     =  YES / TRUE
  Documents are Valid                  =  YES / TRUE
  Accident is Reported                 =  YES / TRUE
  Premium has been Paid                =  NO  / FALSE
  Fraud Detected                       =  NO  / FALSE

INFERENCE TRACE (How Decision Was Made):
  ✔ Rule 1 fired: Policy is Active AND Documents are Valid
                  → Approve the Claim = TRUE
  ✔ Rule 2 fired: Accident is Reported AND NOT Fraud Detected
                  → Accident is Valid = TRUE
  ✔ Rule 3 fired: Accident is Valid AND Approve the Claim
                  → Final Approval Granted = TRUE
  ✔ Rule 5 fired: NOT Premium has been Paid
                  → Reject the Claim = TRUE

═══════════════════════════════════════════════════════════════════
  FINAL DECISION :  ✘  CLAIM REJECTED
  One or more rejection conditions were triggered.
═══════════════════════════════════════════════════════════════════
```

> **Note:** Even though approval conditions were met, the claim is **rejected** because the premium was not paid. Rejection always takes priority.

---

## Web Interface Features

- Toggle each fact as **Yes** or **No** with a single click
- Add or remove facts and rules dynamically
- Rules displayed in plain English (not code)
- Dropdown menus to build new rules — no typing needed
- Live inference trace showing exactly how the decision was reached
- Derived facts shown separately from input facts

---

## Technologies Used

| Component | Technology |
|-----------|------------|
| Core Logic | Python 3.x |
| Web Interface | HTML + CSS + JavaScript |
| Inference Method | Forward Chaining (Propositional Logic) |
| Rule Format | IF condition AND NOT condition THEN outcome |

---

## Key Design Decisions

- **Forward chaining** was chosen because the system starts from known facts and derives conclusions — the natural direction for claim evaluation
- **NOT support** allows rules like "If premium is NOT paid → Reject" for nuanced logic
- **Chained inference** enables multi-step reasoning — derived facts trigger further rules
- **Rejection takes priority** — if any rejection condition is triggered, the claim is rejected regardless of approval conditions
- **Human-readable UI** — all facts and rules are shown in plain English, not code

---

## Batch Mode — Scenario Comparison

| Scenario | Policy Active | Documents Valid | Premium Paid | Fraud Detected | Decision |
|----------|:---:|:---:|:---:|:---:|:---:|
| Full Approval | ✔ | ✔ | ✔ | ✘ | ✔ Approved |
| Fraud Detected | ✔ | ✔ | ✔ | ✔ | ✘ Rejected |
| Premium Not Paid | ✔ | ✔ | ✘ | ✘ | ✘ Rejected |
| Policy Inactive | ✘ | ✔ | ✔ | ✘ | ✘ Rejected |

---

## Author
- **Contributed by:** X.P.Saffhrin , RA2411026050224
- **Repository:** AI_ProblemSolving_
- **Problem:** Rule-Based Insurance Claim Decision System
- **Method:** Propositional Logic — Rule-Based Inference (Forward Chaining)
