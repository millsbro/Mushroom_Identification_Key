####Tool for Mushroom Identification

import sys

###This is the "Main Question, Gilled Section"

q1=input('QUERY: Does your specimen have gills (y/n)? \n')
if q1=="y" or q1=="Y":
    print('Gilled Specimen')
    
    q2=input('QUERY: Does your MATURE specimen have pinkish, white, or yellow gills? \n'
             'AND your young specimen have a veil forming scaly rings(volva) at BASE of stalk AND/OR '\
             'leaves, flakes, or patches on the cap (y/n)? \n')
    
    if q2=="y" or q2=="Y":
        print('ID: Your Mushroom Is an Amenita')
        sys.exit()
        
    elif q2=="n" or q2=="n":
        print('No Volva or Cap Flakes/Patches')
        
        q3=input('QUERY: Are the young gills covered in a veil which forms a ring on stalk (y/n)? (If the veil is very '\
                 'thin or nonexistant, and forms no ring, respond n) \n')
        
        if q3=='y' or q3=='Y':
            print('Veiled/Collared Specimen')
            
            q4=input('QUERY:If the spores and mature gills are DIFFERENTLY COLORED, or gills are \n attached to stalk respond D \n' 
                     'If the spores and mature gills are CHOCOLATE BROWN, (young gills white or pink) and detached from stalk '\
                     'respond C\n')
            
            if q4=='c' or q4=='C':
                print('Your Mushroom is an Agaricus')
                sys.exit()
            
            elif q4=='d' or q4=='D':
                print('Colored Gills/Spores, or Attached Gills')
                
                q5=input('QUERY: If the spores are white or greenish, AND the mature gills are yellow, white,'\
                         'or greenish, respond G \n If the spores are rusty orange to black, AND mature gills are '\
                         'NOT white, respond R \n')
                
                if q5=='G' or q5=='g':
                    print('ID: Your Mushroom is a Miscellaneous Light-Spored Gilled Mushroom with a Ring')
                    sys.exit()
                    
                elif q5=='R' or q5=='r':
                    print('ID: Your Mushroom is a Miscellaneous Dark-Spored Gilled Mushroom')
                    sys.exit()
                    
                else:
                    print('ERROR: Please respond with G/g or R/r')
                    sys.exit()     
            else:
                print('ERROR: Please Respond With c/C or d/D')
                sys.exit()
        
        elif q3=='n' or q3=='N':
            print('No Veil or Collar')
            
            q4=input('QUERY: Its the Mushroom very brittle, snapping like chalk and possibly exuding milky liquid (y/n)?\n')
            
            if q4=='y' or q4=='Y':
                print('ID: Your Mushroom is a Milk Cap or Russula')
                sys.exit()
                
            elif q4=='n' or q4== 'N':
                print('No Milky Fuid Present')
                
                q5=input('QUERY:If the spores are rusty orange to cinnamon, or brown or black \n AND the Mature gills are' \
                         ' Brown, Black, or Brightly Colored, respond B \nIf the spores are white, pink, or yellowish, with' \
                         ' Pale or Brightly colored \n mature gills, respond P \n')
                
                if q5=='b' or q5=='B':
                    print('ID: Your Mushroom is a Miscellaneous Dark Spored Gilled Mushroom')
                    sys.exit()
                    
                elif q5=='p' or q5=='P':
                    print('Light-Colored Spores')
                    
                    q6=input('QUERY: Are the gills thin-edged and bladelike? (y/n)\n')
                    
                    if q6=='y' or q6=='Y':
                        print('ID: Your Mushroom is a Miscellaneous Light-Spored Gilled Mushroom')
                        sys.exit()
                        
                    elif q6=='n' or q6=='N':
                        print('ID: Your Mushroom is a Chanterelle')
                        sys.exit()
                        
                    else:
                        print('ERROR: Please respond with y/Y or n/N')
                        sys.exit()
                    
                else:
                    print('ERROR: Please respond with p/P or b/B')
        
            else:
                print('ERROR: Please Respond With y/Y or n/N')
                sys.exit()
            
        else:
            print('ERROR: Please Respond With y/Y or n/N')
            sys.exit
    
    else:
        print('ERROR: Please Respond With y/Y or n/N')
        sys.exit()
        
    
