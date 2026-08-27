class Person: 
    def __init__(self, name): 
        self.name = name        
        self.father = None      
        self.mother = None      
        self.children = []      
 
def set_father(child, father): 
    child.father = father 
    father.children.append(child)  

def set_mother(child, mother):  
    child.mother = mother 
    mother.children.append(child) 
 
adam = Person("Adam") 
sara = Person("Sara") 
laila = Person("Laila") 
ali = Person("Ali") 
omar = Person("Omar") 
nour = Person("Nour") 
hana = Person("Hana") 
 
# Connecting the first generation to the second
set_father(ali, adam); set_mother(ali, sara) 
set_father(laila, adam); set_mother(laila, nour) 
set_father(omar, adam); set_mother(omar, hana) 

youssef = Person("Youssef") 
mona = Person("Mona") 
dina = Person("Dina") 
#  link up Youssef and Mona with their parents
set_father(youssef, ali); set_mother(youssef, dina) 
set_father(mona, ali); set_mother(mona, dina) 

hassan = Person("Hassan") 
karim = Person("Karim") 
nada = Person("Nada") 
# link up karim and nada with their parents
set_father(karim, hassan); set_mother(karim, laila) 
set_father(nada, hassan); set_mother(nada, laila) 

lina = Person("Lina") 
tarek = Person("Tarek") 
reem = Person("Reem") 
# link up tarek and reem with their parents
set_father(tarek, omar); set_mother(tarek, lina) 
set_father(reem, omar); set_mother(reem, lina) 

maha = Person("Maha") 
amr = Person("Amr") 
farah = Person("Farah") 
# link up amr and farah with their parents
set_father(amr, youssef); set_mother(amr, maha) 
set_father(farah, youssef); set_mother(farah, maha) 

khaled = Person("Khaled") 
ziad = Person("Ziad") 
sahar = Person("Sahar") 
# link up ziad and sahar with their parents
set_father(ziad, khaled); set_mother(ziad, mona) 
set_father(sahar, khaled); set_mother(sahar, mona) 

mohammed = Person("Mohammed")
mariam = Person("Mariam")
hoda = Person("Hoda")
# link up mohammed and mariam with their parents
set_father(mohammed, karim); set_mother(mohammed, hoda)
set_father(mariam, karim); set_mother(mariam, hoda)

ahmed = Person("Ahmed")
hany = Person("Hany")
islam = Person("Islam")
# link up ahmed and hany with their parents
set_father(ahmed, islam); set_mother(ahmed, nada)
set_father(hany, islam); set_mother(hany, nada)

nesma = Person("Nesma")
rana = Person("Rana")
shahd = Person("Shahd")
# link up nesma and rana with their parents
set_father(nesma, tarek); set_mother(nesma, shahd)
set_father(rana, tarek); set_mother(rana, shahd)

yassin =Person("Yassin")
layan =Person("Layan")
samy =Person("Samy")
# link up yassin and layan with their parents
set_father(yassin, samy); set_mother(yassin, reem)
set_father(layan, samy); set_mother(layan, reem)


# *********** DFS ALGORITHM ***********

#Ancestors_Method
def get_ancestors(person):
    ancestors = []
    visited = set()

    def dfs(p):
        if p is None or p in visited:
            return
        visited.add(p)

        if p.father:
            ancestors.append(p.father.name)
            dfs(p.father)

        if p.mother:
            ancestors.append(p.mother.name)
            dfs(p.mother)

    dfs(person)

    seen = set()
    result = []
    for name in ancestors:
        if name not in seen:
            seen.add(name)
            result.append(name)

    return result
 
# Descendants_Method
def get_descendants(person): 
    descendants = [] 
    def dfs(p): 
        for child in p.children: 
            descendants.append(child.name) 
            dfs(child) 
    dfs(person) 
    return descendants 
 
# Generation_Depth_Method
def get_generation_depth(person):
    if person.father is None and person.mother is None:
        return 0
    
    depth_father = get_generation_depth(person.father) if person.father else 0
    depth_mother = get_generation_depth(person.mother) if person.mother else 0
    
    return 1 + max(depth_father, depth_mother)
 
# Sibling_Method
def get_siblings(person):
    siblings = set()
    parents = [p for p in [person.father, person.mother] if p]
    for parent in parents:
        for child in parent.children:
            if child != person:
                siblings.add(child.name)
    return list(siblings)

def get_sibling_count(person):
    return len(get_siblings(person))

# LCA_Method

def get_lca(p1, p2):

    def get_ancestors_with_depth(p):
        anc = {p: 0} 
        stack = [(p, 0)]
        visited = set()

        while stack:
            curr, depth = stack.pop()

            if curr in visited:
                continue
            visited.add(curr)

            for parent in [curr.father, curr.mother]:
                if parent:
                    if parent not in anc or depth + 1 < anc[parent]:
                        anc[parent] = depth + 1
                    stack.append((parent, depth + 1))

        return anc

    anc1 = get_ancestors_with_depth(p1)
    anc2 = get_ancestors_with_depth(p2)
    common = set(anc1.keys()) & set(anc2.keys())

    if not common:
        return "No Common Ancestor"
    lca = min(common, key=lambda x: anc1[x] + anc2[x])
    return lca.name

