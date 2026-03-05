binfile = open('file.bin','wb+')
input = 'This is my binary input'
binfile.write(input.encode('utf-8'))
binfile.seek(0)
bin_data = binfile.read()
print("binary output:", bin_data)
decoded_output = bin_data.decode("utf-8")
print("Decoded data:",decoded_output)