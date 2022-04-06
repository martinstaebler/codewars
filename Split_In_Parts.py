# https://www.codewars.com/kata/5650ab06d11d675371000003/train/python

def split_in_parts(s, part_length): 
    return " ".join(s[i:i+part_length] for i in range(0, len(s), part_length))

print(split_in_parts("supercalifragilisticexpialidocious", 3))#, "sup erc ali fra gil ist ice xpi ali doc iou s")
print(split_in_parts("HelloKata", 1))#, "H e l l o K a t a")
print(split_in_parts("HelloKata", 9))#, "HelloKata")


