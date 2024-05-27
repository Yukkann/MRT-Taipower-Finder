# ============================== 模組
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
import csv
import pandas as pd
import datetime as dt
# ============================== 檔案數據
# 這樣就可以不用管檔案了，但很醜
red = ['象山', '台北101/世貿', '信義安和', '大安', '大安森林公園', '東門', '中正紀念堂', '台大醫院', '台北車站', '中山', '雙連', '民權西路', '圓山', '劍潭', '士林', '芝山', '明德', '石牌', '唭哩岸', '奇岩', '北投', '復興崗', '忠義', '關渡', '竹圍', '紅樹林', '淡水']
green = ['新店', '新店區公所', '七張', '大坪林', '景美', '萬隆', '公館', '台電大樓', '古亭', '中正紀念堂', '小南門', '西門', '北門', '中山', '松江南京', '南京復興', '台北小巨蛋', '南京三民', '松山']
orange = ['南勢角', '景安', '永安市場', '頂溪', '古亭', '東門', '忠孝新生', '松江南京', '行天宮', '中山國小', '民權西路', '大橋頭', '台北橋', '菜寮', '三重', '先嗇宮', '頭前庄', '新莊', '輔大', '丹鳳', '迴龍', '三重國小', '三和國中', '徐匯中學', '三民高中', '蘆洲']
blue = ['頂埔', '永寧', '土城', '海山', '亞東醫院', '府中', '板橋', '新埔', '江子翠', '龍山寺', '西門', '台北車站', '善導寺', '忠孝新生', '忠孝復興', '忠孝敦化', '國父紀念館', '市政府', '永春', '後山埤', '昆陽', '南港', '南港展覽館']
red1 = ['象山', '台北101/世貿', '信義安和', '大安', '大安森林公園', 'R07東門', 'R08中正紀念堂', '台大醫院', 'R10台北車站', 'R11中山', '雙連', 'R13民權西路', '圓山', '劍潭', '士林', '芝山', '明德', '石牌', '唭哩岸', '奇岩', '北投', '復興崗', '忠義', '關渡', '竹圍', '紅樹林', '淡水']
green1 = ['新店', '新店區公所', '七張', '大坪林', '景美', '萬隆', '公館', '台電大樓', 'G09古亭', 'G10中正紀念堂', '小南門', 'G12西門', '北門', 'G14中山', 'G15松江南京', '南京復興', '台北小巨蛋', '南京三民', '松山']
orange1 = ['南勢角', '景安', '永安市場', '頂溪', 'O05古亭', 'O06東門', 'O07忠孝新生', 'O08松江南京', '行天宮', '中山國小', 'O11民權西路', '大橋頭', '台北橋', '菜寮', '三重', '先嗇宮', '頭前庄', '新莊', '輔大', '丹鳳', '迴龍', '三重國小', '三和國中', '徐匯中學', '三民高中', '蘆洲']
blue1 = ['頂埔', '永寧', '土城', '海山', '亞東醫院', '府中', '板橋', '新埔', '江子翠', '龍山寺', 'B11西門', 'B12台北車站', '善導寺', 'B14忠孝新生', '忠孝復興', '忠孝敦化', '國父紀念館', '市政府', '永春', '後山埤', '昆陽', '南港', '南港展覽館']

all_stations = red + green + orange + blue
R_a=pd.read_csv("R-a-1,2,3,4,5.csv",index_col=0)
G_a = pd.read_csv("G-a-1,2,3,4,5.csv",index_col=0)
BL_a = pd.read_csv("BL-a-1,2,3,4.csv",index_col=0)
O_a = pd.read_csv("O-a-1,2,3,4,5.csv",index_col=0)
R_b=pd.read_csv("R-b-1,2,3,4,5.csv",index_col=0)
G_b = pd.read_csv("G-b-1,2,3,4,5.csv",index_col=0)
BL_b = pd.read_csv("BL-b-1,2,3,4.csv",index_col=0)
O_b = pd.read_csv("O-b-1,2,3,4,5.csv",index_col=0)



