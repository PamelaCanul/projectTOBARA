#Function that receives a string and returns a truth table with the minterms of the expression.

def getTable (eq): 
    boolean=[0, 1]
    terms=2
    if terms==2:
        print('A\tB')
        print('-'*13)
        for A in boolean:
            for B in boolean:
                if ('-A-B' in expresion or '-AB' in expresion or 'A-B' in expresion or 'AB' in expresion or'-A' in expresion or 'A' in expresion or '-B' in expresion or 'B' in expresion):
                    x=1
                    print(A, B, x,sep='\t')
                else :   
                    x=0 
                    print(A, B, x,sep='\t')          
    elif terms==3:
        print('A\tB\tC')
        print('-'*18)
        for A in boolean:
            for B in boolean:
               for C in boolean:
                    if ('-A-B-C' in expresion or '-A-BC' in expresion or '-AB-C' in expresion or '-ABC' in expresion or 'A-B-C' in expresion or 'A-BC' in expresion or 'AB-C' in expresion or 'ABC' in expresion or '-A' in expresion or 'A' in expresion or '-B' in expresion or 'B' in expresion or 'C' in expresion or '-C' or '-A-B' in expresion or '-A-C' in expresion or '-AC' in expresion or '-B-C' in expresion or '-AC' in expresion or '-BC' in expresion or 'B-C' in expresion or 'BC' in expresion or 'AC' in expresion or 'AB' in expresion):
                        x=1
                        print(A, B, C, x,sep='\t')
                    else :   
                        x=0 
                        print(A, B, C, x,sep='\t')
    elif terms==4:
        print('A\tB\tC\tD')
        print('-'*26)
        for A in boolean:
           for B in boolean:
               for C in boolean:
                   for D in boolean:
                        if ('-A-B-C-D' in expresion or '-A-B-D' in expresion or '-A-B-C' in expresion or '-B-C-D' in expresion or '-A-BC' in expresion or '-A-C-D' in expresion or '-A-BC' in expresion or '-A-B' in expresion or '-A-C' in expresion or '-A-D' in expresion or '-B-C' in expresion or '-B-D' in expresion or '-C-D' in expresion or '-A-CD' in expresion or '-B-CD' in expresion or '-AD' in expresion or '-BD' in expresion or '-CD' in expresion or '-A-BC' in expresion or '-BC-D' in expresion or '-AC-D' in expresion or '-AC' in expresion or 'C-D' in expresion or '-A-BD' in expresion or '-BCD' in expresion or '-ACD' in expresion or 'CD' in expresion or '-AB-C' in expresion or 'B-C-D' in expresion or '-AB-D' in expresion or '-AB' in expresion or 'B-C' in expresion or 'B-D' in expresion or 'B-CD' in expresion or 'BD' in expresion or '-ABC' in expresion or'BC-D' in expresion or 'BC' in expresion or'BCD' in expresion or 'A-B-C' in expresion or'A-C-D' in expresion or'A-B-D' in expresion or 'A-B' in expresion or 'A-C' in expresion or 'A-D' in expresion or 'A-CD' in expresion or 'A-BD' in expresion or'AD' in expresion or 'A-BC' in expresion or 'AC-D' in expresion or 'AC' in expresion or 'ACD' in expresion or'AB-C' in expresion or'AB-D' in expresion or'AB' in expresion or 'ABD' in expresion or 'ABC' in expresion or '-A' in expresion or 'A' in expresion or '-B' in expresion or 'B' in expresion or '-C' in expresion or 'C' in expresion or '-D' in expresion or 'D' in expresion):
                            x=1
                            print(A, B, C, x,sep='\t')
                        else :   
                            x=0 
                            print(A, B, C, x,sep='\t')
    elif terms==5:
        print('A\tB\tC\tD\tE')
        print('-'*26)
        for A in boolean:
           for B in boolean:
               for C in boolean:
                   for D in boolean:
                       for E in boolean:
                        if ('-A-B-C-D' in expresion or '-A-B-D' in expresion or '-A-B-C' in expresion or '-B-C-D' in expresion or '-A-BC' in expresion or '-A-C-D' in expresion or '-A-BC' in expresion or '-A-B' in expresion or '-A-C' in expresion or '-A-D' in expresion or '-B-C' in expresion or '-B-D' in expresion or '-C-D' in expresion or '-A-CD' in expresion or '-B-CD' in expresion or '-AD' in expresion or '-BD' in expresion or '-CD' in expresion or '-A-BC' in expresion or '-BC-D' in expresion or '-AC-D' in expresion or '-AC' in expresion or 'C-D' in expresion or '-A-BD' in expresion or '-BCD' in expresion or '-ACD' in expresion or 'CD' in expresion or '-AB-C' in expresion or 'B-C-D' in expresion or '-AB-D' in expresion or '-AB' in expresion or 'B-C' in expresion or 'B-D' in expresion or 'B-CD' in expresion or 'BD' in expresion or '-ABC' in expresion or'BC-D' in expresion or 'BC' in expresion or'BCD' in expresion or 'A-B-C' in expresion or'A-C-D' in expresion or'A-B-D' in expresion or 'A-B' in expresion or 'A-C' in expresion or 'A-D' in expresion or 'A-CD' in expresion or 'A-BD' in expresion or'AD' in expresion or 'A-BC' in expresion or 'AC-D' in expresion or 'AC' in expresion or 'ACD' in expresion or'AB-C' in expresion or'AB-D' in expresion or'AB' in expresion or 'ABD' in expresion or 'ABC' in expresion or '-A' in expresion or 'A' in expresion or '-B' in expresion or 'B' in expresion or '-C' in expresion or 'C' in expresion or '-D' in expresion or 'D' in expresion):
                            x=1
                            print(A, B, C, x,sep='\t')
                        else :   
                            x=0 
                            print(A, B, C, x,sep='\t')
