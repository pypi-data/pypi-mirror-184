# Some useful functions for reading/writing files 


```python
# Tested with:
# Python 3.9.13
# Windows 10

from write_read_file import write_utf8, write_bytes, read_bytes, copy_file, read_and_decode, iterread_bytes, iterread_text

import numpy as np

alldata = [
    np.array([[1, 2, 3], [54, 56, 77]]),
    [10, 12, 44, 1, "gjad", ""],
    "This is a text",
    b"this is a text",
    {1: 22, 33: "hithere"},
]
path = "f:\\test_write_file\\myfile.txt"
path2 = "f:\\test_write_file\\myfile2.txt"

for data in alldata:
    write_utf8(path, data, endofline="\n")
    print("""iterread_text""")
    for line in iterread_text(
        path, encoding="utf-8", strip_newline=True, ignore_empty_lines=True
    ):
        print(line)
    print("""iterread_bytes""")

    for chunk in iterread_bytes(path, chunksize=128):
        print(chunk)
    print("""write_bytes""")

    write_bytes(path, data=[str(x).encode() for x in data], endofline=b"\n")
    print("""iterread_bytes""")

    for chunk in iterread_bytes(path, chunksize=128):
        print(chunk)
    print("""read_and_decode""")

    bytestostring = read_and_decode(
        path, decodeformat="utf-8", on_encoding_errors="replace"
    )
    print(bytestostring)
    print("""copy_file""")

    copy_file(path, path2)
    print("""iterread_bytes""")

    for chunk in iterread_bytes(path2, chunksize=128):
        print(chunk)
    print("""read_bytes""")

    bytedata = read_bytes(path2)
    print(bytedata)

Output: 
iterread_text
1
2
3
54
56
77
iterread_bytes
b'1\r\n2\r\n3\r\n54\r\n56\r\n77\r\n'
write_bytes
iterread_bytes
b'[1 2 3]\n[54 56 77]\n'
read_and_decode
[1 2 3]
[54 56 77]
copy_file
iterread_bytes
b'[1 2 3]\n[54 56 77]\n'
read_bytes
b'[1 2 3]\n[54 56 77]\n'
iterread_text
10
12
44
1
gjad
iterread_bytes
b'10\r\n12\r\n44\r\n1\r\ngjad\r\n\r\n'
write_bytes
iterread_bytes
b'10\n12\n44\n1\ngjad\n\n'
read_and_decode
10
12
44
1
gjad
copy_file
iterread_bytes
b'10\n12\n44\n1\ngjad\n\n'
read_bytes
b'10\n12\n44\n1\ngjad\n\n'
iterread_text
This is a text
iterread_bytes
b'This is a text\r\n'
write_bytes
iterread_bytes
b'T\nh\ni\ns\n \ni\ns\n \na\n \nt\ne\nx\nt\n'
read_and_decode
T
h
i
s
 
i
s
 
a
 
t
e
x
t
copy_file
iterread_bytes
b'T\nh\ni\ns\n \ni\ns\n \na\n \nt\ne\nx\nt\n'
read_bytes
b'T\nh\ni\ns\n \ni\ns\n \na\n \nt\ne\nx\nt\n'
iterread_text
b'this is a text'
iterread_bytes
b"b'this is a text'\r\n"
write_bytes
iterread_bytes
b'116\n104\n105\n115\n32\n105\n115\n32\n97\n32\n116\n101\n120\n116\n'
read_and_decode
116
104
105
115
32
105
115
32
97
32
116
101
120
116
copy_file
iterread_bytes
b'116\n104\n105\n115\n32\n105\n115\n32\n97\n32\n116\n101\n120\n116\n'
read_bytes
b'116\n104\n105\n115\n32\n105\n115\n32\n97\n32\n116\n101\n120\n116\n'
iterread_text
22
hithere
iterread_bytes
b'22\r\nhithere\r\n'
write_bytes
iterread_bytes
b'1\n33\n'
read_and_decode
1
33
copy_file
iterread_bytes
b'1\n33\n'
read_bytes
b'1\n33\n'
	
	
```




