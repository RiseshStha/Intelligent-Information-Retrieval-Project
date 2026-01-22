import pandas as pd
import os
import random

# Define categories
categories = ['Business', 'Entertainment', 'Health']

# Sample data generation
data = []

# Business samples
business_templates = [
    "Stocks for {company} rose by {percent}% today following positive earnings.",
    "The central bank announced a new policy to combat inflation.",
    "Market analysts predict a bullish trend for the {sector} sector.",
    "Global trade deficit widens as exports slow down.",
    "New merger announced between {company} and {company_2}.",
    "Economy grows at a slower pace in the third quarter.",
    "Oil prices surge amid geopolitical tensions.",
    "Tech startups are attracting record venture capital investment.",
    "Unemployment rate drops to a historic low.",
    "Housing market cools down as mortgage rates climb.",
    "{company} CEO steps down after 10 years.",
    "Cryptocurrency markets see high volatility this week.",
    "Government releases new fiscal budget for the upcoming year.",
    "gold prices remain stable despite market fluctuations.",
    "Investors are cautious ahead of the Fed meeting."
]
companies = ["TechCorp", "FinBank", "GlobalInd", "RetailGiant", "AutoMotive"]
sectors = ["technology", "finance", "energy", "healthcare", "retail"]

for _ in range(40):
    template = random.choice(business_templates)
    text = template.format(
        company=random.choice(companies),
        company_2=random.choice(companies),
        percent=random.randint(1, 15),
        sector=random.choice(sectors)
    )
    data.append({'text': text, 'category': 'Business'})

# Entertainment samples
entertainment_templates = [
    "New movie '{movie}' breaks box office records on opening weekend.",
    "{actor} wins best actor award at the annual film festival.",
    "Pop star {artist} announces a new world tour.",
    "TV series '{show}' renewed for another season.",
    "Critics praise the cinematography in the latest blockbuster.",
    "Celebrity couple announces engagement on social media.",
    "Music festival lineup reveals top headliners for this summer.",
    "Director {director} working on a sequel to the sci-fi hit.",
    "Streaming services battle for dominance with exclusive content.",
    "Theatre production of classic play receives standing ovation.",
    "Gaming convention attracts thousands of fans worldwide.",
    "New album from {artist} tops the charts.",
    "Actor {actor} to star in upcoming superhero movie.",
    "Documentary explores the life of legendary musician.",
    "Viral video challenge takes over the internet."
]
movies = ["The Last Journey", "Star Battle", "Love in Paris", "Action Hero", "Mystery Mansion"]
actors = ["Tom Hanks", "Brad Pitt", "Meryl Streep", "Leonardo DiCaprio", "Jennifer Lawrence"]
artists = ["Taylor Swift", "Beyonce", "Drake", "Adele", "Ed Sheeran"]
directors = ["Spielberg", "Nolan", "Scorsese", "Tarantino", "Cameron"]

for _ in range(40):
    template = random.choice(entertainment_templates)
    text = template.format(
        movie=random.choice(movies),
        actor=random.choice(actors),
        artist=random.choice(artists),
        show=random.choice(movies),
        director=random.choice(directors)
    )
    data.append({'text': text, 'category': 'Entertainment'})

# Health samples
health_templates = [
    "Doctors warn about a new strain of flu spreading rapidly.",
    "Study confirms the benefits of a Mediterranean diet for heart health.",
    "New vaccine shows promise in early clinical trials.",
    "Experts recommend daily exercise to reduce risk of chronic disease.",
    "Mental health awareness campaign launches nationwide.",
    "Hospitals face shortage of staff during winter surge.",
    "Researchers discover link between sleep and memory retention.",
    "Proper hydration is essential for overall well-being.",
    "Yoga and meditation help reduce stress levels.",
    "Vitamin D deficiency linked to immune system weakness.",
    "New guidelines released for blood pressure management.",
    "Global health organization declares end of emergency.",
    "Advances in gene therapy offer hope for rare diseases.",
    "Regular check-ups can detect cancer at an early stage.",
    "Nutritional supplements market sees significant growth."
]

for _ in range(40):
    text = random.choice(health_templates)
    data.append({'text': text, 'category': 'Health'})

# Shuffle and create DataFrame
df = pd.DataFrame(data)
df = df.sample(frac=1).reset_index(drop=True)

# Save to CSV
output_path = os.path.join("backend", "data", "news_dataset.csv")
df.to_csv(output_path, index=False)
print(f"Dataset generated at {output_path} with {len(df)} records.")
