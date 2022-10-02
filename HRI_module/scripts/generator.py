# This pytohn file generates the actions for the menu selection modim implementation

# Example action file: W1C2H1F1.txt

"""
IMAGE
<*,*,*,*>:  img/table.jpeg
----
TEXT
<*,*,it,*>: Ordine completato! Hai ordinato: 1 acqua 2 coca-cola 1 hamburger 1 patatine
<*,*,*,*>:  Completed order! You have ordered: 1 water 2 cokes 1 hamburger 1 french fries
----
TTS
<*,*,it,*>: Ordine completato! Hai ordinato: 1 acqua 2 coca-cola 1 hamburger 1 patatine
<*,*,*,*>:  Completed order! You have ordered: 1 water 2 cokes 1 hamburger 1 french fries
----
"""
# Maximum number of the same plate
# n = 1 ===> 16 combinations
# n = 2 ===> 81 combinations
# n = 3 ===> 256 combinations
# In general, No. of combs = (n+1)^4
n = 5
for wa in range(n+1):
    for co in range(n+1):
        for ha in range(n+1):
            for ff in range(n+1):
                filename = "W"+str(wa)+"C"+str(co)+"H"+str(ha)+"F"+str(ff)
                with open("./confirmations/"+filename, "w") as f:
                    f.write("IMAGE\n<*,*,*,*>: img/table.jpeg\n----\n")
                   
                    ita = "Ordine completato! Hai ordinato: "
                    eng = "Completed order! You have ordered: "
                    if (wa == 0 and co == 0 and ha == 0 and ff == 0):
                        ita = "Non hai ordinato nulla..."
                        eng = "You did not order anything..."
                    if wa == 1:
                        ita += str(wa) + " acqua "
                        eng += str(wa) + " water "
                    elif wa > 1:
                        ita += str(wa) + " acque "
                        eng += str(wa) + " waters "
                    if co == 1:
                        ita += str(co) + " coca-cola "
                        eng += str(co) + " coke "
                    elif co > 1:
                        ita += str(co) + " coca-cola "
                        eng += str(co) + " cokes "
                    if ha == 1:
                        ita += str(ha) + " hamburger "
                        eng += str(ha) + " hamburger "
                    elif ha > 1:
                        ita += str(ha) + " hamburger "
                        eng += str(ha) + " hamburgers "
                    if ff == 1:
                        ita += str(ff) + " patatine "
                        eng += str(ff) + " french fries "
                    elif ff > 1:
                        ita += str(ff) + " patatine "
                        eng += str(ff) + " french fries "
                   
                    f.write("TEXT\n<*,*,it,*>: " + ita + "\n<*,*,*,*>: " + eng + "\n----\n")
                    f.write("TTS\n<*,*,it,*>: " + ita + "\n<*,*,*,*>: " + eng + "\n----")
                    f.write("\nBUTTONS\nConfirm\n<*,*,it,*>: " + 'Confirm\n<*,*,*,*>: ' +'Confirm' "\nCancel\n<*,*,it,*>: " + 'Cancel\n<*,*,*,*>: Cancel' + "\n----")