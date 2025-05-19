palavras = ["python", "java", "c", "javascript", "go"]
palavras_grandes = []
palavras_pequenas = []

for palavra in palavras:
    if len(palavra) > 4:
        palavras_grandes.append(palavra)
    else:
        palavras_pequenas.append(palavra)


print("Palavras grandes:", palavras_grandes)
print("Palavras grandes:", palavras_pequenas)        