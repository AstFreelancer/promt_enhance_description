## Проект по разработке системы улучшения описаний товаров и анализа тональности

**Стек:** Python, OpenAI API

На входе product_data в формате JSON. Эти данные проходят через три функции:
- get_enhanced_description() - используя промпт [get_enhanced_description.txt](prompts/get_enhanced_description.txt), получает от ChatGPT расширенное описание товара;
- get_key_features() - используя промпт [prompts/get_key_features.txt](prompts/get_key_features.txt), получает от ChatGPT список ключевых признаков товара;
- get_sentiment() - используя промпт [prompts/get_sentiment.txt](prompts/get_sentiment.txt), получает от ChatGPT оценку тональности отзыва ("positive", "negative", "neutral", "mixed").

Все полученное собирается в JSON с полями:
- name;
- enhanced_description;
- key_features;
- review_sentiment;
- sentiment_explanation.

Подробности здесь: https://docs.google.com/document/d/1bQ11ikXvDnAgsjz5Khu_gjBCGJkVMNLPx9DaCdu8r7I/edit?usp=sharing
