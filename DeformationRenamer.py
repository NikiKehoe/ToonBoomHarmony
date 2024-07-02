from ToonBoom import harmony  
  
session = harmony.session()  
project = session.project  
scene = project.scene  
nodes = scene.top.nodes  
  
  
def rename_group(group):  
    for node in group.nodes:  
        if node.type.upper() == "GROUP":  
            if node.name.startswith("Deformation-"):  
                if not node.name.endswith("-DEF"):  
                    new_def_name = node.name[12:] + "-DEF"  
                    node.name = new_def_name  
                    print(f"Renamed group '{new_def_name}'")  
            rename_group(node)  
  
rename_group(scene.top)  
  
print("\nGroups renamed")
