#Sims 4 Aspiration and Traits Random Generator. 
#Uses expansion packs Cats&Dogs, City Living, Get Famous, Get to Work, Get Together, and Seasons.
#Uses game packs Dine Out, Outdoor Retreat, Parenthood, Spa Day, and Vampires.
# Use trait one on teens and adults if doing the #100babychallenge.
#
#Author: @Infosec_Taylor

#Import Random Number Generator
import random

#Get user input
age = raw_input("What life stage is your sim? Type toddler, child, teen, or adult) ")

#Defines Toddler traits in a list and then randomly prints a trait.
if(age=="toddler" or age=="Toddler"):
	trait = ["Angelic", "Charmer", "Clingy", "Fussy", "Independent", "Inquisitive", "Silly", "Wild"]

	randomtrait = random.randint(0,7)

	print "Trait is " + trait[randomtrait]

#Defines Child aspirations and traits into lists and then randomly prints an aspiration and one trait.
elif(age=="child" or age=="Child"):
        aspiration = ["Creativity - Artistic Prodigy","Mental - Whiz Kid","Motor - Rambunctious Scamp","Social - Social Butterfly"]
        trait = ["Emotional - Active", "Emotional - Cheerful", "Emotional - Creative", "Emotional - Genius", "Emotional - Gloomy", "Emotional - Goofball", "Emotional - Hot-Headed", "Emotional - Self-Assured", "Hobby - Art Lover", "Hobby - Bookworm", "Hobby - Geek", "Hobby - Music Lover", "Hobby - Perfectionist", "Lifestyle - Cat Lover", "Lifestyle - Dog Lover", "Lifestyle - Erratic", "Lifestyle - Glutton", "Lifestyle - Kleptomaniac", "Lifestyle - Lazy", "Lifestyle - Love Outdoors", "Lifestyle - Neat", "Lifestyle - Slob", "Lifestyle - Squeamish", "Lifestyle - Vegetarian", "Social - Evil", "Social - Good", "Social - Insider", "Social - Loner", "Social - Mean", "Social - Outgoing"]

        randomasp = random.randint(0,3)
        randomtrait = random.randint(0,29)

        print "Aspiration is " + aspiration[randomasp]
        print "Trait is " + trait[randomtrait]

#Defines Teen aspirations and traits into lists and then randomly prints an aspiration and two traits. There is also a check to make sure trait 1 and trait 2 are different.
elif (age=="teen" or age=="Teen"):
        aspiration = ["Animal - Friend of the Animals", "Athletic - Bodybuilder", "Creativity - Bestselling Author", "Creativity - Musical Genius", "Creativity - Master Actor", "Creativity - Painter Extraordinaire", "Deviance - Public Enemy", "Deviance - Chief or Mischief", "Family - Big Happy Family", "Family - Vampire Family", "Family - Super Parent", "Family - Successful Lineage", "Food - Master Chef", "Food - Master Mixologist", "Fortune - Fabulously Wealthy", "Fortune - Mansion Baron", "Knowledge - Comptuer Whiz", "Knowledge - Nerd Brain", "Knowledge - Master Vampire", "Knowledge - Renaissance Sim", "Location - City Native", "Love - Serial Romantic", "Love - Soulmate", "Nature - Angling Ace", "Nature - The Curator", "Nature - Outdoor Enthusiast", "Nature - Freelance Botanist", "Popularity - Friend of the World", "Popularity - Party Animal", "Popularity - Good Vampire", "Popularity - World Famous Celebrity", "Popularity - Leader of the Pack", "Popularity - Joke Star"]
        trait = ["Emotional - Active", "Emotional - Cheerful", "Emotional - Creative", "Emotional - Genius", "Emotional - Gloomy", "Emotional - Goofball", "Emotional - Hot-Headed", "Emotional - Romantic", "Emotional - Self-Assured", "Emotional - Unflirty", "Hobby - Art Lover", "Hobby - Bookworm", "Hobby - Foodie", "Hobby - Geek", "Hobby - Music Lover", "Hobby - Perfectionist", "Lifestyle - Cat Lover", "Lifestyle - Childish", "Lifestyle - Clumsy", "Lifestyle - Dance Machine", "Lifestyle - Dog Lover", "Lifestyle - Erratic", "Lifestyle - Glutton", "Lifestyle - Kleptomaniac", "Lifestyle - Lazy", "Lifestyle - Love Outdoors", "Lifestyle = Materialistic", "Lifestyle - Neat", "Lifestyle - Slob", "Lifestyle - Snob", "Lifestyle - Squeamish", "Lifestyle - Vegetarian", "Social - Bro", "Social - Evil", "Social - Good", "Social - Hates Children", "Social - Insider", "Social - Jealous", "Social - Loner", "Social - Mean", "Social - Outgoing", "Social - Self-Absorbed"]


        randomasp = random.randint(0,32)
        randomtrait1 = random.randint(0,40)
        randomtrait2 = random.randint(0,40)

        while (randomtrait1 == randomtrait2):
             randomtrait2 = random.randint(0,40)   
        
        print "Aspiration is " + aspiration[randomasp]
        print "Trait One is " + trait[randomtrait1]
        print "Trait Two is " + trait[randomtrait2]

