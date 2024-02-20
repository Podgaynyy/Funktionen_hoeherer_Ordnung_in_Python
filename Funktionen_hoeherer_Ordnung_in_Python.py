"""
Aufgabe:
Sie haben Code, den Sie nicht ändern können (dies ist oft der Fall,
wenn der Code im hinteren Teil des Programms häufig
verwendet wird und Sie nichts kaputt machen wollen):
transformation = <????>
Werte = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # oder jede andere Liste
transormed_values = list(map(transformation, values))
Die einzige Möglichkeit, mit diesem Code zu interagieren, besteht in der Einstellung
der Transformationsfunktion.
Sie haben jedoch erkannt, dass Sie für Ihre aktuelle Aufgabe die Liste der Werte nicht in
irgendeiner Weise transformieren müssen, sondern sie so erhalten wollen, wie sie ist.
Schreiben Sie einen Lambda-Ausdruck für die Transformation,
damit transformed_values eine Kopie von values ist.
"""
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformation = lambda a: a #lambda als Funktion, die nimmt Argument a und ausgibt argument a
#sehr gut fuer die Geraeteueberwachung und Automatisierung geeignet
transformed_values = list(map(transformation, values)) #map funktion iteriert objekt values mit
#der Anwendung von andere Funktion (transformation)
print(transformed_values)


# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
# print(‘ok’)
# else:
# print(‘fail’)

"""Aufgabe:
Die Planeten kreisen auf elliptischen Bahnen um die Sterne. 
Nennen wir den am weitesten entfernten Planeten denjenigen, dessen Bahn die größte Fläche hat. 
Schreiben Sie eine Funktion find_farthest_orbit(list_of_orbits), 
die die Bahn des am weitesten entfernten Planeten in der Liste der Planetenbahnen findet. 
Berücksichtigen Sie keine kreisförmigen Bahnen: 
Sie wissen, dass Ihr Stern keine solchen Planeten hat, 
aber künstliche Satelliten wurden in kreisförmige Bahnen gebracht. 
Das Ergebnis der Funktion sollte ein Tupel sein, 
das die Halbachsenlängen der Ellipse der Umlaufbahn des am weitesten entfernten Planeten enthält. 
Jeder Orbit ist ein Tupel aus einem Zahlenpaar - den Halbachsen seiner Ellipse. 
Die Fläche der Ellipse wird nach der Formel S = pi*a*b berechnet, 
wobei a und b die Längen der Halbachsen der Ellipse sind. 
Verwenden Sie bei der Lösung der Aufgabe Listenausdrücke. 
Tipp: Es ist am einfachsten, die Ellipse in zwei Schritten zu finden: 
Berechne zuerst die größte Fläche der Ellipse und finde dann die Ellipse selbst, 
die eine solche Fläche hat. 
Es ist garantiert, dass der am weitesten entfernte Planet genau eine"""
list_of_orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
list_of_planets = list(filter(lambda a:  a[0] != a[1], list_of_orbits))
#filter-Funktion filtriert iteriertes Objekt, mit Bedingungen a[0] != a[1]
#es wird die Liste von einfiltriertes Objekt erstellt
print(list_of_planets)
find_farthest_orbit = max(list(map(lambda x: 3.14 * x[0] * x[1], list_of_planets)))
max_orbit = list(filter(lambda a: 3.14 * a[0] * a[1] == find_farthest_orbit, list_of_planets))
print(*max_orbit)

#Alternative Lösung
# print(*max(orbits, key = lambda pair: pair[0] * pair[1] * (pair[0] != pair[1])))