import win32gui
import win32api
import win32con

def draw_rectangle(x, y, width, height):
    # Получаем хэндл окна рабочего стола
    desktop_hwnd = win32gui.GetDesktopWindow()

    # Получаем контекст устройства для рабочего стола
    desktop_dc = win32gui.GetDC(desktop_hwnd)

    # Создаем перо для рисования
    #pen = win32gui.CreatePen(win32con.PS_, 2, win32api.RGB(255, 0, 0))
    # Выбираем перо в контекст устройства
    #win32gui.SelectObject(desktop_dc, pen)
    # Рисуем прямоугольник на рабочем столе
    #win32gui.Rectangle(desktop_dc, x, y, x + width, y + height)
    color_red = win32api.RGB(255, 0, 0)

    pen = win32gui.CreatePen(win32con.PS_SOLID, 2, color_red)    
    win32gui.SelectObject(desktop_dc, pen)    
    # Рисуем линию на рабочем столе
    xpre=x
    ypre=y
    import time
    while(xpre<=(x+width)):
        print(f"{xpre}:{x+width}")
        xpre+=5
        win32gui.MoveToEx(desktop_dc, x, y)
        win32gui.LineTo(desktop_dc, xpre, y)
    while(ypre>=(y-height)):
        print(f"{ypre}:{y-height}")
        ypre-=5
        win32gui.MoveToEx(desktop_dc, xpre, y)
        win32gui.LineTo(desktop_dc, xpre, ypre)


    # Освобождаем дескриптор контекста устройства
    win32gui.ReleaseDC(desktop_hwnd, desktop_dc)

# Пример использования функции
draw_rectangle(0, 0, 500, 500)