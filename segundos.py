s = int(input('Por favor, entre com o número de segundos que deseja converter: '))
d = (s // (3600 * 24))
h = ((s // 3600) % 24)
m = (s % 3600) // 60
sr = (s % 3600) % 60
print(d, 'dias,', h, 'horas,', m, 'minutos e', sr, 'segundos.')
