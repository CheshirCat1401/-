font.init()
font = font.SysFont('Arial', 40)
text_count = font.render('Счет:', 1, (255, 255, 255))
text_lose = font.render('Пропущено:' + str(lost), 1, (255, 255, 255))
winner = font.render('YOU WIN!', True, (252, 210, 0))
lose = font.render('YOU LOSE!', True, (194, 0, 0))


