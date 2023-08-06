def resolve(clause1, clause2):
    """
    Performs resolution on two clauses.
    """
    resolvents = set()
    for literal1 in clause1:
        for literal2 in clause2:
            if literal1[1:] == literal2[1:] or literal1[0] != literal2[0]:
                continue
            resolvent = clause1.union(clause2) - {literal1, literal2}
            if not resolvent:
                return None
            resolvents.add(frozenset(resolvent))
    return resolvents

