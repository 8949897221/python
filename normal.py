# def normalize(data):
#     min_val = min(data)
#     max_val = max(data)
#     range_val = max_val - min_val
#     return [(x - min_val) / range_val for x in data]

# if __name__ == "__main__":
#     sample_data = [10, 20, 30, 40, 50]
#     normalized_data = normalize(sample_data)
#     print("Normalized Data:", normalized_data)


    #data types
a=int(input("Enter your age: "))
if(a<13):
    print("You are a child")
elif(a>=13 and a<=19):
    print("You are a teenager")
elif(a>=20 and a<=59):
    print("You are an adult")
else:
    print("You are a senior citizen")