from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Usamos DiscreteBayesianNetwork en lugar de BayesianNetwork
model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Test')
])

cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=2,
    values=[[0.1], [0.9]]
)

cpd_fever = TabularCPD(
    variable='Fever',
    variable_card=2,
    values=[[0.8, 0.2], [0.2, 0.8]],
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_test = TabularCPD(
    variable='Test',
    variable_card=2,
    values=[[0.9, 0.1], [0.1, 0.9]],
    evidence=['Disease'],
    evidence_card=[2]
)

model.add_cpds(cpd_disease, cpd_fever, cpd_test)
inference = VariableElimination(model)

# --- PRUEBAS DE INFERENCIA ---

# 1. Probabilidad de Enfermedad si sabemos que el paciente TIENE fiebre (Fever = 1)
print("--- Probabilidad de Enfermedad dado que hay Fiebre ---")
resultado_fiebre = inference.query(variables=['Disease'], evidence={'Fever': 1})
print(resultado_fiebre)

# 2. Probabilidad de Enfermedad si sabemos que la prueba salió POSITIVA (Test = 1)
print("\n--- Probabilidad de Enfermedad dado que el Test es Positivo ---")
resultado_test = inference.query(variables=['Disease'], evidence={'Test': 1})
print(resultado_test)