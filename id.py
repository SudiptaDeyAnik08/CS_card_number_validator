# Python3 program to validate Visa
# Card number using regular expression
import re



# Function to validate Visa Card
# number using regular expression.
def isValidVisaCardNo(string):	

	# Regex to check valid Visa
	# Card number
	regexVisa= "^4[0-9]{12}(?:[0-9]{3})?$";
	
	# Regex to check valid Amex Card
	regexAmex= "^3[47][0-9]{13}$";



	# Regex to check valid Dinner Club
	regexDinersClub= "^3(?:0[0-5]|[68][0-9])[0-9]{11}$";


	# Regex to check valid Master Card
	regexMastercard= "^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$";

	# Regex to check valid Union Pay
	regexUnionPay= "^(62[0-9]{14,17})$";

	# Regex to check valid Visa Master Card
	regexVisaMasterCard= "^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$";

	# Compile the ReGex
	pVisa = re.compile(regexVisa);
	pAmex = re.compile(regexAmex);
	pDinnerClub = re.compile(regexDinersClub);
	pMasterCard = re.compile(regexMastercard);
	pUnionPay = re.compile(regexUnionPay);
	pVisaMaster = re.compile(regexVisaMasterCard);
	
	#Making a global variable named M 
	m=1
	cardType="Not Found The card"

	# If the string is empty
	# return false
	if (string == ''):
		m = False
	elif(re.match(pVisa,string)):
		cardType = "Card Type is VISA";
		m = True
	elif(re.match(pAmex,string)):
		cardType = "Card Type is Amex";
		m = True
	elif(re.match(pDinnerClub,string)):
		cardType = "Card Type is Dinner Club";
		m = True
	elif(re.match(pMasterCard,string)):
		cardType = "Card Type is Master Card";
		m = True
	elif(re.match(pUnionPay,string)):
		cardType = "Card Type is Union Pay";
		m = True
	elif(re.match(pVisaMaster,string)):
		cardType = "Card Type is Visa Master";
		m = True
		

	# Pattern class contains matcher()
	# method to find matching between
	# given string and regular expression.
	#m = re.match(p, string);
	
	# Return True if the string
	# matched the ReGex else False
	if m is None:
		r = False;
		cardType="No Cart Found";
		result = [r,cardType]
		return result;
	elif m is True:
		r = True
		result = [r,cardType]
		return result;
	else:
		r = False;
		cardType="No Cart Found";
		result = [r,cardType]
		return result;

# Driver code
if __name__ == "__main__":
	
	# Test Case 1
	str1 = input("Enter Number: ");
	result = isValidVisaCardNo(str1);
	
	print("Given Card is ",result[0],"and ",result[1])
	
	

