from ToonBoom import harmony

sess = harmony.session()
proj = sess.project
elems = proj.elements

for elem in elems:
    try:
        print("Element Name: %s" % (elem.name))
        drawing_list = elem.drawings
        print(" Contains %s Drawings: " % (len(drawing_list)))

        # Check if "Zzz_Blank" already exists
        blank_exists = False
        for drawing in drawing_list:
            if drawing.name == "Zzz_Blank":
                blank_exists = True
                break

        if not blank_exists:
            # Create "Zzz_Blank" drawing if it doesn't exist
            new_drawing = drawing_list.create("Zzz_Blank", False, True)
            print("New Drawing Created: %s" % (new_drawing.name))
        else:
            print("\"Zzz_Blank\" already exists in this element.")
    except Exception as e:
    
        print(f"Error processing element {elem.name}: {e}")
