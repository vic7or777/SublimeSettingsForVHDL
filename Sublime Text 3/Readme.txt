25_03_2018
Кнопки и фичи программы Sublime Text3

Интеграция с Xilinx ISE:
	Edit->Preferences->Editors: Text Editor-> Editor = Custom
	Command line syntax =   {C:\Program Files\Sublime Text 3\sublime_text.exe} $1

Интеграция с Vivado:
	Tools -> Options -> Text Editor:Current Editor = Custom Editor
	C:\Program Files\Sublime Text 3\sublime_text.exe [file name]


Скопировать в C:\Users\Пользователь\AppData\Roaming\ папку Sublime Text 3 с плагинами


Настройки Sublime text: Preferences->Key Bindings:  User:

    "font_size": 14,
    "translate_tabs_to_spaces": true,
    "tab_size": 4


Комментарий Ctrl+/
Изменение кодировки на "Kirillic"  Ctrl+Shift+/

Отображение нескольких окон: View->Layout
Отображение одного файла несколько раз: File-> New View into File
Вертикальное выделение -  средняя кнопка мыши

Установка/удаление закладки: Ctrl+F2
    Прыжок к следующей закладки: F2
    Удалить все закладки: Ctrl+Shift+F2

Для нормального открытия ucf скопировать файл Tcl.sublime-settings в C:\Users\user\AppData\Roaming\Sublime Text 3\Packages\User   ИЛИ
	Для открытия ucf можно или выставить View->Syntax->TCL или быстрее Ctrl+Shift_p = ss TCL

Чтобы работали атоматические коментарии: скопировать файл Default (Windows).sublime-keymap в 	
	C:\Users\user\AppData\Roaming\Sublime Text 3\Packages\User

Автоматический комментарий: Ctrl+/ или Ctrl+Shift+/

Find and replace - Ctrl+h
    Поиск по всем файлам Ctrl+Shift+f
	Чтобы найти и заменить все ПОД найденым значением, надо или нажать кнопку Replace и не отпускать ее или Ctrl+Shift+h
	Wrap опция при поиске = зацикливанию по тексту

    Поиск RgExp: Ctlr+I
    Выбрать * Чтобы рисовались ближайшие символы , соответствущие нашему REgExp
    Alt+Enter - выделит нам ВСЕ вхождения Regexp
    Например поиск текста между тегами, не включая сами теги:   (?<=<h2>).+(?=</h2>)


Работа Package Text Pastry:
    Ctrl+Shift+p -> ищем TextPasty Command line -> Enter.
    Появится командная панель TextPasty, выделяем нужный текст и пишем в панели:
     1                      - Для вставки цифр от 1 до последнего выделенного(инкремент +1 по умолчанию):
     \i(1,10)               - от 1 с инкрементом 10
     1 end=4                - вставляет числа 1,2,3,4,1,2,3,4
     letters a-c upper      -  A B C A B C
     letters a-c upper x3   -  A A A B B B C C C
     1 x3                   -  1 1 1 2 2 2 3 3 3 и т.д.
     x y z                  -  x y z x y z x y z и т.д.


Работа Package Smart VHDL:
    При наведении на сигнал или порт появляется подсказка о количестве бит
    ПКМ на сигнале или модуле -> Goto Definishion - прыгнуть к объявлению данного сигнала/модуля

Работа Package VHDL Mode:
    Preference-> Package Settings -> VHDL Mode -> Settings   Настраиваем шапку, если надо
    Alt+k p h   (Paste Header)  Вставка шапки (Сначала Alt+k, затем нажимаем t, затем h (не одновременно))  
                После вставки шапки, по Ctrl+S (save file) будет изменяться поле -- Last update  
    Alt+k f   -  автоформатирование vhdl файла для красоты (офигенная вещь!!!!)
    Alt+k c p   -  (Copy Ports) копирование портов модуля.
        Alt+k p t  (paste testbench) после копирования портов, можно создать тестбенч: 
        Alt+k p r  (paste reverse)  можно скопированные порты инвертировать (in заменить на out и наоборот)
        Alt+k p s  (paste signals)  данные портов вставляются как объявления сигналов
        Alt+k p с  (paste component) 
        Alt+k p i  (paste Inst_component) (объявление компонента не требуется, круто !!!) 
        Alt+k p e  (paste entity)        
      
    Snippets (Сниппеты запускаются при нажатии tab после написания символов):    
    ..  -  =>
    ,,  -  <=
    ot -  (others=>'0');  oth
    --=  - блок (box) комментария из трех линий
    use    (библиотеки use) 
    type    -  объявление нового типа type и сигнала
    procclk -  процесс с портом clk	
	procrst -  процесс с портом clk,rst
	procce  -  процесс с портом clk,ce,rst
	sint    -  signal int -  объявление сигнала типа int
	sstd    -  signal std_logic 
	svector -  signal std_logic_vector

    Работа с тестбенчем:
       Alt+k p t  (paste testbench) после копирования портов, можно создать тестбенч  
	   teststd -  в тестбенче формирование сигналов типа std_logic
	   testvector - testbench std_logic_vector
	   testfor  - testbench for loop
	   testfile - считывание/запись данных тестирования из файла/в файл
	   testrand - генерация случайных (random) данных тестирования 
 
    Подключение буферов:
        buf  -
        ibuf и т.д.

    работа с *.ucf файлами:
        clk - подключение контакта clk
        net - подключение одиночного контакта
        netlvds -  подключение lvds контакта



Создание Snippets: Tools->Developer -> New Snippet    ( не забываем, чтобы сниппет работал надо расширение файла сохранить как .sublime-snippet   )

Работа SyncScroll- синхронизация горизонтальной и вертикальной прокрутки    
    нескольких одновременно открытых файлов: View -> SyncScroll