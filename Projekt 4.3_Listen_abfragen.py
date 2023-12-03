def vorstellung():
    print("Gerne möchte ich Ihnen mit diesem Code zeigen, dass ich mich auch bereits Privat mit dem Thema Programmieren beschäftige.")
    print("Seit nun mehr als einem halben Jahr versuche ich mich an Python und bis jetzt lerne ich täglich etwas neues dazu.")
    print("Nun suche ich nach einem Arbeitgeber, der mich in dieser Leidenschaft unterstützt.")
    print("In diesem kurzen Code habe ich versucht Ihre Fragen via systematischer Abfrage zu beantworten.")

def frage_1():
    return "Ich bin sehr wissbegierig, möchte mich stetig weiterentwickeln und das am besten im Team, denn ich bin ein absoluter Teamplayer. Meine Ecken & Kanten sind in gewissen Maßen meine Verfügbarkeit in Zeiten von Projekten, da ich dort stets mein Herzblut mit einbringe und daher privat nicht viel Zeit habe."

def frage_2():
    return "Ich bin in der freiwilligen Feuerwehr in Greven aktiv und dies erfüllt mich vollumfänglich. Im Team zu arbeiten und Menschen zu helfen ist eine sehr ehrenswerte Aufgabe und ich erfülle sie mit Stolz."

def frage_3():
    return "Antwort auf diese Frage steht noch aus."

def frage_4():
    return "Antwort auf diese Frage steht noch aus."

def Hauptprogramm():
    vorstellung()

    while True:
        fragen = {
            "1": "Was zeichnet dich aus - Was sind deine Ecken und Kanten?",
            "2": "Was machst du so in deiner Freizeit?",
            "3": "Was reizt dich am Berufsbild Wirtschaftsinformatiker? (Antwort steht noch aus)",
            "4": "Warum willst du dieses duale Studium bei uns in der FI machen? (Antwort steht noch aus)"
        }

        for key in fragen:
            print(f"{key}) {fragen[key]}")

        auswahl = input("Wähle eine Frage (1-4) oder drücke 'z' zum Beenden: ")

        if auswahl == "1":
            print(frage_1())
        elif auswahl == "2":
            print(frage_2())
        elif auswahl == "3":
            print(frage_3())
        elif auswahl == "4":
            print(frage_4())
        elif auswahl.lower() == 'z':
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

        print("\n---\n")

if __name__ == "__main__":
    Hauptprogramm()