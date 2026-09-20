# Här skriver du ditt textäventyr
name = input("Vad heter du?")
input(f"{name} anlände hem klockan 16.00. Hen har mycket att göra, bl.a träning kl 19.00 och ett super viktigt prov dagen därpå. frågan är om hon föredrar att spela spel eller plugga?")

val1 = input(f"klockan är 16.15, vad vill {name} göra? Sova/äta_mellanmål")

if val1 == "Sova":
    print(f"\n{name} sov lite för länge, klockan är 18.00 och om en timme har {name} träning")

    val2 = input(f"\n{name} kan välja mellan att äta eller plugga. Vad väljer hen?")
    if val2 == "äta":
        print(f"\n{name} hann bara att äta, nu är det dags att åka till träningen")

    elif val2 == "plugga":
        print("\n hen valde att plugga, vilket var positivt för att hen har prov imorgon. Efter plugget ska hen till träningen")

    val3 = input(f"\n Klockan är 21.00, {name} är helt slut, tänker hen kämpa lite till och plugga eller föredrar hen att sova")

    if val3 == "plugga":
        print(f"\nVäldigt bra kämpat!, ett sista ryck och sedan kan {name} gå och lägga sig.")

    else:
        print(f"\n{name} har haft en väldigt stressig eftermiddag, det är nog för det bästa om hen går och lägger sig")

elif val1 == "äta_mellanmål":
    print(f"{name} bestämde sig för att äta mellanmål men vad tänker hen göra härnäst?")

    val2_mellis = input("\n Hen kan välja mellan att spela spel eller studera innan träningen")
    if val2_mellis == "spela spel":
        print(f"\n Detta kanske inte var det bästa alternativet, {name} har trots allt prov imorgon.")

    elif val2_mellis == "studera":
        print(f"\n Vad imponerande av {name} att studera istället för att spela, hen vet att plugget är viktigare.")
    val3_mellis = input(f"\n{name} kan välja mellan att sitta upp och spela spel till klockan 03.00 eller sova.")

    if val3_mellis == "spela spel":
        print(f"\nDetta kommer {name} att ångra imorgon, hen fick inte tillräckligt med sömn.")

    elif val3_mellis == "sova":
        print(f"Skönt att {name} äntligen kan gå och lägga sig.")