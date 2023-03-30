import curses

def main(stdscr):
    # 화면 초기화
    curses.curs_set(0)
    stdscr.clear()

    # 상단 출력 창 생성
    output_win = curses.newwin(curses.LINES // 2, curses.COLS, 0, 0)

    # 하단 입력 창 생성
    input_win = curses.newwin(curses.LINES // 2, curses.COLS, curses.LINES // 2, 0)

    # 상단 출력 창에 메시지 출력
    output_win.addstr("상단 출력 창입니다....\n")
    output_win.refresh()

    # 하단 입력 창에 메시지 출력 및 사용자 입력 받기
    input_win.addstr("하단 입력 창: ")
    input_win.refresh()
    user_input = input_win.getstr().decode('utf-8')

    # 사용자 입력을 상단 출력 창에 출력
    output_win.addstr(f"사용자 입력: {user_input}\n")
    output_win.refresh()

    # 종료 대기
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
