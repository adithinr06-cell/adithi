import pandas as pd

data = {
    "Name": ["Aditi", "Rahul", "Sneha", "Kiran", "Arjun"],
    "USN": ["1AA01", "1AA02", "1AA03", "1AA04", "1AA05"],
    "Marks": [85, 78, 92, 74, 88]
}

df = pd.DataFrame(data)

df.to_excel("students.xlsx", index=False)

print("Excel file created successfully!")