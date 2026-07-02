import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

address, latitude , longitude , name, = np.genfromtxt("FastFoodRestaurants.csv",
                                                                delimiter=',',
                                                                usecols=(0, 4, 5, 6),
                                                                unpack=True,
                                                                dtype=('U100', 'f8', 'f8', 'U100'),   # force correct types
                                                                encoding='utf-8',
                                                                skip_header=1,
                                                                invalid_raise=False)

print(address)
print(latitude)
print(longitude)
print(name)


# FastFoodRestaurants   latitude - statistics operations
print('FastFoodRestaurants latitude mean:',np.mean(latitude))
print('FastFoodRestaurants latitude average:',np.average(latitude))
print('FastFoodRestaurants latitude std:',np.std(latitude))
print('FastFoodRestaurants latitude mod:',np.median(latitude))
print('FastFoodRestaurants latitude percentile - 25:',np.percentile(latitude,25))
print('FastFoodRestaurants latitude percentile - 75:',np.percentile(latitude,75))
print('FastFoodRestaurants latitude percentile - 3:',np.percentile(latitude,3))
print('FastFoodRestaurants latitude min:',np.min(latitude))
print('FastFoodRestaurants latitude max:',np.max(latitude))

# FastFoodRestaurants  latitude - maths operations
print('FastFoodRestaurants  latiude square:',np.square(latitude))
print('FastFoodRestaurants  latitude sqrt:',np.sqrt(latitude))
print('FastFoodRestaurants  latitude pow:',np.power(latitude,latitude))
print('FastFoodRestaurants  latitude abs:',np.abs(latitude))

#FastFoodRestaurants   latitude -arithmetic operations

addition= latitude+longitude
subtraction= longitude - latitude
multiplication = longitude * latitude
division = longitude / latitude

print("FastFoodRestaurants latitude-longitude -Addition:",addition)
print("FastFoodRestaurants latitude-longitude  -Subtraction:",subtraction)
print("FastFoodRestaurants latitude-longitude  -Multiplication:",multiplication)
print("FastFoodRestaurants latitude-longitude  -Division:",division)

#Trigonometric Functions
latitudepie=(latitude/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values=np.sin(latitudepie)
cosine_values=np.cos(latitudepie)
tangent_values=np.tan(latitudepie)

print("FastFoodRestaurants - latitude - div - pie - sinevalues:",sine_values)
print("FastFoodRestaurants - latitude - div - pie - cosinevalues:",cosine_values)
print("FastFoodRestaurants - latitude - div - pie- tangentvalues:",tangent_values)

print("FastFoodRestaurants - latitude - div - pie - Exponentialvalues:",np.exp(latitude))

# Calculate the natural logarithm and base-10 logarithm
log_array=np.log(latitudepie)
log10_array=np.log10(latitudepie)

print("FastFoodRestaurants - latitude - div - pie - Natural logarithm values:",log_array)
print("FastFoodRestaurants - latitude - div - pie = Base10  logarithm values:",log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(latitudepie)
print("FastFoodRestaurants - latitude - div - pie   - Hyperbolic Sine values:", sinh_values)

#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(latitudepie)
print("FastFoodRestaurants - latitude - div - pie   - Hyperbolic Cosine values:", cosh_values)


#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(latitudepie)
print("FastFoodRestaurants - latitude - div - pie   -Hyperbolic Tangent values:", tanh_values)



#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(latitudepie)
print("FastFoodRestaurants - latitude - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(latitudepie)
print("FastFoodRestaurants - latitude  - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)

#RealEstate-USA Long Plus Lat - 2 dimentional arrary
D2latitudelongitude= np.array([latitude,
                     longitude])
print ("FastFoodRestaurants - latitude Plus longitude - 2 dimentional arrary - " ,D2latitudelongitude)


# check the dimension of array1
print("FastFoodRestaurants - latitude Plus longitude  - 2 dimentional arrary - dimension" , D2latitudelongitude.ndim) 

# return total number of elements in array1
print("FastFoodRestaurants - latitude Plus longitude  - 2 dimentional arrary - total number of elements" ,D2latitudelongitude.size)


# return a tuple that gives size of array in each dimension
print("FastFoodRestaurants - latitude Plus longitude  - 2 dimentional arrary - gives size of array in each dimension" ,D2latitudelongitude.shape)


# check the data type of array1
print("FastFoodRestaurants - latitude Plus longitude - 2 dimentional arrary - data type" ,D2latitudelongitude.dtype) 

# Splicing array
D2latitudelongitudeSlice= D2latitudelongitude[:2,:5]
print("FastFoodRestaurants - latitude Plus longitude  - 2 dimentional array - Splicing array -2Dlatitudelongitude[:1,:5]",D2latitudelongitudeSlice)
D2latitudelongitudeSlice2= D2latitudelongitude[:1,3:10:3]
print("FastFoodRestaurants - latitude Plus longitude  - 2 dimentional array - Splicing array -2Dlatitudelongitude[:1,3:10:3]",D2latitudelongitudeSlice2)

# Indexing arra
D2latitudelongitudeItemOnly= D2latitudelongitude[0,1]
print("FastFoodRestaurants - latitude Plus longitude - 2 dimentional array - Splicing array -2Dlatitudelongitude[1,5]",D2latitudelongitudeItemOnly)
D2latitudelongitudeItemOnly= D2latitudelongitude[0,3]
print("FastFoodRestaurants - latitude Plus longitude  - 2 dimentional array - Splicing array -2Dlatitudelongitude[0,3]",D2latitudelongitudeItemOnly)