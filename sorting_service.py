#sorting service: 

# errors and exceptions have not yet been processed

from operator import itemgetter

books = []
while True:
	newtitle = input("Vai adicionar um novo título?s/n \n ")
	if newtitle == "n":
		print("tudo bem \n")
		break
	else:
		newtitle == "s"

		books.append(
		{
		'Title':(input)("Adicione um novo título: ",),
		'Author':(input)("Qual o autor desse livro? "),
		'EditionYear':(input)("qual o ano de publicação? " )
		}
		)
#exception: ("digite novamente")
valid_fields = ['Title','Author','EditionYear']


while True:
	organize = input("Adicionar critério de organização?(s/n)")
	if organize == "n":
		break
	else:
		sorting = input("Escolha a alternativa:\n Gostaria de organizar os livros por título(a), autor(b) ou ano de publicação(c)?")
		if sorting == "a":
			direction = input("ordem ascendente(a) ou decrescente?(b)")
			if direction == "a":
				books = sorted(books, key = itemgetter("Title"))
			elif direction == "b":
				books = sorted(books, key = itemgetter("Title"), reverse = True)
			else:
				print("digite novamente a ou b")
		elif sorting == "b":
			direction = input("ordem ascendente(a) ou decrescente?(b)")
			if direction == "a":
				books = sorted(books, key = itemgetter("Author"))
			elif direction == "b":
				books = sorted(books, key = itemgetter("Author"), reverse = True)
			else:
				print("digite novamente")
		elif sorting == "c":
			direction = input("ordem ascendente(a) ou decrescente?(b)")
			if direction == "a":
				books = sorted(books, key = itemgetter("EditionYear"))
			elif direction == "b":
				books = sorted(books, key = itemgetter("EditionYear"), reverse = True)
			else:
				print("digite novamente a ou b")
		else:
				print("digite novamente, alternativa a, b ou c")
	
print(books)