#Defines Teen aspirations and traits into lists and then randomly prints an aspiration and three traits. There is also a check to make sure trait 1, trait 2, and trait 3 are different.
elif (age=="adult" or age=="Adult"):
        aspiration = ["Animal - Friend of the Animals", "Athletic - Bodybuilder", "Creativity - Bestselling Author", "Creativity - Musical Genius", "Creativity - Master Actor", "Creativity - Painter Extraordinaire", "Deviance - Public Enemy", "Deviance - Chief or Mischief", "Family - Big Happy Family", "Family - Vampire Family", "Family - Super Parent", "Family - Successful Lineage", "Food - Master Chef", "Food - Master Mixologist", "Fortune - Fabulously Wealthy", "Fortune - Mansion Baron", "Knowledge - Comptuer Whiz", "Knowledge - Nerd Brain", "Knowledge - Master Vampire", "Knowledge - Renaissance Sim", "Location - City Native", "Love - Serial Romantic", "Love - Soulmate", "Nature - Angling Ace", "Nature - The Curator", "Nature - Outdoor Enthusiast", "Nature - Freelance Botanist", "Popularity - Friend of the World", "Popularity - Party Animal", "Popularity - Good Vampire", "Popularity - World Famous Celebrity", "Popularity - Leader of the Pack", "Popularity - Joke Star"]
        trait = ["Emotional - Active", "Emotional - Cheerful", "Emotional - Creative", "Emotional - Genius", "Emotional - Gloomy", "Emotional - Goofball", "Emotional - Hot-Headed", "Emotional - Romantic", "Emotional - Self-Assured", "Emotional - Unflirty", "Hobby - Art Lover", "Hobby - Bookworm", "Hobby - Foodie", "Hobby - Geek", "Hobby - Music Lover", "Hobby - Perfectionist", "Lifestyle - Cat Lover", "Lifestyle - Childish", "Lifestyle - Clumsy", "Lifestyle - Dance Machine", "Lifestyle - Dog Lover", "Lifestyle - Erratic", "Lifestyle - Glutton", "Lifestyle - Kleptomaniac", "Lifestyle - Lazy", "Lifestyle - Love Outdoors", "Lifestyle = Materialistic", "Lifestyle - Neat", "Lifestyle - Slob", "Lifestyle - Snob", "Lifestyle - Squeamish", "Lifestyle - Vegetarian", "Social - Bro", "Social - Evil", "Social - Good", "Social - Hates Children", "Social - Insider", "Social - Jealous", "Social - Loner", "Social - Mean", "Social - Outgoing", "Social - Self-Absorbed"]

        randomasp = random.randint(0,32)
        randomtrait1 = random.randint(0,40)
        randomtrait2 = random.randint(0,40)
        randomtrait3 = random.randint(0,40)

        while (randomtrait1 == randomtrait2):
             randomtrait2 = random.randint(0,40)

        while (randomtrait3 == randomtrait1 or randomtrait3 == randomtrait2):
             randomtrait3 = random.randint(0,40)
        
        print "Aspiration is " + aspiration[randomasp]
        print "Trait One is " + trait[randomtrait1]
        print "Trait Two is " + trait[randomtrait2]
        print "Trait Three is " + trait[randomtrait3]

#If choice is not toddler, child, teen, or adult script will generate an error.
else:
        print "**ERROR** Life stage must be equal to toddler, child, teen, or adult."
