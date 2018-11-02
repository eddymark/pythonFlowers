# Flower Shop Ordering To Go - 
# Create a flower shop application which deals in flower objects and use those flower objects in a 
# bouquet object which can then be sold. 
# Keep track of the number of objects and when you may need to order more.

class Flower:
    #initialize the flowers 
    def __init__(self, type_of_flower, color, size):
        #the self is just making the variables exist
        self.type_of_flower = type_of_flower
        self.color = color
        self.size = size



   

class Bouquet :
    #initialize the boquet
    def __init__(self,number_of_flowers, flowers):
        self.number_of_flowers = number_of_flowers
        self.flowers = flowers
    
    def show_flowers(self):
        #print all flowers
        for flower in self.flowers: 
            print("Flower type: " + flower.type_of_flower)
            print("Flower color: " + flower.color)
            print("Flower size: " + flower.size)
            print("==============")
        return True 

        
    
    def addFlower(self,flower):
        #append to the array
        self.flowers.append(flower)


#created two flowers before creating add to flower 
red_rose = Flower('Rose', 'Red', 'Small')
pink_rose = Flower('Rose', 'Pink', 'Medium')

#created a flower array 
flowers = [red_rose, pink_rose]
#created the first boquet object with an array of flowers 
first_bouquet = Bouquet(2, flowers)



blue_sunflower = Flower('Sunflower', 'Blue' , 'Mad Big')


first_bouquet.addFlower(blue_sunflower)

(first_bouquet.show_flowers())


