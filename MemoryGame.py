import pygame

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
''' 2-1. 배경 '''
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

''' 4. 종료 '''
pygame.quit()