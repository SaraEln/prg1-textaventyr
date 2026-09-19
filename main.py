# Här skriver du ditt textäventyr
name = input("Vad heter du?")
input(f"{name} anlände hem klockan 16.00. Hon har mycket att göra, bl.a träning kl 19.00 och ett super viktigt prov dagen därpå. frågan är om hon föredrar att spela spel eller plugga?")

val1 = input(f"klockan är 16.15, vad vill {name} göra? Sova/äta_mellanmål")

if val1 == "Sova":
    print(f"\n{name} sov lite för länge, klockan är 18.00 och om en timme har {name} träning")

    val2 = input("Sara kan välja mellan att äta eller plugga. Vad väljer hon?")
    if val2 == "äta":
        print(f"\n{name} hann bara att äta, nu är det dags att åka till träningen")

    elif val2 == "plugga":
        print("\nSara valde att plugga, vilket var positivt för att hon har prov imorgon. Efter plugget ska hon till träningen")

elif val1 == "äta_mellanmål":
    print("Sara bestämde sig för att äta mellanmål men vad tänker hon göra härnäst?")

    val2_mellis = input("\n Sara kan välja mellan att spela spel eller studera innan träningen")
    if val2_mellis == "spela spel":
        print(f"\n Detta kanske inte var det bästa alternativet, {name} har trots allt prov imorgon.")
    elif val2_mellis == "studera":
        print(f"\n Vad imponerande av {name} att studera istället för att spela, hon vet att plugget är viktigare.")
