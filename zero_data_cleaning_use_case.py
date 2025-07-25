import pandas as pd
import  matplotlib.pyplot as plt

df = pd.read_csv('MenuPage.csv')

df['full_height'] = pd.to_numeric(df['full_height'], errors='coerce')
df['full_width']  = pd.to_numeric(df['full_width'],  errors='coerce')
df = df.dropna(subset=['full_height', 'full_width'])

df['area'] = (df['full_height'] / 400) * (df['full_width'] / 400)

plt.hist(df['area'], bins=100)
plt.title('Distribution of Menu Page Areas')
plt.xlabel('Area (inches squared)* \n *assuming a DPI of 400 was used by the scanner ')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()