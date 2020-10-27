 # definir el dictionary

countryCode = { 57 : 'Colombia' , 46 : 'Sweden', 44 : 'UK', 1 : 'USA' , 52 : 'Mexico' , 56 : 'Chile'}

# define la lista de telefonos

telephones = [ '+573016251193', '+180155666', '+4456294634']

#pruebas para hacer el loop del dictionary, el primero muestra las llaves, y el segundo el valor

for x in countryCode:
      print(str(x))
	  
countryCode['Colombia']

#funcion fi nal
	  
def findCountry():
    for x in telephones:
        NumberLength = len(x)
        phoneNoPlusSign = x[1:NumberLength]
        # print(phoneNoPlusSign)
        for y in countryCode:
            CountryPrefix = str(y)
            if phoneNoPlusSign.startswith(CountryPrefix):
                # print(CountryPrefix)
                print(str(x) + " is from " + countryCode[y])

findCountry()


numberArray = { 1, 2, 3, 4, 5, 6, 7, 8, 10, 11}

def findimpar():
	for x in numberArray:
		if x % 2 == 0:	
			print( x + "es impar" )
