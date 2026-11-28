file = open("bucket-list.txt", "w")
file.write("1. visit the Araku Valley\n")
file.write("2. Learn to slay in arts\n")
file.write("3.Code my own website\n")
file.close()
print("Bucket list saved to bucket-list.txt!")


file = open("bucket-list.txt", "r")
content = file.read()
print("\n=== My Bucket List ===")
print(content)
file.close()


file = open("bucket-list.txt", "r")
lines = file.readlines()
print(f"You have {len(lines)} items on your bucket list.")
file.close()

file = open("bucket-list.txt", "a")
file.write("4. Travel to USA\n")
file.write("5. Complete my dream project\n")
file.close()
print("\n2 more items added!")


file = open("bucket-list.txt", "r")
print("\n=== Updated Bucket List ===")
print(file.read())
file.close()