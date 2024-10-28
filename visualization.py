import matplotlib.pyplot as plt
import seaborn as sns
import folium

sns.set(style="whitegrid")

def plot_price_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Price'], bins=50, kde=True)
    plt.title("Distribution of Property Prices")
    plt.xlabel("Price (Euros)")
    plt.ylabel("Frequency")
    plt.show()

def plot_property_type_counts(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, y='Type', order=df['Type'].value_counts().index)
    plt.title("Count of Properties by Type")
    plt.xlabel("Count")
    plt.ylabel("Property Type")
    plt.show()

def plot_price_vs_area(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='UsableArea', y='Price', data=df, alpha=0.5)
    plt.title("Price vs. Usable Area")
    plt.xlabel("Usable Area (sqm)")
    plt.ylabel("Price (Euros)")
    plt.show()

def plot_district_prices(df):
    district_prices = df.groupby('District')['PricePerSqMeter'].median().sort_values()
    plt.figure(figsize=(12, 8))
    district_prices.plot(kind='barh')
    plt.title("Median Price per Square Meter by District")
    plt.xlabel("Median Price per Square Meter (Euros)")
    plt.ylabel("District")
    plt.show()

def plot_correlation_heatmap(df):
    corr_matrix = df[['Price', 'UsableArea', 'LivingArea', 'LotSize', 'BuiltArea', 'Age', 'PricePerSqMeter']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", square=True)
    plt.title("Correlation Heatmap of Numerical Features")
    plt.show()

def plot_pairplot(df):
    sns.pairplot(df[['Price', 'UsableArea', 'LivingArea', 'LotSize', 'BuiltArea', 'PricePerSqMeter']])
    plt.suptitle("Pairplot of Key Numerical Features", y=1.02)
    plt.show()

def create_interactive_map(df, save_path):
    map_data = df.dropna(subset=['Latitude', 'Longitude'])
    portugal_map = folium.Map(location=[39.5, -8], zoom_start=6)
    for _, row in map_data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['Type']}: €{row['Price']}"
        ).add_to(portugal_map)
    portugal_map.save(save_path)

