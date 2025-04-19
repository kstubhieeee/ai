from sympy.logic.boolalg import And, Or, Not, Implies
from sympy import symbols

# Define propositional variables
human_socrates = symbols('HumanSocrates')
mortal_socrates = symbols('MortalSocrates')

# Define the premise: If Socrates is human, then Socrates is mortal
premise = Implies(human_socrates, mortal_socrates)

# Fact: Socrates is human
fact = human_socrates

# Conclusion we want to prove: Socrates is mortal
conclusion = mortal_socrates

print("Premise:", premise)
print("Fact:", fact)
print("Conclusion (Mortal Socrates):", conclusion)

print("\nIs conclusion logically entailed?")
# Create knowledge base with premise and fact
knowledge_base = And(premise, fact)

# Check if the negation of the conclusion with the knowledge base is satisfiable
# If it's not satisfiable, then the conclusion is valid
from sympy.logic.inference import satisfiable
result = satisfiable(And(knowledge_base, Not(conclusion)))

if result == False:
    print("Yes, Socrates is mortal (Valid by propositional logic).")
else:
    print("Could not prove conclusively.")