### This is "Main Question, Ungilled Section"

elif q1=="n" or q1=="N":
    print('Non-gilled Specimen')
    
    q2=input('QUERY: Is the underside of the cap lined with pores that are the mouths of closely-packed tubes? (y/n)\n')
    
    if q2=='y' or q2=='Y':
        print('Porous Cap')
        
        q3=input('QUERY:Is the specimen soft and fleshy, with a roughly centered stalk and spongy pores? (y/n)\nIf the '\
                 'specimen is Woody, Shelf-like, or has Offcenter Stalk and Tough Tube Layer, respond n \n')
        
        if q3=='y' or q3=='Y':
            print('ID: Your Mushroom is a Bolete')
            sys.exit()
            
        elif q3=='n' or q3=='N':
            print('ID: Your Mushroom is a Polypore')
            sys.exit()
            
        else:
            print('ERROR: Please respond with y/Y or n/N')
            sys.exit()
            
    
    elif q2=='n' or q2=='N':
        print('Non-Porous Cap')
        
        q3=input('QUERY: Does your specimen have downward-pointing spines or teeth (with or without a well defind cap and '\
                 'stalk) (y/n)? \n')
        
        if q3=='y' or q3=='Y':
            print('ID: Your Mushroom is in the group Teeth Fungi')
            sys.exit()
            
        elif q3=='n' or q3=='N':
            print('No Downward-Facing Spines')
            
            q4=input('QUERY: Is the cap of your specimen brain-like, saddle-shaped, thimble-like, or honeycombed with '\
                     'pits and ridges \nAND there is NOT a sack at the base of the stalk (y/n)? \n')
            
            if q4=='y' or q4=='Y':
                print('ID: Your Mushroom is a Morel or False Morel')
                sys.exit()
                
            elif q4=='n' or q4=='N':
                print('Lacks a stalk, sack, or is not shaped like a Morel')
                
                q5=input('QUERY: Is your specimen erect and club-shaped or coral-shaped (branched)with smooth to slightly '\
                         'wrinkled surfaces and WITHOUT a well-defined cap (y/n)? \n')
                
                if q5=='y' or q5=='Y':
                    print('ID: Your Mushroom is a Coral or Crab Mushroom')
                    sys.exit()
                    
                elif q5=='n' or q5=='N':
                    print('Not Club-Like or Coral-Like')
                    
                    q6=input('QUERY: Does your specimen have a spore case* with or without rays or stalk, \n'\
                             'AND grow on the ground (y/n)? \n \n * A spore case is a sac-like structure conatining spore dust when mature. \n')
                    
                    if q6=='y' or q6=='Y':
                        print('ID: Your Mushroom is a Puffball or Earthstar')
                        sys.exit()
                        
                    elif q6=='n' or q6=='N':
                        print('No Spore Case')
                        
                        q7=input('QUERY: Does your specimen have a cap and stalk that are NOT jelly-like (if it grows '\
                                 'on the ground) \n And the underside is wrinkled, veined or trumpetlike and smooth (y/n)? \n')
                        
                        if q7=='y' or q7=='Y':
                            print('ID: Your Mushroom is a Chanterelle')
                            sys.exit()
                            
                        elif q7=='n' or q7=='N':
                            print('ID: Your Mushroom is OTHER')
                            sys.exit()
                            
                        else:
                            print('ERROR: Please respond with y/Y or n/N')
                            sys.exit()
                        
                    else:
                        print('ERROR: Please respond with y/Y or n/N')
                        sys.exit()
                    
                else:
                    print('ERROR: Please respond with y/Y or n/N')
                    sys.exit()
                
            else:
                print('ERROR: Please respond with y/Y or n/N')
                sys.exit()
            
        else:
            print('ERROR: Please respond with y/Y or n/N')
            sys.exit()
                 
    else:
        print('ERROR: Please respond with y/Y or n/N')
        sys.exit()

else:
    print('ERROR: Please Respond With y/Y or n/N')
    sys.exit()

