# Projekcik

Projekt programu wykorzystującego algorytm ewolucyjny do odwzorowywania zadanego przez użytkownika obrazu z wykorzystaniem wyewoluowanych z pomocą algorytmu kształtów. Działa dla prostych obrazów.

## Conda
"conda_spec.txt" to plik z wszystkimi paczkami które miałem na wirtualce condy, jest ich więcej niż potrzeba więc można stworzyć sobie swoje i zainstalować paczki: numpy, matplotlib, pillow, numexpr. Możliwe że o czymś zapomniałem to trzeba będzie doinstalować. 
Link jak zrobić nowe środowisko condy z wykorzystaniem pliczku: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file

## VENV
Jeśli ktoś chce zrobić nowe środowisko bez używania condy to dodałem plik "requirements.txt". Jak ktoś używa PyCharma i chciałby tak zrobić to zamieszczam krótką instrukcję:
1. Mając otworzony projekt wchodzimy w File->Settings->Project: DL_Gene_team->Python interpreter -> klikamy w trybik -> Add -> Virtualenv 
2. Zaznaczamy New environment, ścieżna do folderu projektu powinna zaktualizować się sama upewniamy się że na końcu jest "DL_Gene_team\venv" jeśli nie to trzeba zmienić.
3. Jak już się zrobi to powinien pojawić się nam folder venv. Teraz robimy tak: wchodzimy venv/Scripts/activate.bat klikamy prawym -> copy path -> copy absolute path
4. Jak już się zrobi to na pasku pycharma na dole(tam gdzie zakładki git/TODO itd.) wybieramy Terminal i wpisujemy: "cmd.exe" /k <wklejamy to co dostaliśmy w pkt. 3>
5. teraz w terminalu wpisujemy: pip install -r requirements.txt
6. Gotowe, dodajemy w konfiguracji ścieżkę do maina, odpalamy i powinno śmigać. 

# Obrazek

![alt text](https://user-images.githubusercontent.com/39136856/110666618-c8ab2100-81c9-11eb-8988-dae143ef5ae7.jpg)
