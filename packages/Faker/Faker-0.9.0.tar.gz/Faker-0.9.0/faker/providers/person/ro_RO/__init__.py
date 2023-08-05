# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{first_name_female}} {{last_name}}'
    )
    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{first_name_male}} {{last_name}}'
    )

    # sources: https://ro.wikipedia.org/wiki/List%C4%83_de_prenume_rom%C3%A2ne%C8%99ti
    first_names_female = (
        'Ada', 'Adela', 'Adelaida', 'Adelina', 'Adina', 'Adriana', 'Agata', 'Aglaia', 'Agripina', 'Aida', 'Alberta',
        'Albertina', 'Alexandra', 'Alexandrina', 'Alice', 'Alida', 'Alina', 'Alis', 'Alma', 'Amalia', 'Amanda',
        'Amelia',
        'Ana', 'Anabela', 'Anaida', 'Anamaria', 'Anastasia', 'Anca', 'Ancuța', 'Anda', 'Andra', 'Andrada', 'Andreea',
        'Anemona', 'Aneta', 'Angela', 'Anghelina', 'Anica', 'Anișoara', 'Antoaneta', 'Antonela', 'Antonia', 'Anuța',
        'Ariadna', 'Ariana', 'Arina', 'Aristița', 'Artemisa', 'Astrid', 'Atena', 'Augustina', 'Aura', 'Aurelia',
        'Aureliana', 'Aurica', 'Aurora', 'Axenia', 'Beatrice', 'Betina', 'Bianca', 'Blanduzia', 'Bogdana', 'Brândușa',
        'Camelia', 'Carina', 'Carla', 'Carmen', 'Carmina', 'Carolina', 'Casandra', 'Casiana', 'Caterina', 'Catinca',
        'Catrina', 'Catrinel', 'Cătălina', 'Cecilia', 'Celia', 'Cerasela', 'Cezara', 'Cipriana', 'Clara', 'Clarisa',
        'Claudia', 'Clementina', 'Cleopatra', 'Codrina', 'Codruța', 'Constanța', 'Constantina', 'Consuela', 'Coralia',
        'Corina', 'Cornelia', 'Cosmina', 'Crenguța', 'Crina', 'Cristina', 'Daciana', 'Dafina', 'Daiana', 'Dalia',
        'Dana',
        'Daniela', 'Daria', 'Dariana', 'Delia', 'Demetra', 'Denisa', 'Despina', 'Diana', 'Dida', 'Didina', 'Dimitrina',
        'Dina', 'Dochia', 'Doina', 'Domnica', 'Dora', 'Doriana', 'Dorina', 'Dorli', 'Draga', 'Dumitra', 'Dumitrana',
        'Ecaterina', 'Eftimia', 'Elena', 'Eleonora', 'Eliana', 'Elisabeta', 'Elisaveta', 'Eliza', 'Elodia', 'Elvira',
        'Emanuela', 'Emilia', 'Erica', 'Estera', 'Eufrosina', 'Eugenia', 'Eusebia', 'Eva', 'Evanghelina', 'Evelina',
        'Fabia', 'Fabiana', 'Felicia', 'Filofteia', 'Fiona', 'Flavia', 'Floare', 'Floarea', 'Flora', 'Florența',
        'Florentina', 'Floriana', 'Florica', 'Florina', 'Francesca', 'Frusina', 'Gabriela', 'Geanina', 'Gențiana',
        'Georgeta', 'Georgia', 'Georgiana', 'Geta', 'Gherghina', 'Gianina', 'Gina', 'Giorgiana', 'Grațiana', 'Grațiela',
        'Henrieta', 'Heracleea', 'Hortensia', 'Iasmina', 'Ica', 'Ileana', 'Ilinca', 'Ilona', 'Ina', 'Ioana', 'Ioanina',
        'Iolanda', 'Ionela', 'Ionelia', 'Iosefina', 'Iridenta', 'Irina', 'Iris', 'Isabela', 'Iulia', 'Iuliana',
        'Iustina',
        'Ivona', 'Izabela', 'Jana', 'Janeta', 'Janina', 'Jasmina', 'Jeana', 'Julia', 'Julieta', 'Larisa', 'Laura',
        'Laurenția', 'Lavinia', 'Lăcrămioara', 'Leana', 'Lelia', 'Leontina', 'Leopoldina', 'Letiția', 'Lia', 'Liana',
        'Lidia', 'Ligia', 'Lili', 'Liliana', 'Lioara', 'Livia', 'Loredana', 'Lorelei', 'Lorena', 'Luana', 'Lucia',
        'Luciana', 'Lucreția', 'Ludmila', 'Ludovica', 'Luiza', 'Luminița', 'Magdalena', 'Maia', 'Malvina', 'Manuela',
        'Mara', 'Marcela', 'Marcheta', 'Marga', 'Margareta', 'Maria', 'Mariana', 'Maricica', 'Marilena', 'Marina',
        'Marinela', 'Marioara', 'Marta', 'Matilda', 'Mădălina', 'Mălina', 'Mărioara', 'Măriuca', 'Melania', 'Melina',
        'Mihaela', 'Milena', 'Mina', 'Minodora', 'Mioara', 'Mirabela', 'Mirela', 'Mirona', 'Miruna', 'Mona', 'Monalisa',
        'Monica', 'Nadia', 'Narcisa', 'Natalia', 'Natașa', 'Nicoleta', 'Niculina', 'Nidia', 'Noemi', 'Nora', 'Norica',
        'Oana', 'Octavia', 'Octaviana', 'Ofelia', 'Olga', 'Olimpia', 'Olivia', 'Ortansa', 'Otilia', 'Ozana', 'Pamela',
        'Paraschiva', 'Patricia', 'Paula', 'Paulica', 'Paulina', 'Petronela', 'Petruța', 'Pompilia', 'Profira', 'Rada',
        'Rafila', 'Raluca', 'Ramona', 'Rebeca', 'Renata', 'Rica', 'Roberta', 'Robertina', 'Rodica', 'Romanița',
        'Romina',
        'Roxana', 'Roxelana', 'Roza', 'Rozalia', 'Ruxanda', 'Ruxandra', 'Sabina', 'Sabrina', 'Safta', 'Salomea',
        'Sanda',
        'Saveta', 'Savina', 'Sânziana', 'Semenica', 'Severina', 'Sidonia', 'Silvana', 'Silvia', 'Silviana', 'Simina',
        'Simona', 'Smaranda', 'Sofia', 'Sonia', 'Sorana', 'Sorina', 'Speranța', 'Stana', 'Stanca', 'Stela', 'Steliana',
        'Steluța', 'Suzana', 'Svetlana', 'Ștefana', 'Ștefania', 'Tamara', 'Tania', 'Tatiana', 'Teea', 'Teodora',
        'Teodosia',
        'Teona', 'Tiberia', 'Timea', 'Tinca', 'Tincuța', 'Tudora', 'Tudorița', 'Tudosia', 'Valentina', 'Valeria',
        'Vanesa',
        'Varvara', 'Vasilica', 'Venera', 'Vera', 'Veronica', 'Veta', 'Vicenția', 'Victoria', 'Violeta', 'Viorela',
        'Viorica', 'Virginia', 'Viviana', 'Vlădelina', 'Voichița', 'Xenia', 'Zaharia', 'Zamfira', 'Zaraza', 'Zenobia',
        'Zenovia', 'Zina', 'Zoe')

    first_names_male = (
        'Achim', 'Adam', 'Adelin', 'Adi', 'Adonis', 'Adrian', 'Agnos', 'Albert', 'Aleodor', 'Alex', 'Alexandru',
        'Alexe', 'Alin', 'Alistar', 'Amedeu', 'Amza', 'Anatolie', 'Andrei', 'Andrian', 'Angel', 'Anghel', 'Antim',
        'Anton',
        'Antonie', 'Antoniu', 'Arian', 'Aristide', 'Arsenie', 'Augustin', 'Aurel', 'Aurelian', 'Aurică', 'Avram',
        'Axinte',
        'Barbu', 'Bartolomeu', 'Basarab', 'Bănel', 'Bebe', 'Beniamin', 'Benone', 'Bernard', 'Bogdan', 'Brăduț', 'Bucur',
        'Caius', 'Camil', 'Cantemir', 'Carol', 'Casian', 'Cazimir', 'Călin', 'Cătălin', 'Cedrin', 'Cezar', 'Ciprian',
        'Claudiu', 'Codin', 'Codrin', 'Codruț', 'Constantin', 'Cornel', 'Corneliu', 'Corvin', 'Cosmin', 'Costache',
        'Costel', 'Costin', 'Crin', 'Cristea', 'Cristian', 'Cristobal', 'Cristofor', 'Dacian', 'Damian', 'Dan',
        'Daniel',
        'Darius', 'David', 'Decebal', 'Denis', 'Dinu', 'Dominic', 'Dorel', 'Dorian', 'Dorin', 'Dorinel', 'Doru',
        'Dragoș',
        'Ducu', 'Dumitru', 'Edgar', 'Edmond', 'Eduard', 'Eftimie', 'Emanoil', 'Emanuel', 'Emanuil', 'Emil', 'Emilian',
        'Eremia', 'Eric', 'Ernest', 'Eugen', 'Eusebiu', 'Eustațiu', 'Fabian', 'Felix', 'Filip', 'Fiodor', 'Flaviu',
        'Florea', 'Florentin', 'Florian', 'Florin', 'Francisc', 'Frederic', 'Gabi', 'Gabriel', 'Gelu', 'George',
        'Georgel',
        'Georgian', 'Ghenadie', 'Gheorghe', 'Gheorghiță', 'Ghiță', 'Gică', 'Gicu', 'Giorgian', 'Grațian', 'Gregorian',
        'Grigore', 'Haralamb', 'Haralambie', 'Horațiu', 'Horea', 'Horia', 'Iacob', 'Iancu', 'Ianis', 'Ieremia',
        'Ilarie',
        'Ilarion', 'Ilie', 'Inocențiu', 'Ioan', 'Ion', 'Ionel', 'Ionică', 'Ionuț', 'Iosif', 'Irinel', 'Iulian', 'Iuliu',
        'Iurie', 'Iustin', 'Iustinian', 'Ivan', 'Jan', 'Jean', 'Jenel', 'Ladislau', 'Lascăr', 'Laurențiu', 'Laurian',
        'Lazăr', 'Leonard', 'Leontin', 'Leordean', 'Lică', 'Liviu', 'Lorin', 'Luca', 'Lucențiu', 'Lucian', 'Lucrețiu',
        'Ludovic', 'Manole', 'Marcel', 'Marcu', 'Marian', 'Marin', 'Marius', 'Martin', 'Matei', 'Maxim', 'Maximilian',
        'Mădălin', 'Mihai', 'Mihail', 'Mihnea', 'Mircea', 'Miron', 'Mitică', 'Mitruț', 'Mugur', 'Mugurel', 'Nae',
        'Narcis',
        'Nechifor', 'Nelu', 'Nichifor', 'Nicoară', 'Nicodim', 'Nicolae', 'Nicolaie', 'Nicu', 'Niculiță', 'Nicușor',
        'Nicuță', 'Norbert', 'Norman', 'Octav', 'Octavian', 'Octaviu', 'Olimpian', 'Olimpiu', 'Oliviu', 'Ovidiu',
        'Pamfil',
        'Panagachie', 'Panait', 'Paul', 'Pavel', 'Pătru', 'Petre', 'Petrică', 'Petrișor', 'Petru', 'Petruț', 'Pleșu',
        'Pompiliu', 'Radu', 'Rafael', 'Rareș', 'Raul', 'Răducu', 'Răzvan', 'Relu', 'Remus', 'Robert', 'Romeo',
        'Romulus',
        'Sabin', 'Sandu', 'Sandu', 'Sava', 'Sebastian', 'Sergiu', 'Sever', 'Severin', 'Silvian', 'Silviu', 'Simi',
        'Simion',
        'Sinică', 'Sorin', 'Stan', 'Stancu', 'Stelian', 'Șerban', 'Ștefan', 'Teodor', 'Teofil', 'Teohari', 'Theodor',
        'Tiberiu', 'Timotei', 'Titus', 'Todor', 'Toma', 'Traian', 'Tudor', 'Valentin', 'Valeriu', 'Valter', 'Vasile',
        'Vasilică', 'Veniamin', 'Vicențiu', 'Victor', 'Vincențiu', 'Viorel', 'Visarion', 'Vlad', 'Vladimir', 'Vlaicu',
        'Voicu', 'Zamfir', 'Zeno')

    # sources: https://ro.wikipedia.org/wiki/Lista_celor_mai_uzuale_nume_de_familie#Rom%C3%A2nia
    last_names = (
        'Aanei', 'Ababei', 'Albu', 'Ardelean', 'Barbu', 'Cristea', 'Diaconescu', 'Diaconu', 'Dima', 'Dinu', 'Dobre',
        'Dochioiu', 'Dumitrescu', 'Eftimie', 'Ene', 'Florea', 'Georgescu', 'Gheorghiu', 'Ionescu', 'Ioniță',
        'Manole', 'Marin', 'Mazilescu', 'Mocanu', 'Nemeș', 'Nistor', 'Nistor', 'Niță', 'Oprea', 'Pop',
        'Popa', 'Popescu', 'Preda', 'Pușcașu', 'Stan', 'Stancu', 'Stoica', 'Stănescu', 'Suciu', 'Tabacu', 'Toma',
        'Tomescu', 'Tudor', 'Voinea')
