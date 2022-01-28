#In mainfunc.py I have written the functions for nutrition application
List_product = {} #Dictionary for storing data from the file

def Open_File():
    with open("Products.txt") as file:
        for row in file:
            if not row:
                continue
            else:
                product, value = row.split(', ')
                List_product[product] = value

#Calculate the nutritional value and return the Final Result
def Final_result(product, gram):
    KcalValue  = Protein_value = Carb_Value = Fat_Value = 0
    #To check if the product are in the file and
    if product in List_product:
        (Kcal, Protein, carb, fat) = List_product[product].split(':')
        KcalValue += gram / 100 * int(Kcal)
        Protein_value += gram / 100 * int(Protein)
        Carb_Value += gram / 100 * int(carb)
        Fat_Value += gram / 100 * int(fat)
        Out_Come = "The Product provides you with %d kcal, %d protein, %d carbs oraz %d fat."
    else:
        Out_Come = "The product you have Entered is not in our Data_Base: %s, But still you can add it!" %(product)
    return Out_Come

