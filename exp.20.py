from typing import Dict, List
from copy import deepcopy

class CSP:
    def __init__(self, variables: List[str], domains: Dict[str, List[str]], constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def solve(self):
        assignments = {}
        return self.backtrack(assignments)

    def backtrack(self, assignments):
        if len(assignments) == len(self.variables):
            return assignments

        var = self.select_unassigned_variable(assignments)

        for value in self.order_domain_values(var, assignments):
            new_assignments = deepcopy(assignments)
            new_assignments[var] = value

            if self.is_consistent(new_assignments):
                result = self.backtrack(new_assignments)
                if result is not None:
                    return result

        return None

    def select_unassigned_variable(self, assignments):
        for var in self.variables:
            if var not in assignments:
                return var

    def order_domain_values(self, var, assignments):
        values = self.domains[var]
        return sorted(values, key=lambda value: self.get_num_conflicts(var, value, assignments))

    def get_num_conflicts(self, var, value, assignments):
        conflicts = 0
        for constraint in self.constraints:
            if var in constraint and len(constraint) == 2:
                other_var = constraint[0] if constraint[1] == var else constraint[1]
                if other_var in assignments and assignments[other_var] == value:
                    conflicts += 1
        return conflicts

    def is_consistent(self, assignments):
        for constraint in self.constraints:
            if all(var in assignments for var in constraint):
                if not self.satisfies_constraint(assignments, constraint):
                    return False
        return True

    def satisfies_constraint(self, assignments, constraint):
        if len(constraint) == 2:
            val1 = assignments[constraint[0]]
            val2 = assignments[constraint[1]]
            return val1 != val2
        else:
            return True


def map_coloring():
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

    domains = {
        'WA': ['r', 'g', 'b'],
        'NT': ['r', 'g', 'b'],
        'SA': ['r', 'g', 'b'],
        'Q': ['r', 'g', 'b'],
        'NSW': ['r', 'g', 'b'],
        'V': ['r', 'g', 'b'],
        'T': ['r', 'g', 'b']
    }

    constraints = [
        ('WA', 'NT'),
        ('WA', 'SA'),
        ('NT', 'SA'),
        ('NT', 'Q'),
        ('SA', 'Q'),
        ('SA', 'NSW'),
        ('SA', 'V'),
        ('Q', 'NSW'),
        ('NSW', 'V')
    ]

    csp = CSP(variables, domains, constraints)
    result = csp.solve()

    if result is not None:
        print(result)
    else:
        print("No solution found")
map_coloring()
