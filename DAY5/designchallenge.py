# AI Knowledge and Logical Reasoning System

knowledge = {
    "human": ["mortal"],
    "socrates": ["human"],
    "bird": ["animal", "can_fly"],
    "penguin": ["bird", "cannot_fly"]
}

rules = [
    ("human", "mortal"),
    ("bird", "animal"),
    ("bird", "can_fly")
]


def get_facts(entity):
    """Return all known facts about an entity."""
    facts = set(knowledge.get(entity, []))
    changed = True

    while changed:
        changed = False

        for fact in list(facts):
            # Apply rules
            for condition, conclusion in rules:
                if fact == condition and conclusion not in facts:
                    facts.add(conclusion)
                    changed = True

    return facts


def reason(entity, question):
    """Check whether the AI can logically prove a statement."""
    facts = get_facts(entity)

    if question in facts:
        return True

    # Handle negative facts
    if question == "can_fly" and "cannot_fly" in facts:
        return False

    return False


# Examples
print("Socrates facts:", get_facts("socrates"))
print("Bird facts:", get_facts("bird"))
print("Penguin facts:", get_facts("penguin"))

print("\nLogical Reasoning:")

if reason("socrates", "mortal"):
    print("Socrates is mortal.")

if reason("bird", "can_fly"):
    print("A bird can fly.")

if not reason("penguin", "can_fly"):
    print("A penguin cannot fly.")
