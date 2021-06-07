import pygame

def display_start_button(): # start button 화면 표시 함수
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) #(Surface, Color, Pos, Radius, Width) 의 circle

''' 1. 기본 설정 '''
pygame.init() # 초기화
''' 1-1. 화면'''
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MEMORY GAME")
''' 1-2. font '''
''' 1-3. FPS '''
''' 1-4. 음악 '''

''' 2. 게임 내 요소 '''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
''' 2-1. 배경 '''
start_button = pygame.Rect(0, 0, 120, 120) # (left, top, width, height) 의 Rect
start_button.center = (120, screen_height - 120) # start_button Rect 중심 이동 (0, 0) → (120, screen_height - 120)
''' 2-2. 캐릭터 '''
''' 2-3. 무기 '''
''' 2-4. 적 '''

''' 3. 메인루프(메인 이벤트 처리) '''
running = True # 게임 실행 여부 확인 변수
while running: # running == True 
    ''' 3-1. FPS '''
    ''' 3-2. 이벤트 처리(키, 마우스, 종료 등) '''
    for event in pygame.event.get(): # 이벤트 종류에 따른 동작
        if event.type == pygame.QUIT: # 창 닫힘 버튼
            running = False
    

    ''' 3-3. 게임 내 요소 위치 정의 '''
    ''' 3-4. 충돌처리 '''
    ''' 3-5. 화면에 그리기 '''
    screen.fill(BLACK) # 화면 채우기(이후 그리는 것들 겹치지 않기 위함)
    
    display_start_button() # 시작 버튼 표시

    pygame.display.update() # 화면 업데이트

''' 4. 종료 '''
pygame.quit()