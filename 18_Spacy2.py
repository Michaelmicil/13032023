import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp ("Microsoft is making artificial intelligence one of its top priorities.During its fiscal third-quarter earnings call, CEO Satya Nadella explained that “investing in the new AI wave” would remain a key focus for the software giant.Microsoft announced in January a multibillion-dollar investment in OpenAI, the artificial intelligence lab that created ChatGPT. Since then, Microsoft has begun to incorporate AI technology, dubbed “Copilot,” into some of its well-known products including Word, PowerPoint and Excel.The company expects AI will help drive revenue growth over time because it will improve its product offerings.Fiscal third-quarter revenue grew 7% to $52.86 billion, beating analysts’ prediction of $51.02 billion, according to Refinitiv consensus estimates. Additionally, Microsoft reported earnings per share of $2.45, which surpassed the $2.23 analysts expected.")

for ent in doc.ents :
    print (ent.text, ent.start_char, ent.end_char, ent.label_)
