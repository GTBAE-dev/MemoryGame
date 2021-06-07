import pygame
from random import*

def display_start_button(): # start button 화면 표시 함수
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) #(Surface, Color, Pos, Radius, Width) 의 circle

def display_game_screen(): # game screen 표시 함수
    for idx, rect in enumerate(number_buttons, start = 1): # 시작 idx 1
        pygame.draw.rect(screen, WHITE, rect)
        cell_text = game_font.render(str(idx), True, BLACK) # idx = number
        text_rect = cell_text.get_rect(center = rect.center) # cell_text의 rect가져오기 + center 설정
        screen.blit(cell_text, text_rect)

def check_button(pos): # start_button 클릭 처리 함수(전달값: 마우스 클릭 좌표)
    global start # 전역변수 start 사용 위한 호출
    if start_button.collidepoint(pos): # start_button 내 pos 위치하는지 확인 
        start = True 

def setup(level): # level에 따라 보여지는 숫자 처리 함수(전달값: level)
    number_count = (level // 3) + 5
    number_count = min(number_count, 20) # 상한 설정
    shuffle_grid(number_count) # 숫자 섞는 함수

def shuffle_grid(number_count): # 숫자 섞는 함수(전달값: number_count(갯수))
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110
    screen_left_margin = 55
    screen_top_margin = 20

    grid = [[0 for col in range(columns)] for row in range(rows)] # [[0,0,0,0,0,0,0,0,0] * 5] 형태의 리스트

    number = 1 # 1 부터 number_count 까지 위치 랜덤 배치
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)
        if grid[row_idx][col_idx] == 0: # 이중 리스트 좌표(큰 리스트 좌표 순, 현재 columns 리스트가 rows 내 위치한 형태)
            grid[row_idx][col_idx] = number
            number += 1
            # grid 내 해당 위치(x, y)
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)
            button = pygame.Rect(0, 0, button_size, button_size) # 해당 좌표로 버튼 만들기
            button.center = (center_x, center_y)
            number_buttons.append(button) # 버튼 리스트 내 삽입

''' 1. 기본 설정 '''
pygame.init() # 초기화
''' 1-1. 화면'''
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MEMORY GAME")
''' 1-2. font '''
game_font = pygame.font.Font(None, 120)
''' 1-3. FPS '''
''' 1-4. 음악 '''

''' 2. 게임 내 요소 '''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
''' 2-1. 배경 '''
start_button = pygame.Rect(0, 0, 120, 120) # (left, top, width, height) 의 Rect
start_button.center = (120, screen_height - 120) # start_button Rect 중심 이동 (0, 0) → (120, screen_height - 120)
''' 2-2. 캐릭터 '''
number_buttons = [] # 버튼 리스트(클릭 대상)
''' 2-3. 무기 '''
''' 2-4. 적 '''

''' 3. 메인루프(메인 이벤트 처리) '''
start = False # 게임 화면 전환 변수(False = start screen / True = game screen)

setup(1)

running = True # 게임 실행 여부 확인 변수
while running: # running == True 
    click_pos = None # 마우스 좌표 변수
    ''' 3-1. FPS '''
    ''' 3-2. 이벤트 처리(키, 마우스, 종료 등) '''
    for event in pygame.event.get(): # 이벤트 종류에 따른 동작
        if event.type == pygame.QUIT: # 창 닫힘 버튼
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: # 마우스 클릭에 따른 동작
            click_pos = pygame.mouse.get_pos() # 클릭 좌표 출력
            print(click_pos)
    
    ''' 3-3. 게임 내 요소 위치 정의 '''
    ''' 3-4. 충돌처리 '''
    ''' 3-5. 화면에 그리기 '''
    screen.fill(BLACK) # 화면 채우기(이후 그리는 것들 겹치지 않기 위함)

    if click_pos: # click_pos != None
        check_button(click_pos)

    if start: # start == True
        display_game_screen()
    else:
        display_start_button() # 시작 버튼 표시
    
    pygame.display.update() # 화면 업데이트

''' 4. 종료 '''
pygame.quit()