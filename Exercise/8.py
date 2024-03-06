books=[{'title': '1984','author':'Georg Orwell','year': '1949'},
       {'title': 'To kill a Mockingbird','author':'Harper lee','year':'1960'},
       {'title': 'Brave Ne World','author':'aldous Huxley','year':'1932'}]
sorted_books=sorted(books,key=lambda x:x['year'])
titles=[book['title'] for book in sorted_books]
print("Sorted list of books based on year: ")
for book in sorted_books:
    print(f"{book['title']}by{book['author']}({book['year']})")
print("\nList of books titles: ")
for title in titles:
    print(title)