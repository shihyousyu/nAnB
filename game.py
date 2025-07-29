import sys      # python的標準函式庫
import pygame   # 製作遊戲常用模組
from pygame.locals import QUIT
import random   # 產生亂數

pygame.init()   # 初始化

# 宣告視窗和大小
# [surface_name] = pygame.display.set_mode([size])
screen = pygame.display.set_mode((800, 600))

# 填充背景色
# [surface_name].fill([color])
screen.fill((0, 0, 0))

# 視窗標題
# pygame.display.set_caption([text])
pygame.display.set_caption('1A2B')

# 以下四行為設定字體(同字型，不同大小)
# [fone_name] = pygame.font.Font([font(.ttf檔)], [size])
font_main = pygame.font.Font('dlxfont.ttf', 12 )
font_logo = pygame.font.Font('dlxfont.ttf', 150)
font_wins = pygame.font.Font('dlxfont.ttf', 70 )
fnt_start = pygame.font.Font('dlxfont.ttf', 30 )
#dlxfont.ttf
# 說明文字放在 txt[] 這個list
txt = [
    "input 4 numbers: ____",
    "\"1 A 2 B\":",
    "    1 number  is  correct and in the right place",
    "    2 numbers are correct but in the wrong place",
    "for example:",
    "    the answer is \"1234\",",
    "    and the input is \"2345\",",
    "    it will be \"0 A 3 B\"",
    "Tap to start..."
    ]

color = (0, 255, 0 ) # 文字顏色(純綠)

# 由random函數從0~9隨機取四個數作為答案
# ans為一 list(ans[])
ans  = random.sample(range(0, 9), 4)

text = "" # 儲存玩家輸入的數字(字串形式)

mode = 0 # mode = 0:遊戲開始介面 1:遊戲介面 2:玩家獲勝

jugA = 0 # jugA:數字、位置皆正確的個數

jugB = 0 # jugB:數字對、位置不對的個數

# 數字、位置皆正確的數量
def check_a(player, ans):
    
    n = 0 # 從第0個開始比對
    a = 0 # 記錄個數，從0個開始計數
    
    while n < 4:
        # 玩家輸入的第n個數和答案的第n個數相同
        if player[n] == ans[n]:
            a += 1
        n += 1 # 不管是否相同都要比對下一個
    return a; # 回傳個數
    
# 數字對、位置不對的數量
def check_b(player, ans):
    
    n = 0
    b = 0
    
    while n < 4:
        # 玩家輸入的第n個數存在於答案中
        # 但不是答案的第n個數
        if (player[n] in ans) & (player[n] != ans[n]):
            b += 1
        n += 1
    return b;

# 遊戲主程式
def game(num, ans):
    
    # 把輸入的數字轉成list
    # 1234 -> [1,2,3,4]
    player = [
        num // 1000, num % 1000 // 100, 
        num % 100 // 10, num % 10
        ]
    
    # 當a不等於4(全部相同)時回傳(a,b)
    if int(check_a(player, ans)) < 4:
        return(check_a(player, ans), check_b(player, ans))

    # 全部相同時，回傳(5,5)，此時玩家獲勝
    else:
        return(5, 5)

while True:
    screen.fill((0, 0, 0))
    
    # 宣告text_surface
    # [obj_name] = [font].render([text], [平滑值], [color])
    # 此物件讓玩家看到他輸入什麼
    text_surface = font_main.render(text, True, color)
    
    #渲染物件，使其出現在螢幕上
    # [surface_name].blit([obj_name], [locate])
    screen.blit(text_surface, (465, 300))

    if mode == 0: # mode = 0:顯示遊戲開始介面
        logo = font_logo.render("1A2B", True, color)
        strt = fnt_start.render(txt[8], True, color)
        screen.blit(logo, (120, 130))
        screen.blit(strt, (200, 400))

    elif mode == 1: # mode = 1:顯示遊戲介面
        
        # 比對結果(玩家輸入和答案)
        # 字串和字串才能用'+'
        # str([obj]) -> 把[obj]強制轉換成字串
        result = str(jugA) + "A" + str(jugB) + "B"
        result = font_logo.render(result, True, color)
        screen.blit(result, (120, 130))
        
        # 文字:input 4 numbers: ____
        input_ = font_main.render(txt[0], True, color)
        screen.blit(input_, (260, 300))
        
        # 以下 7 個物件為說明文字
        guide1 = font_main.render(txt[1], True, color)
        guide2 = font_main.render(txt[2], True, color)
        guide3 = font_main.render(txt[3], True, color)
        guide4 = font_main.render(txt[4], True, color)
        guide5 = font_main.render(txt[5], True, color)
        guide6 = font_main.render(txt[6], True, color)
        guide7 = font_main.render(txt[7], True, color)
        screen.blit(guide1, (100, 365))
        screen.blit(guide2, (100, 390))
        screen.blit(guide3, (100, 415))
        screen.blit(guide4, (100, 440))
        screen.blit(guide5, (100, 465))
        screen.blit(guide6, (100, 490))
        screen.blit(guide7, (100, 515))
        
    elif mode == 2: # mode = 2:玩家獲勝介面
        win = font_wins.render("You Win!", True, color)
        screen.blit(win, (150, 200))
    
    # 不斷刷新介面
    # 否則上一個渲染的物件不會消失>>多個物件重疊
    pygame.display.update()
    
    # 遍歷所有事件
    for event in pygame.event.get():
        
        # 若鍵盤被按下 且 處於遊戲狀態
        if (event.type == pygame.KEYDOWN) & (mode == 1):
            
            # 若玩家已輸入 4 個數字 或 按下enter鍵
            if (len(text) == 4) | (event.key == pygame.K_RETURN):

                (jugA, jugB) = game(int(text), ans) # 回傳對比結果
                
                if (jugA, jugB) == (5, 5): # 若玩家輸入和答案相符
                    mode = 2
                    
                text = "" # 清空輸入
            
            # 若玩家按下刪除鍵
            elif event.key == pygame.K_BACKSPACE:
                
                # 刪除最後輸入的字元
                # 1234 -> 123
                text = text[:-1]
                
            # 玩家按下的不是enter或刪除鍵
            # 且還能繼續輸入
            else:
                
                # 若玩家按的是數字鍵
                if '0' <= event.unicode <= '9':
                    
                    # text添加輸入的數字
                    text += event.unicode
                    
        # 若玩家點擊滑鼠 且 尚未開始遊戲
        if (event.type == pygame.MOUSEBUTTONDOWN) & (mode == 0):
            screen.fill((0, 0, 0))
            mode = 1
            
        # 若玩家點擊"關閉視窗">>結束程式及視窗
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
