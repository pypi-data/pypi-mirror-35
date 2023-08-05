# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}',
        '{{first_name_male}} {{last_name}}, {{suffix}}',
        '{{first_name_female}} {{last_name}}, {{suffix}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}, {{suffix}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}, {{suffix}}',
    )

    # From http://www.nama.web.id/search.php?gender=male&origin=Indonesia+-+Jawa&letter=&submit=Search
    # via
    # https://github.com/fzaninotto/faker/blob/master/src/Faker/Provider/id_ID/Person.php
    first_names_male = (
        'Abyasa', 'Ade', 'Adhiarja', 'Adiarja', 'Adika', 'Adikara', 'Adinata',
        'Aditya', 'Agus', 'Ajiman', 'Ajimat', 'Ajimin', 'Ajiono', 'Akarsana',
        'Alambana', 'Among', 'Anggabaya', 'Anom', 'Argono', 'Aris', 'Arta',
        'Artanto', 'Artawan', 'Arsipatra', 'Asirwada', 'Asirwanda', 'Aslijan',
        'Asmadi', 'Asman', 'Asmianto', 'Asmuni', 'Aswani', 'Atma', 'Atmaja',
        'Bagas', 'Bagiya', 'Bagus', 'Bagya', 'Bahuraksa', 'Bahuwarna',
        'Bahuwirya', 'Bajragin', 'Bakda', 'Bakiadi', 'Bakianto', 'Bakidin',
        'Bakijan', 'Bakiman', 'Bakiono', 'Bakti', 'Baktiadi', 'Baktianto',
        'Baktiono', 'Bala', 'Balamantri', 'Balangga', 'Balapati', 'Balidin',
        'Balijan', 'Bambang', 'Banara', 'Banawa', 'Banawi', 'Bancar', 'Budi',
        'Cagak', 'Cager', 'Cahyadi', 'Cahyanto', 'Cahya', 'Cahyo', 'Cahyono',
        'Caket', 'Cakrabirawa', 'Cakrabuana', 'Cakrajiya', 'Cakrawala',
        'Cakrawangsa', 'Candra', 'Chandra', 'Candrakanta', 'Capa', 'Caraka',
        'Carub', 'Catur', 'Caturangga', 'Cawisadi', 'Cawisono', 'Cawuk',
        'Cayadi', 'Cecep', 'Cemani', 'Cemeti', 'Cemplunk', 'Cengkal', 'Cengkir',
        'Dacin', 'Dadap', 'Dadi', 'Dagel', 'Daliman', 'Dalimin', 'Daliono',
        'Damar', 'Damu', 'Danang', 'Daniswara', 'Danu', 'Danuja', 'Dariati',
        'Darijan', 'Darimin', 'Darmaji', 'Darman', 'Darmana', 'Darmanto',
        'Darsirah', 'Dartono', 'Daru', 'Daruna', 'Daryani', 'Dasa', 'Digdaya',
        'Dimas', 'Dimaz', 'Dipa', 'Dirja', 'Drajat', 'Dwi', 'Dono', 'Dodo',
        'Edi', 'Eka', 'Elon', 'Eluh', 'Eman', 'Emas', 'Embuh', 'Emong',
        'Empluk', 'Endra', 'Enteng', 'Estiawan', 'Estiono', 'Eko', 'Edi',
        'Edison', 'Edward', 'Elvin', 'Erik', 'Emil', 'Ega', 'Emin', 'Eja',
        'Gada', 'Gadang', 'Gaduh', 'Gaiman', 'Galak', 'Galang', 'Galar',
        'Galih', 'Galiono', 'Galuh', 'Galur', 'Gaman', 'Gamani', 'Gamanto',
        'Gambira', 'Gamblang', 'Ganda', 'Gandewa', 'Gandi', 'Gandi', 'Ganep',
        'Gangsa', 'Gangsar', 'Ganjaran', 'Gantar', 'Gara', 'Garan', 'Garang',
        'Garda', 'Gatot', 'Gatra', 'Gilang', 'Galih', 'Ghani', 'Gading',
        'Hairyanto', 'Hardana', 'Hardi', 'Harimurti', 'Harja', 'Harjasa',
        'Harjaya', 'Harjo', 'Harsana', 'Harsanto', 'Harsaya', 'Hartaka',
        'Hartana', 'Harto', 'Hasta', 'Heru', 'Himawan', 'Hadi', 'Halim',
        'Hasim', 'Hasan', 'Hendra', 'Hendri', 'Heryanto', 'Hamzah', 'Hari',
        'Imam', 'Indra', 'Irwan', 'Irsad', 'Ikhsan', 'Irfan', 'Ian', 'Ibrahim',
        'Ibrani', 'Ismail', 'Irnanto', 'Ilyas', 'Ibun', 'Ivan', 'Ikin', 'Ihsan',
        'Jabal', 'Jaeman', 'Jaga', 'Jagapati', 'Jagaraga', 'Jail', 'Jaiman',
        'Jaka', 'Jarwa', 'Jarwadi', 'Jarwi', 'Jasmani', 'Jaswadi', 'Jati',
        'Jatmiko', 'Jaya', 'Jayadi', 'Jayeng', 'Jinawi', 'Jindra', 'Joko',
        'Jumadi', 'Jumari', 'Jamal', 'Jamil', 'Jais', 'Jefri', 'Johan', 'Jono',
        'Kacung', 'Kajen', 'Kambali', 'Kamidin', 'Kariman', 'Karja', 'Karma',
        'Karman', 'Karna', 'Karsa', 'Karsana', 'Karta', 'Kasiran', 'Kasusra',
        'Kawaca', 'Kawaya', 'Kayun', 'Kemba', 'Kenari', 'Kenes', 'Kuncara',
        'Kunthara', 'Kusuma', 'Kadir', 'Kala', 'Kalim', 'Kurnia', 'Kanda',
        'Kardi', 'Karya', 'Kasim', 'Kairav', 'Kenzie', 'Kemal', 'Kamal', 'Koko',
        'Labuh', 'Laksana', 'Lamar', 'Lanang', 'Langgeng', 'Lanjar', 'Lantar',
        'Lega', 'Legawa', 'Lembah', 'Liman', 'Limar', 'Luhung', 'Lukita',
        'Luluh', 'Lulut', 'Lurhur', 'Luwar', 'Luwes', 'Latif', 'Lasmanto',
        'Lukman', 'Luthfi', 'Leo', 'Luis', 'Lutfan', 'Lasmono', 'Laswi',
        'Mahesa', 'Makara', 'Makuta', 'Manah', 'Maras', 'Margana', 'Mariadi',
        'Marsudi', 'Martaka', 'Martana', 'Martani', 'Marwata', 'Maryadi',
        'Maryanto', 'Mitra', 'Mujur', 'Mulya', 'Mulyanto', 'Mulyono', 'Mumpuni',
        'Muni', 'Mursita', 'Murti', 'Mustika', 'Maman', 'Mahmud', 'Mahdi',
        'Mahfud', 'Malik', 'Muhammad', 'Mustofa', 'Marsito', 'Mursinin',
        'Nalar', 'Naradi', 'Nardi', 'Niyaga', 'Nrima', 'Nugraha', 'Nyana',
        'Narji', 'Nasab', 'Nasrullah', 'Nasim', 'Najib', 'Najam', 'Nyoman',
        'Olga', 'Ozy', 'Omar', 'Opan', 'Oskar', 'Oman', 'Okto', 'Okta', 'Opung',
        'Paiman', 'Panca', 'Pangeran', 'Pangestu', 'Pardi', 'Parman', 'Perkasa',
        'Praba', 'Prabu', 'Prabawa', 'Prabowo', 'Prakosa', 'Pranata', 'Pranawa',
        'Prasetya', 'Prasetyo', 'Prayitna', 'Prayoga', 'Prayogo', 'Purwadi',
        'Purwa', 'Purwanto', 'Panji', 'Pandu', 'Paiman', 'Prima', 'Putu',
        'Raden', 'Raditya', 'Raharja', 'Rama', 'Rangga', 'Reksa', 'Respati',
        'Rusman', 'Rosman', 'Rahmat', 'Rahman', 'Rendy', 'Reza', 'Rizki',
        'Ridwan', 'Rudi', 'Raden', 'Radit', 'Radika', 'Rafi', 'Rafid', 'Raihan',
        'Salman', 'Saadat', 'Saiful', 'Surya', 'Slamet', 'Samsul', 'Soleh',
        'Simon', 'Sabar', 'Sabri', 'Sidiq', 'Satya', 'Setya', 'Saka', 'Sakti',
        'Taswir', 'Tedi', 'Teddy', 'Taufan', 'Taufik', 'Tomi', 'Tasnim',
        'Teguh', 'Tasdik', 'Timbul', 'Tirta', 'Tirtayasa', 'Tri', 'Tugiman',
        'Umar', 'Usman', 'Uda', 'Umay', 'Unggul', 'Utama', 'Umaya', 'Upik',
        'Viktor', 'Vino', 'Vinsen', 'Vero', 'Vega', 'Viman', 'Virman',
        'Wahyu', 'Wira', 'Wisnu', 'Wadi', 'Wardi', 'Warji', 'Waluyo', 'Wakiman',
        'Wage', 'Wardaya', 'Warsa', 'Warsita', 'Warta', 'Wasis', 'Wawan',
        'Xanana', 'Yahya', 'Yusuf', 'Yosef', 'Yono', 'Yoga',
    )

    # From http://namafb.com/2010/08/12/top-1000-nama-populer-indonesia/
    # via
    # https://github.com/fzaninotto/faker/blob/master/src/Faker/Provider/id_ID/Person.php
    first_names_female = (
        'Ade', 'Agnes', 'Ajeng', 'Amalia', 'Anita', 'Ayu', 'Aisyah', 'Ana',
        'Ami', 'Ani', 'Azalea', 'Aurora', 'Alika', 'Anastasia', 'Amelia',
        'Almira', 'Bella', 'Betania', 'Belinda', 'Citra', 'Cindy', 'Chelsea',
        'Clara', 'Cornelia', 'Cinta', 'Cinthia', 'Ciaobella', 'Cici', 'Carla',
        'Calista', 'Devi', 'Dewi', 'Dian', 'Diah', 'Diana', 'Dina', 'Dinda',
        'Dalima', 'Eka', 'Eva', 'Endah', 'Elisa', 'Eli', 'Ella', 'Ellis',
        'Elma', 'Elvina', 'Fitria', 'Fitriani', 'Febi', 'Faizah', 'Farah',
        'Farhunnisa', 'Fathonah', 'Gabriella', 'Gasti', 'Gawati', 'Genta',
        'Ghaliyati', 'Gina', 'Gilda', 'Halima', 'Hesti', 'Hilda', 'Hafshah',
        'Hamima', 'Hana', 'Hani', 'Hasna', 'Humaira', 'Ika', 'Indah', 'Intan',
        'Irma', 'Icha', 'Ida', 'Ifa', 'Ilsa', 'Ina', 'Ira', 'Iriana', 'Jamalia',
        'Janet', 'Jane', 'Julia', 'Juli', 'Jessica', 'Jasmin', 'Jelita',
        'Kamaria', 'Kamila', 'Kani', 'Karen', 'Karimah', 'Kartika', 'Kasiyah',
        'Keisha', 'Kezia', 'Kiandra', 'Kayla', 'Kania', 'Lala', 'Lalita',
        'Latika', 'Laila', 'Laras', 'Lidya', 'Lili', 'Lintang', 'Maria', 'Mala',
        'Maya', 'Maida', 'Maimunah', 'Melinda', 'Mila', 'Mutia', 'Michelle',
        'Malika', 'Nadia', 'Nadine', 'Nabila', 'Natalia', 'Novi', 'Nova',
        'Nurul', 'Nilam', 'Najwa', 'Olivia', 'Ophelia', 'Oni', 'Oliva', 'Padma',
        'Putri', 'Paramita', 'Paris', 'Patricia', 'Paulin', 'Puput', 'Puji',
        'Pia', 'Puspa', 'Puti', 'Putri', 'Padmi', 'Qori', 'Queen', 'Ratih',
        'Ratna', 'Restu', 'Rini', 'Rika', 'Rina', 'Rahayu', 'Rahmi', 'Rachel',
        'Rahmi', 'Raisa', 'Raina', 'Sarah', 'Sari', 'Siti', 'Siska', 'Suci',
        'Syahrini', 'Septi', 'Sadina', 'Safina', 'Sakura', 'Salimah', 'Salwa',
        'Salsabila', 'Samiah', 'Shania', 'Sabrina', 'Silvia', 'Shakila',
        'Talia', 'Tami', 'Tira', 'Tiara', 'Titin', 'Tania', 'Tina', 'Tantri',
        'Tari', 'Titi', 'Uchita', 'Unjani', 'Ulya', 'Uli', 'Ulva', 'Umi',
        'Usyi', 'Vanya', 'Vanesa', 'Vivi', 'Vera', 'Vicky', 'Victoria',
        'Violet', 'Winda', 'Widya', 'Wulan', 'Wirda', 'Wani', 'Yani', 'Yessi',
        'Yulia', 'Yuliana', 'Yuni', 'Yunita', 'Yance', 'Zahra', 'Zalindra',
        'Zaenab', 'Zulfa', 'Zizi', 'Zulaikha', 'Zamira', 'Zelda', 'Zelaya',
    )

    first_names = first_names_male + first_names_female

    # From http://namafb.com/2010/08/12/top-1000-nama-populer-indonesia/
    # From http://id.wikipedia.org/wiki/Daftar_marga_suku_Batak_di_Toba
    # via
    # https://github.com/fzaninotto/faker/blob/master/src/Faker/Provider/id_ID/Person.php
    last_names_male = (
        'Adriansyah', 'Ardianto', 'Anggriawan', 'Budiman', 'Budiyanto',
        'Damanik', 'Dongoran', 'Dabukke', 'Firmansyah', 'Firgantoro',
        'Gunarto', 'Gunawan', 'Hardiansyah', 'Habibi', 'Hakim', 'Halim',
        'Haryanto', 'Hidayat', 'Hidayanto', 'Hutagalung', 'Hutapea', 'Hutasoit',
        'Irawan', 'Iswahyudi', 'Kuswoyo', 'Januar', 'Jailani', 'Kurniawan',
        'Kusumo', 'Latupono', 'Lazuardi', 'Maheswara', 'Mahendra', 'Mustofa',
        'Mansur', 'Mandala', 'Megantara', 'Maulana', 'Maryadi', 'Mangunsong',
        'Manullang', 'Marpaung', 'Marbun', 'Narpati', 'Natsir', 'Nugroho',
        'Najmudin', 'Nashiruddin', 'Nainggolan', 'Nababan', 'Napitupulu',
        'Pangestu', 'Putra', 'Pranowo', 'Prabowo', 'Pratama', 'Prasetya',
        'Prasetyo', 'Pradana', 'Pradipta', 'Prakasa', 'Permadi', 'Prasasta',
        'Prayoga', 'Ramadan', 'Rajasa', 'Rajata', 'Saptono', 'Santoso',
        'Saputra', 'Saefullah', 'Setiawan', 'Suryono', 'Suwarno', 'Siregar',
        'Sihombing', 'Salahudin', 'Sihombing', 'Samosir', 'Saragih', 'Sihotang',
        'Simanjuntak', 'Sinaga', 'Simbolon', 'Sitompul', 'Sitorus', 'Sirait',
        'Siregar', 'Situmorang', 'Tampubolon', 'Thamrin', 'Tamba', 'Tarihoran',
        'Utama', 'Uwais', 'Wahyudin', 'Waluyo', 'Wibowo', 'Winarno', 'Wibisono',
        'Wijaya', 'Widodo', 'Wacana', 'Waskita', 'Wasita', 'Zulkarnain',
    )

    # From http://namafb.com/2010/08/12/top-1000-nama-populer-indonesia/
    # via
    # https://github.com/fzaninotto/faker/blob/master/src/Faker/Provider/id_ID/Person.php
    last_names_female = (
        'Agustina', 'Andriani', 'Anggraini', 'Aryani', 'Astuti',
        'Fujiati', 'Farida', 'Handayani', 'Hassanah', 'Hartati', 'Hasanah',
        'Haryanti', 'Hariyah', 'Hastuti', 'Halimah', 'Kusmawati', 'Kuswandari',
        'Laksmiwati', 'Laksita', 'Lestari', 'Lailasari', 'Mandasari',
        'Mardhiyah', 'Mayasari', 'Melani', 'Mulyani', 'Maryati', 'Nurdiyanti',
        'Novitasari', 'Nuraini', 'Nasyidah', 'Nasyiah', 'Namaga', 'Palastri',
        'Pudjiastuti', 'Puspasari', 'Puspita', 'Purwanti', 'Pratiwi',
        'Purnawati', 'Pertiwi', 'Permata', 'Prastuti', 'Padmasari', 'Rahmawati',
        'Rahayu', 'Riyanti', 'Rahimah', 'Suartini', 'Sudiati', 'Suryatmi',
        'Susanti', 'Safitri', 'Oktaviani', 'Utami', 'Usamah', 'Usada',
        'Uyainah', 'Yuniar', 'Yuliarti', 'Yulianti', 'Yolanda', 'Wahyuni',
        'Wijayanti', 'Widiastuti', 'Winarsih', 'Wulandari', 'Wastuti', 'Zulaika',
    )

    last_names = last_names_male + last_names_female

    prefixes_male = (
        'Dt.', 'R.', 'R.M.', 'Sutan', 'T.', 'Tgk.',

        # From http://id.wikipedia.org/wiki/Gelar_akademik
        # via
        # https://github.com/fzaninotto/faker/blob/master/src/Faker/Provider/id_ID/Person.php
        # plus noble titles
        'dr.', 'drg.', 'Dr.', 'Drs.', 'Ir.', 'H.', 'KH.',
    )

    prefixes_female = (
        'Cut', 'Puti', 'R.', 'R.A.', 'Tgk.',

        # From http://id.wikipedia.org/wiki/Gelar_akademik
        # via
        # https://github.com/fzaninotto/faker/blob/master/src/Faker/Provider/id_ID/Person.php
        # plus noble titles
        'dr.', 'drg.', 'Dr.', 'Drs.', 'Ir.' 'Hj.',
    )

    # From http://id.wikipedia.org/wiki/Gelar_akademik
    # via
    # https://github.com/fzaninotto/faker/blob/master/src/Faker/Provider/id_ID/Person.php
    suffixes = (
        'S.Ked', 'S.Gz', 'S.Pt', 'S.IP', 'S.E.I', 'S.E.', 'S.Kom', 'S.H.',
        'S.T.', 'S.Pd', 'S.Psi', 'S.I.Kom', 'S.Sos', 'S.Farm', 'M.M.', 'M.Kom.',
        'M.TI.', 'M.Pd', 'M.Farm', 'M.Ak',
    )
