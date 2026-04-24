"""
Rule-Based Insurance Claim Decision System
Using Propositional Logic Inference (Forward Chaining)
"""

import re


def parse_rule(rule_str):
    """Parse a rule string into conditions and outcome."""
    match = re.match(r"^IF\s+(.+?)\s+THEN\s+(.+)$", rule_str.strip(), re.IGNORECASE)
    if not match:
        return None
    cond_str, outcome = match.group(1).strip(), match.group(2).strip().lower().replace(" ", "_")
    conditions = []
    for part in re.split(r"\s+AND\s+", cond_str, flags=re.IGNORECASE):
        part = part.strip()
        negated = bool(re.match(r"^NOT\s+", part, re.IGNORECASE))
        name = re.sub(r"^NOT\s+", "", part, flags=re.IGNORECASE).strip().lower().replace(" ", "_")
        conditions.append({"name": name, "negated": negated})
    return {"conditions": conditions, "outcome": outcome}


def forward_chain(facts, rules):
    """Run forward chaining inference on the knowledge base."""
    kb = {k.lower().replace(" ", "_"): v for k, v in facts.items()}
    trace = []
    changed = True
    iterations = 0

    while changed and iterations < 20:
        changed = False
        iterations += 1
        for i, rule_str in enumerate(rules):
            parsed = parse_rule(rule_str)
            if not parsed:
                trace.append(f"  [SKIP] Rule {i+1}: could not parse — '{rule_str}'")
                continue
            if kb.get(parsed["outcome"]) is True:
                continue  # already known
            all_met = all(
                (not kb.get(c["name"], False)) if c["negated"] else kb.get(c["name"], False)
                for c in parsed["conditions"]
            )
            if all_met:
                kb[parsed["outcome"]] = True
                changed = True
                cond_summary = " AND ".join(
                    ("NOT " if c["negated"] else "") + c["name"]
                    for c in parsed["conditions"]
                )
                trace.append(f"  [FIRED] Rule {i+1}: {cond_summary} → {parsed['outcome']} = TRUE")

    return kb, trace


def get_verdict(kb):
    if kb.get("reject_claim"):
        return "CLAIM REJECTED"
    elif kb.get("final_approve") or kb.get("approve_claim"):
        return "CLAIM APPROVED"
    return "NO DECISION REACHED"


def print_divider(char="-", width=60):
    print(char * width)


def get_facts_from_user():
    print("\n" + "=" * 60)
    print("  INSURANCE CLAIM DECISION SYSTEM")
    print("  Rule-Based Propositional Logic Inference")
    print("=" * 60)
    print("\nDefault facts available:")
    defaults = [
        "policy_active", "documents_valid", "accident_reported",
        "premium_paid", "fraud_detected"
    ]
    for d in defaults:
        print(f"  • {d}")
    print("\nEnter facts (press Enter with no name to stop).")
    print("Format: fact_name [true/false]")
    print_divider()

    facts = {}
    while True:
        entry = input("Fact: ").strip()
        if not entry:
            break
        parts = entry.split()
        if len(parts) == 2:
            name = parts[0].lower().replace(" ", "_")
            value = parts[1].lower() in ("true", "yes", "1", "y")
            facts[name] = value
            print(f"  Added: {name} = {value}")
        elif len(parts) == 1:
            name = parts[0].lower().replace(" ", "_")
            val_str = input(f"  Value for '{name}' (true/false): ").strip().lower()
            facts[name] = val_str in ("true", "yes", "1", "y")
        else:
            print("  Invalid input. Use: fact_name true/false")
    return facts


def get_rules_from_user():
    print_divider()
    print("Enter inference rules (press Enter with no input to use defaults).")
    print("Format: IF cond1 AND NOT cond2 THEN outcome")
    print_divider()

    default_rules = [
        "IF policy_active AND documents_valid THEN approve_claim",
        "IF accident_reported AND NOT fraud_detected THEN accident_valid",
        "IF accident_valid AND approve_claim THEN final_approve",
        "IF fraud_detected THEN reject_claim",
        "IF NOT premium_paid THEN reject_claim",
        "IF NOT policy_active THEN reject_claim",
    ]

    user_rules = []
    while True:
        rule = input("Rule: ").strip()
        if not rule:
            break
        if parse_rule(rule):
            user_rules.append(rule)
            print(f"  Added rule {len(user_rules)}")
        else:
            print("  Could not parse rule. Check syntax: IF ... THEN ...")

    if not user_rules:
        print("\n  No rules entered — using default ruleset.")
        return default_rules
    return user_rules


def display_results(facts, rules, kb, trace):
    print("\n" + "=" * 60)
    print("  EVALUATION RESULTS")
    print("=" * 60)

    print("\n[INPUT FACTS]")
    print_divider()
    for name, value in facts.items():
        status = "TRUE " if value else "FALSE"
        print(f"  {name:<30} = {status}")

    print("\n[RULES APPLIED]")
    print_divider()
    for i, rule in enumerate(rules, 1):
        print(f"  Rule {i}: {rule}")

    print("\n[INFERENCE TRACE]")
    print_divider()
    if trace:
        for t in trace:
            print(t)
    else:
        print("  No rules fired.")

    derived = {k: v for k, v in kb.items() if v and k not in facts}
    if derived:
        print("\n[DERIVED FACTS]")
        print_divider()
        for k in derived:
            print(f"  {k} = TRUE (derived)")

    verdict = get_verdict(kb)
    print("\n" + "=" * 60)
    print(f"  DECISION: {verdict}")
    print("=" * 60 + "\n")


def demo_run():
    """Run with sample input from the problem statement."""
    print("\n[DEMO MODE — using sample input from problem statement]")
    facts = {
        "policy_active": True,
        "documents_valid": True,
        "accident_reported": True,
    }
    rules = [
        "IF policy_active AND documents_valid THEN approve_claim",
        "IF accident_reported AND NOT fraud_detected THEN accident_valid",
        "IF NOT accident_reported THEN reject_claim",
    ]
    kb, trace = forward_chain(facts, rules)
    display_results(facts, rules, kb, trace)


def main():
    print("\nMode: (1) Interactive  (2) Demo with sample input")
    choice = input("Select [1/2]: ").strip()
    if choice == "2":
        demo_run()
        return

    facts = get_facts_from_user()
    if not facts:
        print("No facts entered. Running demo instead.")
        demo_run()
        return

    rules = get_rules_from_user()
    kb, trace = forward_chain(facts, rules)
    display_results(facts, rules, kb, trace)


if __name__ == "__main__":
    main()
