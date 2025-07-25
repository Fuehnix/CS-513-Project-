import pandas as pd
import matplotlib.pyplot as plt

def main():
    menu_page = pd.read_csv('MenuPage.csv')
    menu = pd.read_csv('Menu_cleaned_dates.csv')

    menu_page['width_in'] = menu_page['full_width'] / 400
    menu_page['height_in'] = menu_page['full_height'] / 400
    menu_page['area'] = menu_page['width_in'] * menu_page['height_in']

    df = menu_page.merge(
        menu[['id', 'date']],
        how='left',
        left_on='menu_id',
        right_on='id'
    )

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    df['year'] = df['date'].dt.year

    plt.figure(figsize=(10, 6))
    plt.scatter(df['year'], df['area'])
    plt.xlabel('Year\n*assuming a DPI of 400 was used by the scanner')
    plt.ylabel('Area (inches squared)*')
    plt.title('Menu Page Area Over Years')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