#All_Family_Members
family_dict = {
    "Adam": adam, "Sara": sara, "Laila": laila, "Ali": ali, "Omar": omar,
    "Nour": nour, "Hana": hana, "Youssef": youssef, "Mona": mona, "Dina": dina,
    "Hassan": hassan, "Karim": karim, "Nada": nada, "Lina": lina, "Tarek": tarek,
    "Reem": reem, "Maha": maha, "Amr": amr, "Farah": farah, "Khaled": khaled,
    "Ziad": ziad, "Sahar": sahar,"Mohammed": mohammed,"Mariam": mariam, "Hoda": hoda,
    "Ahmed":ahmed, "Hany": hany, "Islam": islam, "Nesma": nesma, "Rana": rana,
    "Shahd": shahd, "Yassin": yassin, "Layan": layan, "Samy": samy
}

#Family_Tree_Map
def display_tree():
    print("\n" + "#"*50)
    print("                 FAMILY TREE MAP")
    print("#"*50)
    print("Adam (Root)")
    print("├── Ali (Father: Adam, Mother: Sara)") 
    print("│   ├── Youssef (Father: Ali, Mother: Dina)")
    print("│   │   ├── Amr (Father: Youssef, Mother: Maha)")
    print("│   │   │")
    print("│   │   └── Farah (Father: Youssef, Mother: Maha)")
    print("│   │")
    print("│   └── Mona (Father: Ali, Mother: Dina)")
    print("│       ├── Ziad (Father: Khaled, Mother: Mona)")
    print("│       │")
    print("│       └── Sahar (Father: Khaled, Mother: Mona)")
    print("│")
    print("├── Laila (Father: Adam, Mother: Nour)")
    print("│   ├── Karim (Father: Hassan, Mother: Laila)")
    print("│   │   ├── Mohammed (Father: Karim, Mother: Hoda)")
    print("│   │   │")
    print("│   │   └── Mariam (Father: Karim, Mother: Hoda)")
    print("│   │")
    print("│   └── Nada (Father: Hassan, Mother: Laila)")
    print("│       ├── Ahmed (Father: Islam, Mother: Nada)")
    print("│       │")
    print("│       └── Hany (Father: Islam, Mother: Nada)")
    print("│")
    print("└── Omar (Father: Adam, Mother: Hana)")
    print("    ├── Tarek (Father: Omar, Mother: Lina)")
    print("    │   ├── Nesma (Father: Tarek, Mother: Shahd)")
    print("    │   │")
    print("    │   └── Rana (Father: Tarek, Mother: Shahd)")
    print("    │")
    print("    └── Reem (Father: Omar, Mother: Lina)")
    print("        ├── Yassin (Father: Samy, Mother: Reem)")
    print("        │")
    print("        └── Layan (Father: Samy, Mother: Reem)")
    print("#"*50)

# Main_Program
def main_program():
    print("\n" + "="*50)
    print("--- Family Genealogy Tree Analyzer [DFS] ---")
    print("="*50)    

    while True:
        print("\nAvailable Queries:")
        print("0. Show Family Tree Map")
        print("1. list of ancestors")
        print("2. list of descendants")
        print("3. Lowest Common Ancestor (LCA)")
        print("4. Total sibling count")
        print("5. Generation depth")
        print("6. Exit")

        choice = input("\nSelect a query (0-6): ").strip()

        if choice not in ['0','1','2','3','4','5','6'] :
            print("Invalid selection. Please try again.")
            continue

        if choice == '0':
            display_tree()
            continue
        
        if choice == '6':
            print("Exiting program. Good luck!")
            break

        target_name = input("Enter member name: ").strip().capitalize()

        if target_name not in family_dict:
            print(f"Error: Member '{target_name}' not found in the family tree.")
            continue

        person_obj = family_dict[target_name]

        if choice == '1':
            result = get_ancestors(person_obj)
            print(f"Ancestors of \'{target_name}\': {result}")

        elif choice == '2':
            result = get_descendants(person_obj)
            print(f"Descendants of \'{target_name}\': {result}")

        elif choice == '3':
            other_name = input("Enter the other member's name ").strip().capitalize()
            if other_name in family_dict:
                other_obj = family_dict[other_name]
                result = get_lca(person_obj, other_obj)
                print(f"LCA of \'{target_name}\' and \'{other_name}\' is: {result}")
            else:
                print("Error: Second member name not found.")

        elif choice == '4':
            result = get_sibling_count(person_obj)
            print(f"Total siblings of \'{target_name}\': {result}")

        elif choice == '5':
            result = get_generation_depth(person_obj)
            print(f"Generation depth of \'{target_name}\' is: {result} (Root=0)")

        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main_program()
