

stored_content=[]

with open("messages.pot","r") as f:
    for i in f.readlines():
        if i.startswith("msgid") or i.startswith("msgstr"):
            stored_content.append(i)

start=0
end=80

for file_count in range(1,(len(stored_content)//80)+1):
    clean_stord_content=''''''

    for i in stored_content[start:end]:
        if "msgstr" in i:
            clean_stord_content+=(i+"\n")
        else:
            clean_stord_content+=i


    file_name = f"file_{file_count}.txt"
    with open(f'massages/{file_name}', 'w') as file:
        file.write(clean_stord_content)

    print(f"Content written to {file_name} successfully.")
    
    start = end
    end += 80