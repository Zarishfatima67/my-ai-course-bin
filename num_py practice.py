import numpy as np

brokered_,status,price,city,zip_code,=np.genfromtxt('RealEstate-USA.csv',  delimiter=',',usecols=(0,1,2,8,10),unpack=True, dtype=None,skip_header=1 )

print(brokered_)
print(status)
print(price)
print(city)
print(zip_code)

# RealEstate-USA  brokered_ - statistics operations
print('RealEstate-USA brokered_ mean:',np.mean(brokered_))
print('RealEstate-USA brokered_ average:',np.average(brokered_))
print('RealEstate-USA brokered_ std:',np.std(brokered_))
print('RealEstate-USA brokered_ mod:',np.median(brokered_))
print('RealEstate-USA brokered_ percentile - 25:',np.percentile(brokered_,25))
print('RealEstate-USA brokered_ percentile - 75:',np.percentile(brokered_,75))
print('RealEstate-USA brokered_ percentile - 3:',np.percentile(brokered_,3))
print('RealEstate-USA brokered_ min:',np.min(brokered_))
print('RealEstate-USA brokered_ max:',np.max(brokered_))

# RealEstate-USA  brokered_ - maths operations
print('RealEstate-USA brokered_ square:',np.square(brokered_))
print('RealEstate-USA brokered_ sqrt:',np.sqrt(brokered_))
print('RealEstate-USA brokered_ pow:',np.power(brokered_,brokered_))
print('RealEstate-USA brokered_ abs:',np.abs(brokered_))

# RealEstate-USA  brokered_ -arithmetic operations

addition= price+zip_code
subtraction=price-zip_code
multiplication = price * zip_code
division = price / zip_code

print("RealEstate-USA price-zip_code -Addition:",addition)
print("RealEstate-USA price-zip_code -Subtraction:",subtraction)
print("RealEstate-USA price-zip_code -Multiplication:",multiplication)
print("RealEstate-USA price-zip_code -Division:",division)

#Trigonometric Functions
brokered_pie=(brokered_/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values=np.sin(brokered_pie)
cosine_values=np.cos(brokered_pie)
tangent_values=np.tan(brokered_pie)

print("RealEstate-USA-brokered_ - div - pie - sinevalues:",sine_values)
print("RealEstate-USA-brokered_ - div - pie - cosinevalues:",cosine_values)
print("RealEstate-USA-brokered_ - div - pie- tangentvalues:",tangent_values)

print("RealEstate-USA-brokered_ - div - pie - Exponentialvalues:",np.exp(brokered_pie))

# Calculate the natural logarithm and base-10 logarithm
log_array=np.log(brokered_pie)
log10_array=np.log10(brokered_pie)

print("RealEstate-USA-brokered_ - div - pie - Natural logarithm values:",log_array)
print("RealEstate-USA-brokered_ - div - pie = Base10  logarithm values:",log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(brokered_pie)
print("RealEstate-USA-brokered_ - div - pie   - Hyperbolic Sine values:", sinh_values)

#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(brokered_pie)
print("RealEstate-USA-brokered_ - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(brokered_pie)
print("RealEstate-USA-brokered_ - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(brokered_pie)
print("RealEstate-USA-brokered_ - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(brokered_pie)
print("RealEstate-USA-brokered_  - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)

#RealEstate-USA Long Plus Lat - 2 dimentional arrary
D2pricezip_code= np.array([price,
                     zip_code])
print ("RealEstate-USA - price Plus zip_code - 2 dimentional arrary - " ,D2pricezip_code)

# check the dimension of array1
print("RealEstate-USA - price Plus zip_code  - 2 dimentional arrary - dimension" , D2pricezip_code.ndim) 


# return total number of elements in array1
print("RealEstate-USA - price Plus zip_code  - 2 dimentional arrary - total number of elements" ,D2pricezip_code.size)


# return a tuple that gives size of array in each dimension
print("RealEstate-USA - price Plus zip_code  - 2 dimentional arrary - gives size of array in each dimension" ,D2pricezip_code.shape)


# check the data type of array1
print("RealEstate-USA - price Plus zip_code  - 2 dimentional arrary - data type" ,D2pricezip_code.dtype) 

# Splicing array
D2pricezip_codeSlice= D2pricezip_code[:2,:5]
print("RealEstate-USA - price Plus zip-code  - 2 dimentional array - Splicing array -2Dpricezip_code[:1,:5]",D2pricezip_codeSlice)
D2pricezip_codeSlice2= D2pricezip_code[:1,3:10:3]
print("RealEstate-USA - price Plus zip-code  - 2 dimentional array - Splicing array -2Dpricezip_code[:1,3:10:3]",D2pricezip_codeSlice2)

# Indexing array
D2pricezip_codeItemOnly= D2pricezip_code[0,1]
print("RealEstate-USA - price Plus zip-code  - 2 dimentional array - Splicing array -2Dpricezip_code[1,5]",D2pricezip_codeItemOnly)
D2pricezip_codeItemOnly= D2pricezip_code[0,3]
print("RealEstate-USA - price Plus zip-code  - 2 dimentional array - Splicing array -2Dpricezip_code[0,3]",D2pricezip_codeItemOnly)