import openai
import json

openai.api_key = 'this is a key'

def get_enhanced_description(description):
    file = open("prompts/get_enhanced_description.txt", 'r', encoding='utf-8')
    prompt = file.read()
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt + " " + description,
        max_tokens=150
    )
    return response.choices[0].text.strip()
def get_key_features(description):
    file = open("prompts/get_key_features.txt", 'r', encoding='utf-8')
    prompt = file.read()
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt + " " + description,
        max_tokens=50
    )
    return response.choices[0].text.strip().split('\n')

def get_sentiment(review):
    file = open("prompts/get_sentiment.txt", 'r', encoding='utf-8')
    prompt = file.read()
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt + " " + review,
        max_tokens=50
    )
    answer = response.choices[0].text.strip().split('\n')
    # answer[0] is one word ("positive", "negative", "neutral", "mixed")
    return answer[0], answer[1:]

def process_data(product_data):
    enhanced_description = get_enhanced_description(product_data["basic_description"])
    review_sentiment, sentiment_explanation = get_sentiment(product_data['review'])

    return {
        "name": product_data["name"],
        "enhanced_description": enhanced_description,
        "key_features": get_key_features(enhanced_description),
        "review_sentiment": review_sentiment,
        "sentiment_explanation": sentiment_explanation
    }

product_data = {
    "name": "Умные часы FitLife Pro",
    "basic_description": "Умные часы с функцией отслеживания активности и уведомлениями.",
    "review": "Часы работают хорошо, но батарея разряжается слишком быстро."
}

print(process_data(product_data))