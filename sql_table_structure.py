
def sql_structure_max(variable):
    output=[]
    for len_count in variable:
        output.append(len(len_count))
    return max(output)

variable=["hari","vasanth","anandaraj","ranjith"]
ans=sql_structure_max(variable)+2

def sql_table_structure():
    print("+" + "-"*ans + "+")
    print(f"| {'NAMES' +' '*(ans-len('NAMES')-2)} |")
    print("+" + "-"*ans + "+")

    for name in variable: 
        name_len=len(name)
        print(f"| {name +' '*(ans-name_len-1)}"+"|")
    else:
        print("+"+"-"*ans+"+")

sql_table_structure()