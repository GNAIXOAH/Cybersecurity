string = 'wxqvn$Zae${deyZv$d"i'
binary_converted = "" .join(format(c, 'b')for c in bytearray(string, "utf-8"))
print(binary_converted)
i = 0
output = ""
for i in range(1, len(binary_converted), 2):
    output += "".join(binary_converted[i - 1])
    if eval(binary_converted[i - 1]) == 1 and eval(binary_converted[i]) == 1:
        output += str(0)
    else:
        output += str(1)
u = "".join([chr(int(x,2)) for x in [output[i:i+8]
                           for i in range(0,len(output), 8)
                           ]
            ])
print(u.decode("utf-8"))