# =============================== 初始化視窗
class ColorDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # 獲取選項文本
        text = index.data(Qt.DisplayRole)
        
        # 設置不同選項的顏色
        if text in red1:
            color = QColor(227,0,44)  # 紅色
        elif text in green1:
            color = QColor(0,134,89)  # 綠色
        elif text in orange1:
            color = QColor(248,182,28)  # 橘色
        elif text in blue1:
            color = QColor(0,112,189)  #  藍色
        else:
            color = option.palette.color(QPalette.Text)
        
        # 渲染項目
        option.palette.setColor(QPalette.Text, color)
        QStyledItemDelegate.paint(self, painter, option, index)
  
class Window(QMainWindow): 
  
    def __init__(self): 
        super().__init__() 
        
        self.shortest_route = None
  
        # setting title 
        self.setWindowTitle("台電大樓退散！") 
        
        self.setWindowIcon(QtGui.QIcon('metrotaipei.png'))
  
        # setting geometry 
        self.setGeometry(100, 100, 700, 450) 
  
        # calling method 
        self.UiComponents() 
  
        # showing all the widgets 
        self.show() 
  
    # method for widgets 
    def UiComponents(self):
    # 創建第一個下拉式選單
        self.combo_box1 = QComboBox(self)
        self.combo_box1.setGeometry(200, 150, 250, 30)
        self.combo_box1.setEditable(True)
        geek_list1 = all_stations
        self.combo_box1.addItems(geek_list1)
        delegate1 = ColorDelegate(self.combo_box1)
        self.combo_box1.setItemDelegate(delegate1)

        # 創建第二個下拉式選單
        self.combo_box2 = QComboBox(self)
        self.combo_box2.setGeometry(200, 200, 250, 30)
        self.combo_box2.setEditable(True)
        geek_list2 = all_stations
        self.combo_box2.addItems(geek_list2)
        delegate2 = ColorDelegate(self.combo_box2)
        self.combo_box2.setItemDelegate(delegate2)
        
        # Create the label
        self.label1 = QLabel('請選擇起點：', self)
        self.label2 = QLabel('請選擇終點：', self)
        self.label3 = QLabel('最短路徑：', self)
        self.label4 = QLabel(self)
        self.label5 = QLabel('您在下列時間搭車會被台電大樓喔：', self)
        self.label6 = QLabel(self)
        
        self.label7 = QLabel(self)  # 貓咪
        self.label7.setGeometry(450, 150, 300, 150)
        self.label7.hide()  # 初始時隱藏標籤
        
        self.label8 = QLabel(self)
        self.label8.setGeometry(350, 150, 300, 300)  # 設置標籤位置和大小
        self.label8.hide()  # 初始時隱藏標籤
    
        # 創建QMovie物件
        self.movie = QMovie("fast-cat-cat-excited.gif")  # 替換為您的GIF文件路徑
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(75)  # 調整播放速度,值越大越快
        # 將GIF動畫與label8關聯
        self.label8.setMovie(self.movie)

        
        # 創建按鈕
        self.button = QPushButton('我是按鈕', self)
        self.button.setStyleSheet("background-color: yellow") # Set background color to yellow
        self.button.clicked.connect(self.calc)
        
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.combo_box1)
        layout.addWidget(self.label2)
        layout.addWidget(self.combo_box2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addWidget(self.label5)
        layout.addWidget(self.label6)
        layout.addStretch()  # Add stretchable space
        layout.addWidget(self.button)

        # Set layout to central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
    # ================================================= 按鈕的功能
    def calc(self):
        def MRT_algorithm(start_station, end_station):
            '''
            輸入起始及終點站名
            輸出一個包含各條路線dataframe的list
            '''
            class Line:
                key_to_name = {
                    "BL": "板南線",
                    "O": "中和新蘆線",
                    "R": "淡水信義線",
                    "G": "松山新店線"
                }

                def __init__(self, lines_key, stations): 
                    self.key = lines_key
                    self.name = self.key_to_name[lines_key]
                    self.stations = stations
                    self.terminal_station = [self.stations[0], self.stations[-1]]
                    self.len_line = len(self.stations)

            def MRT():
                routes = []

                for line in lines.values():
                    if start_station in line.stations:
                        if start_station != line.terminal_station[0]:
                            df = pd.DataFrame(columns=["station", "line", "direction", "transfer"])
                            df.loc[0] = [start_station, line.key, -1, 0]
                            routes.append(df)
                        if start_station != line.terminal_station[-1]:
                            df = pd.DataFrame(columns=["station", "line", "direction", "transfer"])
                            df.loc[0] = [start_station, line.key, 1, 0]
                            routes.append(df)

                n = 0
                while len(routes) > n:
                    df = routes[n]

                    running = True
                    if df.iloc[-1]["transfer"] > 2:
                        running = False

                    while running:
                        current_station = df.iloc[-1]["station"]
                        direction = df.iloc[-1]["direction"]
                        current_line = lines[df.iloc[-1]["line"]]
                        transfer = df.iloc[-1]["transfer"]

                        next_station_index = current_line.stations.index(current_station) + direction
                        if next_station_index < 0 or next_station_index >= len(current_line.stations):
                            running = False
                            continue

                        next_station = current_line.stations[next_station_index]

                        next_loc = len(df)
                        df.loc[next_loc] = [next_station, current_line.key, direction, transfer]

                        if next_station in current_line.terminal_station or next_station == end_station:
                            running = False

                        for new_line in lines.values():
                            if next_station in new_line.stations and current_line != new_line:
                                df_new1 = df.copy()
                                df_new1.loc[next_loc + 1] = [next_station, new_line.key, -1, transfer + 1]
                                routes.append(df_new1)
                                df_new2 = df.copy()
                                df_new2.loc[next_loc + 1] = [next_station, new_line.key, 1, transfer + 1]
                                routes.append(df_new2)

                    n += 1

                routes = [route for route in routes if route.iloc[-1]['station'] == end_station]
                routes_len = [len(i) for i in routes]
                routes = [route for route in routes if len(route) <= min(routes_len) * 1.3]

                final_output = []
                for route in routes:
                    df_final = pd.DataFrame(columns=["line", "start", "end", "direction"])
                    next_loc = 0
                    start = route.iloc[0]["station"]
                    line = route.iloc[0]["line"]
                    direction = "a" if route.iloc[0]["direction"] == 1 else "b"

                    for i in range(len(route)):
                        if i == len(route) - 1:
                            end = route.iloc[i]["station"]
                            df_final.loc[next_loc] = [line, start, end, direction]
                        elif route.iloc[i]["line"] != line:
                            end = route.iloc[i]["station"]
                            df_final.loc[next_loc] = [line, start, end, direction]
                            next_loc += 1
                            start = end
                            line = route.iloc[i]["line"]
                            direction = "a" if route.iloc[i]["direction"] == 1 else "b"

                    final_output.append(df_final)

                return final_output

            lines = {
                "BL": Line("BL", blue),
                "O": Line("O", orange),
                "R": Line("R", red),
                "G": Line("G", green)
            }

            Huilong = ['台北橋', '菜寮', '三重', '先嗇宮', '頭前庄', '新莊', '輔大', '丹鳳', '迴龍']
            Luzhou = ['三重國小', '三和國中', '徐匯中學', '三民高中', '蘆洲']
            if (start_station in Huilong and end_station in Luzhou) or (start_station in Luzhou and end_station in Huilong):
                df_final = pd.DataFrame(columns=["line", "start", "end", "direction"])
                df_final.loc[0] = ["O", start_station, "大橋頭", 'b']
                df_final.loc[1] = ["O", "大橋頭", end_station, "a"]
                return [df_final]
            else:
                df_final = MRT()
                return df_final
        def find_shortest_route(df_final):
            shortest_route = None
            shortest_len = float('inf')
            for route in df_final:
                route_len = len(route)
                if route_len < shortest_len:
                    shortest_len = route_len
                    shortest_route = route
            return shortest_route
        # ======================================= 定義結束
        # ======================================= 運算開始
        # Define MRT lines

        start_station = self.combo_box1.currentText()
        end_station = self.combo_box2.currentText()


        df_final = MRT_algorithm(start_station, end_station)
        shortest_route = find_shortest_route(df_final)
        self.shortest_route = shortest_route
        self.label4.setText(f'{shortest_route.to_string(index=False, header=True)}')
        print(shortest_route)
        # 1.要不要轉車?
        Transition = False
        if len(shortest_route) > 1:
            Transition = True
        else:
            Transition = False
        # 2.會不會經過區間車站?(只無法直接到目的地，必須下車在那邊再等一班的那種)
        asshole_stations = ["台電大樓","北投", "大安","大橋頭", "亞東醫院", "昆陽"]
        assholes = set(asshole_stations)
        # (1)先找經過路線
        def get_the_route(start_station, end_station, shortest_route, red, green, orange, blue):
            lines = {'red': red, 'green': green, 'orange': orange, 'blue': blue}
            route = []
            if Transition == False:
                # find a line that includes the start station and the end station at the same time
                stations_to_find = {start_station, end_station}
                for line_name, line_stations in zip(['red', 'green', 'orange', 'blue'], [red, green, orange, blue]):
                    if stations_to_find.issubset(line_stations):
                        line_we_need = lines[line_name]
                # 加上1的原因是不想算入起始點 起點終點是區間車終點是沒關係的
                start_index, end_index = line_we_need.index(start_station), line_we_need.index(end_station)
                if start_index > end_index:
                    route.extend(line_we_need[end_index + 1:start_index])
                else:
                    route.extend(line_we_need[start_index + 1:end_index])
                return route
            elif Transition == True:
                first_line = {start_station, shortest_route.iloc[0,2]}
                second_line = {shortest_route.iloc[0,2],end_station}
                for line_name, line_stations in zip(['red', 'green', 'orange', 'blue'], [red, green, orange, blue]):
                    if first_line.issubset(line_stations):
                        first_line_we_need = lines[line_name]
                for line_name, line_stations in zip(['red', 'green', 'orange', 'blue'], [red, green, orange, blue]):
                    if second_line.issubset(line_stations):
                        second_line_we_need = lines[line_name]
                start_index, end_index = first_line_we_need.index(start_station), second_line_we_need.index(end_station)
                first_transition_index, second_transition_index = first_line_we_need.index(shortest_route.iloc[0,2]), second_line_we_need.index(shortest_route.iloc[0,2])
                if start_index > first_transition_index:
                    route.extend(first_line_we_need[first_transition_index : start_index])
                else:
                    route.extend(first_line_we_need[start_index : first_transition_index])
                if end_index > second_transition_index:
                    route.extend(second_line_we_need[second_transition_index + 1 : end_index])
                elif end_index < second_transition_index:
                    route.extend(second_line_we_need[end_index + 1 : second_transition_index])
            # Exception: O
            Huilong = ['台北橋', '菜寮', '三重', '先嗇宮', '頭前庄', '新莊', '輔大', '丹鳳', '迴龍']
            Luzhou = ['三重國小', '三和國中', '徐匯中學', '三民高中', '蘆洲']
            if (start_station in Huilong and end_station in Luzhou):
                route = []
                Huilong.reverse()
                start_index, end_index = Huilong.index(start_station), Luzhou.index(end_station)
                route.extend(Huilong[start_index:])
                route.extend(Luzhou[1:end_index])
            elif(start_station in Luzhou and end_station in Huilong):
                route = []
                Luzhou.reverse()
                start_index, end_index = Luzhou.index(start_station), Huilong.index(end_station)
                route.extend(Luzhou[start_index:])
                route.extend(Huilong[:end_index])
            return route
        route = get_the_route(start_station, end_station, shortest_route, red, green, orange, blue)
        # (2)再找會不會經過區間車站
        def will_it_pass(route, assholes):
            for station in route:
                if station in assholes:
                    Yes = True
            return Yes
        # 3.確認呼叫檔案名 要轉車就呼叫一個 不轉車就呼叫兩個
        def file_name(G_a, G_b, R_a, R_b, BL_a, BL_b, O_a, O_b, shortest_route):
            file2 = None
            if shortest_route.iloc[0,0] == 'G' and shortest_route.iloc[0,3] == 'a':
                file = G_a
            elif shortest_route.iloc[0,0] == 'G' and shortest_route.iloc[0,3] == 'b':
                file = G_b
            elif shortest_route.iloc[0,0] == 'R' and shortest_route.iloc[0,3] == 'a':
                file = R_a
            elif shortest_route.iloc[0,0] == 'R' and shortest_route.iloc[0,3] == 'b':
                file = R_b
            elif shortest_route.iloc[0,0] == 'O' and shortest_route.iloc[0,3] == 'a':
                file = O_a
            elif shortest_route.iloc[0,0] == 'O' and shortest_route.iloc[0,3] == 'b':
                file = O_b
            elif shortest_route.iloc[0,0] == 'BL' and shortest_route.iloc[0,3] == 'a':
                file = BL_a
            elif shortest_route.iloc[0,0] == 'BL' and shortest_route.iloc[0,3] == 'b':
                file = BL_b
            if shortest_route.shape[0] > 1:
                if shortest_route.iloc[1,0] == 'G' and shortest_route.iloc[1,3] == 'a':
                    file2 = G_a
                elif shortest_route.iloc[1,0] == 'G' and shortest_route.iloc[1,3] == 'b':
                    file2 = G_b
                elif shortest_route.iloc[1,0] == 'R' and shortest_route.iloc[1,3] == 'a':
                    file2 = R_a
                elif shortest_route.iloc[1,0] == 'R' and shortest_route.iloc[1,3] == 'b':
                    file2 = R_b
                elif shortest_route.iloc[1,0] == 'O' and shortest_route.iloc[1,3] == 'a':
                    file2 = O_a
                elif shortest_route.iloc[1,0] == 'O' and shortest_route.iloc[1,3] == 'b':
                    file2 = O_b
                elif shortest_route.iloc[1,0] == 'BL' and shortest_route.iloc[1,3] == 'a':
                    file2 = BL_a
                elif shortest_route.iloc[1,0] == 'BL' and shortest_route.iloc[1,3] == 'b':
                    file2 = BL_b
            return file, file2
        file, file2 = file_name(G_a, G_b, R_a, R_b, BL_a, BL_b, O_a, O_b, shortest_route)
        # 4.不轉車所呼叫的輸出函數
        def get_the_bad_time1(start_station, end_station, file):
            bad_time = []  # 來裝糟糕的時間
            # 判斷是在哪一線、方向
            start_time = file[start_station].to_list()
            end_time = file[end_station].to_list()
            for i in range(min(len(start_time), len(end_time))):
                if pd.isna(end_time[i]) == True or end_time[i] == '==' or end_time[i] == '//'or end_time[i] == '||':
                    if pd.isna(start_time[i]) == False:
                        bad_time.append(start_time[i])
            return bad_time
        # 5.找轉車所對應的下一個列車時間
        def get_the_bad_time2(start_station, end_station, file, file2, shortest_route):
            transition_station = shortest_route.iloc[0,2]
            start_time = file[start_station].to_list()
            first_transition_time = file[transition_station].to_list()
            end_time = file2[end_station].to_list()
            second_transition_time = file2[transition_station].to_list()
            bad_time = []  # 來裝在轉車店點的糟糕的時間
            train_list = dict()  # 字典{搭第一條線的班次時間:到達時間}
            for i in range(min(len(start_time), len(end_time), len(second_transition_time))):  # 不取最小值會out of range
                if pd.isna(end_time[i]) == True or end_time[i] == '==' or end_time[i] == '//'or end_time[i] == '||':
                    if pd.isna(start_time[i]) == False:
                        bad_time.append(second_transition_time[i])
            for i in range(len(start_time)): # create dict train_list
            # 當只有直行兩站都有數字才可以進字典
                if pd.isna(start_time[i]) == False and pd.isna(first_transition_time[i]) == False:
                    train_list[start_time[i]] = first_transition_time[i]
            def find_the_next_train(train_list, second_transition_time):
                next_list = dict()  # 字典{到達時間: 下一班時間}
                next_train = []  # 下個班次是誰
                for value in train_list.values():
                    next = dt.timedelta(100000)
                    id = 0
                    for i in range(len(second_transition_time)):
                    # 往新店的班次時間 減掉 來到西門的時間 至少要是正的
                        if pd.isna(second_transition_time[i]) == False:
                            transition_start = dt.datetime.strptime(value, '%H:%M')
                            transition_next = dt.datetime.strptime(second_transition_time[i], '%H:%M')
                            if transition_start.hour != 0 and transition_next.hour == 0 :  # 改正00:00 to 24:00
                                passed_time = transition_next - transition_start + dt.timedelta(hours=24)
                            else:
                                passed_time = transition_next - transition_start
                            if passed_time >= dt.timedelta(0) and passed_time <= next:
                                next = passed_time
                                id = i
                    next_train.append(second_transition_time[id])
                next_list = {value: next for value, next in zip(train_list.values(), next_train)}
                return next_list
            return find_the_next_train(train_list, second_transition_time), train_list, bad_time
        # 6.轉車所呼叫的輸出函數
        def find_the_bad_time(bad_time, next_list, train_list):
            bad_list = []  # 我們最討厭的會被台電大樓的時間
            for key1, value1 in train_list.items():
            # 如果 下一班時間 == 區間車會來的時間 輸出list加入搭低一條線的班次時間(回溯回去)
                for i in range(len(bad_time)):
                    if next_list.get(value1) == bad_time[i]:
                        bad_list.append(key1)
            return bad_list
        # 輸出模組
        if Transition == False:  # 不轉車
            result = get_the_bad_time1(start_station, end_station, file)
            if result == []:
                self.label6.setText("恭喜您不會被台電大樓！")
                self.label7.hide()  # 隱藏label7
                self.label8.show()  # 顯示label8
                self.movie.start()  # 開始播放GIF動畫
            else:
                bad_time_str = [str(time) for time in result]
                items_per_line = 10
                bad_time_lines = [bad_time_str[i:i+items_per_line] for i in range(0, len(bad_time_str), items_per_line)]
                formatted_lines = [' '.join(line) for line in bad_time_lines]
                formatted_text = '\n'.join(formatted_lines)
                print(formatted_text)
                self.movie.stop()   # 停止播放GIF動畫
                self.label8.hide()  # 隱藏label8
                qpixmap = QPixmap()
                qpixmap.load('images.jpg')  # 替換為您的 QQ 貓咪圖片路徑
                self.label7.setPixmap(qpixmap)
                self.label7.show()  # 顯示 QQ 貓咪圖片
                self.label6.setText(formatted_text)
        elif Transition == True:  # 要轉車
            next_list, train_list, bad_time = get_the_bad_time2(start_station, end_station, file, file2, shortest_route)
            bad_list = find_the_bad_time(bad_time, next_list, train_list)
            result = find_the_bad_time(bad_time, next_list, train_list)
            # ============================================ 轉輸出格式
            if result == []:
                self.label6.setText("恭喜您不會被台電大樓！")
                self.label7.hide()  # 隱藏label7
                self.label8.show()  # 顯示label8
                self.movie.start()  # 開始播放GIF動畫
            else:
                bad_time_str = [str(time) for time in result]
                items_per_line = 10
                bad_time_lines = [bad_time_str[i:i+items_per_line] for i in range(0, len(bad_time_str), items_per_line)]
                formatted_lines = [' '.join(line) for line in bad_time_lines]
                formatted_text = '\n'.join(formatted_lines)
                print(formatted_text)
                self.label6.setText(formatted_text)
                self.movie.stop()   # 停止播放GIF動畫
                self.label8.hide()  # 隱藏label8
                qpixmap = QPixmap()
                qpixmap.load('images.jpg')  # 替換為您的 QQ 貓咪圖片路徑
                self.label7.setPixmap(qpixmap)
                self.label7.show()  # 顯示 QQ 貓咪圖片

            
            # ============================================
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 