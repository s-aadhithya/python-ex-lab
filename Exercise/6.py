def title_case(sentence):
    common_terms={"and","the","in","a"}
    terms=sentence.split()
    n_sentence=' '.join([word.capitalize() if word.lower() not in common_terms or sm==0 else word.lower() for sm, word in enumerate(terms)])
    return n_sentence
m_s="i want a proper cup of coffee in a proper coffee pot"
result=title_case(m_s)
print(result)
